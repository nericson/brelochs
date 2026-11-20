"""Check census and source-line relationships; run with Python 3.9+."""
import csv
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
TEI = {"t": "http://www.tei-c.org/ns/1.0"}
XML_ID = "{http://www.w3.org/XML/1998/namespace}id"


def table(path):
    with (ROOT / path).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def check(condition, message):
    if not condition:
        raise ValueError(message)


years = table("census/forecast-years.csv")
witnesses = table("census/witnesses.csv")
rank = ["dedication", "reader-address", "title-only", "located", "historical"]
check([int(r["forecast_year"]) for r in years] == list(range(1528, 1560)),
      "Census must have one row for each forecast year")
by_year = defaultdict(list)
for w in witnesses:
    check(w["access_evidence"] in rank, "Unknown witness evidence class")
    check(1528 <= int(w["forecast_year"]) <= 1559, "Witness outside census")
    by_year[w["forecast_year"]].append(w)
for row in years:
    current = by_year[row["forecast_year"]]
    classes = {w["access_evidence"] for w in current}
    best = next((c for c in rank if c in classes), "untraced")
    check(best == row["strongest_evidence"], f"Evidence mismatch: {row}")
    languages = "+".join(dict.fromkeys(w["language"] for w in current))
    check(languages == row["languages_documented"], f"Language mismatch: {row}")
german = table("analysis/year-matrix.csv")
check({r["forecast_year"] for r in german} ==
      {r["forecast_year"] for r in years if r["strongest_evidence"] == "dedication"},
      "German evidence matrix and census differ")

folder = ROOT / "comparanda/1533-geneva"
doc = ET.parse(folder / "address.xml")
ids = {node.get(XML_ID) for node in doc.iter() if node.get(XML_ID)}
lines = doc.findall('.//t:div[@type="readerAddress"]//t:lb', TEI)
check([node.get("n") for node in lines] == [str(i) for i in range(1, 35)],
      "French address line numbering")
line_index = {node.get(XML_ID): i for i, node in enumerate(lines)}
for node in doc.iter():
    for attr in ("facs", "corresp"):
        for ref in node.get(attr, "").split():
            check(ref.lstrip("#") in ids, f"Unresolved TEI pointer {ref}")
for graphic in doc.findall(".//t:graphic", TEI):
    url = graphic.get("url")
    if not url.startswith("https://"):
        check((folder / url).is_file(), f"Missing facsimile {url}")
codes = table("analysis/1533-passages.csv")
for code in codes:
    check(code["forecast_year"] == "1533", "Unexpected French forecast year")
    check(line_index[code["start_id"]] <= line_index[code["end_id"]], "Invalid span")
    check(code["evidence_class"] in {"E", "R", "I", "E-behavior", "N"}, "Unknown code")
summary = Counter(row["strongest_evidence"] for row in years)
print("Forecast-year evidence:", dict(summary))
print("German years / developed defenses:", len(german),
      sum(r["developed_argument"] == "True" for r in german))
print("French address lines / coded passages:", len(lines), len(codes))
print("French codes:", dict(Counter(r["evidence_class"] for r in codes)))

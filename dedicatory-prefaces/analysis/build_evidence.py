"""Regenerate transparent evidence tables from the adjacent TEI; Python standard library only."""
from pathlib import Path
import xml.etree.ElementTree as ET
import csv, re, unicodedata, hashlib, json
from difflib import SequenceMatcher
ROOT=Path(__file__).resolve().parent
NS={'t':'http://www.tei-c.org/ns/1.0'}
XMLID='{http://www.w3.org/XML/1998/namespace}id'

def read(p):
    tree=ET.parse(p); div=tree.find('.//t:div[@type="dedication"]', NS)
    lines=[]; current=None; page=''
    def walk(el):
        nonlocal current,page
        tag=el.tag.rsplit('}',1)[-1]
        if tag=='pb': page=el.get('n')
        if tag=='lb':
            current={'id':el.get(XMLID),'leaf':page,'line':int(el.get('n')),'text':''}; lines.append(current)
        if el.text and current is not None: current['text']+=el.text
        for ch in el:
            walk(ch)
            if ch.tail and current is not None: current['text']+=ch.tail
    walk(div)
    for row in lines: row['text']=row['text'].strip()
    return lines

def tokens(s):
    s=re.sub(r'-\s*\n\s*','',s.lower()).replace('v','u').replace('j','i').replace('ß','ss')
    s=''.join(c for c in unicodedata.normalize('NFD',s) if not unicodedata.combining(c))
    return re.findall(r'[a-z0-9]+',s)

def csvout(name,rows):
    with (ROOT/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

corpus={}
for p in sorted((ROOT.parent/'tei').glob('*.xml')):
    key=p.stem.removeprefix('brelochs-').removesuffix('-preface')
    corpus[key]=read(p)
# unit, year, page index, start/end inclusive, topic, evidence class, interpretation, competing reading
units=[
('U01','1528',1,6,25,'CREATION;AUTHORITY','I','Created heavens are a legitimately readable order of natural events.','Positive exposition need not answer an actual critic.'),
('U02','1528',1,26,42,'CAUSALITY;AUTHORITY','I','Learned natural knowledge supports broad celestial influence.','No named opponent or reported accusation.'),
('U03','1528',2,1,10,'UTILITY;CONTINGENCY','I','Foreknowledge can avert harm; forecast is a warning rather than necessity.','Pedagogical explanation is sufficient; failed predictions are not reported.'),
('U04','1529',1,5,8,'TRUTHFULNESS','E','Practicas reportedly have a bad reputation and are regarded as lying booklets.','Brelochs is the only witness to the reported criticism; its grounds are unspecified.'),
('U05','1529',1,8,22,'DIVINE_FREEDOM','R','Conditional concession: astrology would deserve criticism if it constrained divine power or providence.','This is Brelochs constructing an objection, not quoting an identifiable critic.'),
('U06','1529',1,23,28,'CHRISTIAN_LEGITIMACY','I','Knowledge and action are subordinated to Christ.','May be affirmative devotion as well as apologetic positioning.'),
('U07','1529',1,29,47,'NATURAL_ORDER;DIVINE_FREEDOM','I','Seasonal effects authorize a wider natural order, while God remains free.','The analogy does not independently prove planetary causes of war.'),
('U08','1529',2,1,10,'FEAR;CHRISTIAN_LEGITIMACY','I','The pious should fear God, not the stars; moral standing changes the significance of fortune.','Pastoral instruction does not establish an external accusation of fearmongering.'),
('U09','1529',2,11,14,'CONTINGENCY;UTILITY','I','Forecast remains warning rather than necessity.','Continues the 1528 disclaimer rather than demonstrating a new objection.'),
('U10','1531',1,4,14,'DEDICATION','N','Brief annual presentation with modesty and a request for acceptance.','No developed defense here; opposition elsewhere cannot be excluded.'),
('U11','1532',1,4,15,'DEDICATION','N','Brief presentation of a compressed forecast.','Absence in this dedication is not absence from the entire practica.'),
('U12','1535',1,5,23,'DEDICATION','N','Custom and gracious reception dominate.','The Augsburg witness is the same transcribed text, not an independent annual observation.'),
('U13','1538',1,5,17,'DEDICATION','N','Brief presentation closely related to the 1531 formula.','A gap in apologetic content does not measure a fall in criticism.'),
('U14','1542',1,6,11,'DISCIPLINARY_STATUS','E','Brelochs explicitly reports contempt by envious talkative people.','Neither their identity nor their specific reasoning is reported.'),
('U15','1542',1,12,17,'HUMAN_NONCOMPULSION','I','Stellar influence inclines but does not compel human beings.','Explicit qualification by the author; an external determinist charge is inferred.'),
('U16','1542',1,18,35,'MEDICAL_AUTHORITY;NATURAL_CAUSALITY','I','Medical experience and hidden natural properties defend astrology as necessary physician knowledge.','Professional self-presentation can explain the argument without a new medical controversy.'),
('U17','1547',1,6,14,'CAUSALITY;RETROSPECTIVE_VALIDATION','I','Ptolemaic authority and remembered calamities support prediction.','General calamity lists are not a matched test of earlier forecasts.'),
('U18','1547',1,14,25,'UNHEEDED_WARNING;REPENTANCE','E-behavior','Warnings and ecclesiastical rebuke reportedly meet with increasing stubbornness.','Reports of audience behavior are not reports of critics arguments.'),
('U19','1557',1,10,20,'CAUSALITY;RETROSPECTIVE_VALIDATION','I','Reprises the sequence of Ptolemaic authority, experience and calamities from 1547.','Textual reuse or common source; no proof of newly intensified pressure.'),
('U20','1557',1,20,24,'UNHEEDED_WARNING;REPENTANCE','E-behavior','Reuses the unheeded-warning and prophetic-stubbornness complaint.','The earlier explicit church-rebuke passage is omitted; motive unknown.'),
('U21','1558',1,10,28,'CELESTIAL_REGULARITY;DIVINE_FREEDOM','I','Humans cannot reverse celestial movements; God alone can.','This concerns heavenly motions and eclipses, not the inevitability of all terrestrial outcomes.'),
('U22','1558',2,1,11,'CREATION;CHRISTIAN_LEGITIMACY','I','Creation and the Redeemer authorize reading heavenly signs of earthly events.','Late natural explanation remains explicitly theological.'),
('U23','1558',2,12,20,'COUNTERCAUSES;CONTINGENCY','I','Stronger contrary causes may prevent indicated effects; analogies of magnet and wound.','Possible answer to failed prediction, but no failed forecast or critic is identified.'),
('U24','1558',2,21,33,'UTILITY;PREVENTION','I','Navigation, farming and husbandry illustrate utility; wise action may avert harm.','This develops a defense already present in 1528; not its first appearance.'),
('U25','1559',1,7,23,'DEDICATION','N','Annual custom, modesty and presentation return to the foreground.','Late date does not imply increasingly elaborate polemic.'),
]
rows=[]
for uid,year,page,a,b,topics,cls,interp,alt in units:
    chosen=[x for x in corpus[year] if x['id'].startswith(f'line-{year}-{page}-') and a<=x['line']<=b]
    assert len(chosen)==b-a+1,(uid,len(chosen),b-a+1)
    rows.append(dict(unit=uid,forecast_year=year,start_id=chosen[0]['id'],end_id=chosen[-1]['id'],leaf=chosen[0]['leaf'],topics=topics,evidence_class=cls,interpretation=interp,alternative=alt,transcribed_evidence='\n'.join(x['text'] for x in chosen)))
csvout('coded-passages.csv',rows)
# Export all lines for audit, including uncoded subscriptions and the alternate copy.
csvout('line-register.csv',[dict(witness=k,**r) for k,ls in corpus.items() for r in ls])
dates={'1528':'1527-07-12?','1529':'1528-06-24','1531':'1530-06-12','1532':'1531-08-27','1535':'1535-08-02 (printed; unresolved)','1538':'1537-07-13','1542':'1541-07-04','1547':'1546-05-15','1557':'1556-06-08','1558':'1557-06-24','1559':'1558-04-23'}
summary=[]
for k,ls in corpus.items():
    if k=='1535-Augsburg':continue
    s='\n'.join(x['text'] for x in ls)
    summary.append(dict(forecast_year=k,dedication_date=dates[k],transcribed_lines=len(ls),normalized_token_proxy=len(tokens(s)),developed_argument=k in {'1528','1529','1542','1547','1557','1558'},reported_disparagement=k in {'1529','1542'},reported_unheeded_warnings=k in {'1547','1557'}))
csvout('year-matrix.csv',summary)
# Exact token runs under declared mechanical normalization. Not a semantic similarity score.
pairs=[('1531','1538'),('1547','1557'),('1528','1529'),('1528','1558')]
shared=[]
for a,b in pairs:
    ta=tokens('\n'.join(x['text'] for x in corpus[a]));tb=tokens('\n'.join(x['text'] for x in corpus[b]))
    for match in SequenceMatcher(None,ta,tb,autojunk=False).get_matching_blocks():
        if match.size>=5:shared.append(dict(first=a,second=b,token_run=match.size,first_token_offset=match.a,second_token_offset=match.b,normalized_text=' '.join(ta[match.a:match.a+match.size])))
csvout('shared-token-runs.csv',shared)
assert [x['text'] for x in corpus['1535']]==[x['text'] for x in corpus['1535-Augsburg']]
hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((ROOT.parent/'tei').glob('*.xml'))}
(ROOT/'input-checksums.json').write_text(json.dumps(hashes,indent=2)+'\n')
print(json.dumps(summary,indent=2));print('PASS: 25 passage ranges; alternate 1535 text identical; tables rebuilt.')

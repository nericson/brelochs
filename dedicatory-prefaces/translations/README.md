# English translations of the dedicatory prefaces

The [1533 French reader’s address and English translation](../comparanda/1533-geneva/README.md) supplement these German dedicatory translations.

Version 0.1 • November 20, 2026 • Complete scholarly working translations, AI-assisted and checked against the German transcriptions

Twelve witness-specific translations cover **eleven forecast years**, including the alternate Augsburg copy of 1535. Each is available as readable Markdown and TEI P5 XML. The alternate copy has the same translated wording, with its own source references. The unretrieved 1548 dedication is outside this translation set.

| Forecast year / witness | English reading copy | English TEI | German TEI |
|---|---|---|---|
| 1528 | [Read](en/brelochs-1528-preface-en.md) | [XML](en/brelochs-1528-preface-en.xml) | [Source](../tei/brelochs-1528-preface.xml) |
| 1529 | [Read](en/brelochs-1529-preface-en.md) | [XML](en/brelochs-1529-preface-en.xml) | [Source](../tei/brelochs-1529-preface.xml) |
| 1531 | [Read](en/brelochs-1531-preface-en.md) | [XML](en/brelochs-1531-preface-en.xml) | [Source](../tei/brelochs-1531-preface.xml) |
| 1532 | [Read](en/brelochs-1532-preface-en.md) | [XML](en/brelochs-1532-preface-en.xml) | [Source](../tei/brelochs-1532-preface.xml) |
| 1535 — Munich | [Read](en/brelochs-1535-preface-en.md) | [XML](en/brelochs-1535-preface-en.xml) | [Source](../tei/brelochs-1535-preface.xml) |
| 1535 — Augsburg | [Read](en/brelochs-1535-Augsburg-preface-en.md) | [XML](en/brelochs-1535-Augsburg-preface-en.xml) | [Source](../tei/brelochs-1535-Augsburg-preface.xml) |
| 1538 | [Read](en/brelochs-1538-preface-en.md) | [XML](en/brelochs-1538-preface-en.xml) | [Source](../tei/brelochs-1538-preface.xml) |
| 1542 | [Read](en/brelochs-1542-preface-en.md) | [XML](en/brelochs-1542-preface-en.xml) | [Source](../tei/brelochs-1542-preface.xml) |
| 1547 | [Read](en/brelochs-1547-preface-en.md) | [XML](en/brelochs-1547-preface-en.xml) | [Source](../tei/brelochs-1547-preface.xml) |
| 1557 | [Read](en/brelochs-1557-preface-en.md) | [XML](en/brelochs-1557-preface-en.xml) | [Source](../tei/brelochs-1557-preface.xml) |
| 1558 | [Read](en/brelochs-1558-preface-en.md) | [XML](en/brelochs-1558-preface-en.xml) | [Source](../tei/brelochs-1558-preface.xml) |
| 1559 | [Read](en/brelochs-1559-preface-en.md) | [XML](en/brelochs-1559-preface-en.xml) | [Source](../tei/brelochs-1559-preface.xml) |

## Translation approach

The translations aim at complete, faithful, readable English, including addresses, salutations, dates and signatures. Editorial paragraphs and punctuation make long German sentences readable; printed lineation remains available in the German TEI. A second AI reading checked the translations against all eleven distinct German texts. Independent human collation, external peer review and a critically established German text remain outstanding.

- **Honorifics:** variable abbreviated forms of civic address are generally rendered “Your Worships.” *Stetmeister* is rendered “mayors,” an approximate historical civic title. *Gebietenden* is rendered with “lords in authority” or an equivalent phrase. These are functional English renderings rather than letter-by-letter expansions of the abbreviations.
- **Astrological vocabulary:** predictive *Astronomia/Astronomei* is usually rendered “astrology.” The historical art included celestial motions and their supposed influences; modern disciplinary boundaries must not be imposed on it. *Practica* names the prognostication genre. “Influence,” “inclination,” “compulsion,” and “necessity” retain their different roles in the arguments.
- **Theology:** divine *Fürsichtigkeit* is rendered “providence.” The 1529 discussion retains God's freedom in relation to his customary order, along with the source's strong claims concerning the devout and the wicked. No particular theological opponent is supplied.
- **Historical claims:** medical, mineralogical and cosmological assertions are translated as written. Attributions to named authorities remain Brelochs's attributions unless a note expressly says otherwise.
- **Uncertainties:** brackets mark tentative readings or explanatory supplies; notes identify source problems. The anomalous printed 1535 date is retained. Proposed readings in the translation do not silently amend the German TEI.
- **Dating:** filenames give forecast years. Translated subscriptions retain their earlier dedication dates and feast references. English month names translate the historical German names; no conversion to the Gregorian calendar is performed.

## Alignment and verification

Each English TEI `div` of type `translationSegment` links through `@corresp` to the first and last German `xml:id` in an **inclusive** source-line interval. One target denotes a single-line interval. These are paragraph- or passage-level correspondences, not word-level equivalences. Ranges account for every transcribed line exactly once and in source order. Markdown reading copies link to the corresponding source passage and page images.

The English XML files validate against the bundled TEI All RELAX NG schema. Coverage and link checks help detect missing material and broken references; they do not establish translation accuracy. See [validation-report.txt](validation-report.txt), [manifest.csv](manifest.csv) and [source-checksums.json](source-checksums.json).

## Editing and regeneration

Edit [data/english-translations.json](data/english-translations.json) and run `python3 build_translations.py` (Python 3.9+ and `lxml`). This rebuilds the twelve English XML files, twelve Markdown reading copies, manifest, input checksums and validation report. The JSON contains the authoritative English wording and editorial notes. The German witnesses and source images are not rewritten.

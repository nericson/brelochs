# Changing defenses, changing critics? Anton Brelochs’s dedicatory prefaces, 1528–1559

Working research report • 24 October 2026 • AI-assisted, single-reader exploratory analysis

**Finding:** The retrieved prefaces support a change in the selection and elaboration of Brelochs’s defensive arguments. They do **not yet establish a chronological change in the actual objections made by his critics**. The strongest model is a recurring apologetic repertoire, deployed differently in different years, rather than a succession of discrete controversies. This qualified result makes the proposed investigation worth pursuing, especially through the missing 1548 preface and independently surviving criticism.

This report analyzes all eleven distinct annual dedication texts in the existing collection. The second 1535 witness is treated as corroborating copy evidence, not a twelfth independent observation. No primary text for 1548 was retrieved or coded. References below identify the forecast year, leaf and transcribed line numbers; these correspond to the `xml:id` values in the adjacent TEI. Dates of dedication are generally earlier than forecast years. English renderings are working translations; ellipses and joined line-break words are editorial.

## 1. Method and inferential limits

### Research questions and rival explanations

The user's hypothesis can be divided into two propositions:

- **H1: Defensive strategy changes.** The topics, authorities, imagined objections or forms of persuasion differ across the series.
- **H2: Criticism changes.** These differences reflect changes in objections actually voiced by contemporaries.

H1 can be tested directly against the prefaces. H2 requires an additional inference: an author's defense is an interested representation of the controversy, not a transcript of it. Even explicit reports of criticism remain testimony by the person being criticized.

Three rivals are tested: **repertoire reuse** (old arguments recur without a new controversy), **paratextual economy** (short presentation letters have less room for defense), and **professional or patronal positioning** (different arguments serve the author's role and intended audience). The surviving sample is determined by retrieval, not random selection. No significance test, trend regression or claim of population frequency is appropriate.

### Procedure actually followed

1. Read all twelve TEI witnesses and their editorial documentation. Separate forecast year from the dedication's stated date; retain the unresolved 1535 date and the uncertain 1528 date.
2. Segment twenty-five relevant passages into argument units. Code topic, evidential relation to criticism, authorial response and a competing interpretation. Short dedicatory texts receive explicit negative-observation records rather than disappearing from the analysis.
3. Compare units across years, including counterexamples to a linear sequence. Compare the 1531/1538 presentation formula, 1547/1557 warning argument, 1528/1529 nonnecessity qualification, and 1528/1558 preventive utility.
4. Reinspect nine source images containing the central arguments: both 1528 leaves, both 1529 leaves, 1542 A1v, 1547 A1v, 1557 A2r, and 1558 A2r–v. This is targeted image checking, not independent collation of every character of the corpus.
5. Generate a line register, coded evidence table, annual matrix, input checksums, and limited mechanical reuse aid. These are reproducible using `python3 build_evidence.py`; substantive coding remains an explicit human-reviewable judgment.
6. Consult scholarship to contextualize the genre and identify material omissions. Keep secondary testimony about unretrieved editions separate from primary observations.

### Evidence classes

| Code | Meaning | Permissible conclusion |
|---|---|---|
| E | Author explicitly reports disparagement or an objection | Brelochs says criticism existed; its independent truth and representativeness remain unverified |
| R | Author formulates an objection conditionally | The objection is explicitly staged, but not necessarily reported from an opponent |
| I | An objection can be inferred from a defense or qualification | A possible implied polemic, also compatible with exposition or conventional apology |
| E-behavior | Author reports rejection in behavior, such as ignoring warnings | Evidence of a represented audience response, not a proposition asserted by a critic |
| N | No developed defense in the selected dedication | Local silence only, not evidence of absent controversy |

Multiple topics may occur in one unit. Classes describe the relation to external criticism, not the explicitness of Brelochs's own assertions. For example, the noncompulsion claim in 1542 is explicit, but a critic's determinist accusation is only inferred. The codebook was developed during this reading; this is not a preregistered or independently double-coded study. A future reader should code independently before consulting these conclusions and record disagreements, especially R versus I.

## 2. Chronological results

| Forecast year | Stated dedication date | Dominant rhetorical work | Evidence concerning critics |
|---|---|---|---|
| 1528 | 1527; day/month reading provisional | Created cosmic order, learned authorities, preventive usefulness | Implied objections only |
| 1529 | 24 June 1528 | Reputation of practicas; divine freedom; Christian trust | Explicit report of disrepute; theological objection conditionally staged |
| 1531 | 12 June 1530 | Brief presentation to civic patrons | No developed defense |
| 1532 | 27 August 1531 | Brief presentation to civic patrons | No developed defense |
| 1535 | 2 August 1535 as printed; unresolved | Annual custom and favorable reception | No developed defense |
| 1538 | 13 July 1537 | Brief presentation; related to 1531 | No developed defense |
| 1542 | 4 July 1541, St. Ulrich | Disciplinary dignity, noncompulsion, medical expertise | Explicit report of contempt, without a specified counterargument |
| 1547 | 15 May 1546 | Calamities validate warnings; audience fails to reform | Reported neglect and stubbornness, not explicit anti-astrological argument |
| 1557 | 8 June 1556 | Reprise of 1547 warning argument | Repeated complaint about reception |
| 1558 | 24 June 1557 | Regular celestial movements, contingent earthly effects, preventive action | Implied objections only |
| 1559 | 23 April 1558 | Annual custom and presentation | No developed defense |

These are descriptive groupings, not chronological periods with established boundaries. Within eleven texts, six contain developed legitimation or admonition; five are primarily presentation letters. Only 1529 and 1542 explicitly report disparagement. The two warning texts form a separate category, because indifference is not equivalent to doctrinal or epistemological criticism.

### 1528: legitimacy and usefulness already include contingency

The earliest retrieved dedication presents astronomy/astrology as knowledge of God's created order. The heavens are readable, with authorization drawn from a large company of ancient, biblical and Christian authorities (A2r, lines 6–25; U01). This is Brelochs's deployment of attributed authorities: their exact source passages and attribution accuracy have not been established here. His word *Astronomei* should not be mapped mechanically onto the modern disciplinary distinction between astronomy and astrology.

The crucial qualification occurs on A2v, lines 1–10 (U03). The art helps a person prevent harm or endure what cannot be avoided. The forecast is published “Nit das es von nöten sey allwegen / also zů beschehn/sonder zu eyner warnung”: **not because it must always happen that way, but as a warning**. These lines rule out treating the later conditional model as a wholly new retreat from an initially absolute determinism.

An implied opponent might deny that knowledge of the future is permitted or useful. But the preface does not identify that opponent or say that such a charge has just been made. The positive argument is compatible with standard legitimation of the annual publication.

### 1529: a sharp theological defense, but distinguish report from construction

This dedication supplies the corpus's clearest report of criticism. German practicas have had a bad reputation among high and low and have been regarded as “lügen / büchlein” (A1v, lines 5–8; U04): **little books of lies**. That is evidence of represented disrepute. It does not tell us whether the alleged falsehood consisted in failed forecasts, fraudulent methods, theological error, or some combination.

Brelochs then constructs a conditional concession: if astrology bound God's power and providence within its own rules, criticism would be justified (A1v, lines 8–22; U05). He answers by distinguishing the ordinary order of created effects from a constraint upon the Creator. Knowledge and action belong under Christ, and the natural order remains God's own operation (U06–U07).

On A2r, lines 1–10 (U08), the issue becomes fear and trust. The pious ought to fear God rather than threatening stars; favorable stellar indications cannot rescue the wicked from their misuse of prosperity. This is more than a technical disclaimer: astrology is assigned a subordinate place within Christian life.

The defensible conclusion is that **1529 gives exceptional prominence to Christian legitimacy and divine freedom**. It would overstate the evidence to identify a particular reformer, confessional party, or recent sermon as its target. No such identification is supplied by these lines. Nor does the report of lying booklets independently establish the exact theological reasoning that follows it.

### 1531–1538: brevity is a real alternative explanation

The retrieved 1531, 1532, 1535 and 1538 dedications emphasize modest ability, customary annual service, and favorable reception by Schwäbisch Hall's magistrates. The 1531 and 1538 texts share the sequence of undertaking a forecast, reporting what the heavens signify, condensing it into a prognostication, and presenting it to the same patrons (U10, U13).

They provide no developed polemical propositions. This is not evidence that the criticism ceased. These texts are also much shorter: their normalized token proxies are 124–135, against 782 for 1529. Layout alone is misleading: 1535 has 27 transcribed lines but only 134 token units because its closing text narrows typographically. The 1559 dedication returns to the same broadly presentational mode. That late counterexample prevents a narrative of steadily escalating defensive complexity.

### 1542: the author's medical authority becomes central

Brelochs condemns the contempt shown by “etliche neydige geschwetzige menschen” (A1v, line 10; U14), **some envious, talkative people**. This is explicit hostility, but neither a named party nor a quotation of its reasoning. His ascription of envy is itself polemical, not a diagnosis historians should adopt uncritically.

His response distinguishes inclination from compulsion: “das ge / stirn alleyn naygt vnd nit nöttigt” (lines 13–14; U15), **the stars only incline and do not compel**. He then accumulates observations and authorities connected to birth, illness, plants, minerals and remedies (lines 18–35; U16). Within his argument, hidden natural properties provide a basis for effects not reduced to ordinary hot/cold or wet/dry qualities. These are historical claims, not findings endorsed by this report.

The strongest novelty relative to the retrieved early dedications is the concentration on **medical expertise and the physician's obligation to know the stars**. The text establishes a shift in professional legitimation. It does not establish that critics had newly become physicians or that a specific medical controversy caused the shift. The continuing noncompulsion qualification also links this preface to earlier restrictions on necessity.

### 1547 and 1557: resistance becomes failure to heed warnings

The 1547 dedication combines Ptolemaic authority, a list of familiar calamities and the claim that warnings have already been given. Its charge is that people do not take them to heart. Church admonition about sinful life is explicitly included, and the response is increasing stubbornness (A1v, lines 14–25; U18).

The rhetoric shifts the reader's attention from **whether the art may speak** to **whether its audience will respond**. This lends the astrologer's warnings a relationship to religious admonition without requiring us to treat him as claiming the inspired authority of a biblical prophet. It also does not identify a specific war, epidemic, or failed prediction: generic lists cannot supply that historical identification on their own.

The 1557 text repeats the same extended argumentative sequence (A2r, lines 10–24; U19–U20). It is shorter and omits the earlier expansion about rebuke in church, while retaining the prophetic comparison and stubbornness. This is strong evidence of textual relationship. Whether Brelochs copied his 1547 wording directly, used an intermediary annual version, or reused a common source remains unresolved.

Accordingly, these cannot be treated as two independent signs of newly emerging criticism. Their ten-year separation actually strengthens the repertoire explanation. The omission of the church passage is observable; a motive such as secularization is not. Nor is there warrant to infer a specific conflict in the forecast year 1547 when its dedication is dated May 1546.

### 1558: a developed account of why effects may be prevented

The opening rhetorical questions concern the inability of human beings to reverse heavenly motions or prevent eclipses. God alone is excepted (A2r, lines 10–28, continuing A2v, line 1; U21). This must be read with the next page: immutable-by-human-action heavenly movements do not entail irresistible terrestrial effects.

A2v, lines 12–20 (U23), describes contrary and stronger causes that may overcome indicated outcomes. The examples are garlic supposedly inhibiting a magnet and treatment preventing a wound's decay. Their function is explanatory analogy: a real natural tendency can be obstructed. Navigation, agriculture and husbandry then support the practical value of celestial knowledge, and the wise person may avert harm (lines 21–33; U24).

This is compatible with an implied answer to **why an indicated event sometimes fails to occur**. But there is no actual report of a failed prediction or a critic making that argument. It also develops, rather than invents, the preventive usefulness already articulated in 1528. Creation, God and the Redeemer remain explicit (U22): the contrast with 1529 is not a clean movement from theology to secular natural science.

## 3. Repetition, controls and sensitivity checks

| Test | Result | Consequence |
|---|---|---|
| Count the second 1535 copy separately? | Its transcribed dedication is text-identical | Count once for chronological inference |
| Restrict evidence to explicit disparagement (E) | Only 1529 and 1542 qualify | Actual change in critics' propositions cannot be reconstructed from this subset |
| Add explicit audience nonresponse (E-behavior) | Adds 1547 and 1557 | Expands reception evidence, but does not establish new arguments against astrology |
| Include inferred objections (I) | Makes the different emphases visible | Supports H1; H2 remains underdetermined |
| Compare long texts only | 1528, 1529, 1542, 1547, 1557, 1558 still differ | Brevity cannot explain every contrast |
| Compare late to early contingency claims | 1528 already allows prevention and nonnecessity | Reject a claim that contingency first emerges in 1558 |
| Treat 1547/1557 as one rhetorical family | Repeated admonition loses independent novelty | Favor recurrence over a smooth trajectory |
| Include short 1559 dedication | Extended defense disappears again | Reject monotonic increase in defensive elaboration |

The mechanical token-run file is only an aid to inspection. It detects exact runs after lowercasing, u/v and i/j conflation, diacritic removal and limited hyphen joining. It neither resolves historical spelling comprehensively nor detects all shared argument. For example, the clear conceptual relationship of 1528 and 1558 produces no substantive long exact run under this procedure. This is why keyword totals or a similarity score cannot substitute for the close reading.

All dedications address the civic leadership of Schwäbisch Hall, providing a relatively stable patronal frame. However, this is not proof of an unchanged reading public. Printer, format, typesetting, available space, and the choice between dedication and reader-address can alter what appears in this particular paratext. Only one retrieved 1542 printing is analyzed; the other printing needs collation.

## 4. Historical context and the consequential gap

Jonathan Green describes theological qualifications and defenses as common features of the practica genre. More decisively for this project, he reports that **Brelochs's 1548 practica answers a charge of necromancy** and identifies the passage as **VD16 ZV 2416, a1v**. See *Printing and Prophecy*, pp. 112–13, 131–32, and p. 234, chapter 6, note 5. This is secondary testimony, not an observation added to the eleven-text coding matrix.

The 1548 lead could materially alter the current picture: a supernatural or illicit source of prediction would differ from the medical and reception emphases of 1542 and 1547. Yet its appearance in 1548 would still not prove that the accusation was new then. The primary text must establish whether Brelochs reports an actual accusation, stages an objection, or offers a general disclaimer.

Herbst's entry identifies 1548 copies at Wolfenbüttel (HAB, A: 125.34 Quod. (7)) and Erlangen. No reproduction request has been sent. The earlier collection's references to Green's appendix as p. 162 should be checked: the Brelochs list in the consulted PDF is on printed p. 161. Its copyright page gives 2012, whereas some online metadata uses 2011; this report cites the inspected edition's 2012 date.

These contextual checks do not identify the critics behind 1529 or 1542. The report therefore makes no causal claim about a particular Reformation episode or political event. Such a claim would require independently dated local or printed evidence, not merely chronological proximity.

## 5. Verdict and next tests

**H1 is supported at an exploratory descriptive level.** The selected defenses change in emphasis: broad cosmic authorization; concentrated Christian-theological legitimation; professional-medical justification; admonition about neglected warnings; and a more elaborated account of counteracting causes. These are emphases in a repertoire, not mutually exclusive stages.

**H2 remains plausible but unproven.** The corpus gives too little independently specified criticism, is interrupted by large retrieval gaps, and includes significant reuse. The stronger claim that criticism underwent a directional change—from theological to empirical, for example—is not supported. The late evidence remains theological, while the early evidence already includes contingency and utility.

A defensible provisional thesis is: **Brelochs repeatedly adjusted the presentation of an enduring defense of useful, conditional astrology. His prefaces reveal changes in the objections he chose to answer and the authority he chose to invoke more securely than they reveal changes in the objections actually voiced by his contemporaries.**

The next phase should prioritize:

1. **1548 a1v and surrounding opening leaves**, then its first chapter, to establish the necromancy argument and whether the dedication boundary captures it.
2. **1530** to test persistence after 1529; **1543–1546** to bridge medical legitimation and admonition; **1553 and 1556** to trace the 1547/1557 textual family. These are targeted comparisons, not a presumption of what missing years contain.
3. Other printings, particularly **1542**, to separate authorial variation from printing-specific paratext.
4. Full-practica reading: an apparently nonpolemical dedication may coexist with apologetic material later in the booklet. This study cannot infer whole-work silence.
5. Independent criticism: dated counter-practicas, letters, sermons and civic records with a demonstrable connection to Brelochs or the local controversy. Do not assign a famous contemporary as his target merely because the objection sounds similar.
6. Independent transcription collation and a second coding pass. Preserve disagreement rather than silently reconciling it; revise H2 only when external testimony can be aligned with the author's response.

A finding that missing intervening texts repeat the same defenses would weaken a change-in-criticism account. A sequence of independently dated objections followed by specific new rebuttals would strengthen it. These are different evidential outcomes and should remain so in the eventual article.

## Sources and audit files

Primary sources: the twelve XML witnesses and associated page images in this directory's parent; bibliographic particulars and source URLs in `../manifest.csv`. The analysis is based on the files identified by `input-checksums.json`, not an assumed later version.

- Green, Jonathan. *Printing and Prophecy: Prognostication and Media Change 1450–1550*. Ann Arbor: University of Michigan Press, 2012. [Consulted digitization](https://tile.loc.gov/storage-services/master/gdc/gdcebookspublic/20/20/70/73/92/2020707392/2020707392.pdf). Printed pagination cited above; PDF page indices differ.
- Herbst, Klaus-Dieter. “Brelochs, Anton.” *Biobibliographisches Handbuch der Kalendermacher*. [Entry](https://www.presseforschung.uni-bremen.de/dokuwiki/doku.php?id=brelochs_anton). Accessed October 24, 2026. Used for the 1548 holding leads, not as a substitute for its text.

Companion files: `coded-passages.csv` (25 units with quotations and XML line identifiers); `year-matrix.csv` (11 annual observations); `line-register.csv` (all dedication lines, including the alternate copy); `shared-token-runs.csv` (limited exact-match aid); `build_evidence.py` (regeneration); `input-checksums.json` (provenance); `README.md` (usage and coding rules).

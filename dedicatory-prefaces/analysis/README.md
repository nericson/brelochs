# Comparative analysis of the dedicatory prefaces

Start with the [census-based reassessment](CENSUS-REASSESSMENT.md), including the line-linked 1533 French evidence.

Start with the [completed hypothesis test and methodological reassessment](HYPOTHESIS-TEST.md), updated November 20, 2026. [REPORT.md](REPORT.md) preserves the initial annual readings and 25-unit analysis. This is an exploratory, single-reader study of changing defensive strategies and implied criticism, not an independently reviewed historical conclusion.

## Reproduce and audit

Run `python3 build_evidence.py` from any directory (Python 3.9+; standard library only). It reads the adjacent `../tei` files and overwrites the generated CSV/checksum files here. It does not alter the TEI or images. Before rerunning against edited TEI, preserve the old checksums if you need the original research snapshot.

- `coded-passages.csv`: selected argumentative units, exact line ranges, transcribed text, topic codes, interpretation and alternative reading. Overlap at an argument transition is intentional; units are not independent observations or counts of criticism.
- `line-register.csv`: every transcribed line for audit; the argument selection is not a new complete transcription.
- `year-matrix.csv`: the eleven forecast years; duplication of the 1535 witness is excluded. The 1528 date remains tentative and the anomalous 1535 printed date is not silently corrected. Other dates follow subscriptions, with feast names converted where straightforward; they are not publication dates.
- `shared-token-runs.csv`: exact normalized runs of at least five tokens for four selected comparison pairs. Zero-based offsets refer to normalized token arrays, not XML line numbers. Greedy sequence alignment is an inspection aid, not an exhaustive or statistically calibrated reuse detector. Formulas in addresses and signatures are retained and must not be mistaken for shared substantive argument.
- `input-checksums.json`: SHA-256 hashes of all twelve TEI inputs.

## Coding rules

The evidence class concerns what can be said about critics, separately from what Brelochs explicitly asserts. E = reported disparagement; R = conditionally constructed objection; I = inferred objection; E-behavior = reported audience conduct rather than a critic's proposition; N = no developed defense in this dedication. None supplies independent corroboration of an opponent.

Topic families are descriptive: legitimacy (CREATION, AUTHORITY, CHRISTIAN_LEGITIMACY); theological limits (DIVINE_FREEDOM, FEAR); natural knowledge (CAUSALITY, NATURAL_ORDER, NATURAL_CAUSALITY, CELESTIAL_REGULARITY); professional status (DISCIPLINARY_STATUS, MEDICAL_AUTHORITY); limits and use (HUMAN_NONCOMPULSION, CONTINGENCY, COUNTERCAUSES, UTILITY, PREVENTION); reception (TRUTHFULNESS, RETROSPECTIVE_VALIDATION, UNHEEDED_WARNING, REPENTANCE); presentation (DEDICATION). These topic labels identify the author's rhetorical work and must not be automatically turned into accusations attributed to contemporaries.

A developed argument requires a reason for legitimacy, causal knowledge, utility or moral reception beyond announcing the annual forecast and requesting acceptance. Developed-argument flags are manually assigned. Reported-disparagement flags require an explicit statement that others disparage the art or its publications. Absence is only absence in this retrieved dedication. Do not interpolate missing years, infer the first occurrence of an argument, or count copies as independent texts.

## Verification scope

All twelve TEI texts were read; nine argument-bearing images were visually checked during this study (listed in the report). These checks support the thematic reading but are not a new full collation. The original working transcriptions retain their first-pass status and uncertainties. The 1548 lead is explicitly external and uncoded.

No remote publication is implied by the presence of these local files. The original report and transcription set were synchronized on GitHub. The 1548 follow-up and English translations are subsequent additions; publication should be checked against the repository history.

## November reassessment

[HYPOTHESIS-TEST.md](HYPOTHESIS-TEST.md) develops the method and findings with the complete English translations. [implied-objections.csv](implied-objections.csv) distinguishes authorial form, critic attribution and inference limits in ten records. Regenerate this register with `python3 build_polemic_register.py`. [review-log.md](review-log.md) documents two additional primary-text AI readings and the resulting refinements; their source comparisons are retained in [reviews/](reviews/). No independent human corroboration or statistical inter-rater reliability is claimed.

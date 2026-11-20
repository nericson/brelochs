# Anton Brelochs — dedicatory prefaces, TEI-XML

Version 0.1 • 24 October 2026 • First-pass visual transcriptions for scholarly review

## Expanded census and analysis

The [forecast-year census](census/README.md) documents 26 years. The [Geneva 1533 dossier](comparanda/1533-geneva/README.md) adds the French address, facsimiles, TEI and English translation. The [revised polemic study](analysis/CENSUS-REASSESSMENT.md) compares it with the German dedications below.

## German dedication corpus

Eleven forecast years: 1528, 1529, 1531, 1532, 1535, 1538, 1542, 1547, 1557, 1558, 1559. There are **12 independent TEI documents**: one per year, plus the alternate Augsburg copy of 1535. The latter appears to reproduce the same setting and text, not another distinct dedication or edition. It was compared visually with the primary Munich image and retains separate copy metadata.

These are transcriptions of all dedications in the previously assembled image collection. They are **not all surviving Brelochs editions**. Missing editions in that collection remain outside this transcription set. Years in filenames are the years forecast, not necessarily the dates of printing or of the dedication.

## Files

- `tei/`: UTF-8 TEI P5 XML documents, editable in an XML editor such as Oxygen.
- `images/`: 18 source page images (17 primary images plus the alternate 1535 page), making facsimile references usable offline.
- `manifest.csv`: file, year, line/page counts, holding library, shelfmark, source URL, and validation status.
- `source-index.json`: repository and page-image provenance inherited from the earlier collection, with the alternate copy added.
- `review-readings.csv`: explicitly uncertain readings and their XML line identifiers. This is not an exhaustive list of possible errors.
- `schema/tei_all.rng`: TEI All RELAX NG schema downloaded from the TEI Consortium on 24 October 2026.
- `validation-report.txt`: structural validation results and schema checksum.

## Editorial approach

This is a **semi-diplomatic working transcription**, visually read from the scans with AI assistance. It is not yet an independently collated critical edition. Review against the images before quotation, publication, or quantitative linguistic analysis. Schema validation establishes XML conformity, not textual accuracy.

Historical spelling, capitalization, u/v, i/j and punctuation are retained as read. Long s is rendered as ordinary s; ordinary typographic ligatures are decomposed. Superscript vowels are represented with Unicode diacritics where recognized. Spacing is regularized, particularly around virgules. Printed line-division marks appear as hyphens or slashes; no automatic dehyphenation has been performed. Abbreviation strokes are retained as combining tildes where recognized rather than systematically expanded. Some tiny abbreviation marks and vowel forms may require correction on collation.

Every transcribed printed line begins with `<lb>` and has a unique `xml:id`. `<pb>` marks a page change and points through `@facs` to a `<surface>` containing both a local image reference and an online source. Line numbers restart on each page and count only the transcribed dedication lines. Inferred leaf labels are identified as such in the headers. Heading, paragraph and subscription boundaries are editorial.

`<unclear>` identifies a tentative reading. `<abbr>` identifies a retained abbreviation where explicitly encoded; retained abbreviation strokes elsewhere are not exhaustively tagged. `<sic>` marks the retained date in 1535, without imposing a correction. Unmarked text is also provisional. No modernized German text is supplied. Complete working English translations are now available separately in [translations/](translations/README.md).

Catchwords, printed leaf signatures, ornaments, library stamps and subsequent annotations are omitted. Portions of the main prognostication appearing below a dedication on the same image are excluded. The short statement about division into eight chapters in 1559 is retained because it appears before the authorial signature; corresponding post-signature transitions in 1532, 1538 and 1542 are outside the selected dedication boundary.

## Specific review points

- **1528:** dense impression; inspect the opening terminology, some astronomical vocabulary, the date numerals, abbreviation strokes and superscript vowels. The uncertain readings are explicitly flagged.
- **1529:** this is the WLS copy, shelfmark BF1683 .B74 1529. The theological discussion is transcribed without modernization. Review faint lower lines of A1v and the uncertain adjective before `gestirn`.
- **1535:** both copies visibly print `M. D: XXXV.` in the dedication. That date is preserved, without assuming that it should be 1534.
- **1538:** the contracted author name is retained rather than expanded; consult the scan before adopting a normalized form.
- **1542:** a cramped word after `Meyster/` is uncertain, and a contracted article near the Mesue reference is retained as an abbreviation.
- **1558:** the unclear ending after `liebe` is flagged. The dedication spans three pages; the third contains the date and subscription before the main text begins.

## Repositories and reuse

Page images are included unchanged from the previous image package. Historical printed texts are public domain. Preserve repository credits and consult the linked repositories for image-use conditions. Holding institutions include WLS, Augsburg, Munich, Heidelberg, Kiel, and Dresden. Bibliographic metadata is inherited from the earlier collection, not independently recatalogued here. No new publication-date inference has been made from a forecast year.

TEI schema source: https://tei-c.org/release/xml/tei/custom/schema/relaxng/tei_all.rng

To validate an edited XML file, use its `xml-model` association with the bundled schema. Keep the `tei`, `images`, and `schema` directories together so relative references continue to resolve.

## Comparative research

See [analysis/HYPOTHESIS-TEST.md](analysis/HYPOTHESIS-TEST.md) for the completed comparative hypothesis test and [analysis/REPORT.md](analysis/REPORT.md) for the initial exploratory study of changing defensive strategies, implied criticism, textual reuse and the missing 1548 preface. The [analysis directory](analysis/) includes passage-level coding and reproducible evidence tables.

## English translations

[Read the English translations](translations/README.md), available as Markdown and source-aligned TEI-XML for all twelve witnesses (eleven years, including the alternate 1535 copy). Translation notes preserve uncertainties and the original forecast/dedication date distinction. These are working scholarly translations from the provisional German transcriptions.

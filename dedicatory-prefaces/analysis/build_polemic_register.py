"""Generate the objection register and test its links to the unchanged German TEI.

This is declared interpretive coding, not an automatic detector of polemic.
Python 3.9+ standard library only. Run from any working directory.
"""
from pathlib import Path
from xml.etree import ElementTree as E
import csv
ROOT=Path(__file__).resolve().parent
N={'t':'http://www.tei-c.org/ns/1.0'}
X='{http://www.w3.org/XML/1998/namespace}id'
# An inclusive line interval grounds the observation; it does not make the inferred
# opponent proposition a quotation or an assertion by an independently known critic.
DATA=[
('O01','1529','E','Practicas are regarded as lying booklets.','genre credibility','line-1529-1-6','line-1529-1-8','U04','Brelochs reports a bad reputation among high and low.','Subsequent conditional concession separates legitimate astrology from claims that would constrain God.','The report is explicit, but reasons for the alleged falsehood and identities of critics remain unspecified.'),
('O02','1529','R','Astrological rules would constrain divine omnipotence and providence.','theological permissibility','line-1529-1-8','line-1529-1-22','U05','Brelochs explicitly formulates the objection conditionally.','God works through a created order without being imprisoned in it.','A staged concession cannot be assigned to a particular historical opponent without other evidence.'),
('O03','1529','I','Celestial knowledge or fear might displace Christian trust.','religious orientation','line-1529-1-23','line-1529-2-10','U06;U07;U08','The source explicitly subordinates action to Christ and tells the pious not to fear stellar threats.','Trust and fear properly concern God; favorable indications cannot benefit wicked misuse.','These are also affirmative Christian instruction; no accusation of idolatry or fearmongering is reported.'),
('O04','1542','E','The art is held in contempt.','disciplinary standing','line-1542-1-6','line-1542-1-11','U14','Brelochs reports repeated contempt by people he calls envious and talkative.','Daily experience warrants acceptance of astrology among the arts.','The alleged motive of envy is his characterization; the critics profession and reasoning are unknown.'),
('O05','1542','I','Celestial government might compel human dispositions or behavior.','human noncompulsion','line-1542-1-11','line-1542-1-17','U15','The author explicitly disclaims coercion and affirms inclination.','Stars incline rather than compel; observed character is treated as evidence of influence.','The anticipated determinist objection is inferred; the text does not report its recent occurrence.'),
('O06','1542','I','Astrological causes lack a natural or medically warranted basis.','natural knowledge and professional competence','line-1542-1-18','line-1542-1-36','U16','Examples from illness, plants, minerals and drugs support the physicians need for astrology.','Learned medicine and hidden natural properties authorize celestial influence.','A positive professional justification is not proof of a new controversy among physicians; causation was already defended in 1528 and 1529.'),
('O07','1547','E-behavior','People fail to heed warnings and amend their lives.','audience response','line-1547-1-15','line-1547-1-25','U18','Warnings and ecclesiastical admonition are represented as meeting stubbornness.','The prophetic comparison transfers attention to the audiences response.','Audience conduct is not an objection to astrology; the plural first person also includes the author in the rebuke.'),
('O08','1557','E-behavior','People fail to heed warnings and become more obstinate.','audience response','line-1557-1-19','line-1557-1-24','U20','A closely related sequence reappears ten forecast years later.','Retains the prophetic comparison while abbreviating the earlier church-rebuke passage.','Reuse reduces independence but does not rule out renewed contemporary pressure or relevance.'),
('O09','1558','I','A natural stellar indication may fail to issue in the expected earthly effect.','conditional effects and prediction','line-1558-2-12','line-1558-2-20','U23','The author explains how stronger counteracting causes can prevent effects.','Magnet/garlic and wound/treatment analogies make obstruction intelligible.','No particular failed forecast or critic is reported; the exact construction about the higher bodies remains uncertain.'),
('O10','1528','I','Forewarning would be useless if harm could not be averted.','practical utility','line-1528-2-1','line-1528-2-10','U03','Prevention and warning rather than necessary fulfillment are explicit authorial claims.','Astrological knowledge permits avoidance of harm; also developed in 1558 A2v21-29 (U24).','Usefulness can be explained without answering an actual opponent; the clause at A2v2-3 is uncertain, but A2v5-6 independently states prevention.')
]

FORMS={
'O01':('reported adverse judgment','reported by Brelochs; independently uncorroborated'),
'O02':('conditional concession','author-constructed possible objection'),
'O03':('explicit theological boundary and positive instruction','analyst-inferred objection'),
'O04':('reported contempt','reported by Brelochs; grounds unspecified'),
'O05':('explicit disclaimer and distinction','analyst-inferred external accusation'),
'O06':('positive causal and professional warrant','analyst-inferred objection'),
'O07':('claim of neglected warnings','audience conduct; no critic proposition'),
'O08':('claim of neglected warnings','audience conduct; no critic proposition'),
'O09':('explicit causal qualification','analyst-inferred objection'),
'O10':('positive utility warrant and nonnecessity disclaimer','analyst-inferred objection')
}
rows=[]
for code,y,cls,proposition,target,start,end,units,observation,response,limit in DATA:
    p=ROOT.parent/'tei'/f'brelochs-{y}-preface.xml';tree=E.parse(p)
    ids=[e.get(X) for e in tree.findall('.//t:body//t:lb',N)]
    assert start in ids and end in ids and ids.index(start)<=ids.index(end)
    rows.append(dict(record=code,forecast_year=y,evidence_class=cls,authorial_form=FORMS[code][0],critic_attribution=FORMS[code][1],candidate_objection_or_response=proposition,target=target,start_id=start,end_id=end,original_units=units,textual_observation=observation,defense=response,inference_limit=limit))
with (ROOT/'implied-objections.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('PASS: 10 interpretive register records; all inclusive source intervals resolve in document order.')
print('Classes concern source of evidence, not proof that an external critic held the candidate proposition.')

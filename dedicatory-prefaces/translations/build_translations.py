#!/usr/bin/env python3
"""Build English reading copies and TEI; validate coverage, source links and TEI P5.

Requires Python 3.9+ and lxml. Editorial content lives in data/english-translations.json.
"""
from pathlib import Path
import csv, hashlib, json, re
from lxml import etree as E
ROOT=Path(__file__).resolve().parent
BASE=ROOT.parent
NS='http://www.tei-c.org/ns/1.0'
XML='http://www.w3.org/XML/1998/namespace'
N={'t':NS}
DATE='2026-11-20'

def el(parent,tag,text=None,**attrs):
    node=E.SubElement(parent,'{'+NS+'}'+tag,**attrs)
    if text is not None:node.text=text
    return node

def block(parent,text):
    for para in text.split('\n\n'):
        el(parent,'p',para)

def main():
    (ROOT/'en').mkdir(exist_ok=True)
    data=json.loads((ROOT/'data/english-translations.json').read_text())
    schema=E.RelaxNG(E.parse(str(BASE/'schema/tei_all.rng')))
    manifest=[];logs=[];hashes={}
    expected={p.stem.removeprefix('brelochs-').removesuffix('-preface') for p in (BASE/'tei').glob('*.xml')}
    assert {d['witness'] for d in data}==expected,'Missing or extra translations'
    for d in data:
        key=d['witness'];year=d['year'];stem=f'brelochs-{key}-preface'
        src=BASE/'tei'/f'{stem}.xml'
        tree=E.parse(str(src));source_lines=src.read_text().splitlines()
        source_ids=[x.get('{'+XML+'}id') for x in tree.findall('.//t:body//t:lb',N)]
        # Interval correspondences identify all lines in the inclusive range, not just endpoints.
        all_covered=[]
        for seg in d['segments']:
            a=source_ids.index(seg['start']);b=source_ids.index(seg['end'])
            assert a<=b and seg['text'].strip(),(key,seg)
            all_covered+=source_ids[a:b+1]
        assert all_covered==source_ids,f'{key}: omitted, duplicate, or unordered source lines'
        hashes[src.name]=hashlib.sha256(src.read_bytes()).hexdigest()
        tei=E.Element('{'+NS+'}TEI',nsmap={None:NS});tei.set('{'+XML+'}id',f'brelochs-{key}-en')
        header=el(tei,'teiHeader');fd=el(header,'fileDesc');ts=el(fd,'titleStmt')
        el(ts,'title',f'Anton Brelochs: English translation of the dedicatory preface for {year}'+(' — alternate Augsburg witness' if 'Augsburg' in key else ''))
        el(ts,'author','Anton Brelochs')
        rs=el(ts,'respStmt');el(rs,'resp','AI-assisted English translation and editorial review; scholarly working version');el(rs,'name','OpenAI ChatGPT')
        es=el(fd,'editionStmt');el(es,'edition','Version 0.1. Complete working English translation from the linked semi-diplomatic German transcription.')
        ps=el(fd,'publicationStmt');el(ps,'p',f'Prepared for Nathan Ericson’s Brelochs project, {DATE}. Historical German text is public domain. No independent critical collation or external peer review is claimed.')
        sd=el(fd,'sourceDesc');bibl=el(sd,'bibl');el(bibl,'author','Anton Brelochs');el(bibl,'title',f'Practica Teutsch for {year}: dedicatory preface')
        el(bibl,'date',year,type='forecastYear',when=year)
        el(bibl,'ref','German TEI witness',target=f'../../tei/{stem}.xml')
        for note in tree.findall('.//t:sourceDesc/t:bibl/t:note',N):el(bibl,'note',''.join(note.itertext()))
        enc=el(header,'encodingDesc');ed=el(enc,'editorialDecl')
        el(ed,'p','Complete English translation; spelling and names follow readable English conventions. Your Worships renders the variable civic honorifics approximately; mayors renders Stetmeister without implying identity with a modern mayoralty. Predictive Astronomia/Astronomei is generally translated astrology, with the historical overlap of astronomy and astrology acknowledged. Historical assertions and attributed authorities are translated as presented, without endorsing or authenticating them.')
        el(ed,'p','Editorial English paragraph divisions and punctuation do not reproduce printed lineation. Each translationSegment div has @corresp linking the first and last German xml:id in an inclusive source-line range; a single link denotes one line. The ranges cover all transcribed lines exactly once. Brackets mark explanatory supplies or tentative readings; the end notes discuss uncertainties. Source images and their provenance remain linked in the German TEI. No missing preface is reconstructed.')
        prof=el(header,'profileDesc');lu=el(prof,'langUsage');el(lu,'language','English',ident='en')
        rev=el(header,'revisionDesc',status='draft');el(rev,'change','Initial English translation with source alignment, editorial notes and completeness checks.',when=DATE)
        text=el(tei,'text');text.set('{'+XML+'}lang','en');body=el(text,'body');div=el(body,'div',type='dedication')
        title=''.join(ts.find('t:title',N).itertext());el(div,'head',title)
        md=[f'# {title}', '', f'Working English translation • {DATE} • [German TEI](../../tei/{stem}.xml) • [English TEI]({stem}-en.xml)', '', 'Translated from the provisional German transcription. Editorial notes identify uncertain or supplied readings. Paragraph divisions are editorial.', '']
        images=[]
        for surface in tree.findall('.//t:facsimile/t:surface',N):
            g=surface.find('t:graphic',N)
            if g is not None:images.append(f'[{surface.get("n")}](../{g.get("url")})')
        md+=['Source images: '+', '.join(images), '']
        for i,seg in enumerate(d['segments'],1):
            refs=[f'../../tei/{stem}.xml#{seg["start"]}']
            if seg['end']!=seg['start']:refs.append(f'../../tei/{stem}.xml#{seg["end"]}')
            item=el(div,'div',type='translationSegment',n=str(i),corresp=' '.join(refs));item.set('{'+XML+'}id',f'en-{key}-s{i}')
            block(item,seg['text'])
            a=source_ids.index(seg['start'])+1;b=source_ids.index(seg['end'])+1
            line=next(j for j,s in enumerate(source_lines,1) if f'xml:id="{seg["start"]}"' in s)
            md += [f'<!-- English segment {i}; source range {seg["start"]} through {seg["end"]}, inclusive. -->',seg['text'],'',f'*[German passage, transcribed lines {a}–{b}](../../tei/{stem}.xml#L{line})*','']
        back=el(text,'back');nd=el(back,'div',type='editorialNotes');el(nd,'head','Translation notes')
        md += ['## Translation notes','']
        for i,n in enumerate(d['notes'],1):
            note=el(nd,'note',n['text'],type='translation',n=str(i));note.set('{'+XML+'}id',f'en-{key}-{n["id"]}')
            md += [f'{i}. {n["text"]}','']
        output=E.ElementTree(tei)
        tei.addprevious(E.ProcessingInstruction('xml-model','href="../../schema/tei_all.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"'))
        assert schema.validate(output),(key,str(schema.error_log))
        out=ROOT/'en'/f'{stem}-en.xml'
        out.write_bytes(E.tostring(output,encoding='UTF-8',xml_declaration=True,pretty_print=True))
        (ROOT/'en'/f'{stem}-en.md').write_text('\n'.join(md))
        manifest.append(dict(witness=key,forecast_year=year,german=f'../tei/{stem}.xml',english_tei=f'en/{stem}-en.xml',english_markdown=f'en/{stem}-en.md',source_lines=len(source_ids),aligned_segments=len(d['segments']),status='Working translation; TEI schema valid; complete source-line coverage'))
        logs.append(f'PASS {key}: TEI All RELAX NG; {len(source_ids)} source lines covered once in order; {len(d["segments"])} aligned segments.')
    # Exact duplicate text must remain represented in both witness-specific translations.
    a=next(d for d in data if d['witness']=='1535');b=next(d for d in data if d['witness']=='1535-Augsburg')
    assert [x['text'] for x in a['segments']]==[x['text'] for x in b['segments']]
    (ROOT/'source-checksums.json').write_text(json.dumps(hashes,indent=2)+'\n')
    with (ROOT/'manifest.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=manifest[0]);w.writeheader();w.writerows(manifest)
    logs+=['PASS: all 12 German witnesses have English TEI and Markdown translations.','PASS: alternate 1535 translation wording matches primary witness.','Validation checks structure and interval coverage; it does not establish translation accuracy.']
    (ROOT/'validation-report.txt').write_text('\n'.join(logs)+'\n')
    print('\n'.join(logs))

if __name__=='__main__':main()

#!/usr/bin/env python3
import json
OUT = "/sessions/practical-brave-johnson/mnt/outputs/"
mumis = json.load(open(OUT+"mumis_full.json", encoding="utf-8"))

PDF = "https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/ci_datenbank/"
EDP_URL = "https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf"
NQ_URL = "https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf"

REGION = {"Afrika":"Afrika","Amerika":"Amerika","Asien":"Asien","Europa":"Europa","—":"—"}
CtoR = {  # country -> region (German names)
 "Kolumbien":"Amerika","USA":"Amerika","Mexiko":"Amerika",
 "Kenia":"Afrika","Marokko":"Afrika","Kamerun":"Afrika","Ägypten":"Afrika",
 "Vietnam":"Asien","Syrien":"Asien","China":"Asien","Südkorea":"Asien","Jordanien":"Asien","Iran":"Asien","Indien":"Asien","Bangladesch":"Asien",
 "Rumänien":"Europa","Türkei":"Europa","Spanien":"Europa","Polen":"Europa","Russland":"Europa","Frankreich":"Europa",
 "Arabische Länder":"—","GB & USA":"—",
}

# ---------- unify MuMiS ----------
items = []
for c in mumis:
    items.append({
        "kind":"mumis","collection":"MuMiS","id":c["id"],
        "title":c["name"],"sub":c["fach"],
        "topicMain":"MU:"+c["sitMain"],"topicCode":"MU:"+c["sitSub"],
        "sitMain":c["sitMain"],"sitSub":c["sitSub"],
        "nationality":c["nationality"],"region":c["region"],
        "interaction":c["interaction"],"en":c["en"],
        "themes":[],
        "links":[["de",c["pdf_de"]],["komm",c["pdf_kommentar"]]] + ([["en",c["pdf_en"]]] if c["en"] else []),
    })

# ---------- Eine Frage der Perspektive (30) ----------
EDP_TOPICS = {  # code -> (de,en)
 "RES":("Wohnheim","Residence halls"),"FIN":("Finanzen","Financial matters"),
 "CUL":("Kultur","Culture"),"STU":("Studienorganisation","Study organization"),
 "COM":("Kommunikation","Communication"),"COU":("Beratung","Counselling")}
# (topic, English title, country-de, printed pages)
EDP = [
 ("FIN","A cry for help too late","Kolumbien","40–41"),
 ("FIN","Back rent","Kenia","42–43"),
 ("FIN","Money problems","Vietnam","44–45"),
 ("CUL","The wine tasting","Syrien","46–47"),
 ("CUL","No reply","China","48–49"),
 ("CUL","Shaking hands","Arabische Länder","50–51"),
 ("CUL","Be brief","GB & USA","52–53"),
 ("STU","The daring request","Südkorea","54–55"),
 ("STU","The internship","Jordanien","56–57"),
 ("STU","The tutor","Marokko","58–59"),
 ("STU","Complaint with the president","Rumänien","60–61"),
 ("STU","The invitation","Türkei","62–63"),
 ("COM","Emphatic nodding","China","64–65"),
 ("COM","Lack of interest","Spanien","66–67"),
 ("COM","Cooking in the office kitchen","Iran","68–69"),
 ("COM","A No stays a No","Kamerun","70–71"),
 ("RES","Room assignment","Spanien","12–13"),
 ("RES","House rules","China","14–15"),
 ("RES","Staying overnight with friends","Polen","16–17"),
 ("RES","Room search","Russland","18–19"),
 ("RES","The termination","Indien","20–21"),
 ("RES","The down blanket","USA","22–23"),
 ("RES","The broken stove","China","24–25"),
 ("RES","The party apartment","Frankreich","26–27"),
 ("RES","The dirty kitchen","Bangladesch","28–29"),
 ("COU","The counter","Arabische Länder","30–31"),
 ("COU","The group appointment","Mexiko","32–33"),
 ("COU","The silent wife","Iran","34–35"),
 ("COU","Eye contact","Kamerun","36–37"),
 ("COU","The consultation","Ägypten","38–39"),
]
for i,(topic,title,country,pages) in enumerate(EDP,1):
    items.append({
        "kind":"edp","collection":"Eine Frage der Perspektive","id":f"EdP-{i:02d}",
        "title":title,"sub":country+" · S. "+pages,
        "topicMain":"EP","topicCode":"EP:"+topic,
        "sitMain":"","sitSub":"",
        "nationality":country,"region":CtoR.get(country,"—"),
        "interaction":"Studierende ↔ Studentenwerk / Hochschulverwaltung",
        "en":True,"themes":[EDP_TOPICS[topic][0]],
        "links":[["src",EDP_URL]],
        "pages":pages,
    })

# ---------- NorQuest (21) ----------
NQ_CTX = {"School":("Hochschule / Sprachkurs","School / language class"),
 "Community":("Alltag / Gesellschaft","Community"),
 "Workplace":("Arbeitsplatz / Praktikum","Workplace"),
 "Acculturation":("Akkulturation","Acculturation / culture shock")}
# (num, context, title, [themes])
NQ = [
 (1,"School","Going up the hierarchy to change class",["Machtdistanz","Hierarchie"]),
 (2,"School","Photos of a deceased baby in class",["Selbstoffenbarung","Tabuthemen","Nonverbal"]),
 (3,"School","Caught cheating on a grammar test",["Gesicht wahren","Disziplin"]),
 (4,"School","„The teacher was very cold“",["Beziehung vs. Aufgabe"]),
 (5,"School","Refusing the biography assignment",["Beziehung vs. Aufgabe","Selbstoffenbarung"]),
 (6,"School","„Good evening“ to a latecomer",["Machtdistanz","Respekt","Humor"]),
 (7,"School","A student's unwelcome attention",["Grenzen","Beziehung vs. Aufgabe"]),
 (8,"School","The critical PhD student",["Gesicht wahren","Hierarchie"]),
 (9,"School","The student who talks too long",["Zeitverständnis","Direkt/Indirekt"]),
 (10,"School","Chatting after the break ends",["Zeitverständnis","Direkt/Indirekt"]),
 (11,"School","Excuses for a late assignment",["Entschuldigungen","Machtdistanz"]),
 (12,"Community","Laughed at by schoolgirls",["Machtdistanz","Disziplin"]),
 (13,"Community","Judged for her clothing",["Normen","Stereotype"]),
 (14,"Community","Two names on a tombstone",["Bräuche","Nonverbal"]),
 (15,"Community","Holding hands and a slur",["Identität","Diskriminierung"]),
 (16,"Community","Not shaking hands with women",["Geschlechternormen","Nonverbal"]),
 (17,"Community","„Single women are lazy“",["Geschlecht","Stereotype"]),
 (18,"Workplace","The receptionist on break",["Zeitverständnis","Servicenormen"]),
 (19,"Workplace","Interpersonal problems in the lab",["Beziehung vs. Aufgabe","Arbeitsplatz"]),
 (20,"Workplace","Marking a sex-ed assignment",["Normen","Werte"]),
 (21,"Acculturation","Resistance to learning English",["Identität","Kulturschock"]),
]
for num,ctx,title,themes in NQ:
    items.append({
        "kind":"nq","collection":"NorQuest Toolkit","id":f"NQ-{num:02d}",
        "title":title,"sub":NQ_CTX[ctx][0],
        "topicMain":"NQ","topicCode":"NQ:"+ctx,
        "sitMain":"","sitSub":"",
        "nationality":"—","region":"—",
        "interaction":"Lehrende ↔ Lernende / Neuzugewanderte (Kanada)",
        "en":True,"themes":themes,
        "links":[["src",NQ_URL]],
    })

collections = [
 {"id":"COL-KD","collection":"KulturellDivers",
  "title":"KulturellDivers – Fallbeispiele (Universität Kiel)",
  "count":"14 Fallbeispiele",
  "desc_de":"14 Fallbeispiele, erzählt von Betroffenen, mit jeweils 3–4 Interpretationen aus den beteiligten kulturellen Lebenswelten (Text, Audio, teils Film). Analysemodell K-P-S-I (Kultur–Person–Situation–Institution). Die Fälle sind nur als interaktive Galerie auf einer Seite verfügbar – ohne einzelne Direktlinks.",
  "desc_en":"14 case studies told by those affected, each with 3–4 interpretations from the cultural life-worlds involved (text, audio, partly film). K-P-S-I model (culture–person–situation–institution). The cases are only available as an interactive gallery on one page – no individual deep links.",
  "themes":["Multiperspektivität","Audio/Video","K-P-S-I-Modell"],"langs":["DE"],
  "url":"https://www.kulturelldivers.de/fallbeispiele"},
]

DATA = {"items":items,"collections":collections,
        "edpTopics":EDP_TOPICS,"nqCtx":NQ_CTX}

html = r"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Critical Incidents · Metasuche</title>
<style>
:root{
  --bg:#F0EEE6; --surface:#FBFAF7; --card:#FFFFFF; --ink:#1A1915; --muted:#6E6A60;
  --line:#E5E0D4; --line2:#D8D2C4; --accent:#C9603F; --accent-d:#A84E32; --accent-soft:#F4E5DD;
  --chip:#EFEBDF; --chip-ink:#5C584F; --badge-en:#E7EEE6; --badge-en-ink:#3F6B47;
  --mu:#1A1915; --edp:#3E6B8A; --nq:#7A5BA6;
  --shadow:0 1px 2px rgba(40,35,25,.05),0 4px 16px rgba(40,35,25,.05);
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--ink);
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;
  line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:var(--accent-d);text-decoration:none}
a:hover{text-decoration:underline}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
header.top{border-bottom:1px solid var(--line);background:var(--bg);position:sticky;top:0;z-index:20}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;gap:18px;padding:22px 0 16px}
.brand h1{font-family:Georgia,"Times New Roman",serif;font-weight:600;font-size:25px;margin:0 0 4px;letter-spacing:-.2px}
.brand p{margin:0;color:var(--muted);font-size:14px;max-width:680px}
.langtoggle{display:inline-flex;border:1px solid var(--line2);border-radius:999px;overflow:hidden;background:var(--surface);flex:none}
.langtoggle button{border:0;background:transparent;padding:7px 14px;font-size:13px;font-weight:600;color:var(--muted);cursor:pointer}
.langtoggle button.active{background:var(--accent);color:#fff}
.controls{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr 1fr .8fr auto;gap:10px;padding:0 0 18px}
.controls .field{display:flex;flex-direction:column;gap:4px}
.controls label{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);font-weight:600}
.controls input,.controls select{font:inherit;font-size:14px;padding:9px 11px;border:1px solid var(--line2);
  border-radius:10px;background:var(--surface);color:var(--ink);width:100%}
.controls input:focus,.controls select:focus{outline:2px solid var(--accent-soft);border-color:var(--accent)}
.resetbtn{align-self:end;border:1px solid var(--line2);background:var(--surface);color:var(--ink);
  border-radius:10px;padding:9px 14px;font:inherit;font-size:14px;cursor:pointer;height:39px}
.resetbtn:hover{background:#fff;border-color:var(--accent)}
main{padding:22px 0 60px}
.section-title{font-family:Georgia,serif;font-size:15px;font-weight:600;margin:6px 0 12px;
  display:flex;align-items:center;gap:9px;color:var(--ink)}
.section-title .ln{flex:1;height:1px;background:var(--line)}
.colgrid{display:grid;grid-template-columns:1fr;gap:14px;margin-bottom:30px}
.colcard{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px 18px 14px;
  display:flex;flex-direction:column;box-shadow:var(--shadow)}
.colcard .cname{font-size:12px;font-weight:700;color:var(--accent-d);text-transform:uppercase;letter-spacing:.05em}
.colcard h3{font-family:Georgia,serif;font-size:16px;margin:6px 0 7px;font-weight:600;line-height:1.3}
.colcard p{margin:0 0 11px;font-size:13px;color:var(--muted)}
.themes{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:11px}
.theme{font-size:11px;background:var(--chip);color:var(--chip-ink);border-radius:6px;padding:2px 7px}
.colcard .go{font-size:13px;font-weight:600}
.statusbar{display:flex;align-items:baseline;justify-content:space-between;margin:4px 0 14px;gap:12px;flex-wrap:wrap}
.count{font-size:14px;color:var(--muted)}
.count b{color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:15px 16px 13px;
  display:flex;flex-direction:column;box-shadow:var(--shadow);transition:border-color .12s,transform .12s}
.card:hover{border-color:var(--line2);transform:translateY(-1px)}
.card .head{display:flex;align-items:center;gap:9px;margin-bottom:8px}
.idbadge{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:11.5px;font-weight:700;
  color:#fff;border-radius:6px;padding:3px 8px;letter-spacing:.4px;flex:none}
.idbadge.mu{background:var(--mu)} .idbadge.edp{background:var(--edp)} .idbadge.nq{background:var(--nq)}
.card h3{font-size:15px;margin:0;font-weight:600;line-height:1.25}
.fach{font-size:12.5px;color:var(--muted);margin:0 0 9px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 9px}
.chip{font-size:11.5px;border-radius:7px;padding:3px 9px;display:inline-flex;align-items:center;gap:5px}
.chip.sit{background:var(--accent-soft);color:var(--accent-d)}
.chip.nat{background:var(--chip);color:var(--chip-ink)}
.chip.en{background:var(--badge-en);color:var(--badge-en-ink);font-weight:600}
.chip.coll{background:#ECEAE2;color:var(--chip-ink);font-weight:600}
.inter{font-size:12.5px;color:var(--muted);margin:0 0 12px;flex:1}
.inter b{color:var(--ink);font-weight:600}
.links{display:flex;flex-wrap:wrap;gap:7px;border-top:1px solid var(--line);padding-top:11px;margin-top:auto}
.lnk{font-size:12.5px;font-weight:600;border:1px solid var(--line2);border-radius:8px;padding:6px 10px;
  color:var(--accent-d);background:var(--surface)}
.lnk:hover{background:var(--accent);color:#fff;border-color:var(--accent);text-decoration:none}
.lnk.muted{color:var(--chip-ink)}
.empty{text-align:center;color:var(--muted);padding:60px 20px;font-size:15px}
footer{border-top:1px solid var(--line);margin-top:10px;padding:22px 0 50px;color:var(--muted);font-size:12.5px}
footer p{margin:0 0 8px;max-width:880px}
footer a{color:var(--accent-d)}
.note{background:var(--accent-soft);border:1px solid #EAD3C8;color:#7a4634;border-radius:10px;
  padding:11px 14px;font-size:13px;margin-bottom:18px}
@media(max-width:980px){.controls{grid-template-columns:1fr 1fr}.resetbtn{grid-column:span 2}}
@media(max-width:560px){.controls{grid-template-columns:1fr}.resetbtn{grid-column:span 1}}
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <div class="topbar">
      <div class="brand"><h1 id="t-title"></h1><p id="t-sub"></p></div>
      <div class="langtoggle">
        <button id="lang-de" class="active" onclick="setLang('de')">DE</button>
        <button id="lang-en" onclick="setLang('en')">EN</button>
      </div>
    </div>
    <div class="controls">
      <div class="field"><label id="l-search"></label><input id="q" type="search" oninput="render()"></div>
      <div class="field"><label id="l-coll"></label><select id="f-coll" onchange="render()"></select></div>
      <div class="field"><label id="l-sit"></label><select id="f-sit" onchange="render()"></select></div>
      <div class="field"><label id="l-region"></label><select id="f-region" onchange="render()"></select></div>
      <div class="field"><label id="l-nat"></label><select id="f-nat" onchange="render()"></select></div>
      <div class="field"><label id="l-lang"></label><select id="f-lang" onchange="render()"></select></div>
      <button class="resetbtn" id="l-reset" onclick="resetFilters()"></button>
    </div>
  </div>
</header>
<main class="wrap">
  <div class="note" id="t-note"></div>
  <div id="collections-wrap">
    <div class="section-title"><span id="t-collections"></span><span class="ln"></span></div>
    <div class="colgrid" id="colgrid"></div>
  </div>
  <div class="statusbar">
    <div class="section-title" style="margin:0"><span id="t-cases"></span></div>
    <div class="count" id="count"></div>
  </div>
  <div class="grid" id="grid"></div>
  <div class="empty" id="empty" style="display:none"></div>
</main>
<footer class="wrap">
  <p id="t-foot1"></p><p id="t-foot2"></p><p id="t-foot3"></p>
</footer>
<script>
const DATA = __DATA__;
const I18N = {
 de:{title:"Critical Incidents · Metasuche",
   sub:"Durchsuchbarer Index interkultureller Critical Incidents aus dem Hochschulkontext: MuMiS (162 Fälle), Eine Frage der Perspektive (30) und NorQuest Toolkit (21) – mit Direktlinks zu den Quellen.",
   search:"Suche (Titel, Land, Stichwort, ID …)", coll:"Sammlung", sit:"Situation / Thema", region:"Region",
   nat:"Nationalität", lang:"Sprache", reset:"Zurücksetzen",
   collections:"Weitere Sammlung (ohne Einzellinks)", cases:"Fälle",
   all:"Alle", langEN:"Englisch verfügbar", langDE:"Deutsch verfügbar",
   counts:(n,t)=>`<b>${n}</b> von ${t} Fällen`,
   interaktion:"Interaktion:", openMu:"Fall (DE)", komm:"+ Kommentar", enPdf:"EN PDF",
   openEdp:"Zum PDF (S. ", openNq:"Zum Toolkit (PDF)",
   go:"Zur Sammlung →", empty:"Keine Fälle für diese Filter. Bitte Auswahl anpassen.",
   note:"Hinweis: Aus urheberrechtlichen Gründen werden keine Falltexte gespiegelt. Karten verlinken direkt auf die offiziellen Quellen (MuMiS-PDFs je Fall; EdP- und NorQuest-PDF mit Seitenangabe).",
   gMu:"MuMiS – Kommunikationssituationen", gEp:"Eine Frage der Perspektive – Themen", gNq:"NorQuest – Kontexte",
   foot1:"Datengrundlagen: MuMiS (Univ. Siegen/Bielefeld/Köln, VolkswagenStiftung; gehostet Univ. Kassel) · „Eine Frage der Perspektive“ (Deutsches Studentenwerk, 2016/2018) · NorQuest College, „Critical Incidents for Intercultural Communication“ (2008).",
   foot2:'Quellen: <a target="_blank" href="https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html">MuMiS</a> · <a target="_blank" href="https://www.kulturelldivers.de/fallbeispiele">KulturellDivers</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf">Eine Frage der Perspektive</a> · <a target="_blank" href="https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf">NorQuest Toolkit</a>',
   foot3:"Didaktischer Hinweis: Fälle nicht nach dem Muster „Menschen aus Land X verhalten sich so“ deuten. Kulturelle, institutionelle, situative und persönliche Faktoren wirken zusammen (vgl. K-P-S-I-Modell)."},
 en:{title:"Critical Incidents · Meta-search",
   sub:"Searchable index of intercultural critical incidents in higher education: MuMiS (162 cases), A Matter of Perspective (30) and the NorQuest Toolkit (21) – with direct links to the sources.",
   search:"Search (title, country, keyword, ID …)", coll:"Collection", sit:"Situation / theme", region:"Region",
   nat:"Nationality", lang:"Language", reset:"Reset",
   collections:"Further collection (no individual links)", cases:"Cases",
   all:"All", langEN:"English available", langDE:"German available",
   counts:(n,t)=>`<b>${n}</b> of ${t} cases`,
   interaktion:"Interaction:", openMu:"Case (DE)", komm:"+ Commentary", enPdf:"EN PDF",
   openEdp:"Open PDF (p. ", openNq:"Open toolkit (PDF)",
   go:"Open collection →", empty:"No cases for these filters. Please adjust your selection.",
   note:"Note: for copyright reasons no case texts are mirrored. Cards link directly to the official sources (MuMiS PDFs per case; EdP and NorQuest PDF with page reference).",
   gMu:"MuMiS – communication situations", gEp:"A Matter of Perspective – topics", gNq:"NorQuest – contexts",
   foot1:"Sources: MuMiS (Univ. Siegen/Bielefeld/Cologne, Volkswagen Foundation; hosted at Univ. Kassel) · ‘A Matter of Perspective’ (Deutsches Studentenwerk, 2016/2018) · NorQuest College, ‘Critical Incidents for Intercultural Communication’ (2008).",
   foot2:'Sources: <a target="_blank" href="https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html">MuMiS</a> · <a target="_blank" href="https://www.kulturelldivers.de/fallbeispiele">KulturellDivers</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf">A Matter of Perspective</a> · <a target="_blank" href="https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf">NorQuest Toolkit</a>',
   foot3:"Didactic note: do not read cases as ‘people from country X behave like this’. Cultural, institutional, situational and personal factors interact (cf. the K-P-S-I model)."}
};
const SITMAIN={A:{de:"Kommunikation in Lehrveranstaltungen",en:"Communication in courses"},
 B:{de:"Kommunikation mit Dozenten",en:"Communication with lecturers"},
 C:{de:"Kommunikation in Arbeitsgruppen",en:"Communication in working groups"},
 D:{de:"Kommunikation unter Studierenden",en:"Communication among students"}};
const SITSUB={A1:{de:"Lehr- & Lernstile",en:"Teaching & learning styles"},
 A2:{de:"Verhaltensnormen in Lehrveranstaltungen",en:"Behavioural norms in courses"},
 B1:{de:"Kontaktaufnahme & Kontaktpflege",en:"Making & keeping contact"},
 B2:{de:"Betreuung & Bewertung von Leistungen",en:"Supervision & assessment"},
 C1:{de:"Gruppenarbeit in Lehrveranstaltungen",en:"Group work in courses"},
 C2:{de:"Gruppen-/Partnerarbeit (Leistungen)",en:"Group/pair work (assessment)"},
 C3:{de:"Gruppenarbeit in Forschungsgruppen",en:"Group work in research groups"},
 D1:{de:"Kontaktaufnahme & Verabredungen",en:"Making contact & arrangements"},
 D2:{de:"Einladungen & Besuche",en:"Invitations & visits"},
 D3:{de:"Gesprächsthemen & -stile",en:"Conversation topics & styles"},
 D4:{de:"Zusammenleben im Wohnheim",en:"Living together in halls"}};
const REGIONI={"Afrika":{de:"Afrika",en:"Africa"},"Amerika":{de:"Amerika",en:"Americas"},
 "Asien":{de:"Asien",en:"Asia"},"Europa":{de:"Europa",en:"Europe"},"—":{de:"übergreifend",en:"unspecified"}};
const EDPT=DATA.edpTopics, NQC=DATA.nqCtx;

let LANG="de";
function T(){return I18N[LANG]}
function topicLabel(item){
  if(item.kind==="mumis") return SITSUB[item.sitSub][LANG];
  if(item.kind==="edp") return EDPT[item.topicCode.slice(3)][LANG==="de"?0:1];
  if(item.kind==="nq") return NQC[item.topicCode.slice(3)][LANG==="de"?0:1];
  return "";
}
function setLang(l){LANG=l;
  document.getElementById('lang-de').classList.toggle('active',l==='de');
  document.getElementById('lang-en').classList.toggle('active',l==='en');
  document.documentElement.lang=l; buildStaticText(); buildSelects(true); render();
}
function buildStaticText(){const t=T();
  document.title=t.title;
  for(const[id,key] of [["t-title","title"],["t-sub","sub"],["l-search","search"],["l-coll","coll"],
    ["l-sit","sit"],["l-region","region"],["l-nat","nat"],["l-lang","lang"],["l-reset","reset"],
    ["t-collections","collections"],["t-cases","cases"],["t-note","note"],["t-foot1","foot1"],["t-foot3","foot3"]])
    document.getElementById(id).textContent=t[key];
  document.getElementById('t-foot2').innerHTML=t.foot2;
  document.getElementById('q').placeholder=t.search;
}
function opt(v,l){return `<option value="${v}">${l}</option>`}
function og(label,inner){return `<optgroup label="${label}">${inner}</optgroup>`}
function buildSelects(keep){const t=T();
  const prev=keep?Object.fromEntries(['f-coll','f-sit','f-region','f-nat','f-lang'].map(i=>[i,val(i)])):{};
  const colls=["MuMiS","Eine Frage der Perspektive","NorQuest Toolkit",...DATA.collections.map(c=>c.collection)];
  document.getElementById('f-coll').innerHTML=opt("",t.all)+colls.map(c=>opt(c,c)).join('');
  // situation/theme grouped
  let mu="";["A","B","C","D"].forEach(m=>{ mu+=opt("main:MU:"+m,SITMAIN[m][LANG]);
    DATA.items.filter(c=>c.kind==="mumis"&&c.sitMain===m).map(c=>c.sitSub).filter((v,i,a)=>a.indexOf(v)===i).sort()
      .forEach(s=>{mu+=opt("sub:MU:"+s,"· "+SITSUB[s][LANG])});});
  let ep=Object.keys(EDPT).map(k=>opt("sub:EP:"+k,EDPT[k][LANG==="de"?0:1])).join('');
  let nq=Object.keys(NQC).map(k=>opt("sub:NQ:"+k,NQC[k][LANG==="de"?0:1])).join('');
  document.getElementById('f-sit').innerHTML=opt("",t.all)+og(t.gMu,mu)+og(t.gEp,ep)+og(t.gNq,nq);
  const regs=[...new Set(DATA.items.map(c=>c.region))].filter(r=>r!=="—").sort();
  document.getElementById('f-region').innerHTML=opt("",t.all)+regs.map(r=>opt(r,REGIONI[r]?REGIONI[r][LANG]:r)).join('');
  const nats=[...new Set(DATA.items.map(c=>c.nationality))].filter(n=>n&&n!=="—").sort((a,b)=>a.localeCompare(b,'de'));
  document.getElementById('f-nat').innerHTML=opt("",t.all)+nats.map(n=>opt(n,n)).join('');
  document.getElementById('f-lang').innerHTML=opt("",t.all)+opt("EN",t.langEN);
  if(keep)Object.entries(prev).forEach(([i,v])=>set(i,v));
}
function val(id){const e=document.getElementById(id);return e?e.value:""}
function set(id,v){const e=document.getElementById(id);if(e)e.value=v||""}
function resetFilters(){['q','f-coll','f-sit','f-region','f-nat','f-lang'].forEach(i=>set(i,''));render()}

function matchItem(c,f){
  if(f.coll && c.collection!==f.coll) return false;
  if(f.sit){ if(f.sit.startsWith("main:")){ if(c.topicMain!==f.sit.slice(5))return false; }
             else if(f.sit.startsWith("sub:")){ if(c.topicCode!==f.sit.slice(4))return false; } }
  if(f.region && c.region!==f.region) return false;
  if(f.nat && c.nationality!==f.nat) return false;
  if(f.lang==="EN" && !c.en) return false;
  if(f.q){ const hay=(c.id+" "+c.title+" "+c.sub+" "+c.interaction+" "+c.nationality+" "+c.collection+" "+
      (c.themes||[]).join(" ")+" "+topicLabel(c)).toLowerCase();
    if(!f.q.split(/\s+/).every(w=>hay.includes(w))) return false; }
  return true;
}
function matchColl(col,f){
  if(f.coll && f.coll!==col.collection) return false;
  if(f.sit||f.region||f.nat||f.lang) return false;
  if(f.q){ const hay=(col.collection+" "+col.title+" "+col.desc_de+" "+col.desc_en+" "+col.themes.join(" ")).toLowerCase();
    if(!f.q.split(/\s+/).every(w=>hay.includes(w))) return false; }
  return true;
}
function esc(s){return (s||"").replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]))}

function card(c){const t=T();
  const cls=c.kind==="mumis"?"mu":(c.kind==="edp"?"edp":"nq");
  const en = c.en?`<span class="chip en">EN</span>`:"";
  const nat = c.nationality&&c.nationality!=="—"?`<span class="chip nat">${esc(c.nationality)}</span>`:"";
  const themechips=(c.themes||[]).slice(0,4).map(x=>`<span class="chip nat">${esc(x)}</span>`).join('');
  let links="";
  if(c.kind==="mumis"){
    const L=Object.fromEntries(c.links);
    links=`<a class="lnk" target="_blank" href="${L.de}">${t.openMu}</a>
      <a class="lnk muted" target="_blank" href="${L.komm}">${t.komm}</a>`+
      (L.en?`<a class="lnk" target="_blank" href="${L.en}">${t.enPdf}</a>`:"");
  }else if(c.kind==="edp"){
    links=`<a class="lnk" target="_blank" href="${c.links[0][1]}">${t.openEdp}${esc(c.pages||"")})</a>`;
  }else{
    links=`<a class="lnk" target="_blank" href="${c.links[0][1]}">${t.openNq}</a>`;
  }
  return `<div class="card">
    <div class="head"><span class="idbadge ${cls}">${esc(c.id)}</span><h3>${esc(c.title)}</h3></div>
    <p class="fach">${esc(c.sub||"")}</p>
    <div class="chips">
      <span class="chip sit">${esc(topicLabel(c))}</span>${nat}${en}${c.kind!=="mumis"?themechips:""}
    </div>
    <p class="inter"><b>${t.interaktion}</b> ${esc(c.interaction||"–")}</p>
    <div class="links">${links}</div>
   </div>`;
}
function collCard(col){const t=T();const desc=LANG==="de"?col.desc_de:col.desc_en;
  return `<div class="colcard"><span class="cname">${esc(col.collection)} · ${esc(col.count)}</span>
    <h3>${esc(col.title)}</h3><p>${esc(desc)}</p>
    <div class="themes">${col.themes.map(x=>`<span class="theme">${esc(x)}</span>`).join('')}
      <span class="theme">${col.langs.join(" / ")}</span></div>
    <a class="go" target="_blank" href="${col.url}">${t.go}</a></div>`;
}
function render(){const t=T();
  const f={q:val('q').trim().toLowerCase(),coll:val('f-coll'),sit:val('f-sit'),
    region:val('f-region'),nat:val('f-nat'),lang:val('f-lang')};
  const cols=DATA.collections.filter(c=>matchColl(c,f));
  document.getElementById('colgrid').innerHTML=cols.map(collCard).join('');
  document.getElementById('collections-wrap').style.display=cols.length?"block":"none";
  const cs=DATA.items.filter(c=>matchItem(c,f));
  document.getElementById('grid').innerHTML=cs.map(card).join('');
  document.getElementById('count').innerHTML=t.counts(cs.length,DATA.items.length);
  const emp=document.getElementById('empty');
  if(cs.length===0&&cols.length===0){emp.style.display="block";emp.textContent=t.empty;}else emp.style.display="none";
}
buildStaticText();buildSelects(false);render();
</script>
</body></html>"""

html = html.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(OUT+"critical-incidents-metasuche.html","w",encoding="utf-8").write(html)
print("OK items:",len(items),"| mumis",sum(1 for i in items if i['kind']=='mumis'),
      "edp",sum(1 for i in items if i['kind']=='edp'),"nq",sum(1 for i in items if i['kind']=='nq'),
      "| bytes",len(html))

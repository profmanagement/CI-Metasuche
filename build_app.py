#!/usr/bin/env python3
import json
OUT = "/sessions/practical-brave-johnson/mnt/outputs/"
cases = json.load(open(OUT+"mumis_full.json", encoding="utf-8"))

collections = [
 {"id":"COL-KD","collection":"KulturellDivers","type":"collection",
  "title":"KulturellDivers – Critical Incidents (Universität Kiel)",
  "desc_de":"Critical Incidents als Text-, Audio- und teilweise Filmbeiträge. Mehrere Perspektiven auf denselben Vorfall; bewusst nicht über eine homogene Nationalkultur erklärt. Analysemodell: Kultur – Person – Situation – Institution.",
  "desc_en":"Critical incidents as text, audio and partly film. Multiple perspectives on the same incident; deliberately not explained via a homogeneous national culture. Analytic model: culture – person – situation – institution.",
  "themes":["Multiperspektivität","Audio/Video","Kultur–Person–Situation–Institution"],
  "langs":["DE"],
  "url":"https://www.kulturelldivers.de/critical-incidents-theorie"},
 {"id":"COL-FP","collection":"Eine Frage der Perspektive","type":"collection",
  "title":"Eine Frage der Perspektive (Deutsches Studentenwerk) – 30 Fälle",
  "desc_de":"30 authentische Fälle aus der Begegnung internationaler Studierender mit Studentenwerken bzw. Hochschulverwaltungen. Kommentiert aus den jeweiligen Herkunftskontexten, mit Hinweisen für interkulturelle Trainings.",
  "desc_en":"30 authentic cases from international students' encounters with student services / university administration. Commented from the respective cultural backgrounds, with guidance for intercultural training.",
  "themes":["Hochschulverwaltung","Studentenwerk","30 Fälle","Trainingshinweise"],
  "langs":["DE","EN"],
  "url":"https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf"},
 {"id":"COL-NQ","collection":"NorQuest Toolkit","type":"collection",
  "title":"NorQuest – Critical Incidents for Intercultural Communication Toolkit",
  "desc_de":"Englischsprachiges Toolkit mit Critical Incidents, Analyseübungen, Moderationshinweisen und Incident Cards. Themen u.a.: direkte/indirekte Kommunikation, Hierarchie & Machtdistanz, Zeitverständnis, nonverbale Kommunikation, Identität/Stereotype/Diskriminierung.",
  "desc_en":"English-language toolkit with critical incidents, analysis exercises, facilitation notes and incident cards. Themes incl.: direct/indirect communication, hierarchy & power distance, time, nonverbal communication, identity/stereotypes/discrimination.",
  "themes":["Incident Cards","Machtdistanz","Nonverbale Kommunikation","Stereotype & Diskriminierung","Zeitverständnis"],
  "langs":["EN"],
  "url":"https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf"},
]

DATA = {"cases": cases, "collections": collections}

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
.brand p{margin:0;color:var(--muted);font-size:14px;max-width:640px}
.langtoggle{display:inline-flex;border:1px solid var(--line2);border-radius:999px;overflow:hidden;background:var(--surface);flex:none}
.langtoggle button{border:0;background:transparent;padding:7px 14px;font-size:13px;font-weight:600;color:var(--muted);cursor:pointer}
.langtoggle button.active{background:var(--accent);color:#fff}
.controls{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr 1fr auto;gap:10px;padding:0 0 16px}
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
.colgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:30px}
.colcard{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px 16px 14px;
  display:flex;flex-direction:column;box-shadow:var(--shadow)}
.colcard .cname{font-size:12px;font-weight:700;color:var(--accent-d);text-transform:uppercase;letter-spacing:.05em}
.colcard h3{font-family:Georgia,serif;font-size:16px;margin:6px 0 7px;font-weight:600;line-height:1.3}
.colcard p{margin:0 0 11px;font-size:13px;color:var(--muted);flex:1}
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
.idbadge{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:12px;font-weight:700;background:var(--ink);
  color:#fff;border-radius:6px;padding:3px 8px;letter-spacing:.5px;flex:none}
.card h3{font-size:15.5px;margin:0;font-weight:600;line-height:1.25}
.fach{font-size:12.5px;color:var(--muted);margin:0 0 9px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 9px}
.chip{font-size:11.5px;border-radius:7px;padding:3px 9px;display:inline-flex;align-items:center;gap:5px}
.chip.sit{background:var(--accent-soft);color:var(--accent-d)}
.chip.nat{background:var(--chip);color:var(--chip-ink)}
.chip.en{background:var(--badge-en);color:var(--badge-en-ink);font-weight:600}
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
@media(max-width:980px){.controls{grid-template-columns:1fr 1fr;}.colgrid{grid-template-columns:1fr}
  .resetbtn{grid-column:span 2}}
@media(max-width:560px){.controls{grid-template-columns:1fr}.resetbtn{grid-column:span 1}}
</style>
</head>
<body>
<header class="top">
  <div class="wrap">
    <div class="topbar">
      <div class="brand">
        <h1 id="t-title"></h1>
        <p id="t-sub"></p>
      </div>
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
      <button class="resetbtn" id="l-reset" onclick="resetFilters()"></button>
    </div>
    <div class="controls" style="grid-template-columns:1fr 1fr 1fr;padding-bottom:18px">
      <div class="field"><label id="l-lang"></label><select id="f-lang" onchange="render()"></select></div>
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
  <p id="t-foot1"></p>
  <p id="t-foot2"></p>
  <p id="t-foot3"></p>
</footer>

<script>
const DATA = __DATA__;
const I18N = {
 de:{title:"Critical Incidents · Metasuche",
   sub:"Durchsuchbarer Index interkultureller Critical Incidents aus dem Hochschulkontext. Schwerpunkt: MuMiS-Datenbank (162 Fälle) mit Direktlinks zu den Original-PDFs, ergänzt um drei weitere Sammlungen.",
   search:"Suche (Name, Fach, Stichwort, ID …)", coll:"Sammlung", sit:"Situationstyp", region:"Region",
   nat:"Nationalität", lang:"Sprachfassung", reset:"Zurücksetzen",
   collections:"Weitere Sammlungen", cases:"MuMiS-Fälle",
   all:"Alle", langDE:"Deutsch vorhanden", langEN:"Englisch verfügbar",
   counts:(n,t)=>`<b>${n}</b> von ${t} Fällen`,
   interaktion:"Interaktionspartner:", open:"Fall (DE)", komm:"+ Kommentar", en:"EN",
   go:"Zur Sammlung →", empty:"Keine Fälle für diese Filter. Bitte Auswahl anpassen.",
   note:"Hinweis: Aus urheberrechtlichen Gründen werden die MuMiS-Falltexte nicht gespiegelt. Jede Karte verlinkt direkt auf die offiziellen PDF-Fassungen (Fall, Fall mit Kommentar, ggf. englische Version).",
   foot1:"Datengrundlage: MuMiS – „Mehrsprachigkeit und Multikulturalität im Studium“ (Universitäten Siegen, Bielefeld, Köln; gefördert von der VolkswagenStiftung), gehostet an der Universität Kassel. Index erstellt aus den öffentlichen Suchseiten der CI-Datenbank.",
   foot2:'Quellen: <a target="_blank" href="https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html">MuMiS CI-Datenbank</a> · <a target="_blank" href="https://www.kulturelldivers.de/critical-incidents-theorie">KulturellDivers</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf">Eine Frage der Perspektive</a> · <a target="_blank" href="https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf">NorQuest Toolkit</a>',
   foot3:"Didaktischer Hinweis: Fälle nicht nach dem Muster „Menschen aus Land X verhalten sich so“ deuten. Kulturelle, institutionelle, situative und persönliche Faktoren wirken zusammen; mehrere Erklärungen sind möglich (vgl. KPSI-Analyse)."},
 en:{title:"Critical Incidents · Meta-search",
   sub:"Searchable index of intercultural critical incidents in higher education. Focus: the MuMiS database (162 cases) with direct links to the original PDFs, plus three further collections.",
   search:"Search (name, subject, keyword, ID …)", coll:"Collection", sit:"Situation type", region:"Region",
   nat:"Nationality", lang:"Language version", reset:"Reset",
   collections:"Further collections", cases:"MuMiS cases",
   all:"All", langDE:"German available", langEN:"English available",
   counts:(n,t)=>`<b>${n}</b> of ${t} cases`,
   interaktion:"Interaction partner:", open:"Case (DE)", komm:"+ Commentary", en:"EN",
   go:"Open collection →", empty:"No cases for these filters. Please adjust your selection.",
   note:"Note: for copyright reasons the MuMiS case texts are not mirrored. Each card links directly to the official PDF versions (case, case with commentary, English version where available).",
   foot1:"Source: MuMiS – ‘Multilingualism and Multiculturalism in Higher Education’ (Universities of Siegen, Bielefeld, Cologne; funded by the Volkswagen Foundation), hosted at the University of Kassel. Index compiled from the public search pages of the CI database.",
   foot2:'Sources: <a target="_blank" href="https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html">MuMiS CI database</a> · <a target="_blank" href="https://www.kulturelldivers.de/critical-incidents-theorie">KulturellDivers</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf">A Matter of Perspective</a> · <a target="_blank" href="https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf">NorQuest Toolkit</a>',
   foot3:"Didactic note: do not read cases as ‘people from country X behave like this’. Cultural, institutional, situational and personal factors interact; several explanations are possible (cf. the culture–person–situation–institution model)."}
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
const REGION={"Afrika":{de:"Afrika",en:"Africa"},"Amerika":{de:"Amerika",en:"Americas"},
 "Asien":{de:"Asien",en:"Asia"},"Europa":{de:"Europa",en:"Europe"},"—":{de:"übergreifend",en:"unspecified"}};

let LANG="de";
function T(){return I18N[LANG]}

function setLang(l){LANG=l;
  document.getElementById('lang-de').classList.toggle('active',l==='de');
  document.getElementById('lang-en').classList.toggle('active',l==='en');
  document.documentElement.lang=l;
  buildStaticText(); buildSelects(true); render();
}
function buildStaticText(){const t=T();
  document.title=t.title;
  document.getElementById('t-title').textContent=t.title;
  document.getElementById('t-sub').textContent=t.sub;
  document.getElementById('l-search').textContent=t.search;
  document.getElementById('l-coll').textContent=t.coll;
  document.getElementById('l-sit').textContent=t.sit;
  document.getElementById('l-region').textContent=t.region;
  document.getElementById('l-nat').textContent=t.nat;
  document.getElementById('l-lang').textContent=t.lang;
  document.getElementById('l-reset').textContent=t.reset;
  document.getElementById('t-collections').textContent=t.collections;
  document.getElementById('t-cases').textContent=t.cases;
  document.getElementById('t-note').textContent=t.note;
  document.getElementById('t-foot1').textContent=t.foot1;
  document.getElementById('t-foot2').innerHTML=t.foot2;
  document.getElementById('t-foot3').textContent=t.foot3;
  document.getElementById('q').placeholder=t.search;
}
function opt(v,label){return `<option value="${v}">${label}</option>`}
function buildSelects(keep){
  const t=T();
  const prev=keep?{coll:val('f-coll'),sit:val('f-sit'),region:val('f-region'),nat:val('f-nat'),lang:val('f-lang')}:{};
  // collections
  const colls=["MuMiS",...DATA.collections.map(c=>c.collection)];
  document.getElementById('f-coll').innerHTML=opt("",t.all)+colls.map(c=>opt(c,c)).join('');
  // situation: main + grouped subs
  let sit=opt("",t.all);
  ["A","B","C","D"].forEach(m=>{
    sit+=opt("M:"+m,SITMAIN[m][LANG]);
    DATA.cases.filter(c=>c.sitMain===m).map(c=>c.sitSub).filter((v,i,a)=>a.indexOf(v)===i).sort()
      .forEach(s=>{ sit+=opt("S:"+s,"   · "+SITSUB[s][LANG]); });
  });
  document.getElementById('f-sit').innerHTML=sit;
  // region
  const regs=[...new Set(DATA.cases.map(c=>c.region))].sort();
  document.getElementById('f-region').innerHTML=opt("",t.all)+regs.map(r=>opt(r,REGION[r]?REGION[r][LANG]:r)).join('');
  // nationality
  const nats=[...new Set(DATA.cases.map(c=>c.nationality))].filter(n=>n&&n!=="—").sort((a,b)=>a.localeCompare(b,'de'));
  document.getElementById('f-nat').innerHTML=opt("",t.all)+nats.map(n=>opt(n,n)).join('');
  // language
  document.getElementById('f-lang').innerHTML=opt("",t.all)+opt("DE",t.langDE)+opt("EN",t.langEN);
  if(keep){set('f-coll',prev.coll);set('f-sit',prev.sit);set('f-region',prev.region);set('f-nat',prev.nat);set('f-lang',prev.lang);}
}
function val(id){const e=document.getElementById(id);return e?e.value:""}
function set(id,v){const e=document.getElementById(id);if(e)e.value=v||""}
function resetFilters(){['q','f-coll','f-sit','f-region','f-nat','f-lang'].forEach(id=>set(id,''));render()}

function matchCase(c,f){
  if(f.coll && f.coll!=="MuMiS") return false;
  if(f.sit){ if(f.sit.startsWith("M:")&&c.sitMain!==f.sit.slice(2))return false;
             if(f.sit.startsWith("S:")&&c.sitSub!==f.sit.slice(2))return false; }
  if(f.region && c.region!==f.region) return false;
  if(f.nat && c.nationality!==f.nat) return false;
  if(f.lang==="EN" && !c.en) return false;
  if(f.lang==="DE" && false) return false; // all have DE
  if(f.q){ const hay=(c.id+" "+c.name+" "+c.fach+" "+c.origin+" "+c.interaction+" "+c.nationality+" "+
      SITMAIN[c.sitMain].de+" "+SITMAIN[c.sitMain].en+" "+SITSUB[c.sitSub].de+" "+SITSUB[c.sitSub].en).toLowerCase();
    if(!f.q.split(/\s+/).every(w=>hay.includes(w))) return false; }
  return true;
}
function matchColl(col,f){
  if(f.coll && f.coll!==col.collection) return false;
  if(f.sit||f.region||f.nat) return false; // case-specific filters hide collection cards
  if(f.lang==="EN" && !col.langs.includes("EN")) return false;
  if(f.lang==="DE" && !col.langs.includes("DE")) return false;
  if(f.q){ const hay=(col.collection+" "+col.title+" "+col.desc_de+" "+col.desc_en+" "+col.themes.join(" ")).toLowerCase();
    if(!f.q.split(/\s+/).every(w=>hay.includes(w))) return false; }
  return true;
}
function esc(s){return (s||"").replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]))}

function caseCard(c){const t=T();
  const en = c.en?`<span class="chip en">${t.en}</span>`:"";
  const enlink = c.en?`<a class="lnk" target="_blank" href="${c.pdf_en}">${t.en} PDF</a>`:"";
  const natchip = c.nationality&&c.nationality!=="—"?`<span class="chip nat">${esc(c.nationality)}</span>`:"";
  return `<div class="card">
   <div class="head"><span class="idbadge">${c.id}</span><h3>${esc(c.name)}</h3></div>
   <p class="fach">${esc(c.fach||"")}</p>
   <div class="chips">
     <span class="chip sit" title="${esc(SITMAIN[c.sitMain][LANG])}">${esc(SITSUB[c.sitSub][LANG])}</span>
     ${natchip}${en}
   </div>
   <p class="inter"><b>${t.interaktion}</b> ${esc(c.interaction||"–")}</p>
   <div class="links">
     <a class="lnk" target="_blank" href="${c.pdf_de}">${t.open}</a>
     <a class="lnk muted" target="_blank" href="${c.pdf_kommentar}">${t.komm}</a>
     ${enlink}
   </div></div>`;
}
function collCard(col){const t=T();
  const desc=LANG==="de"?col.desc_de:col.desc_en;
  return `<div class="colcard">
    <span class="cname">${esc(col.collection)}</span>
    <h3>${esc(col.title)}</h3>
    <p>${esc(desc)}</p>
    <div class="themes">${col.themes.map(x=>`<span class="theme">${esc(x)}</span>`).join('')}
      <span class="theme">${col.langs.join(" / ")}</span></div>
    <a class="go" target="_blank" href="${col.url}">${t.go}</a>
   </div>`;
}
function render(){
  const t=T();
  const f={q:val('q').trim().toLowerCase(),coll:val('f-coll'),sit:val('f-sit'),
    region:val('f-region'),nat:val('f-nat'),lang:val('f-lang')};
  // collections
  const cols=DATA.collections.filter(c=>matchColl(c,f));
  const cwrap=document.getElementById('collections-wrap');
  document.getElementById('colgrid').innerHTML=cols.map(collCard).join('');
  cwrap.style.display=cols.length?"block":"none";
  // cases
  const cs=DATA.cases.filter(c=>matchCase(c,f));
  document.getElementById('grid').innerHTML=cs.map(caseCard).join('');
  document.getElementById('count').innerHTML=t.counts(cs.length,DATA.cases.length);
  const emp=document.getElementById('empty');
  if(cs.length===0 && cols.length===0){emp.style.display="block";emp.textContent=t.empty;}
  else emp.style.display="none";
}
buildStaticText();buildSelects(false);render();
</script>
</body>
</html>"""

html = html.replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
open(OUT+"critical-incidents-metasuche.html","w",encoding="utf-8").write(html)
print("written", len(html), "bytes;", len(cases), "cases;", len(collections), "collections")

#!/usr/bin/env python3
import json
OUT = "/sessions/practical-brave-johnson/mnt/outputs/"
mumis = json.load(open(OUT+"mumis_full.json", encoding="utf-8"))

EDP_EN = "https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf"
EDP_DE = "https://www.studierendenwerke.de/fileadmin/user_upload/dsw-fallbeispiele-digital-druckboegen_0.pdf"
NQ_URL = "https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf"

CtoR = {"Kolumbien":"Amerika","USA":"Amerika","Mexiko":"Amerika",
 "Kenia":"Afrika","Marokko":"Afrika","Kamerun":"Afrika","Ägypten":"Afrika",
 "Vietnam":"Asien","Syrien":"Asien","China":"Asien","Südkorea":"Asien","Jordanien":"Asien","Iran":"Asien","Indien":"Asien","Bangladesch":"Asien",
 "Rumänien":"Europa","Türkei":"Europa","Spanien":"Europa","Polen":"Europa","Russland":"Europa","Frankreich":"Europa",
 "Arabische Länder":"—","GB & USA":"—"}

items = []
for c in mumis:
    items.append({"kind":"mumis","collection":"MuMiS","id":c["id"],
        "title":c["name"],"titleEn":None,"sub":c["fach"],
        "topicMain":"MU:"+c["sitMain"],"topicCode":"MU:"+c["sitSub"],
        "sitMain":c["sitMain"],"sitSub":c["sitSub"],
        "nationality":c["nationality"],"region":c["region"],
        "interaction":c["interaction"],"hasDE":True,"hasEN":bool(c["en"]),"themes":[],
        "links":[["de",c["pdf_de"]],["komm",c["pdf_kommentar"]]]+([["en",c["pdf_en"]]] if c["en"] else [])})

EDP_TOPICS={"RES":("Wohnen","Residence halls"),"FIN":("Finanzierung","Financial matters"),
 "CUL":("Kultur","Culture"),"STU":("Studienorganisation","Study organization"),
 "COM":("Kommunikation","Communication"),"COU":("Beratung","Counselling")}
EDP=[
 ("FIN","Zu später Hilferuf","A cry for help too late","Kolumbien","40–41"),
 ("FIN","Der Mietrückstand","Back rent","Kenia","42–43"),
 ("FIN","Geldprobleme","Money problems","Vietnam","44–45"),
 ("CUL","Die Weinprobe","The wine tasting","Syrien","46–47"),
 ("CUL","Keine Antwort","No reply","China","48–49"),
 ("CUL","Händeschütteln","Shaking hands","Arabische Länder","50–51"),
 ("CUL","Fasse dich kurz","Be brief","GB & USA","52–53"),
 ("STU","Die wagemutige Bitte","The daring request","Südkorea","54–55"),
 ("STU","Der Praktikumsplatz","The internship","Jordanien","56–57"),
 ("STU","Die Nachhilfe","The tutor","Marokko","58–59"),
 ("STU","Beschwerde beim Präsidenten","Complaint with the president","Rumänien","60–61"),
 ("STU","Die Essenseinladung","The invitation","Türkei","62–63"),
 ("COM","Eifriges Kopfnicken","Emphatic nodding","China","64–65"),
 ("COM","Desinteresse","Lack of interest","Spanien","66–67"),
 ("COM","Kochen in der Büroküche","Cooking in the office kitchen","Iran","68–69"),
 ("COM","Nein heißt Nein","A No stays a No","Kamerun","70–71"),
 ("RES","Zimmervergabe","Room assignment","Spanien","12–13"),
 ("RES","Die Hausordnung","House rules","China","14–15"),
 ("RES","Übernachtung bei Freundinnen","Staying overnight with friends","Polen","16–17"),
 ("RES","Zimmersuche","Room search","Russland","18–19"),
 ("RES","Die Kündigung","The termination","Indien","20–21"),
 ("RES","Die Daunendecke","The down blanket","USA","22–23"),
 ("RES","Der kaputte Herd","The broken stove","China","24–25"),
 ("RES","Die Party-WG","The party apartment","Frankreich","26–27"),
 ("RES","Die schmutzige Küche","The dirty kitchen","Bangladesch","28–29"),
 ("COU","Die Theke","The counter","Arabische Länder","30–31"),
 ("COU","Der Sammeltermin","The group appointment","Mexiko","32–33"),
 ("COU","Die schweigende Ehefrau","The silent wife","Iran","34–35"),
 ("COU","Blickkontakt","Eye contact","Kamerun","36–37"),
 ("COU","Das Beratungsgespräch","The consultation","Ägypten","38–39"),
]
for i,(topic,tde,ten,country,pages) in enumerate(EDP,1):
    items.append({"kind":"edp","collection":"Eine Frage der Perspektive 1","id":f"EdP-{i:02d}",
        "title":tde,"titleEn":ten,"sub":country+" · S. "+pages,
        "topicMain":"EP","topicCode":"EP:"+topic,"sitMain":"","sitSub":"",
        "nationality":country,"region":CtoR.get(country,"—"),
        "interaction":"Studierende ↔ Studentenwerk / Hochschulverwaltung",
        "hasDE":True,"hasEN":True,"themes":[EDP_TOPICS[topic][0]],
        "links":[["de",EDP_DE],["en",EDP_EN]],"pages":pages,
        "page":int(pages.split("–")[0])//2 + 2})  # physische PDF-Seite (Doppelseiten-Layout)

NQ_CTX={"School":("Hochschule / Sprachkurs","School / language class"),
 "Community":("Alltag / Gesellschaft","Community"),
 "Workplace":("Arbeitsplatz / Praktikum","Workplace"),
 "Acculturation":("Akkulturation","Acculturation / culture shock")}
NQ=[
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
def nq_page(n):  # Doppelseiten-PDF (38 S.): Incident-Cards gedruckt S. 52–63 -> physisch = gedruckt/2+2
    pr = 52 if n<=3 else 54 if n<=6 else 56 if n<=9 else 58 if n<=14 else 60 if n<=18 else 62
    return pr//2 + 2
for num,ctx,title,themes in NQ:
    items.append({"kind":"nq","collection":"NorQuest Toolkit","id":f"NQ-{num:02d}",
        "title":title,"titleEn":None,"sub":NQ_CTX[ctx][0]+" · p. "+str(nq_page(num)),
        "topicMain":"NQ","topicCode":"NQ:"+ctx,"sitMain":"","sitSub":"",
        "nationality":"—","region":"—",
        "interaction":"Lehrende ↔ Lernende / Neuzugewanderte (Kanada)",
        "hasDE":False,"hasEN":True,"themes":themes,"links":[["src",NQ_URL]],
        "page":nq_page(num)})

# ---------- Eine Frage der Perspektive 2 (23 Einzelfälle, HdBA) ----------
EP2_URL="https://www.hdba.de/fileadmin/media/pdf/Lehrende/HILLER__G._-_ZILLMER-TANTAN__U.__2021__Eine_Frage_der_Perspektive_2.pdf"
EP2_TOPICS={"JOB":("Agentur für Arbeit & Jobcenter","Employment agency & job centre"),
 "ARB":("Irritationen am Arbeitsplatz","Workplace"),
 "INT":("Integration in den Arbeitsmarkt","Labour-market integration"),
 "BER":("Studien- & Berufsberatung","Career & study guidance")}
EP2=[
 ("JOB","Die stumme Ehefrau","Indien","18–19"),
 ("JOB","Die Gegensprechanlage","Serbien","20–21"),
 ("JOB","Termin verschlafen","Spanien","22–23"),
 ("JOB","Die brüderliche Hilfe","Marokko","24–25"),
 ("JOB","Mit Kind und Kegel","Italien","26–27"),
 ("JOB","Falscher Name","Polen","28–29"),
 ("JOB","Freches Lächeln","Kolumbien","30–31"),
 ("JOB","Zu pünktlich","Mexiko","32–33"),
 ("JOB","Keine Vollmacht","China","34–35"),
 ("JOB","Der Ordner","Ägypten","36–37"),
 ("JOB","Die unpassende Vertretung","Syrien","38–39"),
 ("ARB","Der kaputte Beamer","Vietnam","40–41"),
 ("ARB","Die „alte Schachtel“","China","42–43"),
 ("ARB","Merkwürdige Kopfbewegung","Pakistan","44–45"),
 ("ARB","Eine Frau an der Spitze","Tunesien","46–47"),
 ("ARB","Unverbindliche Zustimmung","Costa Rica","48–49"),
 ("INT","Der verschmähte Job","Syrien","50–51"),
 ("INT","Der erfahrene Elektriker","Syrien","52–53"),
 ("INT","Verspätung mit Absicht","Ghana","54–55"),
 ("BER","Die stille Schülerin","Japan","56–57"),
 ("BER","Der vehemente Vater","Türkei","58–59"),
 ("BER","Das ungleiche Paar","Singapur","60–61"),
 ("BER","Die Urlaubsvertretung","Türkei","62–63"),
]
EP2_REG={"Indien":"Asien","Serbien":"Europa","Spanien":"Europa","Marokko":"Afrika","Italien":"Europa",
 "Polen":"Europa","Kolumbien":"Amerika","Mexiko":"Amerika","China":"Asien","Ägypten":"Afrika","Syrien":"Asien",
 "Vietnam":"Asien","Pakistan":"Asien","Tunesien":"Afrika","Costa Rica":"Amerika","Ghana":"Afrika",
 "Japan":"Asien","Türkei":"Europa","Singapur":"Asien"}
for i,(topic,title,country,pages) in enumerate(EP2,1):
    items.append({"kind":"ep2","collection":"Eine Frage der Perspektive 2","id":f"EdP2-{i:02d}",
        "title":title,"titleEn":None,"sub":country+" · S. "+pages,
        "topicMain":"EP2","topicCode":"EP2:"+topic,"sitMain":"","sitSub":"",
        "nationality":country,"region":EP2_REG.get(country,"—"),
        "interaction":"Migrant*innen ↔ Agentur für Arbeit / Jobcenter / Arbeitsplatz",
        "hasDE":True,"hasEN":False,"themes":[EP2_TOPICS[topic][0]],
        "links":[["de",EP2_URL]],"pages":pages,"page":int(pages.split("–")[0])//2+2})

# ---------- KulturellDivers (Einzelfälle) ----------
KDT={"EINL":("Einladung & Gastfreundschaft","Invitation & hospitality"),
 "KOMM":("Kommunikation & Höflichkeit","Communication & politeness"),
 "DISK":("Rassismus & Diskriminierung","Racism & discrimination"),
 "GESL":("Geschlechterrollen","Gender roles"),
 "ALLT":("Alltag, Service & Normen","Everyday life, service & norms"),
 "BEH":("Behörden & Institutionen","Authorities & institutions")}
KD=[
 ("marwa","Marwa O.","Marwa: Henna an den Händen","Afghanistan","Asien","DISK","Henna zu Festen – in der Schule dafür gehänselt und ausgegrenzt."),
 ("berfin","Berfin H.","Berfin: Der reservierte Platz","Türkei","Europa","EINL","Bei der Familie des deutschen Freundes wird ihr ein bestimmter Sitzplatz verwehrt."),
 ("wael","Wael Al M.","Wael: Aufstehen vom Esstisch","Syrien","Asien","ALLT","Steht nach dem Essen auf und setzt sich aufs Sofa – die deutsche Familie ist irritiert."),
 ("tabea","Tabea E.","Tabea: Essen ablehnen","Russland","Europa","KOMM","Lehnt bei einer russischstämmigen Gastgeberin Essen ab – diese reagiert enttäuscht."),
 ("jonas","Jonas L.","Jonas: Kein Rückgeld in Indien","Indien","Asien","ALLT","Im Café in Indien bekommt er kein Rückgeld."),
 ("konstantin","Konstantin Z.","Konstantin: Arbeit auf der Ausgrabung","Griechenland","Europa","GESL","Auf einer Grabung in Griechenland wird er von körperlicher Arbeit abgehalten."),
 ("jasina","Jasina Y.","Jasina: Nie zurückeingeladen","Syrien","Asien","EINL","Eine hilfsbereite ältere Dame lädt sie nie zu sich ein – die Distanz irritiert."),
 ("mayyas","Mayyas E.","Mayyas: Lehrerin zu Besuch","Syrien","Asien","EINL","Die Eltern lassen die Lehrerin kaum gehen – diese findet es merkwürdig."),
 ("esam","Esam A.","Esam: Die Frage nach der Familie","Jemen","Asien","KOMM","Die Frage nach der Familie verärgert die deutsche Tandempartnerin."),
 ("mohamad","Mohamad B.","Mohamad: Einladung & getrennt zahlen","Syrien","Asien","EINL","Der deutsche Nachbar lädt ihn ein, will dann aber getrennt zahlen."),
 ("ahmad","Ahmad A.","Ahmad: An der Ausländerbehörde","Syrien","Asien","BEH","Unfreundliche Behandlung am Servicetresen der Ausländerbehörde."),
 ("ida","Ida M.","Ida: Etwas mitbringen","Syrien","Asien","EINL","Bringt zur Einladung bei einer syrischen Familie etwas mit – diese ist irritiert."),
 ("mustafa","Mustafa E.","Mustafa: Kopftuch & Integration","Türkei","Europa","DISK","Nachbarin rät, das Kopftuch wegen des Arbeitsmarkts abzulegen."),
 ("franzi","Franzi C.","Franzi: Verkäuferin im Kaufhaus","Südkorea","Asien","ALLT","In Südkorea folgt ihr eine Verkäuferin trotz Ablehnung."),
 ("lea","Lea P.","Lea: Sinterklaas & „Zwarte Piet“","Niederlande","Europa","DISK","Niederländisches Nikolausfest mit „Zwarte Piet“ – die Freundin ist schockiert."),
 ("anna","Anna K.","Anna: Geschenke im Reisebus","Türkei","Europa","ALLT","Im Türkei-Urlaub gibt es im Bus Kolonya und Wasser – Verwirrung übers Bezahlen."),
 ("verena","Verena S.","Verena: An der Tankstelle in Frankreich","Frankreich","Europa","ALLT","In Frankreich wird sie an der Tankstelle abweisend behandelt."),
 ("roaa","Roaa B.","Roaa: Platz anbieten im Bus","Syrien","Asien","GESL","Ihr Nachbar bietet einer jungen Frau den Platz an – sie lehnt verärgert ab."),
]
KD_BASE="https://www.kulturelldivers.de/fallbeispiel-"
for i,(slug,name,title,nat,reg,topic,desc) in enumerate(KD,1):
    items.append({"kind":"kd","collection":"KulturellDivers","id":f"KD-{i:02d}",
        "title":title,"titleEn":None,"sub":name+" · "+nat,
        "topicMain":"KD","topicCode":"KD:"+topic,"sitMain":"","sitSub":"",
        "nationality":nat,"region":reg,"interaction":desc,
        "hasDE":True,"hasEN":False,"themes":["Multiperspektivität"],
        "links":[["src",KD_BASE+slug]]})

collections=[]

DATA={"items":items,"collections":collections,"edpTopics":EDP_TOPICS,"nqCtx":NQ_CTX,"kdTopics":KDT,"ep2Topics":EP2_TOPICS}

html = r"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Critical Incidents · Metasuche</title>
<style>
:root{--bg:#F0EEE6;--surface:#FBFAF7;--card:#FFFFFF;--ink:#1A1915;--muted:#6E6A60;
 --line:#E5E0D4;--line2:#D8D2C4;--accent:#C9603F;--accent-d:#A84E32;--accent-soft:#F4E5DD;
 --chip:#EFEBDF;--chip-ink:#5C584F;--badge-en:#E7EEE6;--badge-en-ink:#3F6B47;
 --mu:#1A1915;--edp:#3E6B8A;--ep2:#27607A;--nq:#7A5BA6;--kd:#2E7D6B;--shadow:0 1px 2px rgba(40,35,25,.05),0 4px 16px rgba(40,35,25,.05);}
*{box-sizing:border-box}html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:var(--accent-d);text-decoration:none}a:hover{text-decoration:underline}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
header.top{border-bottom:1px solid var(--line);background:var(--bg);position:sticky;top:0;z-index:20}
.topbar{display:flex;align-items:flex-start;justify-content:space-between;gap:18px;padding:22px 0 16px}
.brand h1{font-family:Georgia,"Times New Roman",serif;font-weight:600;font-size:25px;margin:0 0 4px;letter-spacing:-.2px}
.brand p{margin:0;color:var(--muted);font-size:14px;max-width:680px}
.langtoggle{display:inline-flex;border:1px solid var(--line2);border-radius:999px;overflow:hidden;background:var(--surface);flex:none}
.langtoggle button{border:0;background:transparent;padding:7px 14px;font-size:13px;font-weight:600;color:var(--muted);cursor:pointer}
.langtoggle button.active{background:var(--accent);color:#fff}
.controls{display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr 1fr .9fr auto;gap:10px;padding:0 0 18px;align-items:end}
.controls .field{display:flex;flex-direction:column;gap:4px}
.controls label{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);font-weight:600;text-align:left;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.controls input,.controls select{font:inherit;font-size:14px;padding:9px 11px;border:1px solid var(--line2);border-radius:10px;background:var(--surface);color:var(--ink);width:100%}
.controls input:focus,.controls select:focus{outline:2px solid var(--accent-soft);border-color:var(--accent)}
.resetbtn{align-self:end;border:1px solid var(--line2);background:var(--surface);color:var(--ink);border-radius:10px;padding:9px 14px;font:inherit;font-size:14px;cursor:pointer;height:39px}
.resetbtn:hover{background:#fff;border-color:var(--accent)}
main{padding:22px 0 60px}
.section-title{font-family:Georgia,serif;font-size:15px;font-weight:600;margin:6px 0 12px;display:flex;align-items:center;gap:9px;color:var(--ink)}
.section-title .ln{flex:1;height:1px;background:var(--line)}
.colgrid{display:grid;grid-template-columns:1fr;gap:14px;margin-bottom:30px}
.colcard{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:16px 18px 14px;display:flex;flex-direction:column;box-shadow:var(--shadow)}
.colcard .cname{font-size:12px;font-weight:700;color:var(--accent-d);text-transform:uppercase;letter-spacing:.05em}
.colcard h3{font-family:Georgia,serif;font-size:16px;margin:6px 0 7px;font-weight:600;line-height:1.3}
.colcard p{margin:0 0 11px;font-size:13px;color:var(--muted)}
.themes{display:flex;flex-wrap:wrap;gap:5px;margin-bottom:11px}
.theme{font-size:11px;background:var(--chip);color:var(--chip-ink);border-radius:6px;padding:2px 7px}
.colcard .go{font-size:13px;font-weight:600}
.statusbar{display:flex;align-items:baseline;justify-content:space-between;margin:4px 0 14px;gap:12px;flex-wrap:wrap}
.count{font-size:14px;color:var(--muted)}.count b{color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:15px 16px 13px;display:flex;flex-direction:column;box-shadow:var(--shadow);transition:border-color .12s,transform .12s}
.card:hover{border-color:var(--line2);transform:translateY(-1px)}
.card .head{display:flex;align-items:center;gap:9px;margin-bottom:8px}
.idbadge{font-family:"SF Mono",ui-monospace,Menlo,monospace;font-size:11.5px;font-weight:700;color:#fff;border-radius:6px;padding:3px 8px;letter-spacing:.4px;flex:none}
.idbadge.mu{background:var(--mu)}.idbadge.edp{background:var(--edp)}.idbadge.ep2{background:var(--ep2)}.idbadge.nq{background:var(--nq)}.idbadge.kd{background:var(--kd)}
.card h3{font-size:15px;margin:0;font-weight:600;line-height:1.25}
.fach{font-size:12.5px;color:var(--muted);margin:0 0 9px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 9px}
.chip{font-size:11.5px;border-radius:7px;padding:3px 9px;display:inline-flex;align-items:center;gap:5px}
.chip.sit{background:var(--accent-soft);color:var(--accent-d)}
.chip.nat{background:var(--chip);color:var(--chip-ink)}
.chip.en{background:var(--badge-en);color:var(--badge-en-ink);font-weight:600}
.inter{font-size:12.5px;color:var(--muted);margin:0 0 12px;flex:1}.inter b{color:var(--ink);font-weight:600}
.links{display:flex;flex-wrap:wrap;gap:7px;border-top:1px solid var(--line);padding-top:11px;margin-top:auto}
.lnk{font-size:12.5px;font-weight:600;border:1px solid var(--line2);border-radius:8px;padding:6px 10px;color:var(--accent-d);background:var(--surface)}
.lnk:hover{background:var(--accent);color:#fff;border-color:var(--accent);text-decoration:none}
.lnk.muted{color:var(--chip-ink)}
.empty{text-align:center;color:var(--muted);padding:60px 20px;font-size:15px}
footer{border-top:1px solid var(--line);margin-top:10px;padding:22px 0 50px;color:var(--muted);font-size:12.5px}
footer p{margin:0 0 8px;max-width:880px}footer a{color:var(--accent-d)}
.note{background:var(--accent-soft);border:1px solid #EAD3C8;color:#7a4634;border-radius:10px;padding:11px 14px;font-size:13px;margin-bottom:18px}
footer h4{font-family:Georgia,serif;font-size:13.5px;font-weight:600;color:var(--ink);margin:14px 0 8px}
.refs{margin:0 0 14px}
.ref{padding-left:2.2em;text-indent:-2.2em;margin:0 0 9px;max-width:900px;font-size:12.5px;color:var(--muted)}
.ref i{font-style:italic}
.ref a{color:var(--accent-d);word-break:break-word}
@media(max-width:980px){.controls{grid-template-columns:1fr 1fr}.resetbtn{grid-column:span 2}}
@media(max-width:560px){.controls{grid-template-columns:1fr}.resetbtn{grid-column:span 1}}
</style>
</head>
<body>
<header class="top"><div class="wrap">
  <div class="topbar"><div class="brand"><h1 id="t-title"></h1><p id="t-sub"></p></div>
    <div class="langtoggle"><button id="lang-de" class="active" onclick="setLang('de')">DE</button><button id="lang-en" onclick="setLang('en')">EN</button></div></div>
  <div class="controls">
    <div class="field"><label id="l-search"></label><input id="q" type="search" oninput="render()"></div>
    <div class="field"><label id="l-coll"></label><select id="f-coll" onchange="render()"></select></div>
    <div class="field"><label id="l-sit"></label><select id="f-sit" onchange="render()"></select></div>
    <div class="field"><label id="l-region"></label><select id="f-region" onchange="render()"></select></div>
    <div class="field"><label id="l-nat"></label><select id="f-nat" onchange="render()"></select></div>
    <div class="field"><label id="l-lang"></label><select id="f-lang" onchange="render()"></select></div>
    <button class="resetbtn" id="l-reset" onclick="resetFilters()"></button>
  </div></div></header>
<main class="wrap">
  <div class="note" id="t-note"></div>
  <div id="collections-wrap"><div class="section-title"><span id="t-collections"></span><span class="ln"></span></div>
    <div class="colgrid" id="colgrid"></div></div>
  <div class="statusbar"><div class="section-title" style="margin:0"><span id="t-cases"></span></div><div class="count" id="count"></div></div>
  <div class="grid" id="grid"></div><div class="empty" id="empty" style="display:none"></div>
</main>
<footer class="wrap"><p id="t-foot1"></p><p id="t-foot2"></p>
<h4 id="t-refs"></h4>
<div class="refs">
 <p class="ref">Apedaile, S., &amp; Schill, L. (2008). <i>Critical incidents for intercultural communication: An interactive tool for developing awareness, knowledge, and skills</i> (Facilitator and activity guide). NorQuest College, Intercultural Education Programs. <a target="_blank" href="https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf">https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf</a></p>
 <p class="ref">Deutsches Studentenwerk. (2016). <i>Eine Frage der Perspektive: Critical Incidents aus Studentenwerken und Hochschulverwaltung</i>. <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/user_upload/dsw-fallbeispiele-digital-druckboegen_0.pdf">https://www.studierendenwerke.de/fileadmin/user_upload/dsw-fallbeispiele-digital-druckboegen_0.pdf</a></p>
 <p class="ref">Deutsches Studentenwerk. (2018). <i>A matter of perspective: Critical incidents from the point of view of Studentenwerke and higher education institutions</i>. <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf">https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf</a></p>
 <p class="ref">Hiller, G. G., &amp; Zillmer-Tantan, U. (2022). <i>Eine Frage der Perspektive 2: Critical Incidents aus den Bereichen arbeitsmarktbezogene Beratung, Vermittlung und Integration</i>. Hochschule der Bundesagentur f&uuml;r Arbeit. <a target="_blank" href="https://www.hdba.de/fileadmin/media/pdf/Lehrende/HILLER__G._-_ZILLMER-TANTAN__U.__2021__Eine_Frage_der_Perspektive_2.pdf">https://www.hdba.de/fileadmin/media/pdf/Lehrende/HILLER__G._-_ZILLMER-TANTAN__U.__2021__Eine_Frage_der_Perspektive_2.pdf</a></p>
 <p class="ref">MuMiS-Projekt. (2011). <i>Critical Incidents: Datenbank interkultureller Missverst&auml;ndnisse im Hochschulkontext</i> [Datenbank]. Universit&auml;t Kassel. <a target="_blank" href="https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html">https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html</a></p>
 <p class="ref">Zentrum f&uuml;r Schl&uuml;sselqualifikationen, Christian-Albrechts-Universit&auml;t zu Kiel. (2020). <i>Critical Incidents: Fallbeispiele</i>. <a target="_blank" href="https://www.kulturelldivers.de/fallbeispiele">https://www.kulturelldivers.de/fallbeispiele</a></p>
</div>
<p id="t-foot3"></p></footer>
<script>
const DATA=__DATA__;
const I18N={
 de:{title:"Critical Incidents · Metasuche",
  sub:"Durchsuchbarer Index interkultureller Critical Incidents: MuMiS (162), Eine Frage der Perspektive 1 (30, DE+EN) & 2 (23), NorQuest Toolkit (21), KulturellDivers (18) – mit Direktlinks zu den Quellen.",
  search:"Suche (Titel, Land, Stichwort, ID …)",searchLabel:"Suche",coll:"Sammlung",sit:"Situation / Thema",region:"Region",nat:"Nationalität",lang:"Sprache",reset:"Zurücksetzen",
  collections:"Weitere Sammlung (ohne Einzellinks)",cases:"Fälle",all:"Alle",langEN:"Englisch verfügbar",langDE:"Deutsch verfügbar",
  counts:(n,t)=>`<b>${n}</b> von ${t} Fällen`,interaktion:"Interaktion:",openMu:"Fall (DE)",komm:"+ Kommentar",enPdf:"EN PDF",
  edpDe:"DE · S. ",edpEn:"EN · S. ",openNq:"Toolkit (PDF)",openKd:"Zum Fall",go:"Zur Sammlung →",empty:"Keine Fälle für diese Filter. Bitte Auswahl anpassen.",
  note:"Hinweis: Aus urheberrechtlichen Gründen werden keine Falltexte gespiegelt. Karten verlinken direkt auf die offiziellen Quellen (MuMiS-PDFs je Fall; EdP deutsch & englisch mit Seitenangabe; NorQuest-PDF).",
  gMu:"MuMiS – Kommunikationssituationen",gEp:"Eine Frage der Perspektive 1 – Themen",gEp2:"Eine Frage der Perspektive 2 – Themen",gNq:"NorQuest – Kontexte",gKd:"KulturellDivers – Themen",
  refs:"Zitiernachweise (APA, 7. Aufl.)",
  foot1:"Datengrundlagen: MuMiS (Univ. Siegen/Bielefeld/Köln, VolkswagenStiftung; gehostet Univ. Kassel) · „Eine Frage der Perspektive“ (Deutsches Studentenwerk, 2016) · „Eine Frage der Perspektive 2“ (HdBA, 2022) · KulturellDivers (ZfS, Univ. Kiel, 2020) · NorQuest College (2008).",
  foot2:'Quellen: <a target="_blank" href="https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html">MuMiS</a> · <a target="_blank" href="https://www.kulturelldivers.de/fallbeispiele">KulturellDivers</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/user_upload/dsw-fallbeispiele-digital-druckboegen_0.pdf">Eine Frage der Perspektive (DE)</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf">A Matter of Perspective (EN)</a> · <a target="_blank" href="https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf">NorQuest Toolkit</a>',
  foot3:"Didaktischer Hinweis: Fälle nicht nach dem Muster „Menschen aus Land X verhalten sich so“ deuten. Kulturelle, institutionelle, situative und persönliche Faktoren wirken zusammen (vgl. K-P-S-I-Modell)."},
 en:{title:"Critical Incidents · Meta-search",
  sub:"Searchable index of intercultural critical incidents: MuMiS (162), A Matter of Perspective 1 (30, DE+EN) & 2 (23), the NorQuest Toolkit (21), KulturellDivers (18) – with direct links to the sources.",
  search:"Search (title, country, keyword, ID …)",searchLabel:"Search",coll:"Collection",sit:"Situation / theme",region:"Region",nat:"Nationality",lang:"Language",reset:"Reset",
  collections:"Further collection (no individual links)",cases:"Cases",all:"All",langEN:"English available",langDE:"German available",
  counts:(n,t)=>`<b>${n}</b> of ${t} cases`,interaktion:"Interaction:",openMu:"Case (DE)",komm:"+ Commentary",enPdf:"EN PDF",
  edpDe:"DE · p. ",edpEn:"EN · p. ",openNq:"Toolkit (PDF)",openKd:"Open case",go:"Open collection →",empty:"No cases for these filters. Please adjust your selection.",
  note:"Note: for copyright reasons no case texts are mirrored. Cards link directly to the official sources (MuMiS PDFs per case; A Matter of Perspective German & English with page reference; NorQuest PDF).",
  gMu:"MuMiS – communication situations",gEp:"A Matter of Perspective 1 – topics",gEp2:"A Matter of Perspective 2 – topics",gNq:"NorQuest – contexts",gKd:"KulturellDivers – topics",
  refs:"References (APA, 7th ed.)",
  foot1:"Sources: MuMiS (Univ. Siegen/Bielefeld/Cologne, Volkswagen Foundation; hosted at Univ. Kassel) · ‘A Matter of Perspective’ (Deutsches Studentenwerk, 2016) · ‘Eine Frage der Perspektive 2’ (HdBA, 2022) · KulturellDivers (ZfS, Univ. Kiel, 2020) · NorQuest College (2008).",
  foot2:'Sources: <a target="_blank" href="https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html">MuMiS</a> · <a target="_blank" href="https://www.kulturelldivers.de/fallbeispiele">KulturellDivers</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/user_upload/dsw-fallbeispiele-digital-druckboegen_0.pdf">Eine Frage der Perspektive (DE)</a> · <a target="_blank" href="https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf">A Matter of Perspective (EN)</a> · <a target="_blank" href="https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf">NorQuest Toolkit</a>',
  foot3:"Didactic note: do not read cases as ‘people from country X behave like this’. Cultural, institutional, situational and personal factors interact (cf. the K-P-S-I model)."}};
const SITMAIN={A:{de:"Kommunikation in Lehrveranstaltungen",en:"Communication in courses"},B:{de:"Kommunikation mit Dozenten",en:"Communication with lecturers"},C:{de:"Kommunikation in Arbeitsgruppen",en:"Communication in working groups"},D:{de:"Kommunikation unter Studierenden",en:"Communication among students"}};
const SITSUB={A1:{de:"Lehr- & Lernstile",en:"Teaching & learning styles"},A2:{de:"Verhaltensnormen in Lehrveranstaltungen",en:"Behavioural norms in courses"},B1:{de:"Kontaktaufnahme & Kontaktpflege",en:"Making & keeping contact"},B2:{de:"Betreuung & Bewertung von Leistungen",en:"Supervision & assessment"},C1:{de:"Gruppenarbeit in Lehrveranstaltungen",en:"Group work in courses"},C2:{de:"Gruppen-/Partnerarbeit (Leistungen)",en:"Group/pair work (assessment)"},C3:{de:"Gruppenarbeit in Forschungsgruppen",en:"Group work in research groups"},D1:{de:"Kontaktaufnahme & Verabredungen",en:"Making contact & arrangements"},D2:{de:"Einladungen & Besuche",en:"Invitations & visits"},D3:{de:"Gesprächsthemen & -stile",en:"Conversation topics & styles"},D4:{de:"Zusammenleben im Wohnheim",en:"Living together in halls"}};
const REGIONI={"Afrika":{de:"Afrika",en:"Africa"},"Amerika":{de:"Amerika",en:"Americas"},"Asien":{de:"Asien",en:"Asia"},"Europa":{de:"Europa",en:"Europe"},"—":{de:"übergreifend",en:"unspecified"}};
const EDPT=DATA.edpTopics,NQC=DATA.nqCtx,KDC=DATA.kdTopics,EP2C=DATA.ep2Topics;
let LANG="de";
function T(){return I18N[LANG]}
function titleOf(c){return (LANG==="en"&&c.titleEn)?c.titleEn:c.title}
function topicLabel(c){if(c.kind==="mumis")return SITSUB[c.sitSub][LANG];
 if(c.kind==="edp")return EDPT[c.topicCode.slice(3)][LANG==="de"?0:1];
 if(c.kind==="ep2")return EP2C[c.topicCode.slice(4)][LANG==="de"?0:1];
 if(c.kind==="nq")return NQC[c.topicCode.slice(3)][LANG==="de"?0:1];
 if(c.kind==="kd")return KDC[c.topicCode.slice(3)][LANG==="de"?0:1];return""}
function setLang(l){LANG=l;document.getElementById('lang-de').classList.toggle('active',l==='de');
 document.getElementById('lang-en').classList.toggle('active',l==='en');document.documentElement.lang=l;
 buildStaticText();buildSelects(true);render()}
function buildStaticText(){const t=T();document.title=t.title;
 for(const[id,k] of [["t-title","title"],["t-sub","sub"],["l-search","searchLabel"],["l-coll","coll"],["l-sit","sit"],["l-region","region"],["l-nat","nat"],["l-lang","lang"],["l-reset","reset"],["t-collections","collections"],["t-cases","cases"],["t-note","note"],["t-foot1","foot1"],["t-refs","refs"],["t-foot3","foot3"]])document.getElementById(id).textContent=t[k];
 document.getElementById('t-foot2').innerHTML=t.foot2;document.getElementById('q').placeholder=t.search}
function opt(v,l){return `<option value="${v}">${l}</option>`}
function og(l,inner){return `<optgroup label="${l}">${inner}</optgroup>`}
function buildSelects(keep){const t=T();
 const prev=keep?Object.fromEntries(['f-coll','f-sit','f-region','f-nat','f-lang'].map(i=>[i,val(i)])):{};
 const colls=["MuMiS","Eine Frage der Perspektive 1","Eine Frage der Perspektive 2","NorQuest Toolkit","KulturellDivers",...DATA.collections.map(c=>c.collection)];
 document.getElementById('f-coll').innerHTML=opt("",t.all)+colls.map(c=>opt(c,c)).join('');
 let mu="";["A","B","C","D"].forEach(m=>{mu+=opt("main:MU:"+m,SITMAIN[m][LANG]);
   DATA.items.filter(c=>c.kind==="mumis"&&c.sitMain===m).map(c=>c.sitSub).filter((v,i,a)=>a.indexOf(v)===i).sort().forEach(s=>{mu+=opt("sub:MU:"+s,"· "+SITSUB[s][LANG])})});
 let ep=Object.keys(EDPT).map(k=>opt("sub:EP:"+k,EDPT[k][LANG==="de"?0:1])).join('');
 let ep2=Object.keys(EP2C).map(k=>opt("sub:EP2:"+k,EP2C[k][LANG==="de"?0:1])).join('');
 let nq=Object.keys(NQC).map(k=>opt("sub:NQ:"+k,NQC[k][LANG==="de"?0:1])).join('');
 let kd=Object.keys(KDC).map(k=>opt("sub:KD:"+k,KDC[k][LANG==="de"?0:1])).join('');
 document.getElementById('f-sit').innerHTML=opt("",t.all)+og(t.gMu,mu)+og(t.gEp,ep)+og(t.gEp2,ep2)+og(t.gNq,nq)+og(t.gKd,kd);
 const regs=[...new Set(DATA.items.map(c=>c.region))].filter(r=>r!=="—").sort();
 document.getElementById('f-region').innerHTML=opt("",t.all)+regs.map(r=>opt(r,REGIONI[r]?REGIONI[r][LANG]:r)).join('');
 const nats=[...new Set(DATA.items.map(c=>c.nationality))].filter(n=>n&&n!=="—").sort((a,b)=>a.localeCompare(b,'de'));
 document.getElementById('f-nat').innerHTML=opt("",t.all)+nats.map(n=>opt(n,n)).join('');
 document.getElementById('f-lang').innerHTML=opt("",t.all)+opt("DE",t.langDE)+opt("EN",t.langEN);
 if(keep)Object.entries(prev).forEach(([i,v])=>set(i,v))}
function val(id){const e=document.getElementById(id);return e?e.value:""}
function set(id,v){const e=document.getElementById(id);if(e)e.value=v||""}
function resetFilters(){['q','f-coll','f-sit','f-region','f-nat','f-lang'].forEach(i=>set(i,''));render()}
function matchItem(c,f){
 if(f.coll&&c.collection!==f.coll)return false;
 if(f.sit){if(f.sit.startsWith("main:")){if(c.topicMain!==f.sit.slice(5))return false}
   else if(f.sit.startsWith("sub:")){if(c.topicCode!==f.sit.slice(4))return false}}
 if(f.region&&c.region!==f.region)return false;
 if(f.nat&&c.nationality!==f.nat)return false;
 if(f.lang==="EN"&&!c.hasEN)return false;
 if(f.lang==="DE"&&!c.hasDE)return false;
 if(f.q){const hay=(c.id+" "+c.title+" "+(c.titleEn||"")+" "+c.sub+" "+c.interaction+" "+c.nationality+" "+c.collection+" "+(c.themes||[]).join(" ")+" "+SITSUB[c.sitSub]?.de+" "+topicLabel(c)).toLowerCase();
   if(!f.q.split(/\s+/).every(w=>hay.includes(w)))return false}
 return true}
function matchColl(col,f){if(f.coll&&f.coll!==col.collection)return false;
 if(f.sit||f.region||f.nat||f.lang)return false;
 if(f.q){const hay=(col.collection+" "+col.title+" "+col.desc_de+" "+col.desc_en+" "+col.themes.join(" ")).toLowerCase();
   if(!f.q.split(/\s+/).every(w=>hay.includes(w)))return false}return true}
function esc(s){return (s||"").replace(/[&<>"]/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m]))}
function card(c){const t=T();const cls={mumis:"mu",edp:"edp",ep2:"ep2",nq:"nq",kd:"kd"}[c.kind];
 const en=c.hasEN?`<span class="chip en">EN</span>`:"";
 const nat=c.nationality&&c.nationality!=="—"?`<span class="chip nat">${esc(c.nationality)}</span>`:"";
 const themechips=(c.themes||[]).slice(0,4).map(x=>`<span class="chip nat">${esc(x)}</span>`).join('');
 let links="";
 if(c.kind==="mumis"){const L=Object.fromEntries(c.links);
   links=`<a class="lnk" target="_blank" href="${L.de}">${t.openMu}</a><a class="lnk muted" target="_blank" href="${L.komm}">${t.komm}</a>`+(L.en?`<a class="lnk" target="_blank" href="${L.en}">${t.enPdf}</a>`:"")}
 else if(c.kind==="edp"){const L=Object.fromEntries(c.links);const pg=c.page?("#page="+c.page):"";
   links=`<a class="lnk" target="_blank" href="${L.de}${pg}">${t.edpDe}${esc(c.pages||"")}</a><a class="lnk muted" target="_blank" href="${L.en}${pg}">${t.edpEn}${esc(c.pages||"")}</a>`}
 else if(c.kind==="ep2"){const pg=c.page?("#page="+c.page):"";
   links=`<a class="lnk" target="_blank" href="${c.links[0][1]}${pg}">${t.edpDe}${esc(c.pages||"")}</a>`}
 else if(c.kind==="kd"){links=`<a class="lnk" target="_blank" href="${c.links[0][1]}">${t.openKd}</a>`}
 else{const pg=c.page?("#page="+c.page):"";
   links=`<a class="lnk" target="_blank" href="${c.links[0][1]}${pg}">${t.openNq}${c.page?(" · p. "+c.page):""}</a>`}
 return `<div class="card"><div class="head"><span class="idbadge ${cls}">${esc(c.id)}</span><h3>${esc(titleOf(c))}</h3></div>
  <p class="fach">${esc(c.sub||"")}</p>
  <div class="chips"><span class="chip sit">${esc(topicLabel(c))}</span>${nat}${en}${c.kind!=="mumis"?themechips:""}</div>
  <p class="inter"><b>${t.interaktion}</b> ${esc(c.interaction||"–")}</p><div class="links">${links}</div></div>`}
function collCard(col){const t=T();const desc=LANG==="de"?col.desc_de:col.desc_en;
 return `<div class="colcard"><span class="cname">${esc(col.collection)} · ${esc(col.count)}</span><h3>${esc(col.title)}</h3><p>${esc(desc)}</p>
  <div class="themes">${col.themes.map(x=>`<span class="theme">${esc(x)}</span>`).join('')}<span class="theme">${col.langs.join(" / ")}</span></div>
  <a class="go" target="_blank" href="${col.url}">${t.go}</a></div>`}
function render(){const t=T();
 const f={q:val('q').trim().toLowerCase(),coll:val('f-coll'),sit:val('f-sit'),region:val('f-region'),nat:val('f-nat'),lang:val('f-lang')};
 const cols=DATA.collections.filter(c=>matchColl(c,f));
 document.getElementById('colgrid').innerHTML=cols.map(collCard).join('');
 document.getElementById('collections-wrap').style.display=cols.length?"block":"none";
 const cs=DATA.items.filter(c=>matchItem(c,f));
 document.getElementById('grid').innerHTML=cs.map(card).join('');
 document.getElementById('count').innerHTML=t.counts(cs.length,DATA.items.length);
 const emp=document.getElementById('empty');
 if(cs.length===0&&cols.length===0){emp.style.display="block";emp.textContent=t.empty}else emp.style.display="none"}
buildStaticText();buildSelects(false);render();
</script>
</body></html>"""
html=html.replace("__DATA__",json.dumps(DATA,ensure_ascii=False))
open(OUT+"critical-incidents-metasuche.html","w",encoding="utf-8").write(html)
print("OK items",len(items),"edp",sum(1 for i in items if i['kind']=='edp'),"bytes",len(html))

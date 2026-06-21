#!/usr/bin/env python3
import re, json, glob, os

DIR = "/sessions/practical-brave-johnson/mnt/.claude/projects/-Users-maik-Library-Application-Support-Claude-local-agent-mode-sessions-6fcbfcb5-2b32-4f77-8cd5-7daaa9ed68ef-af8a16fe-8178-48bd-ac62-f59795d76e4d-local-63d36b5e-983d-4eea-ac02-6b43c1f3224e-outputs/5f964a52-e085-40c5-a329-76bf77d5e49d/tool-results"
OUT = "/sessions/practical-brave-johnson/mnt/outputs/"
PDF = "https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/ci_datenbank/"

def load_text(path):
    raw = open(path, encoding="utf-8").read()
    if path.endswith(".json"):
        try:
            data = json.loads(raw)
            return "\n".join(b.get("text","") for b in data if isinstance(b,dict))
        except Exception:
            return raw
    return raw

# ---- parse a markdown blob into case dicts ----
header_re = re.compile(r"^\|\s*\*{0,2}([A-D]\d{2})\*{0,2}\s+(.+?)\s*\|\s*$")
inter_re  = re.compile(r"^\|\s*Interaktionspartner:\s*\|\s*(.+?)\s*\|\s*$")

def parse_blob(blob):
    out = {}
    en_ids = set(re.findall(r"([A-D]\d{2})_EN\.pdf", blob))
    de_ids = set(re.findall(r"([A-D]\d{2})_DE\.pdf", blob))
    lines = blob.split("\n")
    for i, line in enumerate(lines):
        m = header_re.match(line)
        if not m: continue
        cid = m.group(1)
        if cid not in de_ids: continue
        title = m.group(2).strip().strip("*").strip()
        inter = ""
        for j in range(i+1, min(i+12, len(lines))):
            im = inter_re.match(lines[j])
            if im: inter = im.group(1).strip(); break
        out[cid] = {"id": cid, "title": title, "interaction": inter, "en": cid in en_ids}
    return out, en_ids

cases = {}
all_en = set()
for path in sorted(glob.glob(os.path.join(DIR, "*.txt")) + glob.glob(os.path.join(DIR, "*.json"))):
    blob = load_text(path)
    parsed, en = parse_blob(blob)
    all_en |= en
    for cid, c in parsed.items():
        if cid not in cases:
            cases[cid] = c
        else:
            # keep richer interaction
            if not cases[cid]["interaction"] and c["interaction"]:
                cases[cid]["interaction"] = c["interaction"]

# ---- inline-only cases (seen in context, not on disk) ----
# format: id : (title, interaction, en)
inline = {
 "A01": ("Ricardo / Kolumbien / Informatik", "deutsche Dozenten", True),
 "A04": ("Sophia / Tschechien / Germanistik", "deutsche Studierende", False),
 "A05": ("John / USA / Germanistik", "deutsche Studierende", True),
 "A06": ("Frau Müller / deutsche Dozentin / Deutsch als Fremdsprache", "taiwanesische Studentinnen", True),
 "A10": ("Elias / Syrien / Wirtschaftsinformatik", "deutsche Dozentin", False),
 "A11": ("François / Gabun / Politikwissenschaften", "deutsche Studentin, deutscher Dozent", False),
 "A12": ("Frau Kleinbauer / deutsche Dozentin / Deutsch als Fremdsprache", "ägyptischer Student", False),
 "A13": ("Ana María / Spanien / Ingenieurwissenschaften", "deutsche Dozenten", False),
 "B24": ("Herr Grosse / deutscher Dozent / Anglistik", "taiwanesischer Student", True),
 "B33": ("Semir / Tunesien / Pharmazie", "deutscher Dozent", False),
 "C01": ("Frau Baumann / deutsche Dozentin / Deutsch als Fremdsprache", "südkoreanischer Student", False),
 "C03": ("Mihai / Rumänien / Betriebswirtschaft", "deutsche Studierende", False),
 "C05": ("Karin / Deutschland / Studiengang unbekannt", "vietnamesischer Student", False),
 "C06": ("Viera / Slowakei / Wirtschaftswissenschaften", "deutscher Student", False),
 "C08": ("Herr Lehmann / deutscher Dozent / Sozialwissenschaften", "marokkanischer Student", False),
 "C28": ("Wadim / Usbekistan / Mechatronik", "zwei deutsche Studenten", True),
 "C29": ("Herr Siebert / deutscher Dozent / Ingenieurwissenschaften", "zwei indische Studenten", False),
 "C30": ("Herr Baumgarten / deutscher Dozent / Ingenieurwissenschaften", "türkischer Student", False),
 "C32": ("Daniela / Deutschland / Ingenieurwissenschaften", "marokkanischer Student", True),
 "D01": ("Kwan / Südkorea / Ingenieurwissenschaften", "deutsche Studierende", False),
 "D02": ("Mourad / Tunesien / Wirtschaftsinformatik", "deutsche Studierende und Schüler", False),
 "D03": ("Esther / Deutschland / Romanistik", "indischer Student", False),
 "D04": ("Dharmesh / Indien / Betriebswirtschaft", "deutscher Student", True),
 "D05": ("Manu / Angola / Maschinenbau", "deutsche Studierende", True),
 "D06": ("Claudia / Deutschland / Kulturwissenschaften", "türkische Studentin", True),
 "D07": ("Linda / Deutschland / Romanistik", "zwei spanische Studenten", True),
 "D08": ("Kerstin / Deutschland / Literaturwissenschaft", "senegalesischer Student", False),
 "D09": ("Janina / Deutschland / Romanistik", "südkoreanischer Student", True),
 "D11": ("Dolores / Spanien / Germanistik", "deutsche Studierende", True),
 "D32": ("Lonell / USA / Germanistik", "deutsche Studierende", True),
 "D33": ("Sybille / Deutschland / Germanistik", "spanische Studierende", True),
 "D37": ("Cosmin / Rumänien / Wirtschaftswissenschaften", "deutsche Studentin", False),
 "D40": ("Ana Paula / Brasilien / Literaturwissenschaften", "deutsche Studentin", True),
 "D42": ("Diana / Rumänien / Sozialwissenschaften", "deutscher Student", False),
 "D45": ("Alba / Spanien / Ingenieurwissenschaften", "deutsche Studierende", True),
 "D46": ("Wayan / Indonesien / Maschinenbau", "zwei deutsche Studenten", True),
 "D47": ("Lucia / Slowakei / Wirtschaftswissenschaften", "deutsche Studierende", True),
 "D48": ("Hülya / Türkei / Wirtschaftswissenschaften", "deutsche Studierende", False),
 "D49": ("Silke / Deutschland / Germanistik", "indischer Student", False),
 "D50": ("Michael und Jan / Deutschland / Physik", "zwei indische Studenten", False),
 "D51": ("Jeff / USA / Geschichte", "deutsche Studierende", True),
 "D52": ("Helene / Deutschland / Romanistik", "taiwanesischer Student", False),
 "D53": ("Debora / Deutschland / Germanistik", "türkische Studentin", True),
 "D54": ("Jürgen / Deutschland / Studiengang unbekannt", "zwei indische Studenten", True),
 "D55": ("Réka / Ungarn / Studiengang unbekannt", "deutscher Student", False),
 "D57": ("Tereza / Tschechien / Germanistik", "zwei deutsche Studenten", True),
 "D61": ("Thanu / Sri Lanka / Wirtschaftwissenschaften", "deutsche Studentin", False),
}
for cid,(title,inter,en) in inline.items():
    if cid not in cases:
        cases[cid] = {"id": cid, "title": title, "interaction": inter, "en": en}

# ---- situation subtype from id ranges ----
def subtype(cid):
    L=cid[0]; n=int(cid[1:])
    if L=="A": return "A1" if n<=15 else "A2"
    if L=="B": return "B1" if n<=22 else "B2"
    if L=="C": return "C1" if n<=8 else ("C2" if n<=26 else "C3")
    if L=="D":
        if n<=12: return "D1"
        if n<=31: return "D2"
        if n<=43: return "D3"
        return "D4"

SIT_MAIN = {"A":"Kommunikation in Lehrveranstaltungen","B":"Kommunikation mit Dozenten",
            "C":"Kommunikation in Arbeitsgruppen","D":"Kommunikation unter Studierenden"}
SUBLABEL = {"A1":"Universitäre Lehr- und Lernstile","A2":"Verhaltensnormen in Lehrveranstaltungen",
 "B1":"Kontaktaufnahme und Kontaktpflege","B2":"Betreuung und Bewertung von Leistungsnachweisen",
 "C1":"Gruppenarbeit in Lehrveranstaltungen","C2":"Gruppen-/Partnerarbeit für Leistungsnachweise",
 "C3":"Gruppenarbeit in Forschungsgruppen","D1":"Kontaktaufnahme und Verabredungen",
 "D2":"Einladungen und Besuche","D3":"Gesprächsthemen und Gesprächsstile",
 "D4":"Zusammenleben im Studentenwohnheim"}

# ---- nationality maps ----
ADJ = {"chinesisch":"China","taiwanesisch":"Taiwan","südkorean":"Südkorea","korean":"Südkorea",
 "indisch":"Indien","vietnamesisch":"Vietnam","indonesisch":"Indonesien","japanisch":"Japan",
 "usbekisch":"Usbekistan","syrisch":"Syrien","türkisch":"Türkei","ägyptisch":"Ägypten",
 "marokkanisch":"Marokko","tunesisch":"Tunesien","senegalesisch":"Senegal","angolanisch":"Angola",
 "kongolesisch":"Kongo","kenian":"Kenia","nigerian":"Nigeria","gabun":"Gabun",
 "polnisch":"Polen","französisch":"Frankreich","tschechisch":"Tschechien","spanisch":"Spanien",
 "russisch":"Russland","rumänisch":"Rumänien","bulgarisch":"Bulgarien","italienisch":"Italien",
 "slowakisch":"Slowakei","ungarisch":"Ungarn","englisch":"England","dänisch":"Dänemark",
 "lettisch":"Lettland","mazedonisch":"Mazedonien","moldav":"Moldavien","portugiesisch":"Portugal",
 "georgisch":"Georgien","peruanisch":"Peru","brasilianisch":"Brasilien","chilenisch":"Chile",
 "kolumbianisch":"Kolumbien","mexikanisch":"Mexiko","amerikanisch":"USA",
 "sri lanka":"Sri Lanka","srilank":"Sri Lanka"}

REGION = {
 "China":"Asien","Taiwan":"Asien","Südkorea":"Asien","Indien":"Asien","Vietnam":"Asien",
 "Indonesien":"Asien","Japan":"Asien","Usbekistan":"Asien","Syrien":"Asien","Sri Lanka":"Asien",
 "Georgien":"Asien","Türkei":"Europa","International":"—",
 "Kasachstan":"Asien","Libanon":"Asien",
 "Moldawien":"Europa","Moldavien":"Europa","Weißrussland":"Europa",
 "Ägypten":"Afrika","Marokko":"Afrika","Tunesien":"Afrika","Senegal":"Afrika","Angola":"Afrika",
 "Kongo":"Afrika","Kenia":"Afrika","Nigeria":"Afrika","Gabun":"Afrika",
 "Polen":"Europa","Frankreich":"Europa","Tschechien":"Europa","Spanien":"Europa","Russland":"Europa",
 "Rumänien":"Europa","Bulgarien":"Europa","Italien":"Europa","Slowakei":"Europa","Ungarn":"Europa",
 "England":"Europa","Dänemark":"Europa","Lettland":"Europa","Mazedonien":"Europa","Moldavien":"Europa",
 "Portugal":"Europa",
 "Peru":"Amerika","Brasilien":"Amerika","Chile":"Amerika","Kolumbien":"Amerika","Mexiko":"Amerika","USA":"Amerika",
}

def split_title(t):
    parts = [p.strip() for p in t.split("/")]
    name = parts[0] if parts else t
    origin = parts[1] if len(parts)>1 else ""
    fach = parts[2] if len(parts)>2 else ""
    return name, origin, fach

def nationality(origin, interaction):
    o = origin.strip()
    if o and o != "Deutschland" and not o.lower().startswith("deutsch"):
        return o
    text = interaction.lower()
    for adj,country in ADJ.items():
        if adj in text:
            return country
    if "international" in text:
        return "International"
    return None

records = []
for cid, c in cases.items():
    name, origin, fach = split_title(c["title"])
    nat = nationality(origin, c["interaction"])
    region = REGION.get(nat, "—") if nat else "—"
    sub = subtype(cid)
    rec = {
        "id": cid,
        "name": name,
        "fach": fach,
        "origin": origin,
        "interaction": c["interaction"],
        "nationality": nat or "—",
        "region": region,
        "sitMain": cid[0],
        "sitMainLabel": SIT_MAIN[cid[0]],
        "sitSub": sub,
        "sitSubLabel": SUBLABEL[sub],
        "en": bool(c["en"]),
        "pdf_de": PDF+cid+"_DE.pdf",
        "pdf_kommentar": PDF+cid+"_DE_Kommentar.pdf",
        "pdf_en": (PDF+cid+"_EN.pdf") if c["en"] else None,
    }
    records.append(rec)

records.sort(key=lambda r:(r["id"][0], int(r["id"][1:])))
json.dump(records, open(OUT+"mumis_full.json","w"), ensure_ascii=False, indent=1)

print("TOTAL:", len(records))
from collections import Counter
print("by sitMain:", dict(Counter(r["sitMain"] for r in records)))
print("by region:", dict(Counter(r["region"] for r in records)))
print("EN:", sum(1 for r in records if r["en"]))
print("nat unknown:", sum(1 for r in records if r["nationality"]=="—"))
print("distinct nationalities:", len(set(r["nationality"] for r in records if r["nationality"]!="—")))
miss=[r["id"] for r in records if r["nationality"]=="—"]
print("unknown-nat ids:", miss)

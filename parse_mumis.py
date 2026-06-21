#!/usr/bin/env python3
import re, json, sys

BASE = "/sessions/practical-brave-johnson/mnt/.claude/projects/-Users-maik-Library-Application-Support-Claude-local-agent-mode-sessions-6fcbfcb5-2b32-4f77-8cd5-7daaa9ed68ef-af8a16fe-8178-48bd-ac62-f59795d76e4d-local-63d36b5e-983d-4eea-ac02-6b43c1f3224e-outputs/5f964a52-e085-40c5-a329-76bf77d5e49d/tool-results/"
OUT = "/sessions/practical-brave-johnson/mnt/outputs/"
FILES = {
    "Asien":  BASE + "mcp-workspace-web_fetch-1781993278419.txt",
    "Europa": BASE + "mcp-workspace-web_fetch-1781993354761.txt",
}

PDF_BASE = "https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/ci_datenbank/"

def parse_file(region, path):
    txt = open(path, encoding="utf-8").read()
    # cut nav/footer: content starts at first "# " country header, ends at "### Critical Incidents" footer nav
    # find all case IDs from PDF links
    cases = {}
    # Track country sections: lines like "# Angola"
    # We'll walk line by line
    lines = txt.split("\n")
    current_country = None
    # First, gather EN availability per ID across whole file
    en_ids = set(re.findall(r"ci_datenbank/([A-Z]\d{2})_EN\.pdf", txt))
    de_ids = set(re.findall(r"ci_datenbank/([A-Z]\d{2})_DE\.pdf", txt))

    # header line pattern: | **A21** Name / Country / Studiengang |  (bold optional)
    header_re = re.compile(r"^\|\s*\*{0,2}([A-Z]\d{2})\*{0,2}\s+(.+?)\s*\|\s*$")
    country_re = re.compile(r"^#\s+([A-Za-zÀ-ÿ' \-]+?)\s*$")
    inter_re = re.compile(r"^\|\s*Interaktionspartner:\s*\|\s*(.+?)\s*\|\s*$")

    i = 0
    last_country_for = {}
    order = []
    while i < len(lines):
        line = lines[i]
        cm = country_re.match(line.strip())
        if cm and cm.group(1) not in ("Amerika",):
            cand = cm.group(1).strip()
            # ignore stray headers
            if cand and not cand.startswith("Critical"):
                current_country = cand
        hm = header_re.match(line)
        if hm:
            cid = hm.group(1)
            title_rest = hm.group(2).strip().strip("*").strip()
            # only accept if this ID actually has a DE pdf somewhere (real case)
            if cid in de_ids and cid not in cases:
                # look ahead for Interaktionspartner within next 8 lines
                inter = ""
                for j in range(i+1, min(i+10, len(lines))):
                    im = inter_re.match(lines[j])
                    if im:
                        inter = im.group(1).strip()
                        break
                cases[cid] = {
                    "id": cid,
                    "title": title_rest,
                    "country": current_country,
                    "region": region,
                    "interaction": inter,
                }
                order.append(cid)
        i += 1
    return cases, en_ids, de_ids

all_cases = {}
all_en = set()
for region, path in FILES.items():
    cases, en_ids, de_ids = parse_file(region, path)
    all_en |= en_ids
    for cid, c in cases.items():
        all_cases[cid] = c

for cid, c in all_cases.items():
    c["en"] = cid in all_en

print("TOTAL parsed:", len(all_cases))
by_region = {}
for c in all_cases.values():
    by_region[c["region"]] = by_region.get(c["region"],0)+1
print("by region:", by_region)
print("EN count:", sum(1 for c in all_cases.values() if c["en"]))
# show countries
countries = sorted(set(c["country"] for c in all_cases.values()))
print("countries:", countries)
# sample
for cid in list(all_cases)[:5]:
    print(all_cases[cid])

json.dump(list(all_cases.values()), open(OUT+"mumis_parsed.json","w"), ensure_ascii=False, indent=1)
print("saved json")

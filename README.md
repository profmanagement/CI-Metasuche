# Critical Incidents · Metasuche

**Eine durchsuchbare Metasuche über interkulturelle *Critical Incidents* aus dem Hochschul- und Beratungskontext.**

[![Lizenz: CC BY-NC-SA 4.0](https://img.shields.io/badge/Lizenz-CC%20BY--NC--SA%204.0-lightgrey.svg)](./LICENSE)
&nbsp;·&nbsp; Open Educational Resource &nbsp;·&nbsp; Lehrveranstaltung *Interkulturelle Kommunikation und Kompetenz*, Hochschule Nordhausen

---

## Idee

*Critical Incidents* sind kurze, authentische Fallbeispiele, in denen Menschen mit unterschiedlichem kulturellem Hintergrund interagieren und es zu Irritationen oder Missverständnissen kommt. Sie sind ein etabliertes Werkzeug in interkulturellen Trainings.

Die einschlägigen Fallsammlungen liegen verstreut auf verschiedenen Projektseiten und in PDFs. Diese **HTML-basiert, auch lokal lauffähige Website** bündelt alle diese Fälle in **einem durchsuchbaren Index** mit einheitlichen Filtern und **Direktlinks zu den Originalquellen** (PDF-Seite bzw. Fallseite). So lässt sich passgenau ein Fall für ein Seminar, eine Übung oder das Selbststudium finden – ohne sich durch mehrere Websites zu klicken.

> **Wichtig:** Es werden **keine Falltexte gespiegelt oder in diese Website integriert, sondern stets nur der Link zum Fall angegeben.** Die App ist ein *Index* (Titel, Land, Thema, Schlagworte) und verlinkt für den vollständigen Fall jeweils auf die offizielle Quelle.

## Aktueller Datenbestand (Juni 2026)

Insgesamt **254 Fälle** aus fünf Sammlungen:

| Sammlung | Fälle | Sprache | Kontext |
| --- | --- | --- | --- |
| **MuMiS** | 162 | DE (80× auch EN) | Hochschulalltag: Lehrveranstaltungen, Dozent\*innen, Arbeitsgruppen, unter Studierenden |
| **Eine Frage der Perspektive 1** | 30 | DE + EN | Studentenwerke & Hochschulverwaltung |
| **Eine Frage der Perspektive 2** | 23 | DE | Arbeitsmarktbezogene Beratung, Vermittlung & Integration (Agentur für Arbeit / Jobcenter) |
| **NorQuest Toolkit** | 21 | EN | Hochschule, Alltag, Arbeitsplatz, Akkulturation (Kanada) |
| **KulturellDivers** | 18 | DE | Multiperspektivische Fallbeispiele (je 3–4 Deutungen) |

## Nutzung

Es handelt sich um eine **HTML-Datei ohne Installation, ohne Server, ohne Internet-Abhängigkeit** (für die Anzeige; die Quell-Links benötigen Sie allerdings eine Internetverbindung).

1. `critical-incidents-metasuche.html` per Doppelklick im Browser öffnen.
2. Filtern und suchen (siehe unten).
3. Über die Buttons auf einer Karte direkt zur Quelle springen.

## Veröffentlichung über GitHub Pages

Das Repository ist für GitHub Pages vorbereitet:

- `index.html` leitet auf die Metasuche weiter, damit die App direkt über die Pages-Startseite erreichbar ist.
- `.github/workflows/pages.yml` veröffentlicht den statischen Inhalt automatisch bei jedem Push auf `main`.

In GitHub muss unter **Settings → Pages → Build and deployment** als Source **GitHub Actions** ausgewählt sein. Danach wird die Seite nach dem nächsten Push automatisch veröffentlicht.

## Funktionen

- **Volltextsuche** über Titel, Land, Schlagwort, ID und Situation
- **Filter** nach Sammlung, Situation/Thema, Region, Nationalität und Sprache (Deutsch / Englisch verfügbar)
- **Umschaltbare Oberfläche Deutsch / Englisch**
- **Direktlinks** zu jedem Fall – bei PDFs seitengenau über `#page=` (Sprung zur richtigen Seite)
- Reduziertes, ruhiges Design; vollständig offline lauffähig

## Nutzungsmöglichkeiten

- **Seminar-Vorbereitung:** schnell einen passenden Fall nach Thema, Region oder Situationstyp finden.
- **Übungen & Trainings:** Fälle als Diskussionsgrundlage; mehrere Perspektiven gegenüberstellen (besonders bei *KulturellDivers*).
- **Selbststudium:** stöbern und vergleichen über Sammlungen hinweg.
- **Strukturierte Analyse:** Fälle eignen sich gut für eine Auswertung nach dem **K-P-S-I-Modell** (Kultur – Person – Situation – Institution; vgl. Bosse, 2011) statt nach dem Muster „Menschen aus Land X verhalten sich so".

### Methodischer Hinweis

Fälle sollten **nicht stereotyp** gedeutet werden. Kulturelle, individuelle, situative und institutionelle Faktoren wirken zusammen; mehrere Erklärungen sind möglich. Leitfragen für eine differenzierte Analyse: *Was irritiert die Beteiligten? Welche Erwartungen treffen aufeinander? Welche kulturellen, personalen, situativen und institutionellen Erklärungen sind denkbar? Welche Handlungsalternative könnte die Situation entschärfen?*

## Urheberrecht & Haftung

- Die **Falltexte, PDFs und Webseiten** liegen bei den jeweiligen Projekten und Herausgebern (siehe *Quellen*). Ihre Rechte bleiben unberührt; sie werden hier **nicht reproduziert**, sondern nur **verlinkt und mit Metadaten erschlossen**.
- Diese Anwendung ist eine **Metasuche / ein Index für Bildungszwecke** und steht in keiner offiziellen Verbindung zu den verlinkten Projekten.
- **Keine Gewähr** für die Verfügbarkeit, Richtigkeit oder Vollständigkeit der verlinkten Originalseiten und ‑datenbanken. Links können sich ändern oder ausfallen. Die zugeordneten Metadaten (Region, Nationalität, Thema) und PDF-Seitenangaben wurden sorgfältig abgeleitet, sind aber ohne Gewähr.
- Wer Inhalte über die bloße Verlinkung hinaus weiterverwenden möchte (z. B. Falltexte spiegeln), muss die Nutzungsrechte bei den jeweiligen Rechteinhabern klären.

## Lizenz

Dieses Repository (Code, Aufbau, Metadaten-Aufbereitung, Dokumentation) ist eine **Open Educational Resource** im Rahmen der Lehrveranstaltung *Interkulturelle Kommunikation und Kompetenz* und steht unter der

**[Creative Commons Namensnennung – Nicht kommerziell – Weitergabe unter gleichen Bedingungen 4.0 International (CC BY-NC-SA 4.0)](./LICENSE).**

Du darfst es **teilen und bearbeiten** und **für nicht-kommerzielle Zwecke weiternutzen und verändern**, solange du die Quelle nennst, nicht kommerziell nutzt und Bearbeitungen unter derselben Lizenz weitergibst.

> Die Lizenz gilt für **dieses Projekt** – **nicht** für die verlinkten Falltexte/Quellen, die ihren eigenen Rechten und Lizenzen unterliegen.

## Quellen (APA, 7. Aufl.)

Apedaile, S., & Schill, L. (2008). *Critical incidents for intercultural communication: An interactive tool for developing awareness, knowledge, and skills* (Facilitator and activity guide). NorQuest College, Intercultural Education Programs. https://www.norquest.ca/NorquestCollege/media/pdf/about/resources/intercultural-resources-for-educators/critical-incidents-for-intercultural-communication-toolkit.pdf

Bosse, Elke (2011). *Qualifizierung für interkulturelle Kommunikation: Trainingskonzeption und -evaluation.* ludicium.

Deutsches Studentenwerk. (2016). *Eine Frage der Perspektive: Critical Incidents aus Studentenwerken und Hochschulverwaltung*. https://www.studierendenwerke.de/fileadmin/user_upload/dsw-fallbeispiele-digital-druckboegen_0.pdf

Deutsches Studentenwerk. (2018). *A matter of perspective: Critical incidents from the point of view of Studentenwerke and higher education institutions*. https://www.studierendenwerke.de/fileadmin/api/files/20180315-dsw-matterofperspective-web-druckboegen.pdf

Hiller, G. G., & Zillmer-Tantan, U. (2022). *Eine Frage der Perspektive 2: Critical Incidents aus den Bereichen arbeitsmarktbezogene Beratung, Vermittlung und Integration*. Hochschule der Bundesagentur für Arbeit. https://www.hdba.de/fileadmin/media/pdf/Lehrende/HILLER__G._-_ZILLMER-TANTAN__U.__2021__Eine_Frage_der_Perspektive_2.pdf

MuMiS-Projekt. (2011). *Critical Incidents: Datenbank interkultureller Missverständnisse im Hochschulkontext* [Datenbank]. Universität Kassel. https://www.uni-kassel.de/mumis/www.mumis-projekt.de/mumis/index.php/critical-incidents.html

Zentrum für Schlüsselqualifikationen, Christian-Albrechts-Universität zu Kiel. (2020). *Critical Incidents: Fallbeispiele*. https://www.kulturelldivers.de/fallbeispiele

---

*Erstellt als Open Educational Resource für die Lehre. Beiträge, Korrekturen und Weiternutzung (nicht-kommerziell) sind ausdrücklich willkommen.*

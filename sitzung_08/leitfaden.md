# Leitfaden — Sitzung 8: Probeklausur & Schwaechen gezielt

**Dauer:** 90 Minuten

---

## Ueberblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Probeklausur schreiben | ~55 Min | Komplette Abituraufgabe unter Zeitdruck | `probeklausur.md` (ausgedruckt) |
| 2. Gemeinsame Besprechung | ~25 Min | Musterloesung, Selbstauswertung, Fehleranalyse | `probeklausur_auswertung.ipynb` |
| 3. Schwaechen nacharbeiten | ~10 Min | Gezielt die groessten Luecken schliessen | Notebook Abschnitt 3–5 |

---

## Vorbereitung (vor der Sitzung)

- `probeklausur.md` **ausdrucken** (oder auf Tablet bereitstellen)
- Stoppuhr / Timer bereitlegen
- Taschenrechner / CAS fuer Teil B bereitlegen (aber NICHT fuer Teil A!)
- Notebook vorab einmal starten, damit alles geladen ist:

```bash
source .venv/bin/activate
jupyter lab sitzung_08/probeklausur_auswertung.ipynb
```

---

## Phase 1: Probeklausur schreiben (~55 Min)

Die Klausur besteht aus zwei Teilen — genau wie im echten Abitur:

**Teil A — hilfsmittelfrei (30 Min, 20 BE)**
- A1: Ableitungen (Potenz-, Ketten-, Produktregel) — 4 BE, ca. 6 Min
- A2: Nullstellen und Extremum von f(x) = x^3 - 3x — 5 BE, ca. 8 Min
- A3: Graphen zuordnen (f zu f') — 5 BE, ca. 8 Min
- A4: Bestimmtes Integral berechnen — 3 BE, ca. 4 Min
- A5: Wahr/Falsch-Aussagen begruenden — 3 BE, ca. 4 Min

**Uebergang (kurze Pause, ~2 Min):** Taschenrechner/CAS ausgeben.

**Teil B — mit Hilfsmitteln (ca. 23 Min verbleibend, eigentlich 50 Min)**
- B1a: Grenzverhalten und Nullstellen von f(x) = (2x - x^2) * e^x — 4 BE
- B1b: Extrempunkte berechnen und Art bestimmen — 7 BE
- B1c: Tangente im Punkt P(-1|f(-1)) — 5 BE
- B1d: Flaechenberechnung auf [0, 2] — 6 BE
- B1e: Funktionenschar, gemeinsame Nullstelle, Ortskurve — 8 BE

### Hinweise zur Durchfuehrung

- **Timer sichtbar laufen lassen** — realistischer Pruefungsdruck ist das Ziel
- Bei Teil A: Kein Taschenrechner, kein CAS, kein Nachschlagen
- **Nicht helfen** waehrend die Schuelerin schreibt — Fehler spaeter analysieren
- Wenn sie bei einer Aufgabe haengt: kurz ermutigen ("Geh zur naechsten, komm spaeter zurueck"), aber keine inhaltlichen Tipps
- Nach 55 Minuten: Stift weglegen, auch wenn nicht alles fertig ist

> **Hinweis zum Zeitdruck:** Die echte Pruefung gibt 80 Minuten fuer 50 BE. Hier sind nur ~55 Min verfuegbar, damit Zeit fuer die Besprechung bleibt. Teil B wird daher vermutlich nicht vollstaendig — das ist okay und erwartbar. Wichtig ist die Erfahrung unter Zeitdruck.

---

## Phase 2: Gemeinsame Besprechung (~25 Min)

Notebook oeffnen (falls nicht schon offen):
```bash
source .venv/bin/activate
jupyter lab sitzung_08/probeklausur_auswertung.ipynb
```

### Schritt 1: Musterloesung durchgehen (Abschnitt 1)

Jede Aufgabe hat einen **Hinweis-Button** und einen aufklappbaren **Loesungsblock**.

Vorgehen pro Aufgabe:
1. Schuelerin zeigt ihre Loesung
2. Gemeinsam mit der Musterloesung vergleichen
3. Bei Fehlern: **Wo genau** ging es schief? (Rechenfehler, Verstaendnisproblem, Zeitproblem?)

**Besonders wichtige Stellen:**
- **A1c (Produktregel):** Haeufiger Fehler — Ableitung von e^x vergessen
- **A2b (Extremum nachweisen):** Muss die Schuelerin zwischen notwendiger und hinreichender Bedingung unterscheiden?
- **A3 (Graphen zuordnen):** Versteht sie den Zusammenhang f' hat Nullstellen, wo f Extrema hat?
- **A5 (Wahr/Falsch):** Kann sie Gegenbeispiele benennen? (z.B. f(x)=x^3 fuer a), Integral mit Vorzeichenwechsel fuer c))
- **B1b (Extrempunkte):** f'(x) = (2 - x^2)*e^x — erkennt sie, dass e^x > 0 und nur 2-x^2=0 relevant ist?
- **B1d (Flaechenberechnung):** Partielle Integration ist noetig — hat sie das Schema drauf?
- **B1e (Ortskurve):** Anspruchsvollste Aufgabe — nur wenn sie weit gekommen ist, besprechen

### Schritt 2: Selbstauswertung (Abschnitt 2)

Im Notebook gibt es **Checkboxen** fuer jede Teilaufgabe. Die Schuelerin hakt ab, was sie geschafft hat.

### Schritt 3: Schwaechen-Analyse (Abschnitt 3)

Auf den Button **"Auswerten"** klicken. Das Notebook zeigt:
- Erreichte BE pro Themengebiet (Ableitungsregeln, Kurvendiskussion, Integralrechnung, etc.)
- Prozentuale Auswertung
- Automatische Empfehlung, welche Themen nochmal geuebt werden sollten

---

## Phase 3: Schwaechen nacharbeiten (~10 Min)

Je nach Ergebnis der Auswertung gezielt vertiefen:

| Schwaeche | Was tun |
|-----------|---------|
| **Ableitungsregeln** | Formeluebersicht im Notebook (Abschnitt 4) durchgehen, 2-3 Aufgaben muendlich rechnen lassen |
| **Kurvendiskussion** | Gesamtplot in Zelle 19 anschauen — alle markanten Punkte von f(x)=(2x-x^2)*e^x auf einen Blick |
| **Tangente** | Schluesselformel wiederholen: t(x) = f'(x_0) * (x - x_0) + f(x_0) |
| **Integralrechnung** | Partielle Integration nochmal Schritt fuer Schritt am Beispiel B1d |
| **Funktionenschar** | Schar-Plot in Zelle 20 zeigen — Slider fuer a, gemeinsame Nullstelle x=0 sichtbar machen |
| **Graphen zuordnen** | Zurueck zu A3: Graph von f und f' uebereinanderlegen, Zusammenhang nochmal klar machen |

### Desmos-Links zum Weiterueben (Abschnitt 5 im Notebook)

Falls die Schuelerin zuhause weiterueben moechte:
- Kurvendiskussion live: [desmos.com/calculator](https://www.desmos.com/calculator)
- Funktionenschar mit Slider fuer Parameter

---

## Tests ausfuehren (zur eigenen Kontrolle)

Die Datei `test_probeklausur.py` enthaelt symbolische Tests (sympy), die alle Musterloesungen verifizieren:

```bash
source .venv/bin/activate
pytest sitzung_08/test_probeklausur.py -v
```

Geprueft werden u.a.: Ableitungen (A1), Nullstellen und Extrema (A2, B1a/b), Integral (A4), Tangente (B1c), Flaeche (B1d), Schar-Nullstelle (B1e).

---

## Tipps fuer die Durchfuehrung

- **Wenn die Schuelerin frueh fertig wird (<45 Min):** Gut! Dann mehr Zeit fuer die Besprechung — jeden Rechenschritt durchgehen
- **Wenn sie kaum ueber Teil A hinauskommt:** Teil B nur die Teilaufgaben a) und b) besprechen, Rest als Hausaufgabe
- **Wenn ein Thema komplett fehlt:** Nicht in 10 Min nachlernen wollen — stattdessen konkreten Uebungsplan fuer zuhause mitgeben (Desmos-Links, alte Aufgaben)
- **Motivierend bleiben:** Das ist die letzte Sitzung — Fokus auf das, was schon sitzt, und 1-2 gezielte Baustellen benennen
- **Notenschluessel** (Orientierung): 1 ab 43 BE, 2 ab 35, 3 ab 27, 4 ab 19 — hilft zur Einordnung

---

## Notenschluessel (aus der Klausur)

| Note | BE |
|------|---:|
| 1    | >= 43 |
| 2    | >= 35 |
| 3    | >= 27 |
| 4    | >= 19 |
| 5    | >= 10 |
| 6    | < 10 |

# Leitfaden — Sitzung 8: Probeklausur & Schwächen gezielt

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Probeklausur schreiben | ~55 Min | Komplette Abituraufgabe unter Zeitdruck | `probeklausur.md` (ausgedruckt) |
| 2. Gemeinsame Besprechung | ~25 Min | Musterlösung, Selbstauswertung, Fehleranalyse | `probeklausur_auswertung.ipynb` |
| 3. Schwächen nacharbeiten | ~10 Min | Gezielt die größten Lücken schließen | Notebook Abschnitt 3–5 |

---

## Vorbereitung (vor der Sitzung)

- `probeklausur.md` **ausdrucken** (oder auf Tablet bereitstellen)
- Stoppuhr / Timer bereitlegen
- Taschenrechner / CAS für Teil B bereitlegen (aber NICHT für Teil A!)
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
- A2: Nullstellen und Extremum von $f(x) = x^3 - 3x$ — 5 BE, ca. 8 Min
- A3: Graphen zuordnen ($f$ zu $f'$) — 5 BE, ca. 8 Min
- A4: Bestimmtes Integral berechnen — 3 BE, ca. 4 Min
- A5: Wahr/Falsch-Aussagen begründen — 3 BE, ca. 4 Min

**Übergang (kurze Pause, ~2 Min):** Taschenrechner/CAS ausgeben.

**Teil B — mit Hilfsmitteln (ca. 23 Min verbleibend, eigentlich 50 Min)**
- B1a: Grenzverhalten und Nullstellen von $f(x) = (2x - x^2) \cdot e^x$ — 4 BE
- B1b: Extrempunkte berechnen und Art bestimmen — 7 BE
- B1c: Tangente im Punkt $P(-1 \mid f(-1))$ — 5 BE
- B1d: Flächenberechnung auf $[0, 2]$ — 6 BE
- B1e: Funktionenschar, gemeinsame Nullstelle, Ortskurve — 8 BE

### Hinweise zur Durchführung

- **Timer sichtbar laufen lassen** — realistischer Prüfungsdruck ist das Ziel
- Bei Teil A: Kein Taschenrechner, kein CAS, kein Nachschlagen
- **Nicht helfen** während die Schülerin schreibt — Fehler später analysieren
- Wenn sie bei einer Aufgabe hängt: kurz ermutigen ("Geh zur nächsten, komm später zurück"), aber keine inhaltlichen Tipps
- Nach 55 Minuten: Stift weglegen, auch wenn nicht alles fertig ist

> **Hinweis zum Zeitdruck:** Die echte Prüfung gibt 80 Minuten für 50 BE. Hier sind nur ~55 Min verfügbar, damit Zeit für die Besprechung bleibt. Teil B wird daher vermutlich nicht vollständig — das ist okay und erwartbar. Wichtig ist die Erfahrung unter Zeitdruck.

---

## Phase 2: Gemeinsame Besprechung (~25 Min)

Notebook öffnen (falls nicht schon offen):
```bash
source .venv/bin/activate
jupyter lab sitzung_08/probeklausur_auswertung.ipynb
```

### Schritt 1: Musterlösung durchgehen (Abschnitt 1)

Jede Aufgabe hat einen **Hinweis-Button** und einen aufklappbaren **Lösungsblock**.

Vorgehen pro Aufgabe:
1. Schülerin zeigt ihre Lösung
2. Gemeinsam mit der Musterlösung vergleichen
3. Bei Fehlern: **Wo genau** ging es schief? (Rechenfehler, Verständnisproblem, Zeitproblem?)

**Besonders wichtige Stellen:**
- **A1c (Produktregel):** Häufiger Fehler — Ableitung von $e^x$ vergessen
- **A2b (Extremum nachweisen):** Muss die Schülerin zwischen notwendiger und hinreichender Bedingung unterscheiden?
- **A3 (Graphen zuordnen):** Versteht sie den Zusammenhang $f'$ hat Nullstellen, wo $f$ Extrema hat?
- **A5 (Wahr/Falsch):** Kann sie Gegenbeispiele benennen? (z.B. $f(x) = x^3$ für a), Integral mit Vorzeichenwechsel für c))
- **B1b (Extrempunkte):** $f'(x) = (2 - x^2) \cdot e^x$ — erkennt sie, dass $e^x > 0$ und nur $2 - x^2 = 0$ relevant ist?
- **B1d (Flächenberechnung):** Partielle Integration ist nötig — hat sie das Schema drauf?
- **B1e (Ortskurve):** Anspruchsvollste Aufgabe — nur wenn sie weit gekommen ist, besprechen

### Schritt 2: Selbstauswertung (Abschnitt 2)

Im Notebook gibt es **Checkboxen** für jede Teilaufgabe. Die Schülerin hakt ab, was sie geschafft hat.

### Schritt 3: Schwächen-Analyse (Abschnitt 3)

Auf den Button **"Auswerten"** klicken. Das Notebook zeigt:
- Erreichte BE pro Themengebiet (Ableitungsregeln, Kurvendiskussion, Integralrechnung, etc.)
- Prozentuale Auswertung
- Automatische Empfehlung, welche Themen nochmal geübt werden sollten

---

## Phase 3: Schwächen nacharbeiten (~10 Min)

Je nach Ergebnis der Auswertung gezielt vertiefen:

| Schwäche | Was tun |
|-----------|---------|
| **Ableitungsregeln** | Formelübersicht im Notebook (Abschnitt 4) durchgehen, 2-3 Aufgaben mündlich rechnen lassen |
| **Kurvendiskussion** | Gesamtplot in Zelle 19 anschauen — alle markanten Punkte von $f(x) = (2x - x^2) \cdot e^x$ auf einen Blick |
| **Tangente** | Schlüsselformel wiederholen: $t(x) = f'(x_0) \cdot (x - x_0) + f(x_0)$ |
| **Integralrechnung** | Partielle Integration nochmal Schritt für Schritt am Beispiel B1d |
| **Funktionenschar** | Schar-Plot in Zelle 20 zeigen — Slider für $a$, gemeinsame Nullstelle $x = 0$ sichtbar machen |
| **Graphen zuordnen** | Zurück zu A3: Graph von $f$ und $f'$ übereinanderlegen, Zusammenhang nochmal klar machen |

### Desmos-Links zum Weiterüben (Abschnitt 5 im Notebook)

Falls die Schülerin zuhause weiterüben möchte:
- Kurvendiskussion live: [desmos.com/calculator](https://www.desmos.com/calculator)
- Funktionenschar mit Slider für Parameter

---

## Tests ausführen (zur eigenen Kontrolle)

Die Datei `test_probeklausur.py` enthält symbolische Tests (sympy), die alle Musterlösungen verifizieren:

```bash
source .venv/bin/activate
pytest sitzung_08/test_probeklausur.py -v
```

Geprüft werden u.a.: Ableitungen (A1), Nullstellen und Extrema (A2, B1a/b), Integral (A4), Tangente (B1c), Fläche (B1d), Schar-Nullstelle (B1e).

---

## Tipps für die Durchführung

- **Wenn die Schülerin früh fertig wird ($< 45$ Min):** Gut! Dann mehr Zeit für die Besprechung — jeden Rechenschritt durchgehen
- **Wenn sie kaum über Teil A hinauskommt:** Teil B nur die Teilaufgaben a) und b) besprechen, Rest als Hausaufgabe
- **Wenn ein Thema komplett fehlt:** Nicht in 10 Min nachlernen wollen — stattdessen konkreten Übungsplan für zuhause mitgeben (Desmos-Links, alte Aufgaben)
- **Motivierend bleiben:** Das ist die letzte Sitzung — Fokus auf das, was schon sitzt, und 1-2 gezielte Baustellen benennen
- **Notenschlüssel** (Orientierung): 1 ab 43 BE, 2 ab 35, 3 ab 27, 4 ab 19 — hilft zur Einordnung

---

## Notenschlüssel (aus der Klausur)

| Note | BE |
|------|---:|
| 1    | $\geq 43$ |
| 2    | $\geq 35$ |
| 3    | $\geq 27$ |
| 4    | $\geq 19$ |
| 5    | $\geq 10$ |
| 6    | $< 10$ |

# Leitfaden — Sitzung 7: Hilfsmittelfreier Teil ueben

**Dauer:** 90 Minuten

---

## Ueberblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Einfuehrung & Pruefungsmodus | ~5 Min | Zeitbudget klaeren, Strategie besprechen | -- |
| 2. Uebungsklausur (Simulation) | ~40 Min | 12 Aufgaben ohne Hilfsmittel | `diagnosetest.md`, `graphen_aufgabe4.png` |
| 3. Besprechung & Fehleranalyse | ~15 Min | Gemeinsam korrigieren, Schwaechen identifizieren | `musterloesung.md`, Auswertungsraster |
| 4. Manim-Animation | ~5 Min | Zusammenhang f, f', f'' visualisieren | `manim/zusammenhang_f_fp_fpp.py` |
| 5. Interaktives Training | ~20 Min | Gezielte Quiz-Aufgaben zu Schwachstellen | `teil_a_training.ipynb` |
| 6. Abschluss & Checkliste | ~5 Min | Persoenliche Fehlerliste, Vorbereitung Sitzung 8 | -- |

---

## Phase 1: Einfuehrung & Pruefungsmodus (~5 Min)

Zu Beginn die Pruefungssituation erklaeren:

- **Teil A im Abitur:** Hilfsmittelfrei, ca. 40 Minuten, Grundkompetenzen
- **Punkteverteilung:** Typisch 30-40 Punkte, alles per Hand rechnen
- **Strategie:** Leichte Aufgaben zuerst, nicht an einer Aufgabe haengenbleiben
- **Heute:** Echte Simulation mit 12 Aufgaben (39 Punkte), danach gezieltes Nacharbeiten

---

## Phase 2: Uebungsklausur — Simulation (~40 Min)

Die Schuelerin bearbeitet den Diagnosetest unter realistischen Bedingungen:

- **Keine Hilfsmittel:** Kein Taschenrechner, keine Formelsammlung
- **Timer stellen:** 40 Minuten (oder den Timer im Notebook nutzen, siehe Phase 5)
- **Lehrer haelt sich zurueck**, notiert aber beobachtete Schwierigkeiten

**Material:**
- `diagnosetest.md` ausdrucken oder am Bildschirm zeigen
- `graphen_aufgabe4.png` fuer Aufgabe 4 (Graphen zuordnen) bereithalten

**Aufgaben-Ueberblick (12 Aufgaben, 39 Punkte):**

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1a-f | Ableitungen (Potenz-, Ketten-, Produktregel, Trig.) | 6 |
| 2a-d | Stammfunktionen (Polynom, e-Fkt., ln, Trig.) | 4 |
| 3a-d | Bestimmte Integrale berechnen | 4 |
| 4 | Graphen zuordnen: f, f', f'' | 3 |
| 5a-d | Zusammenhang f und f' (Wahr/Falsch mit Begruendung) | 3 |
| 6 | Tangentengleichung aufstellen | 3 |
| 7a-b | Extremstellen bestimmen und klassifizieren | 4 |
| 8a-c | Notwendige/hinreichende Bedingung + Gegenbeispiel | 3 |
| 9a-b | Funktionswerte berechnen, Kruemmung interpretieren | 2 |
| 10a-c | Integral vs. Flaecheninhalt (negatives Integral) | 3 |
| 11a-b | Monotonie ueber f'(x) bestimmen | 2 |
| 12a-b | Symmetrie zeigen, Grenzverhalten bestimmen | 2 |

---

## Phase 3: Besprechung & Fehleranalyse (~15 Min)

Gemeinsam den Test durchgehen mit `musterloesung.md`:

1. **Schnell-Check:** Welche Aufgaben wurden richtig geloest?
2. **Fehler kategorisieren:**
   - Rechenfehler (Vorzeichen, Brueche) vs. Verstaendnisfehler (Regel nicht gekonnt)
   - Zeitprobleme (nicht geschafft) vs. inhaltliche Luecken
3. **Auswertungsraster ausfuellen** (am Ende von `diagnosetest.md`):
   - Fuer jeden Bereich: sicher / unsicher / nicht gekonnt
4. **Top-3-Schwaechen** identifizieren fuer Phase 5

**Typische Stolperstellen:**
- Aufgabe 1c/1e: Kettenregel vergessen (aeussere mal innere Ableitung)
- Aufgabe 4: Zusammenhang "Nullstellen von f' = Extrema von f" nicht erkannt
- Aufgabe 8c: Gegenbeispiel f(x) = (x-2)^3 fuer Sattelpunkt nicht parat
- Aufgabe 10c: Unterschied orientiertes Integral vs. Flaecheninhalt

---

## Phase 4: Manim-Animation — Zusammenhang f, f', f'' (~5 Min)

Falls Aufgabe 4 oder 5 Schwierigkeiten bereitet hat, die Animation zeigen:

```bash
source .venv/bin/activate
manim -pql sitzung_07/manim/zusammenhang_f_fp_fpp.py ZusammenhangFFpFpp
```

Die Animation zeigt am Beispiel f(x) = x^3 - 3x:
1. **f(x) zeichnen** (blau) — Hochpunkt bei x = -1, Tiefpunkt bei x = 1
2. **f'(x) zeichnen** (rot) — Nullstellen genau bei den Extrema von f
3. **f''(x) zeichnen** (orange) — Nullstelle bei x = 0 = Wendepunkt von f
4. **Gestrichelte Verbindungslinien** zwischen den Graphen
5. **Vorzeichen-Bereiche:** f' > 0 (gruen) = f steigt, f' < 0 (rot) = f faellt
6. **Zusammenfassung:** Die beiden Schluesselregeln

**Kernbotschaft:** "Nullstelle von f' = Extremstelle von f" und "Nullstelle von f'' = Wendepunkt von f" — das muss im Schlaf sitzen.

---

## Phase 5: Interaktives Training im Notebook (~20 Min)

Notebook starten:
```bash
source .venv/bin/activate
jupyter lab sitzung_07/teil_a_training.ipynb
```

Das Notebook enthaelt **sieben interaktive Module** — gezielt die Schwachstellen aus Phase 3 trainieren:

| Abschnitt | Inhalt | Einsetzen bei Schwaeche in... |
|-----------|--------|-------------------------------|
| Pruefungs-Timer | 40-Min-Countdown | Optionale zweite Simulation |
| 1. Graphen-Zuordnung | f/f'/f'' zuordnen per Dropdown, zufaellige Funktionen | Aufgabe 4 |
| 2. Ableitungs-Quiz | Zufaellige Funktion, Ableitung eingeben, sympy prueft | Aufgabe 1 |
| 3. Stammfunktions-Quiz | Umgekehrt: Stammfunktion eingeben | Aufgabe 2 |
| 4. Bestimmte Integrale | Kopfrechnen, Ergebnis eingeben | Aufgabe 3 |
| 5. Begruendungsaufgaben | Notw./hinr. Bedingung formulieren, Loesung aufdecken | Aufgabe 8 |
| 6. Tangentengleichung | Schritt fuer Schritt aufstellen | Aufgabe 6 |
| 7. Extrema bestimmen | f'=0, f'' pruefen, Funktionswert — jeder Schritt einzeln | Aufgabe 7 |

**Empfohlene Vorgehensweise:**
- Bei 2+ Schwaechen im Ableitungsbereich: Abschnitte 2 und 3 mehrfach durchlaufen (Shift+Enter fuer neue Aufgaben)
- Bei Verstaendnisproblemen f/f'/f'': Zuerst die Manim-Animation (Phase 4), dann Abschnitt 1
- Bei Schwaeche in Begruendungen: Abschnitt 5 — hier muss die Schuelerin zuerst selbst formulieren, bevor die Loesung erscheint

---

## Phase 6: Abschluss & Checkliste (~5 Min)

Gemeinsam eine persoenliche Checkliste erstellen:

**Formeln, die sitzen muessen:**
- Potenzregel: f(x) = x^n => f'(x) = n*x^(n-1)
- Kettenregel: [f(g(x))]' = f'(g(x)) * g'(x)
- Produktregel: (u*v)' = u'v + uv'
- Tangente: t(x) = f(x_0) + f'(x_0) * (x - x_0)
- Notwendig: f'(x_0) = 0, Hinreichend: f''(x_0) != 0
- Stammfunktion e^(ax) => (1/a)*e^(ax)

**Ausblick auf Sitzung 8:**
- Naechstes Mal: Komplette Abituraufgabe (Teil A + Teil B) unter Zeitdruck
- Bis dahin: Schwache Bereiche aus dem Auswertungsraster nochmals ueben
- Die Notebook-Quizze koennen auch eigenstaendig wiederholt werden

---

## Tipps fuer die Durchfuehrung

- **Wenn die Simulation gut laeuft (>30/39 Punkte):** Phase 3 kuerzer, mehr Zeit fuer schwierige Notebook-Aufgaben (Begruendungen, Graphen)
- **Wenn die Simulation schlecht laeuft (<20/39 Punkte):** Phase 2 evtl. nach 30 Min abbrechen, mehr Zeit fuer gemeinsames Durcharbeiten mit Musterloesung und Notebook
- **Zeitpuffer:** Phase 4 (Manim) kann entfallen, wenn der Zusammenhang f/f'/f'' bereits sitzt
- **Tests ausfuehren** (fachliche Validierung der Aufgabenlogik): `pytest sitzung_07/test_teil_a.py -v`

# Leitfaden — Sitzung 7: Hilfsmittelfreier Teil üben

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Einführung & Prüfungsmodus | ~5 Min | Zeitbudget klären, Strategie besprechen | -- |
| 2. Übungsklausur (Simulation) | ~40 Min | 12 Aufgaben ohne Hilfsmittel | `diagnosetest.md`, `graphen_aufgabe4.png` |
| 3. Besprechung & Fehleranalyse | ~15 Min | Gemeinsam korrigieren, Schwächen identifizieren | `musterloesung.md`, Auswertungsraster |
| 4. Manim-Animation | ~5 Min | Zusammenhang $f$, $f'$, $f''$ visualisieren | `manim/zusammenhang_f_fp_fpp.py` |
| 5. Interaktives Training | ~20 Min | Gezielte Quiz-Aufgaben zu Schwachstellen | `teil_a_training.ipynb` |
| 6. Abschluss & Checkliste | ~5 Min | Persönliche Fehlerliste, Vorbereitung Sitzung 8 | -- |

---

## Phase 1: Einführung & Prüfungsmodus (~5 Min)

Zu Beginn die Prüfungssituation erklären:

- **Teil A im Abitur:** Hilfsmittelfrei, ca. 40 Minuten, Grundkompetenzen
- **Punkteverteilung:** Typisch 30-40 Punkte, alles per Hand rechnen
- **Strategie:** Leichte Aufgaben zuerst, nicht an einer Aufgabe hängenbleiben
- **Heute:** Echte Simulation mit 12 Aufgaben (39 Punkte), danach gezieltes Nacharbeiten

---

## Phase 2: Übungsklausur — Simulation (~40 Min)

Die Schülerin bearbeitet den Diagnosetest unter realistischen Bedingungen:

- **Keine Hilfsmittel:** Kein Taschenrechner, keine Formelsammlung
- **Timer stellen:** 40 Minuten (oder den Timer im Notebook nutzen, siehe Phase 5)
- **Lehrer hält sich zurück**, notiert aber beobachtete Schwierigkeiten

**Material:**
- `diagnosetest.md` ausdrucken oder am Bildschirm zeigen
- `graphen_aufgabe4.png` für Aufgabe 4 (Graphen zuordnen) bereithalten

**Aufgaben-Überblick (12 Aufgaben, 39 Punkte):**

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1a-f | Ableitungen (Potenz-, Ketten-, Produktregel, Trig.) | 6 |
| 2a-d | Stammfunktionen (Polynom, e-Fkt., ln, Trig.) | 4 |
| 3a-d | Bestimmte Integrale berechnen | 4 |
| 4 | Graphen zuordnen: $f$, $f'$, $f''$ | 3 |
| 5a-d | Zusammenhang $f$ und $f'$ (Wahr/Falsch mit Begründung) | 3 |
| 6 | Tangentengleichung aufstellen | 3 |
| 7a-b | Extremstellen bestimmen und klassifizieren | 4 |
| 8a-c | Notwendige/hinreichende Bedingung + Gegenbeispiel | 3 |
| 9a-b | Funktionswerte berechnen, Krümmung interpretieren | 2 |
| 10a-c | Integral vs. Flächeninhalt (negatives Integral) | 3 |
| 11a-b | Monotonie über $f'(x)$ bestimmen | 2 |
| 12a-b | Symmetrie zeigen, Grenzverhalten bestimmen | 2 |

---

## Phase 3: Besprechung & Fehleranalyse (~15 Min)

Gemeinsam den Test durchgehen mit `musterloesung.md`:

1. **Schnell-Check:** Welche Aufgaben wurden richtig gelöst?
2. **Fehler kategorisieren:**
   - Rechenfehler (Vorzeichen, Brüche) vs. Verständnisfehler (Regel nicht gekonnt)
   - Zeitprobleme (nicht geschafft) vs. inhaltliche Lücken
3. **Auswertungsraster ausfüllen** (am Ende von `diagnosetest.md`):
   - Für jeden Bereich: sicher / unsicher / nicht gekonnt
4. **Top-3-Schwächen** identifizieren für Phase 5

**Typische Stolperstellen:**
- Aufgabe 1c/1e: Kettenregel vergessen (äußere mal innere Ableitung)
- Aufgabe 4: Zusammenhang "Nullstellen von $f'$ = Extrema von $f$" nicht erkannt
- Aufgabe 8c: Gegenbeispiel $f(x) = (x-2)^3$ für Sattelpunkt nicht parat
- Aufgabe 10c: Unterschied orientiertes Integral vs. Flächeninhalt

---

## Phase 4: Manim-Animation — Zusammenhang f, f', f'' (~5 Min)

Falls Aufgabe 4 oder 5 Schwierigkeiten bereitet hat, die Animation zeigen:

```bash
source .venv/bin/activate
manim -pql sitzung_07/manim/zusammenhang_f_fp_fpp.py ZusammenhangFFpFpp
```

Die Animation zeigt am Beispiel $f(x) = x^3 - 3x$:
1. **$f(x)$ zeichnen** (blau) — Hochpunkt bei $x = -1$, Tiefpunkt bei $x = 1$
2. **$f'(x)$ zeichnen** (rot) — Nullstellen genau bei den Extrema von $f$
3. **$f''(x)$ zeichnen** (orange) — Nullstelle bei $x = 0$ = Wendepunkt von $f$
4. **Gestrichelte Verbindungslinien** zwischen den Graphen
5. **Vorzeichen-Bereiche:** $f' > 0$ (grün) = $f$ steigt, $f' < 0$ (rot) = $f$ fällt
6. **Zusammenfassung:** Die beiden Schlüsselregeln

**Kernbotschaft:** "Nullstelle von $f'$ = Extremstelle von $f$" und "Nullstelle von $f''$ = Wendepunkt von $f$" — das muss im Schlaf sitzen.

---

## Phase 5: Interaktives Training im Notebook (~20 Min)

Notebook starten:
```bash
source .venv/bin/activate
jupyter lab sitzung_07/teil_a_training.ipynb
```

Das Notebook enthält **sieben interaktive Module** — gezielt die Schwachstellen aus Phase 3 trainieren:

| Abschnitt | Inhalt | Einsetzen bei Schwäche in... |
|-----------|--------|-------------------------------|
| Prüfungs-Timer | 40-Min-Countdown | Optionale zweite Simulation |
| 1. Graphen-Zuordnung | $f$/$f'$/$f''$ zuordnen per Dropdown, zufällige Funktionen | Aufgabe 4 |
| 2. Ableitungs-Quiz | Zufällige Funktion, Ableitung eingeben, sympy prüft | Aufgabe 1 |
| 3. Stammfunktions-Quiz | Umgekehrt: Stammfunktion eingeben | Aufgabe 2 |
| 4. Bestimmte Integrale | Kopfrechnen, Ergebnis eingeben | Aufgabe 3 |
| 5. Begründungsaufgaben | Notw./hinr. Bedingung formulieren, Lösung aufdecken | Aufgabe 8 |
| 6. Tangentengleichung | Schritt für Schritt aufstellen | Aufgabe 6 |
| 7. Extrema bestimmen | $f' = 0$, $f''$ prüfen, Funktionswert — jeder Schritt einzeln | Aufgabe 7 |

**Empfohlene Vorgehensweise:**
- Bei 2+ Schwächen im Ableitungsbereich: Abschnitte 2 und 3 mehrfach durchlaufen (Shift+Enter für neue Aufgaben)
- Bei Verständnisproblemen $f$/$f'$/$f''$: Zuerst die Manim-Animation (Phase 4), dann Abschnitt 1
- Bei Schwäche in Begründungen: Abschnitt 5 — hier muss die Schülerin zuerst selbst formulieren, bevor die Lösung erscheint

---

## Phase 6: Abschluss & Checkliste (~5 Min)

Gemeinsam eine persönliche Checkliste erstellen:

**Formeln, die sitzen müssen:**
- Potenzregel: $f(x) = x^n \implies f'(x) = n \cdot x^{n-1}$
- Kettenregel: $[f(g(x))]' = f'(g(x)) \cdot g'(x)$
- Produktregel: $(u \cdot v)' = u'v + uv'$
- Tangente: $t(x) = f(x_0) + f'(x_0) \cdot (x - x_0)$
- Notwendig: $f'(x_0) = 0$, Hinreichend: $f''(x_0) \neq 0$
- Stammfunktion: $e^{ax} \implies \dfrac{1}{a} \cdot e^{ax}$

**Ausblick auf Sitzung 8:**
- Nächstes Mal: Komplette Abituraufgabe (Teil A + Teil B) unter Zeitdruck
- Bis dahin: Schwache Bereiche aus dem Auswertungsraster nochmals üben
- Die Notebook-Quizze können auch eigenständig wiederholt werden

---

## Tipps für die Durchführung

- **Wenn die Simulation gut läuft ($> 30/39$ Punkte):** Phase 3 kürzer, mehr Zeit für schwierige Notebook-Aufgaben (Begründungen, Graphen)
- **Wenn die Simulation schlecht läuft ($< 20/39$ Punkte):** Phase 2 evtl. nach 30 Min abbrechen, mehr Zeit für gemeinsames Durcharbeiten mit Musterlösung und Notebook
- **Zeitpuffer:** Phase 4 (Manim) kann entfallen, wenn der Zusammenhang $f$/$f'$/$f''$ bereits sitzt
- **Tests ausführen** (fachliche Validierung der Aufgabenlogik): `pytest sitzung_07/test_teil_a.py -v`

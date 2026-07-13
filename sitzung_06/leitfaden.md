# Leitfaden — Sitzung 6: Flächen zwischen Kurven & Anwendungen

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Einstieg: Fläche zwischen Kurven | ~15 Min | Manim-Animationen + Erklärung | `manim/flaeche_zwischen_kurven.py` |
| 2. Notebook: Flächen interaktiv | ~20 Min | Funktionenpaare, Slider, Schnittpunkte | `flaechen_anwendungen.ipynb` Abschnitte 1–3 |
| 3. Notebook: Sachkontexte | ~20 Min | Füllproblem, Bevölkerung, Mittelwert | `flaechen_anwendungen.ipynb` Abschnitte 4–6 |
| 4. Diagnosetest | ~25 Min | Selbstständig rechnen | `diagnosetest.md` |
| 5. Besprechung & Fehleranalyse | ~10 Min | Typische Fehler, Merksätze | Auswertungsraster in `diagnosetest.md` |

---

## Phase 1: Einstieg mit Manim-Animationen (~15 Min)

Animationen rendern und zeigen:
```bash
source .venv/bin/activate
manim -pql sitzung_06/manim/flaeche_zwischen_kurven.py FlaecheZwischenKurven
manim -pql sitzung_06/manim/flaeche_zwischen_kurven.py VorzeichenwechselFlaeche
```

### Animation 1: `FlaecheZwischenKurven`
Zeigt $f(x) = x$ und $g(x) = x^2$ auf $[0, 1]$:
1. Graphen + Schnittpunkte ($x = 0$, $x = 1$) erscheinen
2. Riemann-Summe mit $n = 5$ Streifen wird eingeblendet
3. Streifen verfeinern sich: $n = 10 \to 30 \to 100$
4. Exakte Fläche mit Formel: $A = \tfrac{1}{6}$

**Gesprächspunkte:**
- "Was passiert, wenn wir die Streifen immer feiner machen?" → Grenzwert = Integral
- Formel: $A$ = Integral von (obere minus untere Funktion)

### Animation 2: `VorzeichenwechselFlaeche`
Zeigt $f(x) = x^3$ und $g(x) = x$ auf $[-1, 1]$:
1. Naives Integral ergibt $0$ → "Falsch! Die Flächen heben sich auf."
2. Korrekte Aufteilung in zwei Teilflächen: je $\tfrac{1}{4}$
3. Gesamtfläche: $A = \tfrac{1}{4} + \tfrac{1}{4} = \tfrac{1}{2}$

**Kernbotschaft:** "Betrag nicht vergessen! Immer an Schnittpunkten aufteilen."

---

## Phase 2: Notebook — Flächen interaktiv (~20 Min)

Notebook starten:
```bash
source .venv/bin/activate
jupyter lab sitzung_06/flaechen_anwendungen.ipynb
```

### Abschnitt 1 — Fläche zwischen zwei Kurven
- Dropdown mit vier Funktionenpaaren: $x$/$x^2$, $x^2-1$/$-x^2+3$, $x^3$/$x$, $\sin$/$\cos$
- Slider $a$ und $b$ für die Integrationsgrenzen
- Schnittpunkte werden automatisch markiert, Teilflächen annotiert ($A_1$, $A_2$)
- **Aufgabe:** Verschiedene Paare durchprobieren, Slider bewegen, Flächenwerte beobachten

### Abschnitt 2 — Schnittpunkte mit SymPy
- Symbolische Berechnung der Schnittpunkte (exakte Werte)
- **Zusammen besprechen:** Vorgehen bei Flächenaufgaben:
  1. Schnittpunkte bestimmen: $f(x) = g(x)$ lösen
  2. Skizze: Welche Funktion liegt oben?
  3. Integral aufteilen bei Vorzeichenwechsel von $f - g$
  4. Teilflächen addieren (Beträge!)

### Abschnitt 3 — Übungsaufgaben mit Lösungsaufdeckung
- Drei Aufgaben mit aufklappbaren Lösungen
- Die Schülerin rechnet erst selbst, dann Lösung vergleichen

---

## Phase 3: Notebook — Sachkontexte (~20 Min)

### Abschnitt 4 — Füllproblem (Bestandsrekonstruktion)
- Zuflussrate $z(t) = 6t - t^2$ (Liter/Min), Anfangsbestand 10 Liter
- Slider für den Zeitpunkt $t$: zeigt gleichzeitig die Fläche unter $z(t)$ und den Bestandsverlauf $W(t)$
- **Gesprächspunkte:**
  - Blaue Fläche links = zugeflossene Wassermenge
  - Bei $t = 3$ ist $z(t)$ maximal → Bestand steigt am steilsten ($W'(t) = z(t)$)
  - Bestandsfunktion: $W(t) = W_0 + \int_0^t z(s)\,ds$

### Abschnitt 5 — Momentan vs. Gesamtänderung (Bevölkerungswachstum)
- $r(t) = 500 \cdot e^{0{,}02t}$ Personen/Jahr
- Interaktiver Vergleich: momentane Rate $r(t_0)$ vs. Gesamtänderung (Integral)
- **Schlüsseltabelle besprechen:**

| | Momentane Änderungsrate | Gesamtänderung | Mittlere Änderungsrate |
|---|---|---|---|
| Was? | $f'(t_0)$ — ein Wert | $\int_a^b f'(t)\,dt = f(b) - f(a)$ | $\dfrac{f(b) - f(a)}{b - a}$ |
| Einheit | Personen **pro** Jahr | Personen | Personen **pro** Jahr |

### Abschnitt 6 — Mittelwert einer Funktion
- Verschiedene Funktionen: $x^2$, $\sin(x)$, $e^x$, Temperaturmodell
- Slider für Intervall $[a, b]$
- Rote Linie = Mittelwert, rotes Rechteck hat gleiche Fläche wie Kurve
- **Aufgabe:** Temperatur $T(t) = 15 + 8 \sin\!\left(\frac{\pi}{12}(t-6)\right)$ auf $[0, 24]$ → Durchschnittstemperatur ablesen
- Formel: $\bar{f} = \dfrac{1}{b-a} \cdot \int_a^b f(x)\,dx$

---

## Phase 4: Diagnosetest (~25 Min)

Die Schülerin bearbeitet das Aufgabenblatt `diagnosetest.md` selbstständig.

### Aufbau des Tests
- **Teil A (4 Aufgaben):** Fläche zwischen Kurven — Schnittpunkte, Berechnung, Vorzeichenwechsel, e-Funktion
- **Teil B (3 Aufgaben):** Sachkontexte — Wassertank (Zuflussrate → Bestand), Bevölkerungswachstum (momentan vs. gesamt), Auto (Geschwindigkeit → Weg)
- **Teil C (2 Aufgaben):** Mittelwert — $x^2$ auf $[0, 3]$, Durchschnittstemperatur

### Priorisierung bei Zeitmangel
Falls die Zeit knapp wird:
- **Pflicht:** A1, A3 (Vorzeichenwechsel!), B1, C1
- **Kann entfallen:** A2, B3, C2

---

## Phase 5: Besprechung & Fehleranalyse (~10 Min)

Auswertungsraster in `diagnosetest.md` ausfüllen und typische Fehler besprechen.

### Häufige Fehler

1. **Betrag vergessen:** $\int_{-1}^{1} (x^3 - x)\,dx = 0$, aber Fläche $= \tfrac{1}{2}$
   → Immer an Schnittpunkten aufteilen, Teilflächen im Betrag nehmen
2. **Einheiten im Sachkontext verwechseln:** Rate (Liter/Min) vs. Bestand (Liter)
   → "Integral einer Rate = Gesamtmenge"
3. **Mittlere Änderungsrate vs. Mittelwert:** Sind verschiedene Konzepte!
   → Mittlere Änderungsrate = Sekantensteigung, Mittelwert $= \dfrac{1}{b-a} \cdot \int_a^b f(x)\,dx$

### Merksätze zum Mitnehmen

- **Fläche zwischen Kurven:** Schnittpunkte bestimmen → aufteilen → Beträge der Teilintegrale addieren
- **Integral einer Rate** = Gesamtänderung (HDI!)
- **Mittelwert** = "gleich verteilte Fläche" → $\bar{f} = \dfrac{1}{b-a} \cdot \int_a^b f(x)\,dx$

---

## Tipps für die Durchführung

- **Wenn Phase 1 (Manim) begeistert:** Kurz halten, Begeisterung in die Notebook-Phase mitnehmen
- **Wenn Schnittpunkte Probleme machen:** Mehr Zeit in Phase 2, SymPy-Abschnitt nutzen zum Kontrollieren
- **Wenn Sachkontexte schwach:** Phase 3 ausbauen, Diagnosetest auf Teil A + C beschränken
- **Vorwissen aus Sitzung 5:** Stammfunktionen und bestimmtes Integral sollten sitzen — falls nicht, zu Beginn kurz wiederholen

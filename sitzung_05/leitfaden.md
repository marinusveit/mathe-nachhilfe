# Leitfaden — Sitzung 5: Stammfunktionen & bestimmtes Integral

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Diagnosetest | ~25 Min | 10 Aufgaben (A–D) | `diagnosetest.md` |
| 2. Riemann-Summen | ~10 Min | Intuition: Fläche = Grenzwert von Rechtecken | Notebook Abschnitt 1 |
| 3. Hauptsatz (HDI) | ~15 Min | Animation + Notebook: f(x) und F(x) synchron | Manim `HauptsatzAnimation` + Notebook Abschnitt 2 |
| 4. Stammfunktionen & Integralregeln | ~15 Min | Rechner + Regelkatalog interaktiv | Notebook Abschnitte 3 + 6 |
| 5. Bestimmtes Integral berechnen | ~10 Min | Schritt-für-Schritt mit farbiger Fläche | Notebook Abschnitt 4 |
| 6. Fläche bei Vorzeichenwechsel | ~15 Min | Integral vs. Flächeninhalt — das Kernproblem | Notebook Abschnitt 5 |

---

## Phase 1: Diagnosetest (~25 Min)

Der Test in `diagnosetest.md` deckt alle Themen der Sitzung ab:

- **Teil A (A1–A4):** Grundintegrale — Potenz, e-Funktion, 1/x, Verständnisfragen
- **Teil B (B1–B2):** Hauptsatz anwenden und erklären
- **Teil C (C1–C2):** Bestimmte Integrale berechnen
- **Teil D (D1–D2):** Flächenberechnung mit Vorzeichenwechsel

Nutze das **Auswertungsraster** am Ende, um Schwächen zu identifizieren. Das Raster hat Kategorien pro Themenblock — danach gezielt die schwachen Bereiche im Notebook vertiefen.

**Wichtig:** Bei A4 (Verständnisfragen) genau hinhören — hier zeigt sich, ob die Schuelerin den Unterschied zwischen Stammfunktion und bestimmtem Integral verstanden hat.

---

## Phase 2: Riemann-Summen — Intuition aufbauen (~10 Min)

Notebook starten:
```bash
source .venv/bin/activate
jupyter lab sitzung_05/integrale_interaktiv.ipynb
```

- **Abschnitt 1** — Slider fuer n (Anzahl Rechtecke) bei f(x) = x²
  - Erst Denkfrage stellen: "Mit nur 2 Rechtecken — wird die Summe zu gross oder zu klein?"
  - Slider von n = 1 langsam hochziehen, Fehler beobachten
  - Kernbeobachtung: Je mehr Rechtecke, desto naeher an 8/3 ≈ 2.667
  - **Ziel:** Integral = Grenzwert der Rechtecksummen (nicht auswendig lernen, sondern sehen)

---

## Phase 3: Hauptsatz — das Herzstück (~15 Min)

### 3a) Manim-Animation zeigen

```bash
source .venv/bin/activate
manim -pql sitzung_05/manim/hauptsatz.py HauptsatzAnimation
```

Die Animation zeigt:
1. Links: f(x) = x², Flaeche fuellt sich von a = 0 bis b = 2 (blaue Flaeche waechst)
2. Rechts: F(x) = x³/3, roter Punkt wandert synchron nach oben
3. Am Ende: Formel ∫₀² x² dx = F(2) − F(0) = 8/3

**Kernbotschaft:** Die wachsende Flaeche links entspricht exakt dem Hoehenunterschied F(b) − F(a) rechts.

### 3b) Im Notebook selbst explorieren

- **Abschnitt 2** — Slider fuer a und b, Dropdown fuer verschiedene Funktionen (x², sin(x), 2x+1, eˣ)
  - Aufgabe: "Verschiebe b nach rechts — was passiert mit F(b) − F(a)?"
  - sin(x) ausprobieren: Wenn b von 0 bis π wandert, waechst die Flaeche; von π bis 2π schrumpft sie wieder
  - Denkfrage: "Warum wird die Flaeche bei sin(x) ab π wieder kleiner?"

---

## Phase 4: Stammfunktionen & Integralregeln (~15 Min)

- **Abschnitt 3** — Stammfunktionen-Rechner: Eigene Funktionen eingeben, sofort F(x) sehen + Plot
  - Nacheinander durchgehen: `x^3`, `e^(2*x)`, `1/x`, `sin(x)`
  - Bei jeder: "Was ist deine Vermutung fuer F(x)?" → Dann pruefen
  - Probe wird automatisch angezeigt (F'(x) = f(x))

- **Abschnitt 6** — Integralregeln-Explorer: Dropdown nach Kategorie (Potenz, e-Funktion, 1/x, Trig)
  - Schneller Ueberblick ueber die wichtigsten Regeln mit Beispielen
  - Zusammenfassungstabelle am Ende des Notebooks als Spickzettel

**Regeln die sitzen muessen:**

| f(x) | F(x) |
|------|------|
| xⁿ (n ≠ −1) | xⁿ⁺¹ / (n+1) + C |
| e^(ax) | e^(ax) / a + C |
| 1/x | ln\|x\| + C |

---

## Phase 5: Bestimmtes Integral berechnen (~10 Min)

- **Abschnitt 4** — Funktion, a und b eingeben → farbige Flaeche + Schritt-fuer-Schritt-Rechnung
  - Zuerst die Aufgaben aus dem Diagnosetest gemeinsam kontrollieren (C1, C2)
  - Eingabe z.B. `x^2` mit a = 0, b = 2 → Schritte nachvollziehen: F(x) bestimmen, F(b) − F(a)
  - Dann: `e^(2*x)` mit a = 0, b = 1 → e-Funktion ueben
  - Dann: `1/x` mit a = 1, b = e → Ergebnis = 1 (elegant!)

---

## Phase 6: Fläche bei Vorzeichenwechsel — das Kernproblem (~15 Min)

- **Abschnitt 5** — Nebeneinander: Integral (links, mit Vorzeichen) vs. Flaecheninhalt (rechts, Betraege)
  - Einstieg: `x^2 - 4` mit a = −2.5, b = 2.5
    - Integral = −32/3 (negativ!), Flaecheninhalt = 32/3
    - "Warum gibt das Integral ein negatives Ergebnis?"
  - Dann: `x^3 - 4*x` mit a = −2, b = 2
    - Integral = 0 (ungerade Funktion!), Flaecheninhalt = 8
    - "Das Integral sagt 0 — aber es gibt offensichtlich eine Flaeche. Was ist passiert?"
  - Abschnitt zeigt automatisch Nullstellen und die Teilflaechen mit Betraegen

**Vorgehen im Abitur (als Merksatz festhalten):**
1. Nullstellen bestimmen
2. Intervall an Nullstellen aufteilen
3. Teilintegrale berechnen
4. Betraege addieren

---

## Tipps für die Durchführung

- **Wenn Diagnose gut laeuft:** Phase 2 (Riemann) kuerzer, mehr Zeit fuer Phase 6 (Vorzeichenwechsel) — das ist die haeufigste Fehlerquelle im Abitur
- **Wenn Stammfunktionen schwach:** Phase 4 ausbauen, eigene Funktionen rechnen lassen und mit dem Rechner pruefen
- **Wenn Hauptsatz unklar:** Animation nochmal zeigen, dann im Notebook mit verschiedenen Funktionen durchspielen
- **Schluesselformeln** die sitzen muessen:
  - HDI: ∫ₐᵇ f(x) dx = F(b) − F(a)
  - Flaecheninhalt ≠ Integral, wenn Vorzeichenwechsel vorliegt
- **Desmos-Link** als Hausaufgaben-Tool: [desmos.com/calculator](https://www.desmos.com/calculator) — dort koennen Integrale direkt eingegeben und visualisiert werden

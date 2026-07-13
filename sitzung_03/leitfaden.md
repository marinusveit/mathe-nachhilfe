# Leitfaden — Sitzung 3: Tangente, Normale & Funktionsscharen

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Diagnosetest | ~30 Min | 10 Aufgaben (A–D) | `diagnosetest.md` |
| 2. Tangente & Normale | ~20 Min | Interaktiv am Notebook | Notebook Abschnitte 1–2b |
| 3. Funktionsscharen | ~15 Min | Parametervariation | Notebook Abschnitt 3 |
| 4. Ortskurven | ~15 Min | Animation + Notebook | Manim `OrtskurveAnimation` + Notebook 4a/4b |
| 5. Freies Rechnen | ~10 Min | Eigene Funktionen eingeben | Notebook "Probiere selbst" |

---

## Phase 1: Diagnosetest (~30 Min)

Der Test in `diagnosetest.md` deckt alle Themen ab:

- **Teil A (A1–A4):** Tangente aufstellen — von Standard bis externer Punkt
- **Teil B (B1–B2):** Berührpunkte, gemeinsame Tangenten, waagrechte Tangenten
- **Teil C (C1):** Normale + Dreiecksfläche
- **Teil D (D1–D3):** Funktionsscharen mit Parametern, Ortskurven

Nutze das **Auswertungsraster** am Ende, um Schwächen zu identifizieren. Danach gezielt die schwachen Bereiche im Notebook vertiefen.

---

## Phase 2: Tangente & Normale interaktiv (~20 Min)

Notebook starten:
```bash
source .venv/bin/activate
jupyter lab sitzung_03/tangenten_funktionsscharen.ipynb
```

- **Abschnitt 1** — Slider für $x_0$ bei $f(x) = x^3 - 3x$: zeigt Tangente + Normale live
  - Kernbeobachtung: Bei $x_0 = \pm 1$ ist die Tangente waagrecht → Extremstellen!
- **Abschnitt 2a** — Gemeinsame Tangente von $f(x) = x^2$ und $g(x) = -x^2 + 4x - 2$
  - Aufgabe: Berührpunkt bei $x_0 = 1$ finden lassen
- **Abschnitt 2b** — Tangente durch externen Punkt $P(3 \mid 4)$ an $f(x) = x^2 + 1$
  - Variation: $P$ verschieben → 0, 1 oder 2 Tangenten möglich

---

## Phase 3: Funktionsscharen (~15 Min)

- Dropdown mit verschiedenen Scharen + t-Slider
  - $f_t(x) = x^3 - 3t^2x$: Extrempunkte wandern mit $t$
  - $f_a(x) = a \cdot \sin(x)$: Amplitude ändert sich

---

## Phase 4: Ortskurven — das Highlight (~15 Min)

**Zuerst die Manim-Animation zeigen:**
```bash
source .venv/bin/activate
manim -pql sitzung_03/manim/ortskurve.py OrtskurveAnimation
```

Die Animation zeigt:
1. Die Schar $f_t(x) = x^3 - 3t^2x$ durchläuft $t = 0{,}5 \to 2{,}5$
2. Hoch- und Tiefpunkte werden als Punkte getrackt
3. Die **Ortskurve $y = -2x^3$** erscheint als Verbindungslinie

Dann im **Notebook** selbst explorieren:
- Ortskurve der Polynomfamilie ($y = -2x^3$)
- Ortskurve der e-Funktion-Schar $f_a(x) = x \cdot e^{-ax}$ → überraschend: $y = \frac{x}{e}$ (eine Gerade!)

---

## Phase 5: Freies Rechnen (~10 Min)

Die Schülerin kann eigene Funktionen eingeben und Tangenten berechnen lassen — gut zur Kontrolle eigener Rechnungen.

---

## Tipps für die Durchführung

- **Wenn Diagnose gut läuft:** Schneller durch Phase 2, mehr Zeit für Ortskurven
- **Wenn Tangente/Normale schwach:** Phase 2 ausbauen, Ortskurven nur als Demo
- **Schlüsselformel** die sitzen muss: $t(x) = f'(x_0) \cdot (x - x_0) + f(x_0)$

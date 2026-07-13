# Leitfaden — Sitzung 4: Extremwertprobleme, Steckbriefaufgaben & Rotationsvolumen

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Diagnosetest | ~20 Min | 8 Aufgaben (A1–A4, B1–B2, C1–C2) | `diagnosetest.md`, `loesungen.md` |
| 2. Extremwertprobleme interaktiv | ~25 Min | Dose, Zaun, Blech — Slider + symbolisch | Notebook Abschnitte 1–3, Aufgaben A1/A3 |
| 3. Manim: Dose-Animation | ~5 Min | Zylinder-Optimierung visuell | Manim `DoseOptimierung` |
| 4. Steckbriefaufgaben (Kurzversion) | ~10 Min | Methode + 1 Beispiel B1 | Notebook Abschnitt B1 |
| 4b. Rotationsvolumen | ~15 Min | Rezept besprechen, C1/C2 rechnen | `rezepte/14_rotationsvolumen.md`, Diagnosetest Teil C |
| 5. Methodenüberblick & freies Üben | ~15 Min | Fahrplan + eigene Aufgaben | Notebook Abschnitte 5 + "Eigene Steckbriefaufgabe" |

---

## Vorbereitung

```bash
source .venv/bin/activate
```

Manim-Animation vorab rendern (dauert ca. 30 Sekunden):
```bash
manim -pql sitzung_04/manim/dose_optimierung.py DoseOptimierung
```

Notebook starten:
```bash
jupyter lab sitzung_04/extremwert_steckbrief.ipynb
```

---

## Phase 1: Diagnosetest (~20 Min)

Der Test in `diagnosetest.md` deckt beide Themenblöcke ab:

- **Teil A (A1–A4):** Extremwertprobleme — Draht-Rechteck, Dose, Zaun, Blech-Quader
  - A1/A3: Nebenbedingung aufstellen, Zielfunktion ableiten
  - A2: Volumen-Nebenbedingung eliminieren (anspruchsvoller)
  - A4: Definitionsbereich beachten, kubische Ableitung
- **Teil B (B1–B2):** Steckbriefaufgaben — LGS aus Funktionsbedingungen
  - B1: Kubisch, 4 Bedingungen
  - B2: Quadratisch mit Extremum-Bedingung

Nutze das **Auswertungsraster** am Ende des Diagnosetests, um Schwächen zu identifizieren. Danach gezielt die schwachen Bereiche vertiefen.

Lösungen stehen in `loesungen.md`.

---

## Phase 2: Extremwertprobleme interaktiv (~25 Min)

Im Notebook gibt es drei Slider-Explorationen:

### 2a) Dose optimieren (Notebook Cell 3)
- Slider für Radius r: Schülerin sieht, wie sich Zylinder-Form und Oberfläche ändern
- **Kernbeobachtung:** Bei kleinem r ist die Dose hoch (viel Mantel), bei großem r sind die Deckel riesig
- **Ergebnis:** Optimum bei h = 2r (Höhe = Durchmesser)

### 2b) Zaun an der Mauer (Notebook Cell 5)
- Slider für Seitenlänge x: Fläche als Parabel
- **Beobachtung:** Bei x = 0 und x = 20 wird die Fläche 0, Maximum bei x = 10

### 2c) Blech-Quader (Notebook Cell 7)
- Slider für Ausschnittgröße x: Volumen als kubische Funktion
- **Beobachtung:** Optimum bei x = 10/3, nicht in der Mitte

### 2d) Aufgaben selbst lösen (Notebook Cells 9–12)
Die Schülerin trägt Zielfunktion und Nebenbedingung als Strings ein (`'...'` ersetzen). Das Notebook löst dann symbolisch und zeigt den Rechenweg.

- **A1:** `ziel_str='x*y'`, `neben_str='2*x + 2*y = 60'`, `variable_str='y'`
- **A3:** `ziel_str='x*y'`, `neben_str='2*x + y = 40'`, `variable_str='y'`

Falls die Schülerin nicht weiterkommt: Lösungstabelle in Notebook Cell 14.

---

## Phase 3: Manim-Animation — Dose (~5 Min)

```bash
manim -pql sitzung_04/manim/dose_optimierung.py DoseOptimierung
```

Die Animation zeigt:
1. Links: Zylinder-Seitenansicht mit Radius- und Höhe-Beschriftung (dynamisch)
2. Rechts: Graph von O(r) = 2*pi*r^2 + 1000/r mit rotem Punkt
3. r fährt von 2 bis zum Optimum (~4.3 cm) — grüner Stern markiert Minimum
4. r fährt weiter bis 8 (Oberfläche steigt wieder)
5. Zurück zum Optimum — Erkenntnis: **h = 2r**

Guter Moment, um die Formel nochmal an der Tafel zusammenzufassen:
- Nebenbedingung: $V = \pi r^2 h = 500$, also $h = \dfrac{500}{\pi r^2}$
- Einsetzen in Oberfläche
- Ableiten, Nullsetzen, optimaler Radius

---

## Phase 4: Steckbriefaufgaben — Kurzversion (~10 Min)

### 4a) Methode erklären (2–3 Min, mündlich)
Kurzversion des Fahrplans:
1. **Ansatz:** Allgemeines Polynom n-ten Grades aufschreiben
2. **Bedingungen übersetzen:** $f(x_0) = y$, $f'(x_0) = y$, $f''(x_0) = y$ in Gleichungen
3. **LGS lösen:** Koeffizienten bestimmen

### 4b) Beispiel B1 durchrechnen (Notebook Cell 17)
- $f(x) = ax^3 + bx^2 + cx + d$
- 4 Bedingungen ergeben 4 Gleichungen
- Ergebnis: $f(x) = \tfrac{1}{2}x^3 - \tfrac{3}{2}x^2 + 2$
- Das Notebook zeigt den vollständigen Rechenweg mit LGS
- B2 nur besprechen, wenn Zeit bleibt

> **Hinweis:** Steckbriefaufgaben kommen im aktuellen Abitur selten vor. Ein Beispiel reicht zum Verständnis der Methode.

---

## Phase 4b: Rotationsvolumen (~15 Min)

**Warum:** Rotationsvolumen war im ISB-Musterabitur 2026 (Aufgabe A6) — neu im G9-Stoff!

### Rezept besprechen (~5 Min)
Das Rezept `rezepte/14_rotationsvolumen.md` gemeinsam durchgehen:
- **Formel um $x$-Achse:** $V = \pi \cdot \int_a^b [f(x)]^2 \, dx$
- **Formel um $y$-Achse:** Umkehrfunktion nötig → $V = \pi \cdot \int [f^{-1}(y)]^2 \, dy$
- **Kernbotschaft:** „Quadrieren, integrieren, $\pi$ dran — fertig."

### Aufgaben C1 und C2 rechnen (~10 Min)
Die Schülerin rechnet C1 (x-Achse) und C2 (y-Achse) aus dem Diagnosetest.

**C1:** $f(x) = \sqrt{x}$ auf $[0;\,4]$ um $x$-Achse → $V = 8\pi$
- Schlüsselschritt: $(\sqrt{x})^2 = x$ — das Quadrieren vereinfacht!

**C2:** $f(x) = x^2$ auf $[0;\,2]$ um $y$-Achse → Umkehrfunktion $f^{-1}(y) = \sqrt{y}$, $y$-Grenzen $[0;\,4]$
- Schlüsselschritt: Grenzen umrechnen ($x$-Werte → $y$-Werte)

**Häufige Fehler ansprechen:**
- $\pi$ vergessen
- $[f(x)]^2$ vergessen (nur $f(x)$ integriert)
- Bei $y$-Achse: $x$-Grenzen statt $y$-Grenzen verwendet

---

## Phase 5: Methodenüberblick & freies Üben (~15 Min)

### 5a) Fahrplan-Visualisierung (Notebook Cell 23)
Das Notebook zeigt ein Flussdiagramm für den Lösungsweg bei Extremwertproblemen — gut als Zusammenfassung.

### 5b) Zusammenfassung Steckbriefaufgaben (Notebook Cell 24)
Tabelle mit den Schritten: Ansatz, Bedingungen einsetzen, LGS lösen, Kontrolle.

### 5c) Eigene Aufgabe eingeben (Notebook Cell 21)
Die Schülerin kann eigene Steckbriefaufgaben eingeben — gut zur Kontrolle eigener Rechnungen oder für weitere Übung.

---

## Tipps für die Durchführung

- **Wenn der Diagnosetest gut läuft:** Phase 2 straffen (nur Dose + eine Aufgabe), mehr Zeit für Rotationsvolumen
- **Wenn Nebenbedingungen/Zielfunktion schwach:** Phase 2 ausbauen, Steckbrief nur als Demo
- **Wenn Rotationsvolumen Probleme macht:** Mehr einfache Beispiele rechnen (z.B. f(x) = 2 auf [0; 3] → Zylinder)
- **Schlüsselkonzept Extremwertprobleme:** Nebenbedingung eliminieren, dann wie Kurvendiskussion weiter
- **Schlüsselkonzept Steckbriefaufgaben:** Anzahl Bedingungen = Anzahl Unbekannte = Grad + 1
- **Schlüsselkonzept Rotationsvolumen:** Quadrieren → Integrieren → π multiplizieren

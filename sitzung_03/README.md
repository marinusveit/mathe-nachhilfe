# Sitzung 3: Tangente, Normale & Funktionsscharen

## Ziel
Tangenten und Normalen sicher aufstellen, Berührbedingungen verstehen und Funktionsscharen mit Parameter systematisch untersuchen.

## Ablauf (90 Min)

| Zeit | Was | Material |
|------|-----|----------|
| 0–30 Min | Diagnosetest | `diagnosetest.md` |
| 30–50 Min | Notebook: Tangente & Normale, externer Punkt | Notebook Abschnitte 1–2b |
| 50–65 Min | Funktionsscharen mit Parameter | Notebook Abschnitt 3 |
| 65–80 Min | Ortskurven: Animation + Notebook | `manim/ortskurve.py` + Notebook 4a/4b |
| 80–90 Min | Freies Rechnen / Fehleranalyse | Notebook „Probiere selbst" |

Details siehe `leitfaden.md`.

## Dateien

| Datei | Beschreibung |
|-------|-------------|
| `leitfaden.md` | Detaillierter Sitzungsablauf |
| `diagnosetest.md` | Aufgaben zu Tangente, Normale, Funktionsscharen und Ortskurven |
| `tangenten_funktionsscharen.ipynb` | Interaktive Visualisierungen und symbolische Rechnungen |
| `manim/ortskurve.py` | Animation zur Ortskurve (`OrtskurveAnimation`) |
| `test_tangenten.py` | Fachliche Tests zu Tangenten, Normalen und Scharen |

## Ausführen

```bash
source ../.venv/bin/activate

# Notebook starten
jupyter lab tangenten_funktionsscharen.ipynb

# Animation rendern (Vorschau)
cd manim && manim -pql ortskurve.py OrtskurveAnimation

# Animation rendern (1080p)
cd manim && manim -pqh ortskurve.py OrtskurveAnimation
```

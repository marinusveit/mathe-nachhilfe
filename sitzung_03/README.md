# Sitzung 3: Tangente, Normale & Funktionsscharen

## Ziel
Tangenten und Normalen sicher aufstellen, Berührbedingungen verstehen und Funktionsscharen mit Parameter systematisch untersuchen.

## Ablauf (90 Min)

| Zeit | Was | Material |
|------|-----|----------|
| 0–15 Min | Kurze Wiederholung: Tangentengleichung aus Sitzung 2 | Tafel + Heft |
| 15–50 Min | Notebook: Tangente, Normale, externer Punkt, Ortskurven | `tangenten_funktionsscharen.ipynb` |
| 50–75 Min | Diagnosetest / Übungsblatt in Auswahl bearbeiten | `diagnosetest.md` |
| 75–90 Min | Fehleranalyse und Merksätze sichern | — |

## Dateien

| Datei | Beschreibung |
|-------|-------------|
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

# Sitzung 1: Diagnose + Ableitungen

## Ziel
Wissensstand der Schülerin einschätzen und Ableitungsbegriff visuell aufbauen.

## Ablauf (90 Min)

| Zeit | Was | Material |
|------|-----|----------|
| 0–20 Min | Diagnosetest (ohne Hilfe) | `diagnosetest.md` |
| 20–35 Min | Manim-Video: Sekante → Tangente | `manim/sekante_tangente.py` |
| 35–65 Min | Jupyter-Notebook gemeinsam durchgehen | `ableitungen_interaktiv.ipynb` |
| 65–90 Min | Schwächen aus Diagnosetest nacharbeiten | — |

## Dateien

| Datei | Beschreibung |
|-------|-------------|
| `diagnosetest.md` | 11 Aufgaben + Auswertungsraster (ausdrucken) |
| `ableitungen_interaktiv.ipynb` | Interaktive Plots: Tangente, f/f'-Vergleich, Potenzregel, sympy |
| `manim/sekante_tangente.py` | Animation: Sekante wird zur Tangente mit Steigungsdreieck |

## Ausführen

```bash
source ../.venv/bin/activate

# Notebook starten
jupyter lab ableitungen_interaktiv.ipynb

# Animation rendern (Vorschau)
cd manim && manim -pql sekante_tangente.py SekanteTangente

# Animation rendern (1080p)
cd manim && manim -pqh sekante_tangente.py SekanteTangente
```

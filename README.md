# Mathe-Nachhilfe: Abitur Analysis (Bayern GK)

Materialien zur Abiturvorbereitung im Fach Mathematik, Schwerpunkt Analysis.

## Aufbau

| Ordner | Inhalt |
|--------|--------|
| `sitzung_01/` | Diagnose + Ableitungen |
| `sitzung_02/` | Kurvendiskussion komplett |
| `stundenplan.md` | Gesamtplan (8 Sitzungen, 4 Wochen) |

Weitere Sitzungen werden nach und nach ergänzt.

## Setup

```bash
# Virtuelle Umgebung aktivieren (immer zuerst!)
source .venv/bin/activate
```

### Jupyter-Notebooks starten
```bash
jupyter lab sitzung_XX/notebook.ipynb
```

### Manim-Animationen rendern
```bash
# Vorschau (480p, schnell)
manim -pql sitzung_XX/manim/scene.py ClassName

# Hohe Qualität (1080p60)
manim -pqh sitzung_XX/manim/scene.py ClassName
```

## Voraussetzungen

- Python 3.12+ mit venv (`.venv/`)
- System-Pakete: `libpango1.0-dev`, `libcairo2-dev`, `pkg-config`, `ffmpeg`
- Python-Pakete: `manim`, `matplotlib`, `plotly`, `jupyterlab`, `ipywidgets`, `sympy`

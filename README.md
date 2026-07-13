# Mathe-Nachhilfe: Abitur Bayern (eA, Schwerpunkt Analysis)

Materialien zur Abiturvorbereitung im Fach Mathematik (Bayern, erhöhtes
Anforderungsniveau, erstes G9-Abitur 2026). Schwerpunkt Analysis, ergänzt um
Stochastik-Grundlagen.

## Aufbau

| Ordner / Datei | Inhalt |
|--------|--------|
| `stundenplan.md` | Gesamtplan (8 Sitzungen à 90 Min, 4 Wochen) |
| `abitur_info.md` | Prüfungsformat, LehrplanPLUS-Inhalte, Themenhäufigkeit |
| `rezepte/` | Schritt-für-Schritt-Rezepte (00–18) zu allen Analysis-Aufgabentypen |
| `cheatsheets/` | Kompakte Übersichten: Analysis, Grundfunktionen, Stochastik |
| `aufgaben/` | Drill-Aufgabenblätter (nummeriert passend zum Rezept) |
| `sitzung_01/` … `sitzung_08/` | Material pro Sitzung: Leitfaden, Aufgaben, Notebooks, Manim, Tests |
| `pruefungen/` | Altprüfungen (ISB, IQB, IlluPA) + eigene Musterlösungen — siehe `pruefungen/README.md` |
| `utils/` | Gemeinsamer Python-Code für Manim-Szenen |

### Sitzungsthemen

| Sitzung | Thema |
|--------|--------|
| 1 | Diagnose + Ableitungen |
| 2 | Kurvendiskussion komplett |
| 3 | Tangente, Funktionsscharen & Graphentransformationen |
| 4 | Wurzel-/Umkehrfunktionen & Extremwertprobleme |
| 5 | Stammfunktionen & bestimmtes Integral |
| 6 | Flächen, Rotationsvolumen & Sachkontext |
| 7 | Hilfsmittelfreier Teil (Teil A) üben |
| 8 | Probeklausur & Auswertung |

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

### Tests ausführen
```bash
python -m pytest -q
```

## Voraussetzungen

- Python 3.12+ mit venv (`.venv/`)
- System-Pakete: `libpango1.0-dev`, `libcairo2-dev`, `pkg-config`, `ffmpeg`
- Python-Pakete: `manim`, `matplotlib`, `plotly`, `jupyterlab`, `ipywidgets`, `sympy`, `pytest`

## Privatsphäre

Im Repo liegen nur anonyme, wiederverwendbare Materialien. Alles
Schülerspezifische bleibt lokal in `privat/` (gitignored) — Details in
`CLAUDE.md`.

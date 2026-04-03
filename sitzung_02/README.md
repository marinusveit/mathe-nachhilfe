# Sitzung 2: Kurvendiskussion komplett

## Ziel
Alle Schritte einer Kurvendiskussion verstehen und den Zusammenhang f ↔ f' ↔ f'' verinnerlichen.

## Ablauf (90 Min)

| Zeit | Was | Material |
|------|-----|----------|
| 0–15 Min | Manim-Video: f, f', f'' Zusammenhang | `manim/kurvendiskussion.py` |
| 15–35 Min | Cheatsheet durchgehen, Schritte besprechen | `cheatsheet_kurvendiskussion.md` |
| 35–60 Min | Jupyter-Notebook: interaktiv erkunden | `kurvendiskussion_interaktiv.ipynb` |
| 60–90 Min | Gemeinsam eine Kurvendiskussion händisch durchrechnen | Papier + Stift |

## Dateien

| Datei | Beschreibung |
|-------|-------------|
| `cheatsheet_kurvendiskussion.md` | Alle Schritte mit Formeln (ausdrucken!) |
| `kurvendiskussion_interaktiv.ipynb` | f/f'/f''-Vergleich, automatische Kurvendiskussion, Zuordnungsquiz, Monotonie+Krümmung interaktiv |
| `manim/kurvendiskussion.py` | Animation: f, f', f'' in drei Graphen mit Verbindungslinien |

## Ausführen

```bash
source ../.venv/bin/activate

# Notebook starten
jupyter lab kurvendiskussion_interaktiv.ipynb

# Animation rendern (Vorschau)
cd manim && manim -pql kurvendiskussion.py KurvendiskussionAnimation

# Animation rendern (1080p)
cd manim && manim -pqh kurvendiskussion.py KurvendiskussionAnimation
```

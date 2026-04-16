# Mathe-Nachhilfe Abitur (Bayern eA, Analysis)

## Projektstruktur
```
stundenplan.md          # Gesamtplan (8 Sitzungen à 90 Min)
sitzung_XX/             # Material pro Sitzung
  diagnosetest.md       # Aufgabenblätter (Markdown)
  *.ipynb               # Interaktive Jupyter-Notebooks
  manim/                # Manim-Animationen (3b1b-Style)
    *.py                # Scene-Klassen
    media/              # Gerenderte Videos (gitignored)
```

## Konventionen
- **Manim:** 3b1b-Farbpalette, LaTeX-Labels (`MathTex`), `BackgroundRectangle` für Text über Graphen
- **Jupyter:** `plt.rcParams['mathtext.fontset'] = 'cm'`, LaTeX in Legenden (`r'$...$'`), `loc='upper left'`
- **Sprache:** Deutsch (Aufgaben, Labels, Erklärungen)

## Anonymität / Privatsphäre (WICHTIG)
Im Git-Repo **nur anonyme, allgemein wiederverwendbare** Dateien. Alles, was sich auf
eine konkrete Schülerin bezieht (Namen, Noten, ausgefüllte Diagnosen, Fortschritt,
Problem-Aufgaben, private Notizen), bleibt **lokal** und ist via `.gitignore` ausgeschlossen.

**Konvention für schülerspezifische Inhalte:**
- Ordner `privat/` → gitignored, hier kommt alles Persönliche rein
- Dateinamen-Muster: `*_ausgefuellt.md`, `notizen_*.md`, `*_privat.md` → gitignored
- Personen niemals namentlich nennen — „die Schülerin" genügt
- Vor `git add` prüfen: enthält die Datei etwas, das nur für **diese eine** Schülerin gilt?
  Wenn ja → nach `privat/` verschieben oder umbenennen mit `_privat.md`-Suffix.

## Befehle
```bash
source .venv/bin/activate
manim -pql sitzung_XX/manim/scene.py ClassName   # Preview (480p)
manim -pqh sitzung_XX/manim/scene.py ClassName   # HQ (1080p)
jupyter lab sitzung_XX/notebook.ipynb             # Notebook starten
```

## Manim-Referenz
- Doku: https://docs.manim.community/en/stable/
- Beispiele: https://docs.manim.community/en/stable/examples.html
- MathTex: https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html
- Axes: https://docs.manim.community/en/stable/reference/manim.mobject.graphing.coordinate_systems.Axes.html

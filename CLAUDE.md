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
- **Markdown-Formeln:** Alle mathematischen Ausdrücke in LaTeX setzen — `$...$` inline,
  `$$...$$` für abgesetzte Formeln. **Keine** Unicode-Ersatzzeichen (`ℝ`, `²`, `√`, `≠`, `∞`,
  `→`, `≫` usw.) in Formeln verwenden — stattdessen `\mathbb{R}`, `^2`, `\sqrt{}`, `\neq`,
  `\infty`, `\to`, `\gg`. In Tabellen Betragsstriche als `\lvert \dots \rvert` schreiben,
  damit sie nicht die Zellentrennung stören. Fließtext-Pfeile (↗, ↘, ←) und Häkchen sind
  okay, solange sie nicht in einer Formel stehen.

## Rezept-Querverweise
Rezepte bauen aufeinander auf. Damit die Schülerin beim Lesen schnell zurückspringen kann,
ohne den Ordner zu durchsuchen, gilt:

- **Format**: immer `[Rezept NN: Titel](NN_name.md)` — zeigt Nummer und Titel, ist in
  GitHub/VSCode-Preview/Obsidian klickbar und bleibt auch im Druck lesbar.
- **Sparsam einsetzen — nur wo es hilft**, nicht dekorativ. Faustregel: verlinken, wenn
  die Schülerin das Vorwissen ohne Zurückspringen nicht abrufen kann.
- **`**Voraussetzung:**` oben** (direkt unter dem Intro-Zitat, vor „Typische Aufgabenstellung"):
  listet Rezepte, die man **vorher** drauf haben muss. Nur wenn ohne sie der Kern des
  Rezepts nicht verständlich ist.
- **Inline-Verweise** nur an echten Sprungpunkten im Fließtext, z.B.
  „Kurvendiskussion wie gewohnt ([Rezept 01: Kurvendiskussion](01_kurvendiskussion.md))".
- **`## Siehe auch` unten** (optional): weiterführende, nicht zwingende Verweise.
- **Keine Duplikation erzwingen** — wenn Inhalt in einem anderen Rezept bereits steht,
  kurz darauf verlinken statt nachzubauen.

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

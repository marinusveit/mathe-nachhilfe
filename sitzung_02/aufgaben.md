# Aufgaben — Sitzung 2: Kurvendiskussion & Wertemenge

> Übungsaufgaben im Stil der bayerischen Abiturprüfung (G9 eA).
> Echte Altprüfungen liegen in `pruefungen/isb_abitur/` — diese Sammlung schließt
> gezielt Lücken zur Wertemenge und zur vollständigen Kurvendiskussion.

**Zugehörige Rezepte:**
[Rezept 01: Kurvendiskussion](../rezepte/01_kurvendiskussion.md) ·
[Rezept 09: Grenzwerte](../rezepte/09_grenzwerte.md) ·
[Rezept 12: Gebrochen-rationale Funktionen](../rezepte/12_gebrochen_rational.md) ·
[Rezept 18: Wertebereich](../rezepte/18_wertebereich.md)

---

## Prüfungsteil A — hilfsmittelfrei

> Arbeitszeit Richtwert: 20 Minuten. Keine Hilfsmittel. Lösungen vollständig begründen.

| BE | |
|:---:|---|
|     | **1** Gegeben ist die in $\mathbb{R}$ definierte Funktion $f$ mit $f(x) = -\tfrac{1}{2}x^2 + 4$. |
| 2   | **a)** Geben Sie den Wertebereich von $f$ an und begründen Sie Ihre Angabe. |
| 2   | **b)** Die in $\mathbb{R}$ definierte Funktion $g$ ist gegeben durch $g(x) = f(x-3)$. Geben Sie den Wertebereich von $g$ an und begründen Sie Ihre Angabe. |
|     | |
|     | **2** Gegeben ist die in $\mathbb{R} \setminus \{2\}$ definierte Funktion $h$ mit $h(x) = \dfrac{1}{(x-2)^2} + 1$. |
| 2   | **a)** Geben Sie je eine Gleichung der senkrechten und der waagerechten Asymptote des Graphen von $h$ an. |
| 3   | **b)** Begründen Sie, dass der Wertebereich von $h$ das Intervall $\,]1;\infty[\,$ ist. |
|     | |
|     | **3** Gegeben ist eine in $\mathbb{R}$ definierte ganzrationale Funktion $p$ dritten Grades. Der Graph $G_p$ ist punktsymmetrisch zum Ursprung und besitzt genau zwei lokale Extrempunkte: einen Tiefpunkt $T(-2\,\vert\,-3)$ und einen Hochpunkt $H(2\,\vert\,3)$. |
| 2   | **a)** Geben Sie die Anzahl der Nullstellen von $p'$ und die Anzahl der Nullstellen von $p''$ an. |
| 3   | **b)** Beurteilen Sie die folgende Aussage: „Der Wertebereich von $p$ ist $[-3;\,3]$." |
|     | |
|     | **4** Gegeben ist die in $\mathbb{R}$ definierte Funktion $f$ mit $f(x) = x \cdot \mathrm{e}^{-x^2}$. |
| 2   | **a)** Zeigen Sie, dass $f$ punktsymmetrisch zum Ursprung ist. |
| 4   | **b)** Weisen Sie nach, dass $f'(x) = (1 - 2x^2) \cdot \mathrm{e}^{-x^2}$ gilt. |
| **20** | |

---

## Prüfungsteil B — mit Hilfsmitteln

> Arbeitszeit Richtwert: 40 Minuten. GTR/CAS erlaubt, aber zentrale Schritte (Ableitung, notwendige/hinreichende Bedingung, Begründung) müssen dokumentiert sein.

| BE | |
|:---:|---|
|     | **1** Gegeben ist die in $\mathbb{R}$ definierte Funktion $f$ mit $f(x) = \tfrac{1}{4}x^4 - 2x^2 + \tfrac{7}{4}$. Der Graph von $f$ wird mit $G_f$ bezeichnet. |
| 2   | **a)** Untersuchen Sie $G_f$ auf Symmetrie und bestimmen Sie das Verhalten von $f$ für $x \to \pm\infty$. |
| 5   | **b)** Bestimmen Sie die Koordinaten und die Art aller Extrempunkte von $G_f$. |
| 3   | **c)** Bestimmen Sie die Koordinaten der Wendepunkte von $G_f$. |
| 3   | **d)** Bestimmen Sie den Wertebereich von $f$ und begründen Sie, dass $f$ jeden Wert des Wertebereichs mindestens einmal annimmt. |
| 2   | **e)** Skizzieren Sie $G_f$ im Bereich $-3 \le x \le 3$ unter Verwendung der bisherigen Ergebnisse. |
|     | |
|     | **2** Gegeben ist die in $\mathbb{R}^+$ definierte Funktion $k$ mit $k(x) = \dfrac{\ln(x)}{x}$. |
| 3   | **a)** Bestimmen Sie die Nullstelle von $k$ sowie das Verhalten von $k$ für $x \to 0^+$ und für $x \to \infty$. |
| 4   | **b)** Weisen Sie nach, dass $k'(x) = \dfrac{1 - \ln(x)}{x^2}$ gilt, und bestimmen Sie damit die Koordinaten des Hochpunkts von $G_k$. |
| 3   | **c)** Geben Sie den Wertebereich von $k$ an und begründen Sie Ihre Angabe unter Verwendung der Ergebnisse aus a) und b). |
| **25** | |

---

## Hinweise für den Unterricht

- **Aufgabe A3** zielt auf „Eigenschaften interpretieren + Aussage beurteilen" — eine der identifizierten Schwachstellen aus der Diagnose. Die beschriebene Funktion ist $p(x) = -\tfrac{3}{16}x^3 + \tfrac{9}{4}x$ (zur Kontrolle; Probe: $p'(x) = -\tfrac{9}{16}x^2 + \tfrac{9}{4} = 0$ bei $x = \pm 2$, $p(2) = 3$). Zu b): $W_p = [-3;3]$ ist **falsch**, weil $p$ als ganzrationale Funktion ungeraden Grades für $x \to \pm\infty$ gegen $\pm\infty$ strebt. Richtig: $W_p = \mathbb{R}$. Die Extrema sind nur **lokale**, keine globalen.
- **Aufgabe A4b** ist ein Kettenregel-Warm-up ($\mathrm{e}^{-x^2}$) — genau der Aufgabentyp aus 2022 A2 3b und 2025 B1 1c.
- **Aufgabe B1d** verknüpft Kurvendiskussion und Wertemenge. Lösung: globales Min bei $\pm 2$ mit $f(\pm 2) = -\tfrac{9}{4}$, für $x \to \pm\infty$ gilt $f \to \infty$ → $W_f = [-\tfrac{9}{4};\infty[$. Die Begründung „jeder Wert wird angenommen" läuft über Stetigkeit + Zwischenwertsatz.
- **Aufgabe B2** (gebrochen + $\ln$) ist anspruchsvoll — nur einsetzen, wenn Zeit bleibt. Lösung: Hochpunkt $(\mathrm{e}\,\vert\,\tfrac{1}{\mathrm{e}})$, $W_k = \,]-\infty;\,\tfrac{1}{\mathrm{e}}]$.

## Lösungen

Lösungsweg im Unterricht gemeinsam entwickeln. Kontrolle über:
- Notebook `kurvendiskussion_interaktiv.ipynb` → Zelle `kurvendiskussion('...')`
- Rezept 18 (Wertebereich-Tabelle + Beispiele)

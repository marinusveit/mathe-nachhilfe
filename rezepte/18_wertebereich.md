# Rezept: Wertebereich bestimmen

> Der Wertebereich $W_f$ ist die Menge aller $y$-Werte, die $f$ tatsächlich annimmt — die „Projektion des Graphen auf die $y$-Achse". Definitionsbereich sagt, was vorne reindarf; Wertebereich sagt, was hinten rauskommt.

**Voraussetzung:** [Rezept 01: Kurvendiskussion](01_kurvendiskussion.md) (Extrema, Monotonie, Randverhalten — das sind die Werkzeuge, aus denen sich der Wertebereich ergibt).

## Typische Aufgabenstellung
> „Geben Sie den Wertebereich von $f$ an."
> „Bestimmen Sie $W_f$."
> „Begründen Sie, dass $f$ jeden Wert in $[a;b]$ genau einmal annimmt."

## Schritt-für-Schritt: allgemeiner Fall (aus Kurvendiskussion)

1. **Definitionsbereich** klären — Randpunkte mitdenken!
2. **Globale Extrema** bestimmen: alle lokalen Extrema + Funktionswerte an den Rändern von $D$ vergleichen
3. **Randverhalten**: $\lim_{x \to \pm\infty} f(x)$ bzw. Grenzwerte an Definitionslücken
4. **Monotonie** prüfen: füllt $f$ das Intervall zwischen Min und Max **lückenlos**?
   - Ja (stetig + Zwischenwertsatz) → Wertebereich ist ein zusammenhängendes Intervall
   - Nein (z.B. Definitionslücke) → Wertebereich aus Teilintervallen zusammensetzen
5. **Intervall angeben** — auf offene vs. geschlossene Klammer achten:
   - **eckig** $[a;b]$: Wert wird **angenommen** (Extremum an einer konkreten Stelle)
   - **rund** $]a;b[$: Wert wird nur **asymptotisch** erreicht (Grenzwert, aber nie gleich)

## Schritt-für-Schritt: Standardfunktion mit bekanntem Bild

Wenn $f$ eine der Grundfunktionen ist, den Wertebereich direkt aus der Tabelle ablesen — keine Rechnung nötig.

| Funktion | Wertebereich |
|---|---|
| $x^2$ | $[0;\infty[$ |
| $x^3$ | $\mathbb{R}$ |
| $\sqrt{x}$ | $[0;\infty[$ |
| $e^x$ | $]0;\infty[$ |
| $\ln(x)$ | $\mathbb{R}$ |
| $\sin(x)$, $\cos(x)$ | $[-1;1]$ |
| $\dfrac{1}{x}$ ($x > 0$) | $]0;\infty[$ |

## Schritt-für-Schritt: Verkettung $g(x) = h(f(x))$

1. **Innerer Wertebereich** bestimmen: $W_f = $ Werte, die $f$ annimmt
2. **Äußere Funktion $h$** auf diesen Bereich anwenden — Monotonie von $h$ beachten:
   - $h$ streng steigend: Intervallgrenzen übernehmen
   - $h$ streng fallend: Intervallgrenzen vertauschen
3. Ergebnis = $W_g$

### Beispiel: $g(x) = e^{-x^2}$
- Innere Funktion $f(x) = -x^2$ hat Wertebereich $W_f = \mathopen{]}-\infty;\,0]$ (Max bei $x=0$)
- Äußere Funktion $e^{\cdot}$ ist streng steigend, also:
  - $-\infty \to e^{-\infty} = 0$ (nicht angenommen → rund)
  - $0 \to e^{0} = 1$ (angenommen → eckig)
- $W_g = \mathopen{]}0;\,1]$

## Schritt-für-Schritt: aus Graph ablesen

1. $y$-Achse entlangfahren: tiefster erreichter Wert bis höchster
2. Lücken markieren (Polstellen, ausgenommene Werte)
3. Offene Enden (Pfeile, Asymptoten) → runde Klammern

## Häufige Fehler

- Wertebereich als $\mathbb{R}$ angegeben, obwohl $f$ nach oben/unten **beschränkt** ist
- **Grenzwert** als „angenommener" Wert behandelt → eckige statt runder Klammer (Klassiker bei $e^x$, $\ln$, Asymptoten)
- $e^x > 0$ übersehen: Wertebereich ist $\mathopen{]}0;\infty\mathclose{[}$, **nicht** $[0;\infty[$
- Verkettung direkt geraten, statt erst inneren, dann äußeren Wertebereich zu bilden
- Definitionslücke vergessen → an der Polstelle fehlt evtl. ein $y$-Wert
- Bei fallender äußerer Funktion die Intervallgrenzen nicht getauscht

## Operatoren-Hinweis

- „Angeben" = nur das Intervall hinschreiben, keine Begründung nötig
- „Bestimmen" = rechnerisch herleiten (Extrema + Randverhalten) und Intervall angeben
- „Begründen / Zeigen" = Monotonie + Zwischenwertsatz / Extrema + Randverhalten nutzen

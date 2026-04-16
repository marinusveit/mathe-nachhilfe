# Rezept: Graphentransformationen

> Wie aus einem Grundgraphen durch Streckung, Spiegelung und Verschiebung ein neuer Graph entsteht — allgemein $g(x) = a \cdot f\bigl(b(x - c)\bigr) + d$.

### 🔗 Interaktiv in Desmos

**[Desmos-Graph öffnen](https://www.desmos.com/calculator/8mgborkxrg)** — Regler $a$, $b$, $c$, $d$ verschieben und beobachten, wie sich der Graph verformt.

## Typische Aufgabenstellung
> „Beschreiben Sie, wie der Graph von $g$ aus dem Graphen von $f$ hervorgeht."
> „Geben Sie die Koordinaten des Wendepunkts von $h(x) = f(2x) - 1$ an."

## Transformationsregeln

| Transformation | Gleichung | Wirkung |
|---|---|---|
| Verschiebung rechts um $a$ | $g(x) = f(x - a)$ | alle $x$-Werte $+\,a$ |
| Verschiebung links um $a$ | $g(x) = f(x + a)$ | alle $x$-Werte $-\,a$ |
| Verschiebung hoch um $b$ | $g(x) = f(x) + b$ | alle $y$-Werte $+\,b$ |
| Verschiebung runter um $b$ | $g(x) = f(x) - b$ | alle $y$-Werte $-\,b$ |
| Streckung in $y$-Richtung (Faktor $k$) | $g(x) = k \cdot f(x)$ | alle $y$-Werte $\cdot\,k$ |
| Stauchung in $x$-Richtung (Faktor $\tfrac{1}{k}$) | $g(x) = f(k \cdot x)$ | alle $x$-Werte $\div\,k$ |
| Spiegelung an $x$-Achse | $g(x) = -f(x)$ | alle $y$-Werte $\cdot\,(-1)$ |
| Spiegelung an $y$-Achse | $g(x) = f(-x)$ | alle $x$-Werte $\cdot\,(-1)$ |

## Schritt-für-Schritt: Besondere Punkte transformieren

**Gegeben:** $f$ hat einen besonderen Punkt $P(x_0 \mid y_0)$, gesucht: Punkt bei $g(x) = a \cdot f(bx + c) + d$

1. **$x$-Koordinate**: $x_{0,\text{neu}} = \dfrac{x_0 - c}{b}$
2. **$y$-Koordinate**: $y_{0,\text{neu}} = a \cdot y_0 + d$
3. **Neuer Punkt**: $P'(x_{0,\text{neu}} \mid y_{0,\text{neu}})$

**Merke:** Die Lage des Punktes ändert sich systematisch. Ein Wendepunkt bleibt ein Wendepunkt; ein Extrempunkt bleibt ein Extrempunkt, wobei sich bei Spiegelung an der $x$-Achse Maximum und Minimum vertauschen können.

## Beispiel (Abitur 2025 A2 2b)
$f$ hat Wendepunkt $W(2 \mid 3)$, gesucht: Wendepunkt von $h(x) = f(2x) - 1$
- $x$-Koordinate: $\tfrac{2}{2} = 1$
- $y$-Koordinate: $3 - 1 = 2$
- Neuer Wendepunkt: $W'(1 \mid 2)$

## Schritt-für-Schritt: Transformation beschreiben

1. Vergleiche $g(x)$ mit $f(x)$ — identifiziere $a$, $b$, $c$, $d$
2. Beschreibe jede Änderung einzeln, Reihenfolge beachten:
   - Erst $x$-Transformationen (innen), dann $y$-Transformationen (außen)

## Häufige Fehler
- $f(x - 3)$ verschiebt nach RECHTS, nicht links (Vorzeichen-Falle)
- $f(2x)$ staucht um Faktor $\tfrac{1}{2}$, nicht streckt um $2$
- Reihenfolge bei Kombination: $f(2(x - 1)) \neq f(2x - 1)$ — erst verschieben, dann stauchen, oder umgekehrt formulieren

# Rezept: Integrale und Flächenberechnung

> Flächeninhalte zwischen Graph und $x$-Achse (oder zwischen zwei Graphen) per bestimmtem Integral berechnen. Kernpunkt: Vorzeichenwechsel beachten, bei Flächen immer Betrag.

## Typische Aufgabenstellung
> „Berechnen Sie den Flächeninhalt, den der Graph von $f$ mit der $x$-Achse einschließt."
> „Berechnen Sie die Fläche zwischen den Graphen von $f$ und $g$."

## Schritt-für-Schritt: Fläche zwischen Graph und $x$-Achse

1. **Nullstellen** von $f$ bestimmen → Integrationsgrenzen
2. **Vorzeichen prüfen**: Wo ist $f$ positiv, wo negativ?
3. **Betragsmäßig integrieren**: Fläche unter $x$-Achse wird negativ → Betrag nehmen
4. $$A = \left| \int_a^b f(x)\,dx \right| \quad\text{(nur ohne VZW!)} \quad\text{oder intervallweise:}\quad A = \left| \int_a^c f(x)\,dx \right| + \left| \int_c^b f(x)\,dx \right| \quad\text{(VZW bei $c$)}$$

## Schritt-für-Schritt: Fläche zwischen zwei Graphen

1. **Schnittstellen** berechnen: $f(x) = g(x)$ lösen
2. **Prüfen, welche Funktion oben liegt** (Wert einsetzen zwischen den Schnittstellen)
3. $$A = \int_a^b \bigl|f(x) - g(x)\bigr|\,dx = \int_a^b \bigl(\text{oben} - \text{unten}\bigr)\,dx$$

## Wichtige Stammfunktionen

| $f(x)$ | $F(x)$ |
|---|---|
| $x^n$ | $\dfrac{x^{n+1}}{n+1}$ für $n \neq -1$ |
| $e^{ax}$ | $\dfrac{1}{a} \cdot e^{ax}$ |
| $\dfrac{1}{x}$ | $\ln\lvert x\rvert$ |
| $\sin(ax)$ | $-\dfrac{1}{a} \cdot \cos(ax)$ |
| $\cos(ax)$ | $\dfrac{1}{a} \cdot \sin(ax)$ |

## Häufige Fehler
- Vorzeichen ignoriert: $\int$ kann negativ sein, Fläche ist aber immer $\geq 0$
- Falsches Intervall: Nullstellen vergessen → Flächen heben sich auf
- Fläche zwischen Kurven: $(\text{oben} - \text{unten})$ vertauscht → negatives Ergebnis
- Stammfunktion von $e^{2x}$ ist $\tfrac{1}{2} e^{2x}$, NICHT $e^{2x}$

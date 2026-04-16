# Rezept: Integrale und Flächenberechnung

## Typische Aufgabenstellung
> „Berechnen Sie den Flächeninhalt, den der Graph von f mit der x-Achse einschließt."
> „Berechnen Sie die Fläche zwischen den Graphen von f und g."

## Schritt-für-Schritt: Fläche zwischen Graph und x-Achse

1. **Nullstellen** von f bestimmen → Integrationsgrenzen
2. **Vorzeichen prüfen**: Wo ist f positiv, wo negativ?
3. **Betragsmäßig integrieren**: Fläche unter x-Achse wird negativ → Betrag nehmen
4. A = |∫ₐᵇ f(x) dx| oder intervallweise: ∫ₐᶜ f(x) dx − ∫ᶜᵇ f(x) dx (wenn VZW bei c)

## Schritt-für-Schritt: Fläche zwischen zwei Graphen

1. **Schnittstellen** berechnen: f(x) = g(x) lösen
2. **Prüfen, welche Funktion oben liegt** (Wert einsetzen zwischen den Schnittstellen)
3. A = ∫ₐᵇ |f(x) − g(x)| dx = ∫ₐᵇ (oben − unten) dx

## Wichtige Stammfunktionen

| f(x) | F(x) |
|---|---|
| xⁿ | x^(n+1)/(n+1) für n ≠ −1 |
| e^(ax) | (1/a) · e^(ax) |
| 1/x | ln\|x\| |
| sin(ax) | −(1/a) · cos(ax) |
| cos(ax) | (1/a) · sin(ax) |

## Häufige Fehler
- Vorzeichen ignoriert: ∫ kann negativ sein, Fläche ist aber immer ≥ 0
- Falsches Intervall: Nullstellen vergessen → Flächen heben sich auf
- Fläche zwischen Kurven: (oben − unten) vertauscht → negatives Ergebnis
- Stammfunktion von e^(2x) ist (1/2)e^(2x), NICHT e^(2x)

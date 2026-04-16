# Rezept: Funktionenschar und Ortskurve

> Eine ganze Familie von Funktionen $f_k$ mit Parameter $k$ — wie hängen Extrema, Nullstellen und Wendepunkte von $k$ ab, und welche Kurve durchlaufen sie?

## Typische Aufgabenstellung
> „Untersuchen Sie $f_k(x)$ in Abhängigkeit vom Parameter $k$."
> „Bestimmen Sie die Ortskurve der Extrempunkte."

## Schritt-für-Schritt: Funktionenschar untersuchen

1. **Parameter als Konstante** behandeln — ableiten, Nullstellen etc. ganz normal, $k$ steht einfach da
2. **Kurvendiskussion wie gewohnt** (Rezept 01), nur dass Ergebnisse von $k$ abhängen
3. **Besondere Parameterwerte** untersuchen:
   - Für welches $k$ hat $f$ keine Extrema / genau ein Extremum / etc.?
   - Bedingung aufstellen und nach $k$ lösen

## Schritt-für-Schritt: Ortskurve

1. **Extrempunkte berechnen**: $x_E$ und $y_E$ in Abhängigkeit von $k$
   - $x_E(k)$: aus $f'(x) = 0$
   - $y_E(k)$: $x_E$ in $f$ einsetzen
2. **$k$ eliminieren**: Aus $x_E(k)$ nach $k$ auflösen, in $y_E$ einsetzen
3. **Ortskurvengleichung**: $y = g(x)$, ohne $k$

### Beispiel

$$f_k(x) = x^2 - kx \quad\Longrightarrow\quad f'(x) = 2x - k = 0 \quad\Longrightarrow\quad x_E = \tfrac{k}{2}$$

$$y_E = \left(\tfrac{k}{2}\right)^2 - k \cdot \tfrac{k}{2} = -\tfrac{k^2}{4}$$

Aus $x_E = \tfrac{k}{2}$ folgt $k = 2 x_E$, einsetzen:

$$y = -\tfrac{(2x)^2}{4} = -x^2$$

Ortskurve: $y = -x^2$.

## Häufige Fehler
- $k$ bei der Ableitung mitableiten ($k$ ist Konstante, nicht Variable!)
- Ortskurve: $k$ nicht vollständig eliminiert
- Definitionsbereich der Ortskurve vergessen (nicht alle $x$ sind erreichbar)
- Fallunterscheidungen vergessen: z.B. $k > 0$ vs. $k < 0$ kann verschiedene Fälle ergeben

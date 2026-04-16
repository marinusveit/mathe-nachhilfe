# Rezept: Funktionenschar und Ortskurve

## Typische Aufgabenstellung
> „Untersuchen Sie fₖ(x) in Abhängigkeit vom Parameter k."
> „Bestimmen Sie die Ortskurve der Extrempunkte."

## Schritt-für-Schritt: Funktionenschar untersuchen

1. **Parameter als Konstante** behandeln — ableiten, Nullstellen etc. ganz normal, k steht einfach da
2. **Kurvendiskussion wie gewohnt** (Rezept 01), nur dass Ergebnisse von k abhängen
3. **Besondere Parameterwerte** untersuchen:
   - Für welches k hat f keine Extrema / genau ein Extremum / etc.?
   - Bedingung aufstellen und nach k lösen

## Schritt-für-Schritt: Ortskurve

1. **Extrempunkte berechnen**: x_E und y_E in Abhängigkeit von k
   - x_E(k): aus f'(x) = 0
   - y_E(k): x_E in f einsetzen
2. **k eliminieren**: Aus x_E(k) nach k auflösen, in y_E einsetzen
3. **Ortskurvengleichung**: y = g(x), ohne k

### Beispiel
fₖ(x) = x² − kx → f'(x) = 2x − k = 0 → x_E = k/2
y_E = (k/2)² − k·(k/2) = −k²/4
Aus x_E = k/2 → k = 2x_E, einsetzen: y = −(2x)²/4 = −x²
Ortskurve: y = −x²

## Häufige Fehler
- k bei der Ableitung mitableiten (k ist Konstante, nicht Variable!)
- Ortskurve: k nicht vollständig eliminiert
- Definitionsbereich der Ortskurve vergessen (nicht alle x sind erreichbar)
- Fallunterscheidungen vergessen: z.B. k > 0 vs. k < 0 kann verschiedene Fälle ergeben

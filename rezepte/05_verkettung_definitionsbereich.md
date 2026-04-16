# Rezept: Verkettung und Definitionsbereich

## Typische Aufgabenstellung
> „Geben Sie den maximalen Definitionsbereich von g(x) = ln(f(x)) an."
> „Bestimmen Sie g'(x) mithilfe der Kettenregel."

## Schritt-für-Schritt: Definitionsbereich einer Verkettung

### Allgemein: g(x) = h(f(x))
1. **Äußere Funktion h prüfen** — welche Einschränkung hat h?
   - ln(…): Argument muss > 0 sein
   - √(…): Argument muss ≥ 0 sein
   - 1/(…): Argument muss ≠ 0 sein
2. **Bedingung an f(x) aufstellen**: z.B. f(x) > 0
3. **Ungleichung lösen** → Definitionsbereich

### Beispiel: g(x) = ln(f(x)), f hat Nullstelle bei x = 2 und f'(x) > 0 für alle x
- ln braucht: f(x) > 0
- f ist streng monoton steigend mit Nullstelle bei x = 2
- Also: f(x) > 0 für x > 2
- D_g = ]2; ∞[

## Schritt-für-Schritt: Ableitung einer Verkettung (Kettenregel)

g(x) = h(f(x)) → g'(x) = h'(f(x)) · f'(x)

### Wichtige Spezialfälle

| g(x) | g'(x) |
|---|---|
| ln(f(x)) | f'(x) / f(x) |
| e^(f(x)) | f'(x) · e^(f(x)) |
| [f(x)]ⁿ | n · [f(x)]^(n−1) · f'(x) |
| √(f(x)) | f'(x) / (2√(f(x))) |
| sin(f(x)) | f'(x) · cos(f(x)) |

## Häufige Fehler
- Kettenregel vergessen: (e^(2x))' = 2e^(2x), NICHT e^(2x)
- Definitionsbereich der inneren Funktion vergessen
- Bei ln(f(x)): f(x) = 0 gehört NICHT zum Definitionsbereich
- Ableitung von ln(f(x)) = f'(x)/f(x): den Nenner f(x) vergessen

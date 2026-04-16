# Rezept: Grenzwerte und Asymptoten

## Typische Aufgabenstellung
> „Bestimmen Sie das Verhalten von f für x → ±∞."
> „Ermitteln Sie lim f'(x) und deuten Sie das Ergebnis."
> „Bestimmen Sie die Asymptoten."

## Schritt-für-Schritt: Grenzwert für x → ±∞

1. **Dominanten Term identifizieren** — wer wächst am schnellsten?
   - Hierarchie: e^x >> xⁿ >> ln(x) >> Konstante
   - e^(−x) → 0 für x → ∞
2. **Ausklammern** des dominanten Terms, Rest → 0 oder Konstante
3. **Ergebnis**: Zahl, +∞, −∞ oder „existiert nicht"

## Schritt-für-Schritt: Asymptoten

### Waagrechte Asymptote (x → ±∞)
- lim f(x) = c → waagrechte Asymptote y = c

### Senkrechte Asymptote (Polstelle)
- f(x) → ±∞ für x → x₀ → senkrechte Asymptote x = x₀
- Typisch bei gebrochen-rationalen Funktionen: Nenner = 0
- Oft sind **einseitige Grenzwerte** wichtig: x → x₀⁻ und x → x₀⁺ getrennt prüfen

### Schräge Asymptote
- Zählergrad = Nennergrad + 1 → Polynomdivision → y = mx + b

## Wichtige Grenzwerte

| Ausdruck | Grenzwert |
|---|---|
| e^(−x), x → ∞ | 0 |
| x · e^(−x), x → ∞ | 0 (e^x dominiert) |
| x² · e^(−x), x → ∞ | 0 |
| ln(x) / x, x → ∞ | 0 |
| (1 + 1/x)^x, x → ∞ | e |
| sin(x)/x, x → 0 | 1 |

## Sachkontextdeutung

Immer fragen: **Was bedeutet der Grenzwert in der Aufgabe?**
- lim f(t) = 0 für t → ∞ → „Langfristig nähert sich … dem Wert 0 an"
- lim f'(x) = −∞ → „Die Steigung wird beliebig steil negativ" (z.B. senkrechtes Auftreffen)
- lim f(t) = L → „Der Bestand nähert sich langfristig dem Sättigungswert L an"

## Häufige Fehler
- e^(−x) und e^x verwechseln: e^(−x) → 0, e^x → ∞
- „lim = ∞" hinschreiben, aber nicht als „Grenzwert existiert nicht" kennzeichnen
- Sachkontext vergessen: Grenzwert berechnet, aber nicht interpretiert

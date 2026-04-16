# Rezept: Grenzwerte und Asymptoten

> Wie verhält sich $f(x)$, wenn $x$ gegen $\pm\infty$ oder gegen eine Definitionslücke strebt? Liefert Asymptoten und Randverhalten für die Kurvendiskussion.

## Typische Aufgabenstellung
> „Bestimmen Sie das Verhalten von $f$ für $x \to \pm\infty$."
> „Ermitteln Sie $\lim f'(x)$ und deuten Sie das Ergebnis."
> „Bestimmen Sie die Asymptoten."

## Schritt-für-Schritt: Grenzwert für $x \to \pm\infty$

1. **Dominanten Term identifizieren** — wer wächst am schnellsten?
   - Hierarchie: $e^x \;\gg\; x^n \;\gg\; \ln(x) \;\gg\; \text{Konstante}$
   - $e^{-x} \to 0$ für $x \to \infty$
2. **Ausklammern** des dominanten Terms, Rest $\to 0$ oder Konstante
3. **Ergebnis**: Zahl, $+\infty$, $-\infty$ oder „existiert nicht"

## Schritt-für-Schritt: Asymptoten

### Waagrechte Asymptote ($x \to \pm\infty$)
- $\lim_{x \to \pm\infty} f(x) = c$ → waagrechte Asymptote $y = c$

### Senkrechte Asymptote (Polstelle)
- $f(x) \to \pm\infty$ für $x \to x_0$ → senkrechte Asymptote $x = x_0$
- Typisch bei gebrochen-rationalen Funktionen: Nenner $= 0$
- Oft sind **einseitige Grenzwerte** wichtig: $x \to x_0^-$ und $x \to x_0^+$ getrennt prüfen

### Schräge Asymptote
- Zählergrad $=$ Nennergrad $+\,1$ → Polynomdivision → $y = mx + b$

## Wichtige Grenzwerte

| Ausdruck | Grenzwert |
|---|---|
| $e^{-x}$, $x \to \infty$ | $0$ |
| $x \cdot e^{-x}$, $x \to \infty$ | $0$ ($e^x$ dominiert) |
| $x^2 \cdot e^{-x}$, $x \to \infty$ | $0$ |
| $\dfrac{\ln(x)}{x}$, $x \to \infty$ | $0$ |
| $\left(1 + \dfrac{1}{x}\right)^x$, $x \to \infty$ | $e$ |
| $\dfrac{\sin(x)}{x}$, $x \to 0$ | $1$ |

## Sachkontextdeutung

Immer fragen: **Was bedeutet der Grenzwert in der Aufgabe?**
- $\lim_{t \to \infty} f(t) = 0$ → „Langfristig nähert sich … dem Wert $0$ an"
- $\lim f'(x) = -\infty$ → „Die Steigung wird beliebig steil negativ" (z.B. senkrechtes Auftreffen)
- $\lim_{t \to \infty} f(t) = L$ → „Der Bestand nähert sich langfristig dem Sättigungswert $L$ an"

## Häufige Fehler
- $e^{-x}$ und $e^x$ verwechseln: $e^{-x} \to 0$, $e^x \to \infty$
- „$\lim = \infty$" hinschreiben, aber nicht als „Grenzwert existiert nicht" kennzeichnen
- Sachkontext vergessen: Grenzwert berechnet, aber nicht interpretiert

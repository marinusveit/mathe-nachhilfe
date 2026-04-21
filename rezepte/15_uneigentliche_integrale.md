# Rezept: Uneigentliche Integrale

> Integrale mit unendlicher Grenze ($\int_1^\infty$) oder über eine Polstelle — wann ergibt die „unendliche Fläche" dennoch eine endliche Zahl?

**Voraussetzung:** [Rezept 08: Integrale & Fläche](08_integrale_flaeche.md) (Stammfunktionen), [Rezept 09: Grenzwerte und Asymptoten](09_grenzwerte.md) (denn ein uneigentliches Integral ist buchstäblich ein Grenzwert eines Integrals).

## Typische Aufgabenstellung
> „Untersuchen Sie, ob das Integral $\int_1^{\infty} f(x)\,dx$ konvergiert, und berechnen Sie ggf. seinen Wert."
> „Bestimmen Sie den Flächeninhalt zwischen dem Graphen von $f$ und der $x$-Achse für $x \geq 1$."

## Typ 1: Grenze geht gegen ±∞

$$\int_a^{\infty} f(x)\,dx = \lim_{b \to \infty} \int_a^b f(x)\,dx$$

### Schritt-für-Schritt

1. **Obere Grenze durch $b$ ersetzen**: $\int_a^b f(x)\,dx$ ganz normal berechnen
2. **Stammfunktion** $F$ bestimmen und Grenzen einsetzen: $F(b) - F(a)$
3. **Grenzwert** für $b \to \infty$ berechnen
4. **Ergebnis deuten:**
   - Grenzwert existiert (endlich) → Integral **konvergiert**
   - Grenzwert existiert nicht ($\to \infty$) → Integral **divergiert**

### Standardbeispiele

| Integral | Ergebnis | Begründung |
|---|---|---|
| $\int_1^{\infty} \dfrac{1}{x^2}\,dx$ | **$1$** (konvergent) | $F(x) = -\dfrac{1}{x} \;\Rightarrow\; \lim\bigl(-\tfrac{1}{b} + 1\bigr) = 1$ |
| $\int_1^{\infty} \dfrac{1}{x}\,dx$ | **divergent** | $F(x) = \ln x \;\Rightarrow\; \lim \ln(b) = \infty$ |
| $\int_0^{\infty} e^{-x}\,dx$ | **$1$** (konvergent) | $F(x) = -e^{-x} \;\Rightarrow\; \lim\bigl(-e^{-b} + 1\bigr) = 1$ |
| $\int_1^{\infty} \dfrac{1}{x^p}\,dx$ | konvergent $\iff p > 1$ | Merkregel! |

### Merkregel für $\dfrac{1}{x^p}$

- $p > 1$: konvergiert (Funktion fällt „schnell genug")
- $p \leq 1$: divergiert (Funktion fällt „zu langsam")

## Typ 2: Integrand hat Polstelle

$$\int_a^b f(x)\,dx \quad \text{wobei } \lim_{x \to c} f(x) = \pm\infty \text{ für ein } c \in [a,b]$$

### Schritt-für-Schritt

1. **Polstelle $c$ identifizieren** (wo wird der Nenner null?)
2. **Grenze durch Limes ersetzen:**
   - Polstelle am linken Rand: $\displaystyle\lim_{\varepsilon \to 0^+} \int_{a+\varepsilon}^b f(x)\,dx$
   - Polstelle am rechten Rand: $\displaystyle\lim_{\varepsilon \to 0^+} \int_a^{b-\varepsilon} f(x)\,dx$
   - Polstelle im Inneren: In zwei Integrale aufteilen
3. **Stammfunktion** bestimmen, einsetzen, Grenzwert berechnen

### Beispiel
$\displaystyle\int_0^1 \frac{1}{\sqrt{x}}\,dx$:

$f(x) = x^{-1/2}$ hat Polstelle bei $x = 0$.

$$\int_{\varepsilon}^1 x^{-1/2}\,dx = \bigl[2\sqrt{x}\bigr]_{\varepsilon}^1 = 2 - 2\sqrt{\varepsilon} \;\longrightarrow\; 2 \quad\text{für } \varepsilon \to 0^+$$

→ **Konvergent**, Wert $= 2$.

## Deutung im Sachkontext

Ein konvergentes uneigentliches Integral bedeutet: Obwohl der Bereich unendlich lang ist, ist die eingeschlossene Fläche endlich. Die Funktion nähert sich „schnell genug" der $x$-Achse an.

## Häufige Fehler

- **Grenzwert vergessen**: Einfach $\infty$ als Grenze einsetzen ist NICHT erlaubt — immer $\lim$ schreiben!
- **Divergenz nicht erkennen**: Wenn der Grenzwert nicht existiert, muss man das klar sagen
- **Polstelle übersehen**: Bei $\int_0^2 \tfrac{1}{x}\,dx$ liegt eine Polstelle bei $x = 0$ — man darf nicht einfach drüber integrieren
- **Falscher Schluss**: „Die Funktion geht gegen $0$, also konvergiert das Integral" — FALSCH (Gegenbeispiel: $\tfrac{1}{x} \to 0$, aber $\int \tfrac{1}{x}\,dx$ divergiert)

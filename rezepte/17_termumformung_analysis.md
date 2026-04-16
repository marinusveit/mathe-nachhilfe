# Rezept: Termumformung in der Analysis — der „letzte Schritt"-Werkzeugkasten

> Die algebraischen Umformungen, die nach der Ableitung kommen: Brüche zusammenfassen, negative Exponenten in Bruchform, Wurzel im Nenner, Doppelbruch auflösen.

## Warum dieses Rezept?

Viele Analysis-Aufgaben scheitern **nicht an der Ableitungsregel**, sondern am **letzten Umformschritt**: Brüche zusammenfassen, negative Exponenten in Bruchform bringen, Wurzel im Nenner handhaben. Der Rechenweg ist richtig, aber der Term kommt nicht auf die vorgegebene Form — und das kostet Punkte bei „Zeigen Sie / Weisen Sie nach".

## Die 5 wichtigsten Muster

### Muster 1: Negative Exponenten $\leftrightarrow$ Bruch

$$a^{-n} = \frac{1}{a^n} \qquad \frac{1}{a^n} = a^{-n}$$

**In Analysis typisch:**
- Ableitung von $\sqrt{u}$: $\;\tfrac{1}{2} u^{-1/2} \;=\; \dfrac{1}{2\sqrt{u}}$
- Ableitung von $\dfrac{1}{x}$: schreibe als $x^{-1}$, dann $-1 \cdot x^{-2} \;=\; -\dfrac{1}{x^2}$
- Ableitung von $\dfrac{1}{x^2}$: schreibe als $x^{-2}$, dann $-2x^{-3} \;=\; -\dfrac{2}{x^3}$

**Merksatz:** Vor dem Ableiten Exponentenschreibweise → Potenzregel anwenden → **danach zurück in Bruchform**.

### Muster 2: Brüche mit gleichem Nenner addieren

$$\frac{a}{n} + \frac{b}{n} = \frac{a + b}{n} \qquad \frac{a}{n} - \frac{b}{n} = \frac{a - b}{n}$$

**Nur der Zähler wird addiert/subtrahiert, der Nenner bleibt!**

### Muster 3: Hauptnenner bilden

$$\frac{a}{n_1} + \frac{b}{n_2} = \frac{a \cdot n_2 + b \cdot n_1}{n_1 \cdot n_2}$$

**Wenn $n_1$ in $n_2$ enthalten ist** (z.B. $n_2 = 2 \cdot n_1$), nur den kleineren erweitern:

$$\frac{a}{n_1} + \frac{b}{2 n_1} = \frac{2a}{2 n_1} + \frac{b}{2 n_1} = \frac{2a + b}{2 n_1}$$

**Beispiel aus Abitur 2025 B1 1c:** Man hat $\sqrt{6-x} - \dfrac{x+6}{2\sqrt{6-x}}$.

Der erste Summand hat „unsichtbaren Nenner" $1$. Erweitern auf Hauptnenner $2\sqrt{6-x}$:

$$\sqrt{6-x} = \frac{\sqrt{6-x} \cdot 2\sqrt{6-x}}{2\sqrt{6-x}} = \frac{2(6-x)}{2\sqrt{6-x}}$$

Dann:
$$\frac{2(6-x)}{2\sqrt{6-x}} - \frac{x+6}{2\sqrt{6-x}} = \frac{2(6-x) - (x+6)}{2\sqrt{6-x}} = \frac{12 - 2x - x - 6}{2\sqrt{6-x}} = \frac{6 - 3x}{2\sqrt{6-x}}$$

**Zentrale Idee:** $\sqrt{u} \cdot \sqrt{u} = u$ — damit wird die Wurzel im Zähler verschwinden gemacht.

### Muster 4: Wurzel im Nenner

$$\frac{a}{\sqrt{u}} = \frac{a \cdot \sqrt{u}}{u} \quad \text{(Rationalisieren, falls gewünscht)}$$

**Faustregel im Abitur:** Meistens lässt man die Wurzel im Nenner stehen — nur rationalisieren, wenn die Aufgabe das verlangt oder es beim Vereinfachen hilft.

### Muster 5: Doppelbruch auflösen

$$\frac{\dfrac{a}{b}}{c} = \frac{a}{b \cdot c} \qquad \frac{a}{\dfrac{b}{c}} = \frac{a \cdot c}{b}$$

**Faustregel:** „Bruch im Nenner → multiplizieren mit Kehrwert."

**Typisches Beispiel:** $\dfrac{f'(x)}{f(x)^2}$ nach Quotientenregel — passt oft schon, aber bei verketteten Termen wie $\dfrac{1/u}{v}$ unbedingt auflösen.

## Drill: 10 kurze Umformungen

Ergebnisse unten. Versuche, ohne Taschenrechner.

**Negative Exponenten in Bruchform:**
1. $3 x^{-2}$
2. $\tfrac{1}{2} (2x+1)^{-1/2}$
3. $-4 x^{-3}$

**Brüche zusammenfassen:**
4. $\dfrac{x}{3} + \dfrac{2x}{3}$
5. $\dfrac{x+1}{4} - \dfrac{x-3}{4}$
6. $\dfrac{1}{x} + \dfrac{1}{x^2}$
7. $2x + \dfrac{1}{x}$

**Analysis-typische Endformen:**
8. $\sqrt{x} + \dfrac{x}{2\sqrt{x}}$ (auf einen Bruch bringen)
9. $\dfrac{1}{\sqrt{x-1}} \cdot \dfrac{1}{2}$ (aufräumen)
10. $\dfrac{3x^{-1}}{x^{-2}}$ (vereinfachen, positive Exponenten)

---

### Lösungen

1. $\dfrac{3}{x^2}$
2. $\dfrac{1}{2\sqrt{2x+1}}$
3. $-\dfrac{4}{x^3}$
4. $\dfrac{3x}{3} = x$
5. $\dfrac{4}{4} = 1$
6. $\dfrac{x+1}{x^2}$ *(Hauptnenner $x^2$)*
7. $\dfrac{2x^2+1}{x}$ *(Hauptnenner $x$)*
8. $\sqrt{x} = \dfrac{2x}{2\sqrt{x}}$, also $\dfrac{2x + x}{2\sqrt{x}} = \dfrac{3x}{2\sqrt{x}}$
9. $\dfrac{1}{2\sqrt{x-1}}$
10. $3x^{-1} \cdot x^{2} = 3x$

## Typische Stolpersteine

1. **Nenner mitaddieren** — falsch: $\tfrac{a}{n} + \tfrac{b}{n} = \tfrac{a+b}{2n}$. Richtig: $\tfrac{a+b}{n}$.
2. **Vorzeichen beim Hauptnenner** — beim Erweitern mit $(-1)$ oder negativen Termen: Klammern setzen!
3. **$a^{-n}$ mit $-a^n$ verwechseln** — $a^{-2} = \tfrac{1}{a^2}$, **nicht** $-a^2$.
4. **$\sqrt{u}$ mit $u^{1/2}$ nicht verknüpfen** — bei der Ableitung als Potenz rechnen, beim Endergebnis als Wurzel darstellen.
5. **Zu früh aufhören** — bei „Zeigen Sie"-Aufgaben muss die **exakte vorgegebene Form** dastehen, nicht eine äquivalente.

## Anwendung im Unterricht

Dieses Rezept ist als **5-Minuten-Warm-up** konzipiert. Pro Sitzung 2–3 Aufgaben aus dem Drill, bis die Muster automatisiert sind. Direkt vor dem Hauptteil — löst Denkblockaden und reduziert Fehler in den eigentlichen Abituraufgaben.

# Musterlösung — Hilfsmittelfreier Teil (Teil A)

---

## Aufgabe 1: Ableitungen bestimmen (6 Punkte)

### a) $f(x) = 5x^3 - 4x^2 + 2x - 7$

**Methode:** Summenregel + Potenzregel ($f(x) = x^n \implies f'(x) = n \cdot x^{n-1}$)

$$f'(x) = 15x^2 - 8x + 2$$

---

### b) $f(x) = \dfrac{3}{x} + 2\sqrt{x}$

**Methode:** Umschreiben in Potenzform, dann Potenzregel.

Umschreiben: $f(x) = 3x^{-1} + 2x^{1/2}$

$$f'(x) = 3 \cdot (-1) \cdot x^{-2} + 2 \cdot \tfrac{1}{2} \cdot x^{-1/2}$$

**$f'(x) = -\dfrac{3}{x^2} + \dfrac{1}{\sqrt{x}}$**

---

### c) $f(x) = (3x - 1)^4$

**Methode:** Kettenregel. Äußere Funktion: $u^4$, innere Funktion: $u = 3x - 1$.

$$f'(x) = 4 \cdot (3x - 1)^3 \cdot 3$$

**$f'(x) = 12 \cdot (3x - 1)^3$**

---

### d) $f(x) = x^2 \cdot \ln(x)$

**Methode:** Produktregel: $(u \cdot v)' = u' \cdot v + u \cdot v'$.

Setze $u = x^2$, $v = \ln(x)$, also $u' = 2x$, $v' = \dfrac{1}{x}$.

$$f'(x) = 2x \cdot \ln(x) + x^2 \cdot \frac{1}{x}$$

**$f'(x) = 2x \cdot \ln(x) + x$**

---

### e) $f(x) = e^{-x^2}$

**Methode:** Kettenregel. Äußere Funktion: $e^u$, innere Funktion: $u = -x^2$.

$$f'(x) = e^{-x^2} \cdot (-2x)$$

**$f'(x) = -2x \cdot e^{-x^2}$**

---

### f) $f(x) = \sin(2x) + \cos(x)$

**Methode:** Kettenregel bei $\sin(2x)$; Ableitung von $\cos(x)$ ist $-\sin(x)$.

$$f'(x) = \cos(2x) \cdot 2 + (-\sin(x))$$

**$f'(x) = 2 \cdot \cos(2x) - \sin(x)$**

---

## Aufgabe 2: Stammfunktionen bestimmen (4 Punkte)

### a) $f(x) = 6x^2 - 4x + 3$

**Methode:** Potenzregel rückwärts: $\int x^n\,dx = \dfrac{x^{n+1}}{n+1}$.

**$F(x) = 2x^3 - 2x^2 + 3x$**

Probe: $F'(x) = 6x^2 - 4x + 3$ ✓

---

### b) $f(x) = e^{3x}$

**Methode:** Lineare Substitution: $\int e^{ax}\,dx = \dfrac{1}{a} \cdot e^{ax}$.

**$F(x) = \dfrac{1}{3} \cdot e^{3x}$**

Probe: $F'(x) = \dfrac{1}{3} \cdot 3 \cdot e^{3x} = e^{3x}$ ✓

---

### c) $f(x) = \dfrac{1}{x}$  ($x > 0$)

**Methode:** Standardintegral $\int \dfrac{1}{x}\,dx = \ln \lvert x \rvert$. Da $x > 0$ gilt $\ln(x)$.

**$F(x) = \ln(x)$**

---

### d) $f(x) = 4 \cdot \cos(2x)$

**Methode:** Lineare Substitution: $\int \cos(ax)\,dx = \dfrac{1}{a} \cdot \sin(ax)$.

$$F(x) = 4 \cdot \frac{1}{2} \cdot \sin(2x)$$

**$F(x) = 2 \cdot \sin(2x)$**

Probe: $F'(x) = 2 \cdot \cos(2x) \cdot 2 = 4 \cdot \cos(2x)$ ✓

---

## Aufgabe 3: Bestimmte Integrale berechnen (4 Punkte)

### a) $\int_0^3 (2x + 1)\,dx$

**Methode:** Stammfunktion bilden, Hauptsatz der Differential- und Integralrechnung.

$$F(x) = x^2 + x$$

$$\int_0^3 (2x + 1)\,dx = F(3) - F(0) = (9 + 3) - (0 + 0) = 12$$

**Ergebnis: $12$**

---

### b) $\int_1^2 x^2\,dx$

$$F(x) = \frac{x^3}{3}$$

$$\int_1^2 x^2\,dx = \frac{8}{3} - \frac{1}{3} = \frac{7}{3}$$

**Ergebnis: $\tfrac{7}{3}$**

---

### c) $\int_0^1 e^x\,dx$

$$F(x) = e^x$$

$$\int_0^1 e^x\,dx = e^1 - e^0 = e - 1$$

**Ergebnis: $e - 1$**

---

### d) $\int_{-1}^1 x^3\,dx$

**Methode:** $x^3$ ist eine ungerade Funktion (punktsymmetrisch zum Ursprung). Das Integral einer ungeraden Funktion über ein symmetrisches Intervall $[-a; a]$ ist stets $0$.

Rechnerisch: $F(x) = \dfrac{x^4}{4}$

$$\int_{-1}^1 x^3\,dx = \frac{1}{4} - \frac{1}{4} = 0$$

**Ergebnis: $0$**

---

## Aufgabe 4: Graphen zuordnen (3 Punkte)

**Zugrundeliegende Funktion:** $f(x) = \dfrac{x^2(4 - x)^2}{4}$

**Gegeben:**
- Graph A: Nach oben geöffnete Parabel mit Minimum bei $x = 2$.
- Graph B: Maximum bei $x = 2$ und Nullstellen bei $x = 0$ und $x = 4$.
- Graph C: Nullstellen bei $x = 0$, $x = 2$ und $x = 4$.

### Zuordnung:

| Graph | Funktion | Begründung |
|-------|----------|------------|
| **B** | **$f$** | $f$ hat ein Maximum bei $x = 2$ und Nullstellen bei $x = 0, 4$. |
| **C** | **$f'$** | $f'$ hat Nullstellen bei $x = 0, 2, 4$ — dort hat $f$ Extrema bzw. Nullstellen mit waagerechter Tangente. |
| **A** | **$f''$** | $f''$ ist eine nach oben geöffnete Parabel mit Minimum bei $x = 2$. |

**Ausführliche Begründung:**

**Graph B = $f$:** Die Funktion $f(x) = \dfrac{x^2(4-x)^2}{4}$ hat Nullstellen bei $x = 0$ und $x = 4$ und ein Maximum bei $x = 2$ mit $f(2) = 4$. Das passt zu Graph B.

**Graph C = $f'$:** Die Ableitung $f'(x) = x(4-x)(2-x)$ hat drei Nullstellen bei $x = 0$, $x = 2$ und $x = 4$. Bei $x = 2$ wechselt $f'$ das Vorzeichen von $+$ nach $-$ (VZW), was das Maximum von $f$ bei $x = 2$ bestätigt. Das passt zu Graph C.

**Graph A = $f''$:** Die zweite Ableitung $f''(x) = 3x^2 - 12x + 8$ ist eine nach oben geöffnete Parabel. Sie hat ihr Minimum bei $x = 2$ mit $f''(2) = 12 - 24 + 8 = -4 < 0$. Das negative Vorzeichen bestätigt: $f$ hat bei $x = 2$ ein Maximum (Rechtskrümmung). Die Nullstellen von $f''$ (bei $x \approx 0{,}85$ und $x \approx 3{,}15$) sind die Wendepunkte von $f$. Das passt zu Graph A.

**Kontrollregel:** Nullstellen von $f'$ = Extremstellen von $f$. Nullstellen von $f''$ = Wendepunkte von $f$.

---

## Aufgabe 5: Zusammenhang f und f' (3 Punkte)

**Gegeben:** $f'(x) > 0$ für $x < 1$, $f'(1) = 0$, $f'(x) < 0$ für $1 < x < 3$, $f'(3) = 0$, $f'(x) > 0$ für $x > 3$.

### a) „$f$ hat bei $x = 1$ ein lokales Maximum."

**Wahr.** ✓

Begründung: $f'$ wechselt bei $x = 1$ das Vorzeichen von $+$ nach $-$. Das bedeutet: $f$ steigt vor $x = 1$ und fällt nach $x = 1$. Also hat $f$ bei $x = 1$ ein lokales Maximum.

---

### b) „$f$ ist im Intervall $[0; 1]$ monoton fallend."

**Falsch.** ✗

Begründung: Für $x < 1$ gilt $f'(x) > 0$, also insbesondere auch für $x \in [0; 1)$. Da $f'$ dort positiv ist, ist $f$ im Intervall $[0; 1]$ **monoton steigend** (nicht fallend).

---

### c) „$f$ hat bei $x = 3$ ein lokales Minimum."

**Wahr.** ✓

Begründung: $f'$ wechselt bei $x = 3$ das Vorzeichen von $-$ nach $+$. Das bedeutet: $f$ fällt vor $x = 3$ und steigt nach $x = 3$. Also hat $f$ bei $x = 3$ ein lokales Minimum.

---

### d) „$f$ hat im Intervall $]1; 3[$ mindestens einen Wendepunkt."

**Wahr.** ✓

Begründung: $f'$ hat bei $x = 1$ den Wert $0$, ist dazwischen negativ und hat bei $x = 3$ wieder den Wert $0$. Also muss $f'$ im Intervall $]1; 3[$ (mindestens) ein lokales Minimum annehmen. An einem solchen Minimum wechselt $f'$ von fallend zu steigend, d.h. $f''$ wechselt dort das Vorzeichen (von negativ zu positiv) — $f$ hat dort einen Wendepunkt. (Achtung: **Wo genau** im Intervall der Wendepunkt liegt, lässt sich aus den Vorzeichen von $f'$ allein nicht bestimmen.)

*Allgemein: Ein Wendepunkt von $f$ liegt dort, wo $f'$ ein lokales Extremum hat (also $f''$ einen Vorzeichenwechsel).*

---

## Aufgabe 6: Tangentengleichung (3 Punkte)

**Gegeben:** $f(x) = x^3 - 2x + 1$, Punkt $P(1 \mid f(1))$.

**Methode:** Tangentengleichung: $t(x) = f(a) + f'(a) \cdot (x - a)$ mit $a = 1$.

**Schritt 1:** Funktionswert berechnen.

$$f(1) = 1^3 - 2 \cdot 1 + 1 = 1 - 2 + 1 = 0$$

Also $P(1 \mid 0)$.

**Schritt 2:** Ableitung bilden und Steigung berechnen.

$$f'(x) = 3x^2 - 2$$

$$f'(1) = 3 \cdot 1 - 2 = 1$$

**Schritt 3:** Tangentengleichung aufstellen.

$$t(x) = 0 + 1 \cdot (x - 1) = x - 1$$

**$t(x) = x - 1$**

---

## Aufgabe 7: Extrema bestimmen (4 Punkte)

**Gegeben:** $f(x) = x^3 - 6x^2 + 9x - 2$

### a) Extremstellen und deren Art

**Schritt 1:** Erste Ableitung.

$$f'(x) = 3x^2 - 12x + 9$$

**Schritt 2:** Notwendige Bedingung $f'(x) = 0$.

$$3x^2 - 12x + 9 = 0 \quad \big|\; \div 3$$

$$x^2 - 4x + 3 = 0$$

Mitternachtsformel oder Faktorisieren: $(x - 1)(x - 3) = 0$

**$x_1 = 1$,  $x_2 = 3$**

**Schritt 3:** Zweite Ableitung zur Klassifikation.

$$f''(x) = 6x - 12$$

$f''(1) = 6 - 12 = -6 < 0 \implies$ **Hochpunkt bei $x = 1$**

$f''(3) = 18 - 12 = 6 > 0 \implies$ **Tiefpunkt bei $x = 3$**

### b) Funktionswerte an den Extremstellen

$f(1) = 1 - 6 + 9 - 2 = \mathbf{2}$   →  Hochpunkt $H(1 \mid 2)$

$f(3) = 27 - 54 + 27 - 2 = \mathbf{-2}$   →  Tiefpunkt $T(3 \mid -2)$

---

## Aufgabe 8: Notwendige und hinreichende Bedingung (3 Punkte)

### a) Notwendige Bedingung für eine Extremstelle

Ist $x_0$ eine Extremstelle von $f$ und ist $f$ differenzierbar in $x_0$, so gilt:

**$f'(x_0) = 0$**

(Die Ableitung verschwindet an einer Extremstelle.)

---

### b) Hinreichende Bedingung (2. Ableitung)

Gilt $f'(x_0) = 0$ und $f''(x_0) \neq 0$, so hat $f$ bei $x_0$ ein Extremum:

- $f''(x_0) < 0 \implies$ lokales **Maximum** bei $x_0$
- $f''(x_0) > 0 \implies$ lokales **Minimum** bei $x_0$

---

### c) Gegenbeispiel

Die Aussage „$f'(2) = 0$, also hat $f$ bei $x = 2$ ein Extremum" ist **nicht zwingend richtig**, weil $f'(x_0) = 0$ nur eine **notwendige**, aber keine **hinreichende** Bedingung für ein Extremum ist.

**Gegenbeispiel:** $f(x) = (x - 2)^3$

- $f'(x) = 3(x - 2)^2$
- $f'(2) = 3 \cdot 0^2 = 0$  ✓  (notwendige Bedingung erfüllt)
- $f''(x) = 6(x - 2)$
- $f''(2) = 0$  (hinreichende Bedingung greift nicht)

Tatsächlich hat $f$ bei $x = 2$ **kein Extremum**, sondern einen **Sattelpunkt** (Wendepunkt mit waagerechter Tangente). Die Funktion steigt sowohl links als auch rechts von $x = 2$ (denn $f'(x) = 3(x - 2)^2 \geq 0$ für alle $x$) — es findet kein Vorzeichenwechsel von $f'$ statt.

---

## Aufgabe 9: Funktionswerte und Vorzeichen (2 Punkte)

**Gegeben:** $f(x) = -x^4 + 4x^2 - 3$

### a) Funktionswerte berechnen

$f(0) = -0 + 0 - 3 = \mathbf{-3}$

$f(1) = -1 + 4 - 3 = \mathbf{0}$

$f(-1) = -(-1)^4 + 4 \cdot (-1)^2 - 3 = -1 + 4 - 3 = \mathbf{0}$

---

### b) Vorzeichen von $f''(0)$

**Schritt 1:** Erste Ableitung.

$$f'(x) = -4x^3 + 8x$$

**Schritt 2:** Zweite Ableitung.

$$f''(x) = -12x^2 + 8$$

**Schritt 3:** Einsetzen.

$$f''(0) = -12 \cdot 0 + 8 = \mathbf{8 > 0}$$

**Interpretation:** Da $f''(0) > 0$, ist der Graph von $f$ an der Stelle $x = 0$ **linksgekrümmt** (konvex, „nach oben geöffnet"). Weil zusätzlich $f'(0) = 0$ gilt, liegt an der Stelle $x = 0$ ein lokales Minimum — der Graph hat dort eine Mulde. (Die Krümmung allein reicht als Begründung nicht — erst zusammen mit $f'(0) = 0$.)

---

## Aufgabe 10: Integral und Flächeninhalt (3 Punkte)

### a) $\int_0^2 (x^2 - 2x)\,dx$

$$F(x) = \frac{x^3}{3} - x^2$$

$$\int_0^2 (x^2 - 2x)\,dx = F(2) - F(0) = \left(\frac{8}{3} - 4\right) - (0 - 0) = \frac{8}{3} - \frac{12}{3} = \mathbf{-\frac{4}{3}}$$

---

### b) Skizze

$g(x) = x^2 - 2x = x(x - 2)$ hat Nullstellen bei $x = 0$ und $x = 2$. Der Scheitelpunkt liegt bei $x = 1$ mit $g(1) = 1 - 2 = -1$. Die Parabel ist im gesamten Intervall $[0; 2]$ **unterhalb der $x$-Achse**.

```
  y
  |
--+--------2---→ x
  |  \    /
  |   \  /
  |    \/
  |   (1|-1)
```

---

### c) Erklärung: Warum negativ?

Das Integral $\int_0^2 (x^2 - 2x)\,dx = -\tfrac{4}{3}$ ist **negativ**, weil $g(x) = x^2 - 2x$ im gesamten Intervall $[0; 2]$ unterhalb der $x$-Achse liegt ($g(x) \leq 0$).

Das bestimmte Integral misst den **orientierten Flächeninhalt**: Flächen unterhalb der $x$-Achse werden negativ gezählt.

Der tatsächliche **Flächeninhalt** (immer positiv) beträgt:

$$A = \left\lvert \int_0^2 (x^2 - 2x)\,dx \right\rvert = \left\lvert -\frac{4}{3} \right\rvert = \mathbf{\frac{4}{3}}\ \text{FE}$$

---

## Aufgabe 11: Monotonie und Krümmung (2 Punkte)

**Gegeben:** $f(x) = e^x \cdot (x - 1)$

### a) Ableitung bestimmen und vereinfachen

**Methode:** Produktregel mit $u = e^x$, $v = (x - 1)$, also $u' = e^x$, $v' = 1$.

$$f'(x) = e^x \cdot (x - 1) + e^x \cdot 1 = e^x \cdot (x - 1 + 1)$$

**$f'(x) = x \cdot e^x$**

---

### b) Für welche $x$ ist $f$ monoton steigend?

$f$ ist monoton steigend, wo $f'(x) > 0$, also wo $x \cdot e^x > 0$.

Da $e^x > 0$ für alle $x \in \mathbb{R}$, hängt das Vorzeichen nur von $x$ ab:

$$x \cdot e^x > 0 \iff x > 0$$

**$f$ ist monoton steigend für $x > 0$.**

(Für $x < 0$ ist $f$ monoton fallend; bei $x = 0$ hat $f$ ein lokales Minimum.)

---

## Aufgabe 12: Symmetrie und Grenzverhalten (2 Punkte)

**Gegeben:** $f(x) = x^4 - 2x^2$

### a) Achsensymmetrie zeigen

**Methode:** $f$ ist achsensymmetrisch zur $y$-Achse, wenn $f(-x) = f(x)$ für alle $x$.

$f(-x) = (-x)^4 - 2 \cdot (-x)^2 = x^4 - 2x^2 = f(x)$ ✓

Da $f(-x) = f(x)$, ist $f$ **achsensymmetrisch zur $y$-Achse**. $\blacksquare$

*Bemerkung: Dies war zu erwarten, da $f$ nur gerade Exponenten enthält.*

---

### b) Grenzverhalten für $x \to \pm\infty$

Der führende Term ist $x^4$ (höchste Potenz mit positivem Koeffizienten).

Für $x \to +\infty$:  $x^4 \to +\infty$, also **$f(x) \to +\infty$**

Für $x \to -\infty$:  $(-x)^4 = x^4 \to +\infty$, also **$f(x) \to +\infty$**

In beiden Richtungen strebt $f(x)$ gegen $+\infty$. Der Graph geht auf beiden Seiten „nach oben".

---

## Punkteübersicht

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Ableitungen (6 Teilaufgaben) | 6 |
| 2 | Stammfunktionen | 4 |
| 3 | Bestimmte Integrale | 4 |
| 4 | Graphen zuordnen | 3 |
| 5 | Zusammenhang f und f' | 3 |
| 6 | Tangentengleichung | 3 |
| 7 | Extrema bestimmen | 4 |
| 8 | Notw./hinr. Bedingung | 3 |
| 9 | Funktionswerte und Vorzeichen | 2 |
| 10 | Integral und Flächeninhalt | 3 |
| 11 | Monotonie | 2 |
| 12 | Symmetrie und Grenzverhalten | 2 |
| **Gesamt** | | **39** |

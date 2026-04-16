# Übungsaufgaben: Kettenregel im Abiturstil

> Ergänzung zu `16_kettenregel_verschachtelt.md`.
> Fünf Aufgaben im echten bayerischen Teil-A-Stil (hilfsmittelfrei, 2–5 BE).
> Gesamtumfang: **17 BE**, etwa 25–30 Minuten Bearbeitungszeit.

## Aufgaben

### Aufgabe 1 *(2 BE)*

Gegeben ist die in $\mathbb{R}$ definierte Funktion $f$ mit $f(x) = \ln(x^2 + 1)$.

**Zeigen Sie, dass $f'(x) = \dfrac{2x}{x^2 + 1}$ gilt.**

---

### Aufgabe 2 *(3 BE)*

Gegeben ist die in $\mathbb{R}$ definierte Funktion $g$ mit $g(x) = \sqrt{x^2 + 5}$.

**Bestimmen Sie $g'(x)$ und berechnen Sie den Wert $g'(2)$.**

---

### Aufgabe 3 *(4 BE)*

Gegeben ist die in $\mathbb{R}$ definierte Funktion $h$ mit $h(x) = x \cdot e^{-x^2}$.

**Weisen Sie nach, dass $h'(x) = (1 - 2x^2) \cdot e^{-x^2}$ gilt.**

---

### Aufgabe 4 *(3 BE)*

Gegeben ist die in $\mathbb{R}$ definierte Funktion $f$ mit $f(x) = e^{x^3 + 1}$.

**Begründen Sie, dass $f$ keine Extremstelle besitzt.**

---

### Aufgabe 5 *(5 BE)*

In einer pharmakologischen Studie wird die Konzentration eines Wirkstoffs im Blut näherungsweise durch die Funktion
$$k(t) = 120 \cdot e^{-0{,}4\,t}$$
beschrieben. Dabei ist $t \geq 0$ die Zeit in Stunden nach der Einnahme und $k(t)$ die Konzentration in mg pro Liter.

**a)** Zeigen Sie, dass $k'(t) = -0{,}4 \cdot k(t)$ gilt. *(2 BE)*

**b)** Deuten Sie das Ergebnis aus a) im Sachzusammenhang. *(3 BE)*

---

## Musterlösungen

### Lösung 1

**Operator „Zeigen Sie":** Ausgangsfunktion nehmen, Rechenweg bis zum vorgegebenen Term.

Muster 1 (Rezept 16): $\bigl[\ln(f(x))\bigr]' = \dfrac{f'(x)}{f(x)}$.

Mit $f(x) = x^2 + 1$ folgt $f'(x) = 2x$, also

$$f'(x) = \frac{2x}{x^2 + 1} \quad\checkmark$$

---

### Lösung 2

Muster 2: $\bigl[\sqrt{f(x)}\bigr]' = \dfrac{f'(x)}{2\sqrt{f(x)}}$.

Mit $f(x) = x^2 + 5$, $f'(x) = 2x$:

$$g'(x) = \frac{2x}{2\sqrt{x^2+5}} = \frac{x}{\sqrt{x^2+5}}$$

An der Stelle $x = 2$:

$$g'(2) = \frac{2}{\sqrt{9}} = \frac{2}{3}$$

---

### Lösung 3

**Operator „Weisen Sie nach":** Produktregel + Kettenregel sauber trennen.

Produktregel mit $u(x) = x$, $v(x) = e^{-x^2}$:
- $u'(x) = 1$
- $v'(x) = e^{-x^2} \cdot (-2x) = -2x \cdot e^{-x^2}$ *(Muster 3, Kettenregel)*

$$h'(x) = 1 \cdot e^{-x^2} + x \cdot (-2x) \cdot e^{-x^2} = e^{-x^2} - 2x^2 \cdot e^{-x^2}$$

$e^{-x^2}$ ausklammern:

$$h'(x) = (1 - 2x^2) \cdot e^{-x^2} \quad\checkmark$$

---

### Lösung 4

**Operator „Begründen Sie":** Argument in Worten, kurze Rechnung reicht.

Notwendige Bedingung für Extremstelle: $f'(x) = 0$.

Mit Muster 3: $f'(x) = e^{x^3 + 1} \cdot 3x^2$.

- $e^{x^3 + 1} > 0$ für alle $x \in \mathbb{R}$ (Exponentialfunktion immer positiv)
- $3x^2 \geq 0$, mit $3x^2 = 0$ nur bei $x = 0$

Also ist $f'(x) = 0$ genau für $x = 0$.

**Aber:** $3x^2$ wechselt bei $x = 0$ das Vorzeichen **nicht** (beidseitig positiv). Also liegt an $x = 0$ **kein** Vorzeichenwechsel von $f'$ vor → hinreichende Bedingung verletzt.

$\Rightarrow$ $f$ besitzt keine Extremstelle. $\checkmark$

---

### Lösung 5

**a)** Muster 3: $k'(t) = 120 \cdot e^{-0{,}4\,t} \cdot (-0{,}4) = -0{,}4 \cdot 120 \cdot e^{-0{,}4\,t} = -0{,}4 \cdot k(t) \quad\checkmark$

**b)** **Operator „Deuten Sie im Sachzusammenhang":** Mathematik in Alltagssprache übersetzen, mit Einheiten und Bezug zur Situation.

Die Gleichung $k'(t) = -0{,}4 \cdot k(t)$ besagt: Die momentane **Änderungsrate der Konzentration** ist zu jedem Zeitpunkt proportional zur **aktuellen Konzentration** selbst, mit Proportionalitätsfaktor $-0{,}4\,\mathrm{h^{-1}}$.

Das negative Vorzeichen bedeutet, dass die Konzentration **abnimmt**. Je höher die aktuelle Konzentration, desto schneller der Abbau — pro Stunde verringert sich die Konzentration um $40\,\%$ ihres momentanen Werts. Das ist das typische Verhalten eines **exponentiellen Zerfalls**.

## Hinweise zur Bewertung

- **Aufgabe 1, 3, 5a („Zeigen/Nachweisen"):** vollständige Herleitung nötig; Endergebnis ohne Rechenweg = 0 BE.
- **Aufgabe 2 („Bestimmen/Berechnen"):** sowohl Term als auch Zahlenwert angeben; Einheiten (falls im Sachkontext) nicht vergessen.
- **Aufgabe 4 („Begründen"):** Argument in Worten, kurze Rechnung ok; der entscheidende Satz ist der VZW-Hinweis.
- **Aufgabe 5b („Deuten"):** Antwortsatz im Sachkontext; reine Wiederholung der Formel reicht **nicht**.

# Musterlösung: Abitur 2025 — Analysis, Teil B, Aufgabengruppe 1, Aufgabe 1c

## Aufgabe
Gegeben: $f(x) = 0{,}25 \cdot (x + 6) \cdot \sqrt{6 - x}$, definiert für $x \in \mathopen{]}-\infty; 6\mathclose{]}$, relevant: $-5 \leq x \leq 6$.

**Weisen Sie nach, dass $\frac{6 - 3x}{8 \cdot \sqrt{6 - x}}$ ein Term der ersten Ableitungsfunktion $f'$ von $f$ ist. Ermitteln Sie den linksseitigen Grenzwert $\lim_{x \to 6^-} f'(x)$ und deuten Sie das Ergebnis im Sachzusammenhang.**

(Sachkontext: Flugbahn eines Badminton-Federballs, $x$ in Metern, $f(x)$ = Höhe)

## Lösung

### Schritt 1: Ableitung nachweisen (Produktregel)

$$f(x) = 0{,}25 \cdot (x + 6) \cdot \sqrt{6 - x}$$

Wir setzen: $u(x) = x + 6$ und $v(x) = \sqrt{6 - x} = (6 - x)^{1/2}$

**Ableitungen:**
- $u'(x) = 1$
- $v'(x) = \frac{1}{2} \cdot (6 - x)^{-1/2} \cdot (-1) = -\frac{1}{2\sqrt{6 - x}}$   ← Kettenregel!

**Produktregel:** $f'(x) = 0{,}25 \cdot [u' \cdot v + u \cdot v']$

$$f'(x) = 0{,}25 \cdot \left[1 \cdot \sqrt{6 - x} + (x + 6) \cdot \left(-\frac{1}{2\sqrt{6 - x}}\right)\right]$$

$$f'(x) = 0{,}25 \cdot \left[\sqrt{6 - x} - \frac{x + 6}{2\sqrt{6 - x}}\right]$$

**Auf Hauptnenner $2\sqrt{6 - x}$ bringen:**

$$f'(x) = 0{,}25 \cdot \left[\frac{2(6 - x)}{2\sqrt{6 - x}} - \frac{x + 6}{2\sqrt{6 - x}}\right]$$

$$f'(x) = 0{,}25 \cdot \frac{12 - 2x - x - 6}{2\sqrt{6 - x}}$$

$$f'(x) = 0{,}25 \cdot \frac{6 - 3x}{2\sqrt{6 - x}}$$

**$f'(x) = \dfrac{6 - 3x}{8\sqrt{6 - x}}$** ✓

---

### Schritt 2: Grenzwert berechnen

$$\lim_{x \to 6^-} f'(x) = \lim_{x \to 6^-} \frac{6 - 3x}{8\sqrt{6 - x}}$$

Für $x \to 6^-$:
- Zähler: $6 - 3 \cdot 6 = 6 - 18 = \mathbf{-12}$ (fester negativer Wert)
- Nenner: $8 \cdot \sqrt{6 - 6} = 8 \cdot \sqrt{0} = \mathbf{0^+}$ (wird beliebig klein, aber positiv)

$$\to \lim_{x \to 6^-} f'(x) = -\infty$$

---

### Schritt 3: Deutung im Sachkontext

Der Federball hat an der Stelle $x = 6$ eine **beliebig steil abfallende Flugbahn**. Das bedeutet: Der Federball trifft (nahezu) **senkrecht** auf dem Boden auf.

---

## Was hier schwierig ist — und worauf man achten muss
1. **„Nachweisen"** = Man muss den gegebenen Term durch eigene Rechnung herleiten, nicht einfach bestätigen
2. **Produktregel + Kettenregel gleichzeitig**: $v(x) = \sqrt{6-x}$ braucht die Kettenregel (innere Ableitung $-1$)
3. **Hauptnenner bilden**: Der algebraische Umformungsschritt ist der fehleranfälligste Teil
4. **Grenzwert $-\infty$**: Zähler ist $-12$ (nicht $0$!), Nenner geht gegen $0$ → Bruch divergiert
5. **Sachkontext**: „Steigung $\to -\infty$" muss übersetzt werden in „trifft senkrecht auf"

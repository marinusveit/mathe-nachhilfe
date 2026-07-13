# Aufgaben — Termumformung in der Analysis (Drill)

> Zusätzliches Übungsmaterial zu [Rezept 17: Termumformung in der Analysis](../rezepte/17_termumformung_analysis.md).
> Gedacht als **5-Minuten-Warm-up** vor der eigentlichen Sitzung — jede Teilrunde deckt ein Muster ab, sodass über mehrere Sitzungen hinweg variiert werden kann.

**Nutzung:** Pro Sitzung 3–5 Aufgaben. Ohne Taschenrechner. Ziel: Muster automatisieren, sodass die Umformung bei Abituraufgaben „von selbst" läuft.

---

## Teil 1 — Negative Exponenten $\to$ Bruchform

> Aus der Potenzschreibweise (wie sie nach der Potenzregel entsteht) zurück in die Bruchdarstellung.

1. $4 x^{-2}$
2. $-3 x^{-4}$
3. $\tfrac{1}{2} x^{-1/2}$
4. $-\tfrac{3}{2} x^{-5/2}$
5. $5 (2x+1)^{-1}$
6. $-2 (3x-5)^{-2}$
7. $\tfrac{1}{3} (x^2+4)^{-1/2}$
8. $-(x-1)^{-3}$

---

## Teil 2 — Bruchform $\to$ Potenzschreibweise

> Vor dem Ableiten: Bruch und Wurzel in Potenzform bringen, damit die Potenzregel anwendbar ist.

1. $\dfrac{1}{x^3}$
2. $\dfrac{5}{x^4}$
3. $\dfrac{1}{\sqrt{x}}$
4. $\dfrac{2}{\sqrt[3]{x}}$
5. $\dfrac{3}{x^2\sqrt{x}}$ *(Hinweis: $x^2 \cdot x^{1/2} = x^{5/2}$)*
6. $\dfrac{1}{(2x-1)^2}$
7. $\dfrac{4}{\sqrt{3x+2}}$

---

## Teil 3 — Brüche mit gleichem Nenner zusammenfassen

> Nur der Zähler wird addiert/subtrahiert, der Nenner bleibt. Klammern bei Subtraktion!

1. $\dfrac{2x+1}{3} + \dfrac{x-4}{3}$
2. $\dfrac{x^2+2}{x} - \dfrac{x^2-3}{x}$
3. $\dfrac{3x+1}{2\sqrt{x}} - \dfrac{x-5}{2\sqrt{x}}$
4. $\dfrac{2(x+1)}{x^2-1} + \dfrac{x-3}{x^2-1}$

---

## Teil 4 — Hauptnenner bilden

> Wenn die Nenner verschieden sind: kleineren Nenner erweitern, bis beide gleich sind.

1. $\dfrac{1}{x} + \dfrac{2}{x^2}$
2. $\dfrac{3}{x^2} - \dfrac{1}{x^3}$
3. $x + \dfrac{1}{x}$
4. $\dfrac{x}{x+1} + \dfrac{1}{(x+1)^2}$
5. $\dfrac{1}{2x} + \dfrac{1}{x^2}$ *(Hauptnenner $2x^2$)*

---

## Teil 5 — Wurzel im Nenner

> Im Abitur meist **stehen lassen**, nur rationalisieren, wenn es zum Vereinfachen beiträgt.

**In Bruchform bringen (mit Wurzel im Nenner):**

1. $\tfrac{1}{2} x^{-1/2}$
2. $-\tfrac{1}{2}(4-x)^{-1/2}$
3. $\tfrac{3}{2}(2x-1)^{-1/2}$

**Rationalisieren (Wurzel aus dem Nenner entfernen):**

4. $\dfrac{1}{\sqrt{x}}$
5. $\dfrac{3}{\sqrt{x-2}}$
6. $\dfrac{2x}{\sqrt{x^2+1}}$

---

## Teil 6 — Doppelbrüche auflösen

> „Bruch im Nenner $\to$ multiplizieren mit Kehrwert."

**1.**

$$\cfrac{\;\dfrac{1}{x}\;}{2}$$

**2.**

$$\cfrac{3}{\;\dfrac{1}{x}\;}$$

**3.**

$$\cfrac{\;\dfrac{2}{x+1}\;}{x}$$

**4.**

$$\cfrac{x}{\;\dfrac{1}{x-1}\;}$$

**5.**

$$\cfrac{\;\dfrac{1}{\sqrt{x}}\;}{\sqrt{x}}$$

---

## Teil 7 — Analysis-typische Endformen

> „Ableitung zu Ende geführt": kombiniert mehrere Muster auf einmal. Dieser Teil ist der wichtigste für „Zeigen Sie"-Aufgaben.

1. Bringe $\sqrt{x} + \dfrac{1}{2\sqrt{x}}$ auf einen Bruch mit Nenner $2\sqrt{x}$.
2. Bringe $2\sqrt{x+3} - \dfrac{x}{\sqrt{x+3}}$ auf einen Bruch mit Nenner $\sqrt{x+3}$.
3. Bringe $\dfrac{1}{2\sqrt{4-x}} \cdot (-1) + \dfrac{1}{2\sqrt{4-x}}$ auf einfachste Form.
4. Fasse zusammen: $\sqrt{9-x} - \dfrac{x+9}{2\sqrt{9-x}}$ *(analog zu Abitur 2025 B1 1c).*
5. Vereinfache $\dfrac{2x \cdot x^2 - (x^2+1) \cdot 2x}{x^4}$ *(Quotientenregel-Output).*
6. Fasse zusammen zu einem Bruch: $\mathrm{e}^x \cdot x + \mathrm{e}^x$.
7. Vereinfache $\dfrac{(2x) \cdot \mathrm{e}^{x^2} - x^2 \cdot 2x \cdot \mathrm{e}^{x^2}}{\mathrm{e}^{2x^2}}$ *(klammern + kürzen).*
8. **Abi-Abschlussaufgabe:** Gegeben ist $f(x) = (x+3)\sqrt{5-x}$ für $x \leq 5$. Leite ab und fasse $f'(x)$ zu **einem** Bruch mit Nenner $2\sqrt{5-x}$ zusammen. *(Produktregel + Kettenregel + Hauptnenner — genau der Aufgabentyp aus 2025 B1 1c.)*

---

## Lösungen

### Teil 1
1. $\dfrac{4}{x^2}$
2. $-\dfrac{3}{x^4}$
3. $\dfrac{1}{2\sqrt{x}}$
4. $-\dfrac{3}{2 x^{5/2}} = -\dfrac{3}{2 x^2 \sqrt{x}}$
5. $\dfrac{5}{2x+1}$
6. $-\dfrac{2}{(3x-5)^2}$
7. $\dfrac{1}{3\sqrt{x^2+4}}$
8. $-\dfrac{1}{(x-1)^3}$

### Teil 2
1. $x^{-3}$
2. $5 x^{-4}$
3. $x^{-1/2}$
4. $2 x^{-1/3}$
5. $3 x^{-5/2}$
6. $(2x-1)^{-2}$
7. $4 (3x+2)^{-1/2}$

### Teil 3
1. $\dfrac{3x-3}{3} = x - 1$
2. $\dfrac{5}{x}$
3. $\dfrac{2x+6}{2\sqrt{x}} = \dfrac{x+3}{\sqrt{x}}$
4. $\dfrac{3x-1}{x^2-1}$

### Teil 4
1. $\dfrac{x+2}{x^2}$ *(Hauptnenner $x^2$)*
2. $\dfrac{3x-1}{x^3}$
3. $\dfrac{x^2+1}{x}$
4. $\dfrac{x(x+1) + 1}{(x+1)^2} = \dfrac{x^2+x+1}{(x+1)^2}$
5. $\dfrac{x+2}{2x^2}$

### Teil 5
1. $\dfrac{1}{2\sqrt{x}}$
2. $-\dfrac{1}{2\sqrt{4-x}}$
3. $\dfrac{3}{2\sqrt{2x-1}}$
4. $\dfrac{\sqrt{x}}{x}$
5. $\dfrac{3\sqrt{x-2}}{x-2}$
6. $\dfrac{2x\sqrt{x^2+1}}{x^2+1}$

### Teil 6
1. $\dfrac{1}{2x}$
2. $3x$
3. $\dfrac{2}{x(x+1)}$
4. $x(x-1) = x^2 - x$
5. $\dfrac{1}{x}$

### Teil 7
1. $\sqrt{x} = \dfrac{2x}{2\sqrt{x}}$, also $\dfrac{2x+1}{2\sqrt{x}}$.
2. $2\sqrt{x+3} = \dfrac{2(x+3)}{\sqrt{x+3}}$, also $\dfrac{2(x+3) - x}{\sqrt{x+3}} = \dfrac{x+6}{\sqrt{x+3}}$.
3. $\dfrac{-1+1}{2\sqrt{4-x}} = 0$.
4. $\sqrt{9-x} = \dfrac{2(9-x)}{2\sqrt{9-x}}$, also $\dfrac{2(9-x) - (x+9)}{2\sqrt{9-x}} = \dfrac{18-2x-x-9}{2\sqrt{9-x}} = \dfrac{9-3x}{2\sqrt{9-x}}$.
5. $\dfrac{2x \cdot (x^2 - (x^2+1))}{x^4} = \dfrac{2x \cdot (-1)}{x^4} = -\dfrac{2}{x^3}$.
6. $\mathrm{e}^x(x+1)$ — das ist bereits „ein Term"; falls als Bruch gewünscht: $\dfrac{\mathrm{e}^x(x+1)}{1}$.
7. Zähler ausklammern: $2x \cdot \mathrm{e}^{x^2}(1 - x^2)$. Kürzen mit $\mathrm{e}^{x^2}$ im Nenner ($\mathrm{e}^{2x^2} = \mathrm{e}^{x^2} \cdot \mathrm{e}^{x^2}$): $\dfrac{2x(1-x^2)}{\mathrm{e}^{x^2}}$.
8. Produktregel mit $u = x+3$, $v = \sqrt{5-x}$. Ableitung von $v$ per Kettenregel: $v' = \dfrac{-1}{2\sqrt{5-x}}$. Damit:

    $$f'(x) = 1 \cdot \sqrt{5-x} + (x+3) \cdot \frac{-1}{2\sqrt{5-x}} = \sqrt{5-x} - \frac{x+3}{2\sqrt{5-x}}$$

    Hauptnenner $2\sqrt{5-x}$; dabei $\sqrt{5-x} = \dfrac{2(5-x)}{2\sqrt{5-x}}$:

    $$f'(x) = \frac{2(5-x) - (x+3)}{2\sqrt{5-x}} = \frac{10 - 2x - x - 3}{2\sqrt{5-x}} = \frac{7 - 3x}{2\sqrt{5-x}}$$

---

## Hinweise für den Unterricht

- **Teile 1–2** sind reine Schreibweisen-Übung — sollten nach einigen Durchgängen automatisch laufen.
- **Teil 7** ist der anspruchsvollste Abschnitt und spiegelt echte Abiturschritte wider (z.B. 2025 B1 1c). Hier hängt es sich am häufigsten auf: **bei „Zeigen Sie"-Aufgaben zählt die exakte Form**.
- **Nicht alle auf einmal** — 3–5 Aufgaben aus einem oder zwei Teilen pro Sitzung reichen. Wechseln, sobald ein Muster sitzt.
- Wenn ein Muster systematisch hakt, zurück ins [Rezept 17: Termumformung in der Analysis](../rezepte/17_termumformung_analysis.md) springen und gemeinsam die Regel nachlesen.

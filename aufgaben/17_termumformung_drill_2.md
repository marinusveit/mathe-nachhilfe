# Aufgaben — Termumformung Mix (Drill 2)

> Zusätzliches Übungsmaterial zu [Rezept 17: Termumformung in der Analysis](../rezepte/17_termumformung_analysis.md).
> Anders als [Drill 1](17_termumformung_drill.md) sind die Aufgaben hier **gemischt** — jede kombiniert mindestens zwei Muster (negativer Exponent $\to$ Kehrbruch, Hauptnenner, Doppelbruch).

**Nutzung:** 5-Minuten-Warm-up, ohne Taschenrechner. Ziel: zwei Schritte hintereinander automatisieren („erst Kehrbruch, dann Hauptnenner").

---

## Aufgaben

1. Schreibe als einen Bruch ohne negative Exponenten:

    $$3x^{-2} + 2x^{-3}$$

2. Fasse zu einem Bruch zusammen:

    $$4(2x+1)^{-1} - 2(2x+1)^{-2}$$

3. Bringe auf einen Bruch (Hauptnenner $2x\sqrt{x}$):

    $$\tfrac{1}{2} x^{-1/2} - \tfrac{1}{2} x^{-3/2}$$

4. Schreibe als einen Bruch:

    $$x^{-1} + x^{-2} + x^{-3}$$

5. *(Quotientenregel-Output)* Vereinfache:

    $$\dfrac{2x(x^2+1) - (x^2-1) \cdot 2x}{(x^2+1)^2}$$

6. *(Produkt- + Kettenregel-Output)* Bringe auf einen Bruch:

    $$2x \sqrt{x^2+4} + \dfrac{x^3}{\sqrt{x^2+4}}$$

7. *(Doppelbruch + Hauptnenner)* Vereinfache zu einem Bruch:

    $$\dfrac{\sqrt{x+1} - \dfrac{x}{2\sqrt{x+1}}}{x+1}$$

8. **Abitur-Stil:** Gegeben ist $f(x) = (2x-1)\sqrt{x+2}$ für $x \geq -2$. Leite ab und fasse $f'(x)$ zu **einem** Bruch mit Nenner $2\sqrt{x+2}$ zusammen. *(Produktregel + Kettenregel + Hauptnenner.)*

---

## Lösungen

1. Erst Kehrbruch: $\dfrac{3}{x^2} + \dfrac{2}{x^3}$. Hauptnenner $x^3$ (also $\dfrac{3}{x^2} = \dfrac{3x}{x^3}$):

    $$\dfrac{3x + 2}{x^3}$$

2. Erst Kehrbruch: $\dfrac{4}{2x+1} - \dfrac{2}{(2x+1)^2}$. Hauptnenner $(2x+1)^2$:

    $$\dfrac{4(2x+1) - 2}{(2x+1)^2} = \dfrac{8x + 2}{(2x+1)^2} = \dfrac{2(4x+1)}{(2x+1)^2}$$

3. Erst Kehrbruch: $\dfrac{1}{2\sqrt{x}} - \dfrac{1}{2x\sqrt{x}}$ (denn $x^{3/2} = x \cdot \sqrt{x}$). Hauptnenner $2x\sqrt{x}$:

    $$\dfrac{x - 1}{2x\sqrt{x}}$$

4. Erst Kehrbruch: $\dfrac{1}{x} + \dfrac{1}{x^2} + \dfrac{1}{x^3}$. Hauptnenner $x^3$:

    $$\dfrac{x^2 + x + 1}{x^3}$$

5. Im Zähler $2x$ ausklammern: $2x \cdot \big[(x^2+1) - (x^2-1)\big] = 2x \cdot 2 = 4x$. Damit:

    $$\dfrac{4x}{(x^2+1)^2}$$

6. Hauptnenner $\sqrt{x^2+4}$; dabei $2x\sqrt{x^2+4} = \dfrac{2x(x^2+4)}{\sqrt{x^2+4}}$:

    $$\dfrac{2x(x^2+4) + x^3}{\sqrt{x^2+4}} = \dfrac{3x^3 + 8x}{\sqrt{x^2+4}} = \dfrac{x(3x^2 + 8)}{\sqrt{x^2+4}}$$

7. Erst den Zähler auf einen Bruch bringen (Hauptnenner $2\sqrt{x+1}$):

    $$\sqrt{x+1} - \dfrac{x}{2\sqrt{x+1}} = \dfrac{2(x+1) - x}{2\sqrt{x+1}} = \dfrac{x+2}{2\sqrt{x+1}}$$

    Doppelbruch auflösen (Division durch $x+1$ = Multiplikation mit $\tfrac{1}{x+1}$):

    $$\dfrac{x+2}{2(x+1)\sqrt{x+1}}$$

8. Produktregel mit $u = 2x-1$, $v = \sqrt{x+2}$. Ableitung von $v$ per Kettenregel: $v' = \dfrac{1}{2\sqrt{x+2}}$. Damit:

    $$f'(x) = 2 \cdot \sqrt{x+2} + (2x-1) \cdot \dfrac{1}{2\sqrt{x+2}}$$

    Hauptnenner $2\sqrt{x+2}$; dabei $2\sqrt{x+2} = \dfrac{4(x+2)}{2\sqrt{x+2}}$:

    $$f'(x) = \dfrac{4(x+2) + (2x-1)}{2\sqrt{x+2}} = \dfrac{4x + 8 + 2x - 1}{2\sqrt{x+2}} = \dfrac{6x + 7}{2\sqrt{x+2}}$$

---

## Hinweise für den Unterricht

- Aufgaben 1–4 trainieren den Reflex **„erst Kehrbruch, dann Hauptnenner"**. Wenn das hakt, kurz zurück in [Rezept 17](../rezepte/17_termumformung_analysis.md), Abschnitt zu negativen Exponenten.
- Aufgaben 5–6 imitieren typische Quotienten-/Produktregel-Ausgaben — der Schritt, an dem Schüler:innen oft aufhören, obwohl die eigentliche Vereinfachung noch fehlt.
- Aufgabe 7 ist die Vorstufe zu Aufgabe 8: erst den Zähler ordnen, dann den Doppelbruch.
- Aufgabe 8 ist die **Abi-Endform** (vergleichbar zu 2025 B1 1c). Wenn diese sitzt, ist das Muster im Griff.

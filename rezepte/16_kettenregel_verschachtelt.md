# Rezept: Verschachtelte Kettenregel — der Abitur-Klassiker

> Die Kettenregel $[f(g(x))]' = f'(g(x)) \cdot g'(x)$ in typischen Abitur-Kombinationen: verschachtelt mit $\ln$, $\sqrt{\,}$, $e^{\cdot}$ und der Produktregel.

## Warum dieses Rezept?

In drei der vier letzten Problem-Aufgaben (2022 A2 3b, 2025 B1 1c, 2025 A2 2b) taucht die Kettenregel **nicht isoliert** auf, sondern in Kombinationen:
- $\ln(f(x))$, $\sqrt{f(x)}$, $e^{f(x)}$
- Produktregel + Kettenregel gleichzeitig
- Doppelte Verkettung $f(g(h(x)))$

Die Kettenregel an sich ist leicht — der Stolperstein ist, sie **zu erkennen** und **sauber mit anderen Regeln zu kombinieren**.

## Grundformel

$$\bigl[f(g(x))\bigr]' = f'(g(x)) \cdot g'(x)$$

**Merkspruch:** „Äußere Ableitung mal innere Ableitung."
- **Äußere Ableitung:** $f'$ eingesetzt an der Stelle $g(x)$ — die innere Funktion bleibt stehen!
- **Innere Ableitung:** $g'(x)$

## Die drei häufigsten Abitur-Muster

### Muster 1: $\ln(f(x))$

$$\bigl[\ln(f(x))\bigr]' = \frac{f'(x)}{f(x)}$$

**Herleitung:** äußere Funktion $\ln(u)$, Ableitung $1/u$; innere Funktion $f(x)$.
$\Rightarrow$ $\dfrac{1}{f(x)} \cdot f'(x) = \dfrac{f'(x)}{f(x)}$

**Typischer Fehler:** Nur $\dfrac{1}{f(x)}$ schreiben, $f'(x)$ vergessen.

**Beispiel:** $g(x) = \ln(x^2 + 1)$
$$g'(x) = \frac{2x}{x^2 + 1}$$

### Muster 2: $\sqrt{f(x)}$

$$\bigl[\sqrt{f(x)}\bigr]' = \frac{f'(x)}{2\sqrt{f(x)}}$$

**Herleitung:** $\sqrt{u} = u^{1/2}$, Ableitung $\tfrac{1}{2}u^{-1/2} = \tfrac{1}{2\sqrt{u}}$; innere Ableitung $f'(x)$.

**Beispiel:** $g(x) = \sqrt{6 - x}$
$$g'(x) = \frac{-1}{2\sqrt{6-x}}$$

**Achtung:** innere Ableitung von $6-x$ ist $-1$, nicht $1$!

### Muster 3: $e^{f(x)}$

$$\bigl[e^{f(x)}\bigr]' = e^{f(x)} \cdot f'(x)$$

**Merkmal:** Die $e$-Funktion reproduziert sich — der ganze Term $e^{f(x)}$ bleibt, multipliziert mit $f'(x)$.

**Beispiel:** $g(x) = e^{-2x}$
$$g'(x) = e^{-2x} \cdot (-2) = -2e^{-2x}$$

## Kombination mit der Produktregel

**Aufbau:** $h(x) = u(x) \cdot v(x)$, wobei mindestens einer der Faktoren eine Verkettung ist.

**Vorgehen (wie in Abitur 2025 B1 1c):**
1. Setze $u(x)$ und $v(x)$ fest.
2. Leite $u'$ und $v'$ ab — bei der Verkettung **Kettenregel einsetzen**!
3. Produktregel: $h' = u' \cdot v + u \cdot v'$
4. Auf gemeinsamen Nenner bringen, Zähler vereinfachen.

**Beispiel:** $f(x) = 0{,}25 \cdot (x+6) \cdot \sqrt{6-x}$

$u(x) = x+6$, $\;v(x) = \sqrt{6-x}$
$u'(x) = 1$, $\;v'(x) = \dfrac{-1}{2\sqrt{6-x}}$ (Kettenregel!)

$$f'(x) = 0{,}25 \cdot \left[\sqrt{6-x} \;-\; \frac{x+6}{2\sqrt{6-x}}\right]$$

Hauptnenner $2\sqrt{6-x}$:

$$f'(x) = 0{,}25 \cdot \frac{2(6-x) - (x+6)}{2\sqrt{6-x}} = 0{,}25 \cdot \frac{6 - 3x}{2\sqrt{6-x}} = \frac{6-3x}{8\sqrt{6-x}}$$

## Doppelte Kettenregel: $f(g(h(x)))$

$$\bigl[f(g(h(x)))\bigr]' = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x)$$

**Drei Ableitungen multipliziert!** Häufig bei Graphentransformationen wie $h(x) = g(2x) - 1$ für die zweite Ableitung.

**Beispiel:** $g(x) = \ln\!\bigl(\sqrt{x^2 + 1}\bigr)$

- Äußerste: $\ln(u)$ → $\tfrac{1}{u}$ eingesetzt $= \dfrac{1}{\sqrt{x^2+1}}$
- Mitte: $\sqrt{v}$ → $\dfrac{1}{2\sqrt{v}}$ eingesetzt $= \dfrac{1}{2\sqrt{x^2+1}}$
- Innen: $(x^2+1)' = 2x$

$$g'(x) = \frac{1}{\sqrt{x^2+1}} \cdot \frac{1}{2\sqrt{x^2+1}} \cdot 2x = \frac{x}{x^2 + 1}$$

*(Schönes Ergebnis — weil $\ln\sqrt{v} = \tfrac{1}{2}\ln v$.)*

## Drill: Selbst ableiten

Jeweils $f'(x)$ bestimmen. Lösungen unten.

**Level 1 — Grundmuster:**
1. $f(x) = \ln(3x - 5)$
2. $f(x) = \sqrt{x^2 + 4}$
3. $f(x) = e^{x^2}$
4. $f(x) = (2x - 7)^4$

**Level 2 — Produktregel + Kettenregel:**
5. $f(x) = x \cdot e^{-x}$
6. $f(x) = x^2 \cdot \ln(x)$
7. $f(x) = (x+1) \cdot \sqrt{x-2}$

**Level 3 — Doppelte Verkettung:**
8. $f(x) = \sqrt{\ln(x)}$
9. $f(x) = e^{\sqrt{x}}$
10. $f(x) = \ln\!\bigl(e^{2x} + 1\bigr)$

---

### Lösungen

1. $\dfrac{3}{3x-5}$
2. $\dfrac{x}{\sqrt{x^2+4}}$
3. $2x \cdot e^{x^2}$
4. $8(2x-7)^3$
5. $e^{-x} - x\cdot e^{-x} = (1-x)\,e^{-x}$
6. $2x\ln(x) + x$
7. $\sqrt{x-2} + \dfrac{x+1}{2\sqrt{x-2}} = \dfrac{3x-3}{2\sqrt{x-2}} = \dfrac{3(x-1)}{2\sqrt{x-2}}$
8. $\dfrac{1}{2x\sqrt{\ln(x)}}$
9. $\dfrac{e^{\sqrt{x}}}{2\sqrt{x}}$
10. $\dfrac{2e^{2x}}{e^{2x} + 1}$

## Typische Fehler

1. **Innere Ableitung vergessen** — besonders bei $e^{f(x)}$ („Ich hab doch $e^x$ abgeleitet, fertig.") Nein: $\cdot f'(x)$!
2. **Innere Ableitung falsch** — bei $\sqrt{6-x}$ ist sie $-1$, nicht $+1$.
3. **$\ln$-Ableitung halb** — $[\ln(f)]' = f'/f$, nicht nur $1/f$.
4. **Produkt- und Kettenregel vermischt** — erst Produktregel-Struktur $u'v + uv'$ aufschreiben, **dann** innerhalb von $v'$ die Kettenregel anwenden.
5. **Ergebnis nicht vereinfachen** — bei „Zeigen Sie"-Aufgaben muss die vorgegebene Form dastehen; Hauptnenner bilden, kürzen.

## Siehe auch

- [Rezept 05: Verkettung und Definitionsbereich](05_verkettung_definitionsbereich.md) — dieselben Muster als Spezialfall-Tabelle, plus Definitionsbereich
- [Rezept 17: Termumformung in der Analysis](17_termumformung_analysis.md) — Hauptnenner-Technik für den Vereinfachungsschritt
- [Rezept 16b: Kettenregel im Abiturstil](16b_kettenregel_abituraufgaben.md) — Übungsaufgaben mit BE und Musterlösungen

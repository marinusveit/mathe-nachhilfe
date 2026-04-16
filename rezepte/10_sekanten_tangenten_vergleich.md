# Rezept: Sekanten- und Tangentensteigungen vergleichen

> Wenn eine Gerade einen Graphen in zwei (oder mehr) Punkten schneidet oder berührt: welche Steigungen sind möglich? Zentrale Idee: Tangente ist Grenzlage der Sekante.

### 🔗 Interaktiv in Desmos

**[Desmos-Graph öffnen](https://www.desmos.com/calculator/b03srzmsmm)** — Slider für $q$ bewegen und beobachten, wie sich die Sekante durch $P(3 \mid 1)$ und $Q(q \mid f(q))$ dreht.

## Typische Aufgabenstellung
> „Geben Sie alle möglichen Steigungen einer Geraden an, die den Graphen in $P$ und einem weiteren Punkt schneidet."
> „Für welche Steigung $m$ hat die Gerade $y = mx + b$ genau zwei Schnittpunkte mit dem Graphen?"

## Schritt-für-Schritt

1. **Sekantensteigung aufstellen**: Gerade durch $P(p \mid f(p))$ und $Q(q \mid f(q))$
   $$m(q) = \frac{f(q) - f(p)}{q - p}$$
2. **Grenzfälle untersuchen**:
   - $q \to p$: Sekantensteigung $\to$ Tangentensteigung $f'(p)$
   - $q \to \infty$ oder $q \to$ Randwert: Sekantensteigung $\to$ Grenzwert bestimmen
3. **Monotonie von $m(q)$** prüfen: Ist die Sekantensteigung steigend/fallend in $q$?
4. **Wertebereich von $m$** angeben: alle erreichbaren Steigungen
5. **Tangente ausschließen**: Wenn Tangente den Graphen nur in $P$ berührt → diese Steigung ist Grenzwert, wird aber nicht angenommen

## Beispiel (Abitur 2025 A2 4b)

$f(x) = \sqrt{x-2}$, $P(3 \mid 1)$, Tangentensteigung $m_T = \tfrac{1}{2}$.

- Sekantensteigung: $m(q) = \dfrac{\sqrt{q-2} - 1}{q - 3}$ für $q \in [2;\,\infty[\,\setminus\,\{3\}$
- $q \to 2$: $m \to \dfrac{0-1}{2-3} = 1$
- $q \to \infty$: $m \to 0$ (Zähler wächst wie $\sqrt{q}$, Nenner wie $q$)
- $q \to 3$: $m \to f'(3) = \tfrac{1}{2}$
- Steigung $m_T = \tfrac{1}{2}$ nur als Grenzwert → nicht angenommen
- Mögliche Steigungen: $m \in \mathopen{]}0;\,\tfrac{1}{2}\mathclose{[} \;\cup\; \mathopen{]}\tfrac{1}{2};\,1\mathclose{]}$

## Häufige Fehler
- Grenzwert als erreichbaren Wert annehmen (offenes vs. geschlossenes Intervall)
- Fallunterscheidung vergessen: zweiter Punkt links vs. rechts von $P$
- Tangentensteigung nicht erkannt als Grenzfall

# Musterlösung: Abitur 2025 — Analysis, Teil A, Aufgabengruppe 2, Aufgabe 4

## Aufgabe
Gegeben: $g\colon x \mapsto \sqrt{x - 2}$, $x \in [2; \infty[$. Punkt $P(3|1)$ liegt auf $G_g$. Die Tangente an $G_g$ in $P$ hat die Gleichung $y = \frac{1}{2}x - \frac{1}{2}$ und hat mit $G_g$ nur den Punkt $P$ gemeinsam.

**a)** Zeichnen Sie die Tangente in Abbildung 2 ein.

**b)** Betrachtet wird eine Gerade, die mit $G_g$ sowohl den Punkt $P$ als auch einen weiteren Punkt gemeinsam hat. Geben Sie alle möglichen Steigungen dieser Geraden an.

## Lösung

### Teil a)

Tangente $y = \frac{1}{2}x - \frac{1}{2}$ einzeichnen:
- Geht durch $P(3|1)$ ✓
- Steigung $\frac{1}{2}$ → pro 2 Einheiten nach rechts, 1 Einheit nach oben
- $y$-Achsenabschnitt: $-\frac{1}{2}$
- Berührt den Graphen nur in $P$

---

### Teil b): Alle möglichen Sekantensteigungen

**Schritt 1: Sekantensteigung aufstellen**

Sekante durch $P(3|1)$ und einen weiteren Punkt $Q(q|\sqrt{q-2})$ auf dem Graphen:

$$m(q) = \frac{\sqrt{q-2} - 1}{q - 3}, \quad q \in [2; \infty[ \,\setminus\, \{3\}$$

Durch Rationalisieren erhält man für $q \neq 3$:

$$m(q)=\frac{\sqrt{q-2}-1}{q-3}\cdot\frac{\sqrt{q-2}+1}{\sqrt{q-2}+1}
=\frac{q-2-1}{(q-3)(\sqrt{q-2}+1)}
=\frac{1}{\sqrt{q-2}+1}$$

**Schritt 2: Grenzfälle untersuchen**

**Fall 1: $Q$ links von $P$ ($q \to 2^+$)**
- Mit der vereinfachten Form gilt: $m(2) = \frac{1}{0 + 1} = \mathbf{1}$
- Punkt $Q(2|0)$ ist Randpunkt → Steigung $m = 1$ wird **angenommen**

**Fall 2: $Q \to P$ ($q \to 3$)**
- Mit der vereinfachten Form: $m(q) \to \frac{1}{1 + 1} = \mathbf{\frac{1}{2}}$
- Das ist genau der Tangentengrenzfall: $m \to g'(3) = \frac{1}{2}$
- Tangente berührt nur in $P$ → Steigung $m = \frac{1}{2}$ wird **nicht angenommen** (offenes Intervall)

**Fall 3: $Q$ weit rechts ($q \to \infty$)**
- Mit der vereinfachten Form: $m(q) = \frac{1}{\sqrt{q-2} + 1} \to \mathbf{0}$
- $m = 0$ wird nie angenommen, weil der Nenner für jedes endliche $q$ positiv und endlich ist

**Schritt 3: Wertebereich bestimmen**

Für $q \in \mathopen{]}2; 3\mathclose{[}$: $Q$ liegt links von $P$
- Es gilt: $0 < \sqrt{q-2} < 1$
- Daher: $1 < \sqrt{q-2} + 1 < 2$
- Also: **$\frac{1}{2} < m(q) < 1$**
- Zusammen mit $m(2) = 1$ folgt:
- → Steigungen in **$\mathopen{]}\frac{1}{2}; 1\mathclose{]}$** ($1$ wird bei $q=2$ angenommen, $\frac{1}{2}$ nicht)

Für $q \in \mathopen{]}3; \infty\mathclose{[}$: $Q$ liegt rechts von $P$
- Es gilt: $\sqrt{q-2} > 1$
- Daher: $\sqrt{q-2} + 1 > 2$
- Also: **$0 < m(q) < \frac{1}{2}$**
- → Steigungen in **$\mathopen{]}0; \frac{1}{2}\mathclose{[}$**

**Schritt 4: Ergebnis**

Alle möglichen Steigungen: **$m \in \mathopen{]}0; \frac{1}{2}\mathclose{[} \cup \mathopen{]}\frac{1}{2}; 1\mathclose{]}$**

---

## Was hier schwierig ist — und worauf man achten muss

1. **Zwei Fälle**: $Q$ kann links ODER rechts von $P$ liegen — beide untersuchen!
2. **Offene vs. geschlossene Intervalle**:
   - $m = 1$ bei $q = 2$: erreichbar, weil $Q(2|0)$ auf dem Graphen liegt → **eckige Klammer**
   - $m = \frac{1}{2}$: Tangentensteigung, nur Grenzwert → **runde Klammer**
   - $m = 0$: nur Grenzwert für $q \to \infty$ → **runde Klammer**
3. **Rationalisieren lohnt sich**: Aus dem komplizierten Differenzenquotienten wird die einfache Form $m(q)=\frac{1}{\sqrt{q-2}+1}$
4. **Graphische Vorstellung hilft**: Sekante bei $P$ „dreht" sich — welche Steigungen werden dabei durchlaufen?

> **Rezept angewendet:** [Rezept 10: Sekanten- und Tangentensteigungen vergleichen](../../../rezepte/10_sekanten_tangenten_vergleich.md)

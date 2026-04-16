# Musterlösung: Abitur 2025 — Analysis, Teil A, Aufgabengruppe 2, Aufgabe 4

## Aufgabe
Gegeben: g: x → √(x − 2), x ∈ [2; ∞[. Punkt P(3|1) liegt auf G_g. Die Tangente an G_g in P hat die Gleichung y = (1/2)x − 1/2 und hat mit G_g nur den Punkt P gemeinsam.

**a)** Zeichnen Sie die Tangente in Abbildung 2 ein.

**b)** Betrachtet wird eine Gerade, die mit G_g sowohl den Punkt P als auch einen weiteren Punkt gemeinsam hat. Geben Sie alle möglichen Steigungen dieser Geraden an.

## Lösung

### Teil a)

Tangente y = (1/2)x − 1/2 einzeichnen:
- Geht durch P(3|1) ✓
- Steigung 1/2 → pro 2 Einheiten nach rechts, 1 Einheit nach oben
- y-Achsenabschnitt: −1/2
- Berührt den Graphen nur in P

---

### Teil b): Alle möglichen Sekantensteigungen

**Schritt 1: Sekantensteigung aufstellen**

Sekante durch P(3|1) und einen weiteren Punkt Q(q|√(q−2)) auf dem Graphen:

m(q) = (√(q−2) − 1) / (q − 3), wobei q ∈ [2; ∞[ \ {3}

Durch Rationalisieren erhält man für q ≠ 3:

$$m(q)=\frac{\sqrt{q-2}-1}{q-3}\cdot\frac{\sqrt{q-2}+1}{\sqrt{q-2}+1}
=\frac{q-2-1}{(q-3)(\sqrt{q-2}+1)}
=\frac{1}{\sqrt{q-2}+1}$$

**Schritt 2: Grenzfälle untersuchen**

**Fall 1: Q links von P (q → 2⁺)**
- Mit der vereinfachten Form gilt: m(2) = 1 / (0 + 1) = **1**
- Punkt Q(2|0) ist Randpunkt → Steigung m = 1 wird **angenommen**

**Fall 2: Q → P (q → 3)**
- Mit der vereinfachten Form: m(q) → 1 / (1 + 1) = **1/2**
- Das ist genau der Tangentengrenzfall: m → g'(3) = **1/2**
- Tangente berührt nur in P → Steigung m = 1/2 wird **nicht angenommen** (offenes Intervall)

**Fall 3: Q weit rechts (q → ∞)**
- Mit der vereinfachten Form: m(q) = 1 / (\sqrt{q−2} + 1) → **0**
- m = 0 wird nie angenommen, weil der Nenner für jedes endliche q positiv und endlich ist

**Schritt 3: Wertebereich bestimmen**

Für q ∈ ]2; 3[: Q liegt links von P
- Es gilt: 0 < √(q−2) < 1
- Daher: 1 < √(q−2) + 1 < 2
- Also: **1/2 < m(q) < 1**
- Zusammen mit m(2) = 1 folgt:
- → Steigungen in **]1/2; 1]** (1 wird bei q=2 angenommen, 1/2 nicht)

Für q ∈ ]3; ∞[: Q liegt rechts von P
- Es gilt: √(q−2) > 1
- Daher: √(q−2) + 1 > 2
- Also: **0 < m(q) < 1/2**
- → Steigungen in **]0; 1/2[**

**Schritt 4: Ergebnis**

Alle möglichen Steigungen: **m ∈ ]0; 1/2[ ∪ ]1/2; 1]**

---

## Was hier schwierig ist — und worauf man achten muss

1. **Zwei Fälle**: Q kann links ODER rechts von P liegen — beide untersuchen!
2. **Offene vs. geschlossene Intervalle**:
   - m = 1 bei q = 2: erreichbar, weil Q(2|0) auf dem Graphen liegt → **eckige Klammer**
   - m = 1/2: Tangentensteigung, nur Grenzwert → **runde Klammer**
   - m = 0: nur Grenzwert für q → ∞ → **runde Klammer**
3. **Rationalisieren lohnt sich**: Aus dem komplizierten Differenzenquotienten wird die einfache Form \(m(q)=1/(\sqrt{q-2}+1)\)
4. **Graphische Vorstellung hilft**: Sekante bei P „dreht" sich — welche Steigungen werden dabei durchlaufen?

> **Rezept angewendet:** Sekanten- und Tangentensteigungen (Rezept 10)

# Musterlösung: Abitur 2025 — Analysis, Teil B, Aufgabengruppe 1, Aufgabe 1c

## Aufgabe
Gegeben: f(x) = 0,25 · (x + 6) · √(6 − x), definiert für x ∈ ]−∞; 6], relevant: −5 ≤ x ≤ 6.

**Weisen Sie nach, dass (6 − 3x) / (8 · √(6 − x)) ein Term der ersten Ableitungsfunktion f' von f ist. Ermitteln Sie den linksseitigen Grenzwert lim_{x→6^-} f'(x) und deuten Sie das Ergebnis im Sachzusammenhang.**

(Sachkontext: Flugbahn eines Badminton-Federballs, x in Metern, f(x) = Höhe)

## Lösung

### Schritt 1: Ableitung nachweisen (Produktregel)

f(x) = 0,25 · (x + 6) · √(6 − x)

Wir setzen: u(x) = x + 6 und v(x) = √(6 − x) = (6 − x)^(1/2)

**Ableitungen:**
- u'(x) = 1
- v'(x) = (1/2) · (6 − x)^(−1/2) · (−1) = −1 / (2√(6 − x))   ← Kettenregel!

**Produktregel:** f'(x) = 0,25 · [u'·v + u·v']

f'(x) = 0,25 · [1 · √(6 − x) + (x + 6) · (−1/(2√(6 − x)))]

f'(x) = 0,25 · [√(6 − x) − (x + 6)/(2√(6 − x))]

**Auf Hauptnenner 2√(6 − x) bringen:**

f'(x) = 0,25 · [2(6 − x)/(2√(6 − x)) − (x + 6)/(2√(6 − x))]

f'(x) = 0,25 · [(12 − 2x − x − 6) / (2√(6 − x))]

f'(x) = 0,25 · [(6 − 3x) / (2√(6 − x))]

**f'(x) = (6 − 3x) / (8√(6 − x))** ✓

---

### Schritt 2: Grenzwert berechnen

lim_{x→6^-} f'(x) = lim_{x→6^-} (6 − 3x) / (8√(6 − x))

Für x → 6^-:
- Zähler: 6 − 3·6 = 6 − 18 = **−12** (fester negativer Wert)
- Nenner: 8·√(6 − 6) = 8·√0 = **0⁺** (wird beliebig klein, aber positiv)

→ **lim_{x→6^-} f'(x) = −∞**

---

### Schritt 3: Deutung im Sachkontext

Der Federball hat an der Stelle x = 6 eine **beliebig steil abfallende Flugbahn**. Das bedeutet: Der Federball trifft (nahezu) **senkrecht** auf dem Boden auf.

---

## Was hier schwierig ist — und worauf man achten muss
1. **„Nachweisen"** = Man muss den gegebenen Term durch eigene Rechnung herleiten, nicht einfach bestätigen
2. **Produktregel + Kettenregel gleichzeitig**: v(x) = √(6−x) braucht die Kettenregel (innere Ableitung −1)
3. **Hauptnenner bilden**: Der algebraische Umformungsschritt ist der fehleranfälligste Teil
4. **Grenzwert −∞**: Zähler ist −12 (nicht 0!), Nenner geht gegen 0 → Bruch divergiert
5. **Sachkontext**: „Steigung → −∞" muss übersetzt werden in „trifft senkrecht auf"

# Rezept: Sekanten- und Tangentensteigungen vergleichen

## Typische Aufgabenstellung
> „Geben Sie alle möglichen Steigungen einer Geraden an, die den Graphen in P und einem weiteren Punkt schneidet."
> „Für welche Steigung m hat die Gerade y = mx + b genau zwei Schnittpunkte mit dem Graphen?"

## Schritt-für-Schritt

1. **Sekantensteigung aufstellen**: Gerade durch P(p|f(p)) und Q(q|f(q))
   - m(q) = (f(q) − f(p)) / (q − p)
2. **Grenzfälle untersuchen**:
   - q → p: Sekantensteigung → Tangentensteigung f'(p)
   - q → ∞ oder q → Randwert: Sekantensteigung → Grenzwert bestimmen
3. **Monotonie von m(q)** prüfen: Ist die Sekantensteigung steigend/fallend in q?
4. **Wertebereich von m** angeben: alle erreichbaren Steigungen
5. **Tangente ausschließen**: Wenn Tangente den Graphen nur in P berührt → diese Steigung ist Grenzwert, wird aber nicht angenommen

## Beispiel (Abitur 2025 A2 4b)
f(x) = √(x−2), P(3|1), Tangentensteigung m_T = 1/2
- Sekantensteigung: m(q) = (√(q−2) − 1)/(q − 3) für q ∈ [2;∞[\{3}
- q → 2: m → (0−1)/(2−3) = 1
- q → ∞: m → 0 (Zähler wächst wie √q, Nenner wie q)
- q → 3: m → f'(3) = 1/2
- Steigung m_T = 1/2 nur als Grenzwert → nicht angenommen
- Mögliche Steigungen: m ∈ ]0; 1/2[ ∪ ]1/2; 1]

## Häufige Fehler
- Grenzwert als erreichbaren Wert annehmen (offenes vs. geschlossenes Intervall)
- Fallunterscheidung vergessen: zweiter Punkt links vs. rechts von P
- Tangentensteigung nicht erkannt als Grenzfall

# Musterlösung: Abitur 2025 — Analysis, Teil A, Aufgabengruppe 2, Aufgabe 2b

## Aufgabe
Der Punkt (2|3) ist der einzige Wendepunkt des Graphen von g. Die in ℝ definierte Funktion h ist gegeben durch h(x) = g(2x) − 1.

**Geben Sie die Koordinaten des Wendepunkts des Graphen von h an und begründen Sie Ihre Angabe.**

## Lösung

### Schritt 1: Transformationen identifizieren

h(x) = g(**2x**) **− 1**

Zwei Transformationen:
1. **g(2x)**: Argument wird mit 2 multipliziert → **Stauchung in x-Richtung um Faktor 1/2**
2. **− 1**: Vom Funktionswert wird 1 abgezogen → **Verschiebung um 1 nach unten**

### Schritt 2: Wendepunkt transformieren

Alter Wendepunkt von g: **W(2|3)**

**x-Koordinate:** Der Faktor 2 im Argument staucht die x-Achse um 1/2:
- x_neu = 2 / 2 = **1**

**y-Koordinate:** Das „−1" verschiebt nach unten:
- y_neu = 3 − 1 = **2**

### Schritt 3: Ergebnis

**Wendepunkt von h: W'(1|2)**

### Schritt 4: Begründung

Graphentransformationen ändern den Typ besonderer Punkte nicht: Ein Wendepunkt bleibt ein Wendepunkt.

Formal: h''(x) = 4·g''(2x) (zweimalige Anwendung der Kettenregel). Wenn g''(2) = 0 und g'''(2) ≠ 0, dann ist h''(1) = 4·g''(2·1) = 4·g''(2) = 0 und h'''(1) = 8·g'''(2) ≠ 0 → Wendepunkt bei x = 1.

---

## Was hier schwierig ist — und worauf man achten muss

1. **g(2x) staucht, nicht streckt**: Faktor 2 „innen" → x-Werte werden **halbiert**
2. **Begründung verlangt**: Nicht nur Koordinaten hinschreiben, sondern erklären warum
3. **Reihenfolge**: Erst x-Transformation (innen), dann y-Transformation (außen) — hier unabhängig, aber bei f(2(x−1)) + 3 wäre die Reihenfolge wichtig

> **Rezept angewendet:** Graphentransformationen (Rezept 04)
> Formel: x_neu = x_alt / k bei f(kx), y_neu = y_alt + d bei f(…) + d

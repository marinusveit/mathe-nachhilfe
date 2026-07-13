# Musterlösung: Abitur 2025 — Analysis, Teil A, Aufgabengruppe 2, Aufgabe 2b

## Aufgabe
Der Punkt $(2|3)$ ist der einzige Wendepunkt des Graphen von $g$. Die in $\mathbb{R}$ definierte Funktion $h$ ist gegeben durch $h(x) = g(2x) - 1$.

**Geben Sie die Koordinaten des Wendepunkts des Graphen von $h$ an und begründen Sie Ihre Angabe.**

## Lösung

### Schritt 1: Transformationen identifizieren

$h(x) = g(\mathbf{2x}) \mathbf{- 1}$

Zwei Transformationen:
1. **$g(2x)$**: Argument wird mit $2$ multipliziert → **Stauchung in $x$-Richtung um Faktor $\frac{1}{2}$**
2. **$-1$**: Vom Funktionswert wird $1$ abgezogen → **Verschiebung um $1$ nach unten**

### Schritt 2: Wendepunkt transformieren

Alter Wendepunkt von $g$: **$W(2|3)$**

**$x$-Koordinate:** Der Faktor $2$ im Argument staucht die $x$-Achse um $\frac{1}{2}$:
- $x_{\text{neu}} = 2 / 2 = \mathbf{1}$

**$y$-Koordinate:** Das „$-1$" verschiebt nach unten:
- $y_{\text{neu}} = 3 - 1 = \mathbf{2}$

### Schritt 3: Ergebnis

**Wendepunkt von $h$: $W'(1|2)$**

### Schritt 4: Begründung

Graphentransformationen ändern den Typ besonderer Punkte nicht: Ein Wendepunkt bleibt ein Wendepunkt.

Formal: $h''(x) = 4\,g''(2x)$ (zweimalige Anwendung der Kettenregel). Da $g$ bei $x = 2$ seinen (einzigen) Wendepunkt hat, wechselt $g''$ bei $x = 2$ das Vorzeichen. Wegen $h''(x) = 4\,g''(2x)$ überträgt sich dieser Vorzeichenwechsel auf $h''$ an der Stelle $x = 1$ (dort ist $2x = 2$). Also wechselt $h''$ bei $x = 1$ das Vorzeichen → $h$ hat dort einen Wendepunkt.

---

## Was hier schwierig ist — und worauf man achten muss

1. **$g(2x)$ staucht, nicht streckt**: Faktor $2$ „innen" → $x$-Werte werden **halbiert**
2. **Begründung verlangt**: Nicht nur Koordinaten hinschreiben, sondern erklären warum
3. **Reihenfolge**: Erst $x$-Transformation (innen), dann $y$-Transformation (außen) — hier unabhängig, aber bei $f(2(x-1)) + 3$ wäre die Reihenfolge wichtig

> **Rezept angewendet:** [Rezept 04: Graphentransformationen](../../../rezepte/04_graphentransformationen.md)
> Formel: $x_{\text{neu}} = x_{\text{alt}} / k$ bei $f(kx)$, $y_{\text{neu}} = y_{\text{alt}} + d$ bei $f(\dots) + d$

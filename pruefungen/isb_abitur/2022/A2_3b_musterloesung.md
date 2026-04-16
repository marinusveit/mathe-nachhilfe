# Musterlösung: Abitur 2022 — Analysis, Teil A, Aufgabengruppe 2, Aufgabe 3b

## Aufgabe
Die in ℝ definierte Funktion f besitzt die Nullstelle x = 2, außerdem gilt f'(x) > 0 für alle x ∈ ℝ. Abbildung 2 zeigt den Graphen G_f von f.

Betrachtet wird die Funktion g: x → ln(f(x)) mit maximaler Definitionsmenge D_g.

**Geben Sie D_g an und ermitteln Sie mithilfe von Abbildung 2 diejenige Stelle x, für die g'(x) = f'(x) gilt.**

## Lösung

### Schritt 1: Definitionsbereich D_g

ln(…) ist nur für positive Argumente definiert, also brauchen wir: **f(x) > 0**

Was wissen wir über f?
- f hat Nullstelle bei x = 2: f(2) = 0
- f'(x) > 0 für alle x → f ist **streng monoton steigend**

Da f streng monoton steigend ist und f(2) = 0:
- Für x < 2: f(x) < 0 (unter der Nullstelle)
- Für x = 2: f(x) = 0
- Für x > 2: f(x) > 0 (über der Nullstelle)

**→ D_g = ]2; ∞[**

> **Rezept angewendet:** Verkettung & Definitionsbereich (Rezept 05)
> ln braucht positives Argument → Ungleichung f(x) > 0 lösen

---

### Schritt 2: g'(x) = f'(x) lösen

**Kettenregel** auf g(x) = ln(f(x)) anwenden:

g'(x) = f'(x) / f(x)

Jetzt setzen wir g'(x) = f'(x):

f'(x) / f(x) = f'(x)

Da f'(x) > 0 für alle x (können wir durch f'(x) teilen):

1 / f(x) = 1

**f(x) = 1**

→ Wir suchen die Stelle x, an der f den Wert 1 annimmt.

**Aus dem Graphen ablesen:** f(x) = 1 bei **x = 3** (aus Abbildung 2).

---

## Zusammenfassung der Ergebnisse
- D_g = ]2; ∞[
- g'(x) = f'(x) gilt für x = 3

## Was hier schwierig ist — und worauf man achten muss
1. **Kettenregel bei ln(f(x))**: Die Ableitung ist f'(x)/f(x), nicht einfach 1/f(x)
2. **Gleichung vereinfachen**: Man darf durch f'(x) teilen, weil f'(x) > 0 — das steht im Aufgabentext!
3. **Graphen ablesen**: Am Ende muss man aus dem Graphen den x-Wert mit f(x) = 1 ablesen — genau das Thema „aus Graphen Sachen ablesen"

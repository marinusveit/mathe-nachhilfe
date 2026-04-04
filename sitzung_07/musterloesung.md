# Musterlösung — Hilfsmittelfreier Teil (Teil A)

---

## Aufgabe 1: Ableitungen bestimmen (6 Punkte)

### a) f(x) = 5x³ − 4x² + 2x − 7

**Methode:** Summenregel + Potenzregel (f(x) = xⁿ ⟹ f'(x) = n·xⁿ⁻¹)

f'(x) = 15x² − 8x + 2

---

### b) f(x) = 3/x + 2√x

**Methode:** Umschreiben in Potenzform, dann Potenzregel.

Umschreiben: f(x) = 3x⁻¹ + 2x^(1/2)

f'(x) = 3·(−1)·x⁻² + 2·(1/2)·x^(−1/2)

**f'(x) = −3/x² + 1/√x**

---

### c) f(x) = (3x − 1)⁴

**Methode:** Kettenregel. Äußere Funktion: u⁴, innere Funktion: u = 3x − 1.

f'(x) = 4·(3x − 1)³ · 3

**f'(x) = 12·(3x − 1)³**

---

### d) f(x) = x² · ln(x)

**Methode:** Produktregel: (u·v)' = u'·v + u·v'.

Setze u = x², v = ln(x), also u' = 2x, v' = 1/x.

f'(x) = 2x · ln(x) + x² · (1/x)

**f'(x) = 2x · ln(x) + x**

---

### e) f(x) = e^(−x²)

**Methode:** Kettenregel. Äußere Funktion: eᵘ, innere Funktion: u = −x².

f'(x) = e^(−x²) · (−2x)

**f'(x) = −2x · e^(−x²)**

---

### f) f(x) = sin(2x) + cos(x)

**Methode:** Kettenregel bei sin(2x); Ableitung von cos(x) = −sin(x).

f'(x) = cos(2x) · 2 + (−sin(x))

**f'(x) = 2·cos(2x) − sin(x)**

---

## Aufgabe 2: Stammfunktionen bestimmen (4 Punkte)

### a) f(x) = 6x² − 4x + 3

**Methode:** Potenzregel rückwärts: ∫ xⁿ dx = xⁿ⁺¹/(n+1).

**F(x) = 2x³ − 2x² + 3x**

Probe: F'(x) = 6x² − 4x + 3 ✓

---

### b) f(x) = e^(3x)

**Methode:** Lineare Substitution: ∫ e^(ax) dx = (1/a)·e^(ax).

**F(x) = (1/3)·e^(3x)**

Probe: F'(x) = (1/3)·3·e^(3x) = e^(3x) ✓

---

### c) f(x) = 1/x  (x > 0)

**Methode:** Standardintegral ∫ (1/x) dx = ln|x|. Da x > 0 gilt ln(x).

**F(x) = ln(x)**

---

### d) f(x) = 4·cos(2x)

**Methode:** Lineare Substitution: ∫ cos(ax) dx = (1/a)·sin(ax).

F(x) = 4 · (1/2) · sin(2x)

**F(x) = 2·sin(2x)**

Probe: F'(x) = 2·cos(2x)·2 = 4·cos(2x) ✓

---

## Aufgabe 3: Bestimmte Integrale berechnen (4 Punkte)

### a) ∫₀³ (2x + 1) dx

**Methode:** Stammfunktion bilden, Hauptsatz der Differential- und Integralrechnung.

F(x) = x² + x

∫₀³ (2x + 1) dx = F(3) − F(0) = (9 + 3) − (0 + 0) = 12

**Ergebnis: 12**

---

### b) ∫₁² x² dx

F(x) = x³/3

∫₁² x² dx = 8/3 − 1/3 = 7/3

**Ergebnis: 7/3**

---

### c) ∫₀¹ eˣ dx

F(x) = eˣ

∫₀¹ eˣ dx = e¹ − e⁰ = e − 1

**Ergebnis: e − 1**

---

### d) ∫₋₁¹ x³ dx

**Methode:** x³ ist eine ungerade Funktion (punktsymmetrisch zum Ursprung). Das Integral einer ungeraden Funktion über ein symmetrisches Intervall [−a; a] ist stets 0.

Rechnerisch: F(x) = x⁴/4

∫₋₁¹ x³ dx = 1/4 − 1/4 = 0

**Ergebnis: 0**

---

## Aufgabe 4: Graphen zuordnen (3 Punkte)

**Zugrundeliegende Funktion:** f(x) = x²(4 − x)²/4

**Gegeben:**
- Graph A: Nach oben geöffnete Parabel mit Minimum bei x = 2.
- Graph B: Maximum bei x = 2 und Nullstellen bei x = 0 und x = 4.
- Graph C: Nullstellen bei x = 0, x = 2 und x = 4.

### Zuordnung:

| Graph | Funktion | Begründung |
|-------|----------|------------|
| **B** | **f** | f hat ein Maximum bei x = 2 und Nullstellen bei x = 0, 4. |
| **C** | **f'** | f' hat Nullstellen bei x = 0, 2, 4 — dort hat f Extrema bzw. Nullstellen mit waagerechter Tangente. |
| **A** | **f''** | f'' ist eine nach oben geöffnete Parabel mit Minimum bei x = 2. |

**Ausführliche Begründung:**

**Graph B = f:** Die Funktion f(x) = x²(4−x)²/4 hat Nullstellen bei x = 0 und x = 4 und ein Maximum bei x = 2 mit f(2) = 4. Das passt zu Graph B.

**Graph C = f':** Die Ableitung f'(x) = x(4−x)(2−x) hat drei Nullstellen bei x = 0, x = 2 und x = 4. Bei x = 2 wechselt f' das Vorzeichen von + nach − (VZW), was das Maximum von f bei x = 2 bestätigt. Das passt zu Graph C.

**Graph A = f'':** Die zweite Ableitung f''(x) = 3x² − 12x + 8 ist eine nach oben geöffnete Parabel. Sie hat ihr Minimum bei x = 2 mit f''(2) = 12 − 24 + 8 = −4 < 0. Das negative Vorzeichen bestätigt: f hat bei x = 2 ein Maximum (Rechtskrümmung). Die Nullstellen von f'' (bei x ≈ 0.85 und x ≈ 3.15) sind die Wendepunkte von f. Das passt zu Graph A.

**Kontrollregel:** Nullstellen von f' = Extremstellen von f. Nullstellen von f'' = Wendepunkte von f.

---

## Aufgabe 5: Zusammenhang f und f' (3 Punkte)

**Gegeben:** f'(x) > 0 für x < 1, f'(1) = 0, f'(x) < 0 für 1 < x < 3, f'(3) = 0, f'(x) > 0 für x > 3.

### a) „f hat bei x = 1 ein lokales Maximum."

**Wahr.** ✓

Begründung: f' wechselt bei x = 1 das Vorzeichen von + nach −. Das bedeutet: f steigt vor x = 1 und fällt nach x = 1. Also hat f bei x = 1 ein lokales Maximum.

---

### b) „f ist im Intervall [0; 1] monoton fallend."

**Falsch.** ✗

Begründung: Für x < 1 gilt f'(x) > 0, also insbesondere auch für x ∈ [0; 1). Da f' dort positiv ist, ist f im Intervall [0; 1] **monoton steigend** (nicht fallend).

---

### c) „f hat bei x = 3 ein lokales Minimum."

**Wahr.** ✓

Begründung: f' wechselt bei x = 3 das Vorzeichen von − nach +. Das bedeutet: f fällt vor x = 3 und steigt nach x = 3. Also hat f bei x = 3 ein lokales Minimum.

---

### d) „f hat bei x = 2 einen Wendepunkt."

**Wahr.** ✓

Begründung: f' hat bei x = 1 den Wert 0, ist danach negativ, und hat bei x = 3 wieder den Wert 0. Also muss f' im Intervall (1; 3) ein lokales Minimum haben. An diesem Minimum wechselt f'' das Vorzeichen (von negativ zu positiv), was bedeutet: f hat dort einen Wendepunkt. Da x = 2 genau in der Mitte des Intervalls liegt und die Aufgabe diesen Wert vorgibt, ist die Aussage wahr.

*Allgemein: Ein Wendepunkt von f liegt dort, wo f' ein lokales Extremum hat (also f'' einen Vorzeichenwechsel).*

---

## Aufgabe 6: Tangentengleichung (3 Punkte)

**Gegeben:** f(x) = x³ − 2x + 1, Punkt P(1 | f(1)).

**Methode:** Tangentengleichung: t(x) = f(a) + f'(a) · (x − a) mit a = 1.

**Schritt 1:** Funktionswert berechnen.

f(1) = 1³ − 2·1 + 1 = 1 − 2 + 1 = 0

Also P(1 | 0).

**Schritt 2:** Ableitung bilden und Steigung berechnen.

f'(x) = 3x² − 2

f'(1) = 3·1 − 2 = 1

**Schritt 3:** Tangentengleichung aufstellen.

t(x) = 0 + 1·(x − 1) = x − 1

**t(x) = x − 1**

---

## Aufgabe 7: Extrema bestimmen (4 Punkte)

**Gegeben:** f(x) = x³ − 6x² + 9x − 2

### a) Extremstellen und deren Art

**Schritt 1:** Erste Ableitung.

f'(x) = 3x² − 12x + 9

**Schritt 2:** Notwendige Bedingung f'(x) = 0.

3x² − 12x + 9 = 0    | ÷3

x² − 4x + 3 = 0

Mitternachtsformel oder Faktorisieren: (x − 1)(x − 3) = 0

**x₁ = 1,  x₂ = 3**

**Schritt 3:** Zweite Ableitung zur Klassifikation.

f''(x) = 6x − 12

f''(1) = 6 − 12 = −6 < 0  ⟹  **Hochpunkt bei x = 1**

f''(3) = 18 − 12 = 6 > 0  ⟹  **Tiefpunkt bei x = 3**

### b) Funktionswerte an den Extremstellen

f(1) = 1 − 6 + 9 − 2 = **2**   →  Hochpunkt H(1 | 2)

f(3) = 27 − 54 + 27 − 2 = **−2**   →  Tiefpunkt T(3 | −2)

---

## Aufgabe 8: Notwendige und hinreichende Bedingung (3 Punkte)

### a) Notwendige Bedingung für eine Extremstelle

Ist x₀ eine Extremstelle von f und ist f differenzierbar in x₀, so gilt:

**f'(x₀) = 0**

(Die Ableitung verschwindet an einer Extremstelle.)

---

### b) Hinreichende Bedingung (2. Ableitung)

Gilt f'(x₀) = 0 und f''(x₀) ≠ 0, so hat f bei x₀ ein Extremum:

- f''(x₀) < 0  ⟹  lokales **Maximum** bei x₀
- f''(x₀) > 0  ⟹  lokales **Minimum** bei x₀

---

### c) Gegenbeispiel

Die Aussage „f'(2) = 0, also hat f bei x = 2 ein Extremum" ist **nicht zwingend richtig**, weil f'(x₀) = 0 nur eine **notwendige**, aber keine **hinreichende** Bedingung für ein Extremum ist.

**Gegenbeispiel:** f(x) = (x − 2)³

- f'(x) = 3(x − 2)²
- f'(2) = 3·0² = 0  ✓  (notwendige Bedingung erfüllt)
- f''(x) = 6(x − 2)
- f''(2) = 0  (hinreichende Bedingung greift nicht)

Tatsächlich hat f bei x = 2 **kein Extremum**, sondern einen **Sattelpunkt** (Wendepunkt mit waagerechter Tangente). Die Funktion steigt sowohl links als auch rechts von x = 2 (denn f'(x) = 3(x − 2)² ≥ 0 für alle x) — es findet kein Vorzeichenwechsel von f' statt.

---

## Aufgabe 9: Funktionswerte und Vorzeichen (2 Punkte)

**Gegeben:** f(x) = −x⁴ + 4x² − 3

### a) Funktionswerte berechnen

f(0) = −0 + 0 − 3 = **−3**

f(1) = −1 + 4 − 3 = **0**

f(−1) = −(−1)⁴ + 4·(−1)² − 3 = −1 + 4 − 3 = **0**

---

### b) Vorzeichen von f''(0)

**Schritt 1:** Erste Ableitung.

f'(x) = −4x³ + 8x

**Schritt 2:** Zweite Ableitung.

f''(x) = −12x² + 8

**Schritt 3:** Einsetzen.

f''(0) = −12·0 + 8 = **8 > 0**

**Interpretation:** Da f''(0) > 0, ist der Graph von f an der Stelle x = 0 **linksgekrümmt** (konvex, „nach oben geöffnet"). An der Stelle x = 0 liegt also ein lokales Minimum — der Graph hat dort eine Mulde.

---

## Aufgabe 10: Integral und Flächeninhalt (3 Punkte)

### a) ∫₀² (x² − 2x) dx

F(x) = x³/3 − x²

∫₀² (x² − 2x) dx = F(2) − F(0) = (8/3 − 4) − (0 − 0) = 8/3 − 12/3 = **−4/3**

---

### b) Skizze

g(x) = x² − 2x = x(x − 2) hat Nullstellen bei x = 0 und x = 2. Der Scheitelpunkt liegt bei x = 1 mit g(1) = 1 − 2 = −1. Die Parabel ist im gesamten Intervall [0; 2] **unterhalb der x-Achse**.

```
  y
  |
--+--------2---→ x
  |  \    /
  |   \  /
  |    \/
  |   (1|−1)
```

---

### c) Erklärung: Warum negativ?

Das Integral ∫₀² (x² − 2x) dx = −4/3 ist **negativ**, weil g(x) = x² − 2x im gesamten Intervall [0; 2] unterhalb der x-Achse liegt (g(x) ≤ 0).

Das bestimmte Integral misst den **orientierten Flächeninhalt**: Flächen unterhalb der x-Achse werden negativ gezählt.

Der tatsächliche **Flächeninhalt** (immer positiv) beträgt:

A = |∫₀² (x² − 2x) dx| = |−4/3| = **4/3 FE**

---

## Aufgabe 11: Monotonie und Krümmung (2 Punkte)

**Gegeben:** f(x) = eˣ · (x − 1)

### a) Ableitung bestimmen und vereinfachen

**Methode:** Produktregel mit u = eˣ, v = (x − 1), also u' = eˣ, v' = 1.

f'(x) = eˣ · (x − 1) + eˣ · 1 = eˣ · (x − 1 + 1)

**f'(x) = x · eˣ**

---

### b) Für welche x ist f monoton steigend?

f ist monoton steigend, wo f'(x) > 0, also wo x · eˣ > 0.

Da eˣ > 0 für alle x ∈ ℝ, hängt das Vorzeichen nur von x ab:

x · eˣ > 0  ⟺  x > 0

**f ist monoton steigend für x > 0.**

(Für x < 0 ist f monoton fallend; bei x = 0 hat f ein lokales Minimum.)

---

## Aufgabe 12: Symmetrie und Grenzverhalten (2 Punkte)

**Gegeben:** f(x) = x⁴ − 2x²

### a) Achsensymmetrie zeigen

**Methode:** f ist achsensymmetrisch zur y-Achse, wenn f(−x) = f(x) für alle x.

f(−x) = (−x)⁴ − 2·(−x)² = x⁴ − 2x² = f(x)  ✓

Da f(−x) = f(x), ist f **achsensymmetrisch zur y-Achse**. ∎

*Bemerkung: Dies war zu erwarten, da f nur gerade Exponenten enthält.*

---

### b) Grenzverhalten für x → ±∞

Der führende Term ist x⁴ (höchste Potenz mit positivem Koeffizienten).

Für x → +∞:  x⁴ → +∞, also **f(x) → +∞**

Für x → −∞:  (−x)⁴ = x⁴ → +∞, also **f(x) → +∞**

In beiden Richtungen strebt f(x) gegen +∞. Der Graph geht auf beiden Seiten „nach oben".

---

## Punkteübersicht

| Aufgabe | Thema | Punkte |
|---------|-------|--------|
| 1 | Ableitungen (6 Teilaufgaben) | 6 |
| 2 | Stammfunktionen | 4 |
| 3 | Bestimmte Integrale | 4 |
| 4 | Graphen zuordnen | 3 |
| 5 | Zusammenhang f und f' | 3 |
| 6 | Tangentengleichung | 3 |
| 7 | Extrema bestimmen | 4 |
| 8 | Notw./hinr. Bedingung | 3 |
| 9 | Funktionswerte und Vorzeichen | 2 |
| 10 | Integral und Flächeninhalt | 3 |
| 11 | Monotonie | 2 |
| 12 | Symmetrie und Grenzverhalten | 2 |
| **Gesamt** | | **39** |

# Cheatsheet: Analysis (Bayern Abitur, eA)

Überblick über alle Themen. Für Details → jeweiliges Rezept.
Separate Cheatsheets:
- [Cheatsheet Grundfunktionen](grundfunktionen.md) — Skizzen, $\mathbb{D}$/$\mathbb{W}$, Ableitungen und wichtige Werte aller Standardfunktionen
- [Cheatsheet Kurvendiskussion](../sitzung_02/cheatsheet_kurvendiskussion.md) — komplettes Rezept
- [Cheatsheet Stochastik](stochastik.md) — Vierfeldertafel, Binomial, Hypothesentest, Normalverteilung

---

## 0. Operatoren — was verlangt die Aufgabe?

| Operator | Was tun? |
|----------|----------|
| **Berechnen / Bestimmen / Ermitteln** | Rechenweg + Ergebnis |
| **Zeigen / Nachweisen** | Von der Funktion starten, **nicht** vom Ergebnis rückwärts |
| **Begründen** | 1–3 Sätze, warum das mathematisch stimmt |
| **Beschreiben** | Sachverhalt in Worten, keine Rechnung |
| **Deuten** | Ergebnis im Sachkontext erklären |
| **Skizzieren** | Freihand, wichtige Punkte eintragen |

> Goldene Regel bei „Zeigen Sie": **nie mit dem Ergebnis anfangen** → sonst 0 Punkte.

→ [Rezept 00: Operatoren Abitur](../rezepte/00_operatoren_abitur.md)

---

## 1. Ableitungen — die Tabelle

| Funktion $f(x)$ | Ableitung $f'(x)$ |
|---|---|
| $x^n$ | $n \cdot x^{n-1}$ |
| konstant $c$ | $0$ |
| $e^x$ | $e^x$ |
| $e^{ax}$ | $a \cdot e^{ax}$ |
| $\ln(x)$ | $\dfrac{1}{x}$ |
| $\sqrt{x}$ | $\dfrac{1}{2\sqrt{x}}$ |
| $\sin(x)$ | $\cos(x)$ |
| $\cos(x)$ | $-\sin(x)$ |

**Regeln:**
- **Summe:** $(f + g)' = f' + g'$
- **Faktor:** $(c \cdot f)' = c \cdot f'$
- **Produkt:** $(f \cdot g)' = f' \cdot g + f \cdot g'$
- **Quotient:** $\left(\dfrac{f}{g}\right)' = \dfrac{f' \cdot g - f \cdot g'}{g^2}$
- **Kette:** $[f(g(x))]' = f'(g(x)) \cdot g'(x)$ — **äußere × innere!**

**Klassische Fallen:**
- $e^{2x}$ → innere Ableitung $2$ nicht vergessen: $(e^{2x})' = 2e^{2x}$
- $\sqrt{6-x}$ → innere Ableitung $-1$: $(\sqrt{6-x})' = -\dfrac{1}{2\sqrt{6-x}}$
- $\ln(f)$ → Ableitung $\dfrac{f'}{f}$, nicht nur $\dfrac{1}{f}$

→ [Rezept 16: Kettenregel verschachtelt](../rezepte/16_kettenregel_verschachtelt.md)

---

## 2. Stammfunktionen — die Tabelle

| $f(x)$ | Stammfunktion $F(x)$ |
|---|---|
| $x^n \ (n \neq -1)$ | $\dfrac{x^{n+1}}{n+1}$ |
| $\dfrac{1}{x}$ | $\ln\lvert x \rvert$ |
| $e^x$ | $e^x$ |
| $e^{ax}$ | $\dfrac{1}{a} \cdot e^{ax}$ — Faktor $\tfrac{1}{a}$! |
| $\sin(x)$ | $-\cos(x)$ |
| $\cos(x)$ | $\sin(x)$ |

- Summen und feste Faktoren darf man einzeln integrieren:
  $\displaystyle\int (a f + b g)\,dx = a \int f\,dx + b \int g\,dx$
- Unbestimmtes Integral: **$+ C$** nicht vergessen
- Bestimmtes Integral: $\bigl[F(x)\bigr]_a^b = F(b) - F(a)$

---

## 3. Termumformung — die 5 Muster

Unverzichtbar bei „Zeigen Sie"-Aufgaben.

### Muster 1: Negative Exponenten ↔ Bruch
$$a^{-n} = \frac{1}{a^n}$$
Vor dem Ableiten in Exponentialform, nach dem Ableiten zurück in Bruchform.

### Muster 2: Brüche mit gleichem Nenner
$$\frac{a}{n} + \frac{b}{n} = \frac{a+b}{n}$$
Nur Zähler addieren — **der Nenner bleibt gleich**.

### Muster 3: Hauptnenner bilden (Wurzeltrick!)
Alle Terme auf den gleichen Nenner bringen. Der Trick bei Wurzeln im Nenner: beim Erweitern mit $\sqrt{u}$ nutzt man $\sqrt{u} \cdot \sqrt{u} = u$ — so verschwindet die Wurzel im Zähler.

Beispiel:
$$\sqrt{6-x} - \frac{x+6}{2\sqrt{6-x}}$$

Ersten Term erweitern mit $2\sqrt{6-x}$:
$$\sqrt{6-x} = \frac{2(6-x)}{2\sqrt{6-x}}$$

Zähler zusammenfassen:
$$\frac{2(6-x) - (x+6)}{2\sqrt{6-x}} = \frac{6-3x}{2\sqrt{6-x}}$$

### Muster 4: Wurzel im Nenner
$$\frac{a}{\sqrt{u}} = \frac{a\sqrt{u}}{u}$$
Bei „Zeigen Sie" oft die Wurzel im Nenner **stehen lassen** — bloß nicht umbauen, wenn die Zielform sie drin hat.

### Muster 5: Doppelbruch auflösen
$$\frac{a/b}{c} = \frac{a}{bc} \qquad \frac{a}{b/c} = \frac{ac}{b}$$

**Klassische Fehler:**
1. $\dfrac{a}{n} + \dfrac{b}{n} = \dfrac{a+b}{2n}$ ← **FALSCH!** Nenner bleibt $n$.
2. Vorzeichen beim Erweitern — Klammern um den ganzen Zähler setzen!
3. $a^{-2} = -a^2$ ← **FALSCH!** Das ist $\dfrac{1}{a^2}$.
4. „Zeigen Sie" heißt **exakt die Zielform** — nicht nur eine äquivalente Form.

→ [Rezept 17: Termumformung Analysis](../rezepte/17_termumformung_analysis.md)

---

## 4. Definitions- und Wertebereich

Welche $x$ darf man einsetzen, welche $y$-Werte kommen heraus?

### Definitionsbereich $\mathbb{D}$ — wo $x$ eingesetzt werden darf

| Funktionstyp | Bedingung |
|---|---|
| Ganzrational (Polynome: $3x+1$, $x^2-4$, $x^3-2x+7$, …) | $\mathbb{D} = \mathbb{R}$ |
| Bruch | Nenner $\neq 0$ |
| Wurzel $\sqrt{Radikand}$ | Radikand $\geq 0$ |
| $\ln(Argument)$ | Argument $> 0$ |

> **Ganzrational** = nur $x$, $x^2$, $x^3$, … mit Zahlen kombiniert (also Polynome). Kein Bruch mit $x$ im Nenner, keine Wurzel mit $x$ drunter, kein $\ln(x)$. → immer $\mathbb{D} = \mathbb{R}$, weil man jedes $x$ einsetzen darf.

### Wertebereich $\mathbb{W}$ — welche $y$-Werte vorkommen

| Funktion | $W$ |
|---|---|
| $x^2$ | $[0;\infty[$ |
| $x^3$ | $\mathbb{R}$ |
| $\sqrt{x}$ | $[0;\infty[$ |
| $e^x$ | $\,]0;\infty[\,$ — **nicht $0$!** |
| $\ln(x)$ | $\mathbb{R}$ |

**Wertebereich bestimmen:** schauen, welche $y$-Werte der Graph insgesamt annimmt.

In der Praxis reicht **Extrema + Randverhalten per Limes** fast immer:

- **Extrema** (Hoch-/Tiefpunkte): kleinster/größter Wert
- **Randverhalten per Limes**: am Rand von $\mathbb{D}$ und an jeder Definitionslücke (Polstelle → §6)
- Zwischen diesen Stützstellen ist $f$ stetig → alle $y$-Werte dazwischen werden lückenlos angenommen (Monotonie zwischen Extrema ist automatisch)

**Welche Grenzen per Limes untersuchen?** Hängt vom Definitionsbereich ab:

| $\mathbb{D}$ | Zu untersuchen |
|---|---|
| $[a;b]$ (geschlossen) | $f(a)$, $f(b)$ direkt einsetzen — kein Limes nötig |
| $[a;b[$ bzw. $]a;b]$ | geschlossenen Rand einsetzen, offenen per $\displaystyle\lim_{x \to b^-}$ bzw. $\displaystyle\lim_{x \to a^+}$ |
| $]a;b[$ (offen) | beide Ränder per Limes |
| $\mathbb{R} = {]-\infty;+\infty[}$ | $\displaystyle\lim_{x \to \pm\infty} f(x)$ — $\mathbb{R}$ ist beidseitig offen |
| Definitionslücke bei $x_0$ | beidseitig $\displaystyle\lim_{x \to x_0^\pm} f(x)$ (Polstelle → $\pm\infty$) |

> **Beispiel** $f(x) = \tfrac{1}{x}$ mit $\mathbb{D} = \mathbb{R}\setminus\{0\}$ → **4 Stellen** zu prüfen:
> $\displaystyle\lim_{x \to -\infty} f$, $\displaystyle\lim_{x \to 0^-} f$, $\displaystyle\lim_{x \to 0^+} f$, $\displaystyle\lim_{x \to +\infty} f$

- **$[$** eckige Klammer → Wert wird angenommen (Extremum oder geschlossener Rand)
- **$]$** nach außen gedrehte eckige Klammer (= offenes Intervall) → nur Grenzwert, wird **nicht** angenommen (offener Rand, $\pm\infty$, Polstelle)

→ [Rezept 05: Verkettung/Definitionsbereich](../rezepte/05_verkettung_definitionsbereich.md) · [Rezept 18: Wertebereich](../rezepte/18_wertebereich.md)

---

## 5. Grenzwerte & Asymptoten

Was passiert für sehr große $x$ oder an kritischen Stellen?

Eine **Asymptote** ist eine Gerade, an die sich der Graph beliebig nah annähert, ohne sie je zu erreichen.

**Wachstumshierarchie:** $e^x$ wächst schneller als jedes $x^n$, und $x^n$ wächst schneller als $\ln(x)$. Kurz: $e^x \gg x^n \gg \ln(x)$.

Wichtig: $e^{-x} \to 0$ für $x \to \infty$ (nicht $\infty$!)

| Asymptote | Bedingung |
|---|---|
| waagrechte Asymptote $y = c$ | $\displaystyle\lim_{x \to \pm\infty} f(x) = c$ |
| senkrechte Asymptote $x = a$ | Polstelle, Nenner $\to 0$ |
| schräge Asymptote | Zählergrad $=$ Nennergrad $+1$ → Polynomdivision |

> **Beispiel:** $f(x) = \dfrac{1}{x-1} + 2$ hat die senkrechte Asymptote $x = 1$ (dort ist der Nenner $0$) und die waagrechte Asymptote $y = 2$ (für $x \to \pm\infty$ geht $\tfrac{1}{x-1} \to 0$).

> Merksatz: Derselbe Limes liefert sowohl den Rand des Wertebereichs (§4) als auch die Asymptote.

→ [Rezept 09: Grenzwerte](../rezepte/09_grenzwerte.md)

---

## 6. Gebrochen-rationale Funktionen

Funktionen der Form „Polynom durch Polynom".

$$f(x) = \frac{Z(x)}{N(x)}$$

Eine **Polstelle** ist eine Definitionslücke, an der $f$ gegen $\pm\infty$ geht — dort liegt eine senkrechte Asymptote.

- **$\mathbb{D}$:** $\mathbb{R}$ ohne die Nennernullstellen (also ohne alle $x$, für die $N(x) = 0$ ist)
- **Hebbare Lücke:** Zähler und Nenner lassen sich durch denselben Faktor kürzen → Loch im Graphen, **keine** Polstelle
- **Polstelle:** Nennernullstelle bleibt auch nach dem Kürzen stehen → senkrechte Asymptote

> **Beispiele:**
> - $f(x) = \dfrac{1}{x}$ → Polstelle bei $x = 0$ (Nenner wird $0$, kürzen geht nicht).
> - $g(x) = \dfrac{x^2 - 1}{x - 1} = \dfrac{(x-1)(x+1)}{x-1} = x + 1$ (für $x \neq 1$) → bei $x = 1$ nur **hebbare Lücke**, keine Polstelle.

**Waagrechte Asymptote aus Gradvergleich** (Zähler- vs. Nennergrad):
- Zählergrad $<$ Nennergrad → $y = 0$
- Zählergrad $=$ Nennergrad → $y =$ Verhältnis der Leitkoeffizienten (Zahlen vor den höchsten Potenzen)
- Zählergrad $=$ Nennergrad $+1$ → schräge Asymptote (Polynomdivision)

→ [Rezept 12: Gebrochen-rationale Funktionen](../rezepte/12_gebrochen_rational.md)

---

## 7. Kurvendiskussion (Kurzfassung)

Einen Graphen systematisch untersuchen.

1. Definitionsbereich
2. Spiegelung prüfen (Symmetrie):
   - $f(-x) = f(x)$ → gespiegelt an der $y$-Achse (achsensymmetrisch)
   - $f(-x) = -f(x)$ → gespiegelt am Ursprung (punktsymmetrisch)
3. Nullstellen: $f(x) = 0$
4. $y$-Achsenabschnitt: $f(0)$
5. Ableitungen $f'$, $f''$
6. **Extrema (Hoch-/Tiefpunkte):** $f'(x) = 0$ **und** $f''(x) \neq 0$
   - $f'' < 0$ → Hochpunkt (lokales Maximum)
   - $f'' > 0$ → Tiefpunkt (lokales Minimum)
   - $f'' = 0$ → Vorzeichenwechsel von $f'$ prüfen
7. **Wendepunkte:** $f''(x) = 0$ **und** $f'''(x) \neq 0$ (oder Vorzeichenwechsel von $f''$)
8. Wo der Graph steigt oder fällt (Monotonie; Vorzeichen von $f'$)
9. Wie der Graph gekrümmt ist (Krümmung; Vorzeichen von $f''$)
10. Verhalten für $x \to \pm\infty$
11. Graph skizzieren

→ Komplett: [Cheatsheet Kurvendiskussion](../sitzung_02/cheatsheet_kurvendiskussion.md) · [Rezept 01](../rezepte/01_kurvendiskussion.md)

---

## 8. Tangente und Normale

**Tangente an Stelle $a$** (Gerade, die den Graphen dort berührt):
$$t(x) = f'(a) \cdot (x - a) + f(a)$$

**Normale** (steht senkrecht auf der Tangente):
$$n(x) = -\frac{1}{f'(a)} \cdot (x - a) + f(a)$$

**Externe Tangente** (Punkt $P$ liegt **nicht** auf dem Graphen):
- Tangente an Stelle $a$ ansetzen, $P$ einsetzen
- Gleichung nach $a$ auflösen (oft quadratisch → zwei Tangenten möglich)

> Falle: $(x - a)$ vergessen! Nicht einfach nur $f'(a) \cdot x$ schreiben.

→ [Rezept 02: Tangente und Normale](../rezepte/02_tangente_normale.md)

---

## 9. Graphen zuordnen — $f \leftrightarrow f' \leftrightarrow F$

| Beobachtung in $f$ | in $f'$ | in $F$ |
|---|---|---|
| Hoch- oder Tiefpunkt (Extremum) | Nullstelle mit Vorzeichenwechsel | Wendepunkt |
| Wendepunkt | Hoch- oder Tiefpunkt (Extremum) | — |
| steigt ↗ | $f' > 0$ | $F$ ist nach oben gekrümmt |
| fällt ↘ | $f' < 0$ | $F$ ist nach unten gekrümmt |
| Nullstelle mit Vorzeichenwechsel | — | Hoch- oder Tiefpunkt (Extremum) in $F$ |

> Merksatz: **Eine Stufe hoch = Steigung ablesen. Eine Stufe runter = Fläche integrieren.**

→ [Rezept 03: Graphen zuordnen](../rezepte/03_graphen_zuordnen.md)

---

## 10. Graphentransformationen

$$g(x) = a \cdot f\bigl(b(x - c)\bigr) + d$$

| Teil | Wirkung |
|---|---|
| $+d$ außen | nach oben um $d$ |
| $\cdot a$ außen | in $y$-Richtung strecken/spiegeln |
| $-c$ innen | nach **rechts** um $c$ (nicht links!) |
| $\cdot b$ innen | in $x$-Richtung stauchen (Faktor $\tfrac{1}{b}$) |

> Falle: $f(x - 3)$ verschiebt **nach rechts**, nicht nach links.

→ [Rezept 04: Graphentransformationen](../rezepte/04_graphentransformationen.md)

---

## 11. Funktionenschar & Ortskurve

Funktionen mit Parameter $k$; die Ortskurve ist die Kurve, auf der alle Extrempunkte der Schar liegen.

Den Parameter $k$ als **Konstante** behandeln — nicht nach $x$ mit ableiten!

**Ortskurve der Extrempunkte:**
1. Extremstelle in Abhängigkeit von $k$: $x_E(k)$, $y_E(k)$
2. $k$ aus $x_E = \dots$ nach $k$ umformen
3. In $y_E$ einsetzen → Ortskurve $y(x)$

→ [Rezept 06: Funktionenschar](../rezepte/06_funktionenschar.md)

---

## 12. Extremwertprobleme (Optimierung)

Größten oder kleinsten Wert einer Größe finden.

1. Skizze + Variablen benennen
2. **Zielfunktion** aufstellen (was maximal/minimal werden soll: $A$, $V$, Kosten, …)
3. **Nebenbedingung** finden (steht im Text!)
4. Nebenbedingung auflösen, einsetzen → Zielfunktion mit **einer** Variablen
5. $f'(x) = 0$ → Extremstelle, mit $f''$ oder am Rand prüfen
6. **Randwerte** des Definitionsbereichs nicht vergessen!
7. Antwort im Sachkontext **mit Einheiten**

> Fallen: negative Längen, Randwerte ignoriert, Nebenbedingung übersehen.

→ [Rezept 07: Extremwertprobleme](../rezepte/07_extremwertprobleme.md)

---

## 13. Integrale & Flächen

**Fläche = Betrag des Integrals.** Vorzeichen beachten!

$$A = \left\lvert \int_a^b f(x)\,dx \right\rvert$$

- Wechselt $f$ das Vorzeichen im Intervall → Nullstellen finden, **stückweise** integrieren, Beträge addieren.
- **Fläche zwischen zwei Kurven:**
  $$A = \int_a^b \lvert f_\text{oben}(x) - f_\text{unten}(x) \rvert \,dx$$

→ [Rezept 08: Integrale & Fläche](../rezepte/08_integrale_flaeche.md)

---

## 14. Integrale im Sachkontext

Integrale in Textaufgaben — was bedeutet das Integral inhaltlich?

| Was? | Formel |
|---|---|
| Gesamtänderung | $\displaystyle\int_a^b f'(t)\,dt = f(b) - f(a)$ |
| Bestand zum Zeitpunkt $b$ | $f(b) = f(a) + \displaystyle\int_a^b f'(t)\,dt$ |
| Durchschnittswert | $\bar{f} = \dfrac{1}{b-a} \displaystyle\int_a^b f(x)\,dx$ |

**Einheiten:** Beim Integrieren kürzt sich die Zeit weg — aus „Liter/Stunde" wird „Liter".

> Falle: **Durchschnittswert** $\neq$ **mittlere Änderungsrate**.
> Die mittlere Änderungsrate ist $\dfrac{f(b) - f(a)}{b - a}$.

→ [Rezept 11: Sachkontext Integral](../rezepte/11_sachkontext_integral.md)

---

## 15. Umkehrfunktion

Macht die Funktion rückwärts: aus $y$ wird wieder $x$.

**Voraussetzung:** $f$ streng monoton auf $D$ (also im ganzen Definitionsbereich immer nur steigend oder immer nur fallend) — hinreichend dafür: $f'(x) > 0$ überall oder $f'(x) < 0$ überall. (Einzelne Nullstellen von $f'$ ohne Vorzeichenwechsel sind erlaubt: $x^3$ ist streng monoton steigend, obwohl die Ableitung bei $x = 0$ null ist.)

**Bestimmen:**
1. $y = f(x)$ nach $x$ auflösen
2. $x$ und $y$ vertauschen
3. $D_{f^{-1}} = W_f$ und $W_{f^{-1}} = D_f$ (immer mit angeben!)

**Merkpaare:** $e^x \leftrightarrow \ln(x)$ · $x^2 \ (x \geq 0) \leftrightarrow \sqrt{x}$

**Graph:** Spiegelung an der Geraden $y = x$.

→ [Rezept 13: Umkehrfunktion](../rezepte/13_umkehrfunktion.md)

---

## 16. Rotationsvolumen

Volumen eines Körpers, der entsteht, wenn man den Graphen um eine Achse dreht.

**Um $x$-Achse:**
$$V = \pi \int_a^b \bigl[f(x)\bigr]^2\,dx$$

**Um $y$-Achse** (mit Umkehrfunktion, $y$-Grenzen!):
$$V = \pi \int_c^d \bigl[f^{-1}(y)\bigr]^2\,dy$$

**Hohlkörper** (außen $f$, innen $g$):
$$V = \pi \int_a^b \Bigl(\bigl[f(x)\bigr]^2 - \bigl[g(x)\bigr]^2\Bigr)\,dx$$

> Fallen: $\pi$ vergessen. Quadrate **einzeln** bilden, nicht $(f - g)^2$. Falsche Grenzen bei $y$-Achse.

→ [Rezept 14: Rotationsvolumen](../rezepte/14_rotationsvolumen.md)

---

## 17. Uneigentliche Integrale

Integrale mit unendlicher Grenze oder an einer Polstelle.

Bei unendlicher Grenze oder Polstelle: **Grenzwert bilden**, niemals $\infty$ direkt einsetzen.

$$\int_a^\infty f(x)\,dx = \lim_{b \to \infty} \int_a^b f(x)\,dx$$

- **Konvergent** = das Integral hat einen endlichen Wert
- **Divergent** = das Integral hat keinen endlichen Wert
- **Merkregel:** $\displaystyle\int_1^\infty \frac{1}{x^p}\,dx$ konvergiert nur für $p > 1$

> Falle: „$f(x) \to 0 \Rightarrow$ Integral konvergiert" ist **falsch** (Gegenbeispiel: $\tfrac{1}{x}$).

→ [Rezept 15: Uneigentliche Integrale](../rezepte/15_uneigentliche_integrale.md)

---

## 18. Sekanten- und Tangentensteigung

Steigung zwischen zwei Punkten (Sekante) vs. Steigung an einem einzelnen Punkt (Tangente).

Zwischen $P(p \mid f(p))$ und $Q(q \mid f(q))$:
$$m(q) = \frac{f(q) - f(p)}{q - p}$$

Für $q \to p$: **Tangentensteigung $f'(p)$**.

Aufgaben vom Typ „welche Steigungen sind möglich?" → $m(q)$ als Funktion von $q$ untersuchen, Wertebereich bestimmen.

> Falle: Grenzwert wird meist **nicht angenommen** → runde Klammer, nicht eckig.

→ [Rezept 10: Sekanten/Tangenten Vergleich](../rezepte/10_sekanten_tangenten_vergleich.md)

---

## Lern-Checkliste vor der Prüfung

- [ ] Ableitungs- und Stammfunktionstabelle aus dem Kopf
- [ ] Kettenregel sicher (besonders $e^{(\dots)}$ und $\sqrt{(\dots)}$)
- [ ] „Zeigen Sie"-Aufgaben: von $f$ starten, **nie** vom Ergebnis
- [ ] Termumformung: Hauptnenner mit Wurzel-Trick
- [ ] Kurvendiskussion als Fließband
- [ ] $\pi$ nicht vergessen bei Rotationsvolumen
- [ ] Einheiten im Sachkontext
- [ ] Bei Wertebereich: eckig = angenommen, rund = nur Grenzwert

# Cheatsheet: Stochastik (Bayern Abitur, eA)

Überblick über alle Themen. Reihenfolge nach Prüfungs-Häufigkeit.
Separate Cheatsheets:
- [Cheatsheet Analysis](analysis.md)
- [Cheatsheet Grundfunktionen](grundfunktionen.md)

Hilfsmittel im Teil B: **Formeldokument**, **stochastische Tabellen** (kumulierte Binomialverteilung) und Taschenrechner (WTR oder MMS).
Im Teil A: **nichts** — alle Wahrscheinlichkeiten als Bruch oder Term stehen lassen.

---

## 0. Operatoren — was verlangt die Aufgabe?

Identisch zu Analysis (siehe [Cheatsheet Analysis §0](analysis.md#0-operatoren--was-verlangt-die-aufgabe)).

Stochastik-spezifisch:

| Operator | Was tun? |
|----------|----------|
| **Beschreiben Sie ein Ereignis, dessen Wahrscheinlichkeit mit dem Term … berechnet werden kann** | Aus dem Term das Ereignis im Sachzusammenhang **rekonstruieren** (siehe §7) |
| **Begründen Sie, dass … stochastisch (un)abhängig sind** | $P(A \cap B)$ vs. $P(A) \cdot P(B)$ vergleichen (siehe §4) |

---

## 1. Grundbegriffe & Zählprinzip

| Begriff | Bedeutung |
|---|---|
| **Ergebnismenge $\Omega$** | alle möglichen Ausgänge |
| **Ereignis $A$** | Teilmenge von $\Omega$ |
| **Gegenereignis $\overline{A}$** | $P(\overline{A}) = 1 - P(A)$ |
| **Laplace** | alle Ergebnisse gleich wahrscheinlich → $P(A) = \dfrac{\lvert A \rvert}{\lvert \Omega \rvert}$ |

**Zählprinzip:** Bei $k$ Stufen mit jeweils $n_1, n_2, \dots, n_k$ Möglichkeiten gibt es insgesamt $n_1 \cdot n_2 \cdots n_k$ Ergebnisse.

> **Beispiel:** Vier Würfe eines Würfels → $6^4 = 1296$ Ergebnisse.

---

## 2. Kombinatorik

Vier Standardmodelle. Welches passt, hängt davon ab, ob die Reihenfolge zählt und ob mit Zurücklegen gezogen wird.

| Modell | Formel | Wann? | Typische Beispiele |
|---|---|---|---|
| **Permutation** (alle anordnen) | $n!$ | alle $n$ Objekte in eine Reihenfolge | $n$ Personen in einer Reihe aufstellen; $n$ Bücher ins Regal; alle $n$ Buchstaben anordnen |
| **Variation mit Zurücklegen** | $n^k$ | $k$ Stellen, Reihenfolge zählt, Wiederholung erlaubt | Kennwort aus $k$ Zeichen ($26^k$ bei Kleinbuchstaben); Würfel $k$-mal werfen ($6^k$ Ergebnisse); $k$-stellige Zahlencodes |
| **Variation ohne Zurücklegen** | $\dfrac{n!}{(n-k)!}$ | $k$ Stellen, Reihenfolge zählt, **keine** Wiederholung | Sieger/Zweiter/Dritter aus $n$ Sportlern; $k$ Plätze nacheinander besetzen; PIN aus verschiedenen Ziffern |
| **Kombination ohne Zurücklegen** | $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ | $k$ aus $n$ ziehen, Reihenfolge **egal** | Lotto „6 aus 49"; $k$ Personen aus $n$ auslosen; Kartenhand austeilen; Tulpenstrauß zusammenstellen |

**Binomialkoeffizient:**
$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!} \qquad \binom{n}{0}=1, \quad \binom{n}{n}=1, \quad \binom{n}{k}=\binom{n}{n-k}$$

> **Beispiel:** Aus 10 Gummibärchen 3 ziehen: $\binom{10}{3} = 120$ Möglichkeiten.

### Welches Modell passt? — Fragebaum

```
Frage 1: Spielt die Reihenfolge eine Rolle?
  ├─ JA  → Frage 2a: Werden alle Objekte angeordnet?
  │         ├─ JA   → Permutation                    n!
  │         └─ NEIN → Frage 2b: Mit Wiederholung?
  │                    ├─ JA   → Variation m. Z.    n^k
  │                    └─ NEIN → Variation o. Z.    n!/(n-k)!
  │
  └─ NEIN → Kombination                              C(n, k)
```

**Signalwörter im Aufgabentext:**

| Signalwort/-formulierung | spricht für … |
|---|---|
| „in einer Reihe", „nebeneinander", „anordnen", „aufstellen" | **Permutation** |
| „nacheinander", „1./2./3. Platz", „Reihenfolge der Ziehung zählt" | **Variation** (Reihenfolge **ja**) |
| „Zeichen können mehrfach vorkommen", „mit Zurücklegen", „$k$-mal werfen" | **mit Zurücklegen** |
| „verschiedene", „unterschiedliche", „ohne Zurücklegen" | **ohne Zurücklegen** |
| „auswählen", „aussuchen", „zusammenstellen", „ziehen ohne Beachtung der Reihenfolge", „in beliebiger Reihenfolge" | **Kombination** |
| „Anzahl der Möglichkeiten, $k$ aus $n$ zu …" + keine Reihenfolge-Erwähnung | **Kombination** |

> **Praxistipp:** Wenn im Text steht „Anzahl der Möglichkeiten" und nicht klar wird, ob die Reihenfolge zählt, frag dich: *„Macht es einen Unterschied, ob ich erst Tulpe A und dann B nehme, oder umgekehrt?"* — Wenn nein → Kombination.

**Klassische Fallen:**
- „in beliebiger Reihenfolge" → $\binom{n}{k}$ (Kombination), nicht $\dfrac{n!}{(n-k)!}$.
- „in einer Reihe nebeneinander" + zusätzliche Bedingung („drei nebeneinander") → Permutation mit **Block-Trick** (die drei als Block sehen, dann den Block intern noch mal $3!$).
- Wahrscheinlichkeit beim Lotto: $\dfrac{1}{\binom{49}{6}}$, **nicht** $\dfrac{1}{49 \cdot 48 \cdots 44}$ — bei „Reihenfolge egal" ist der Nenner kleiner.

**Aufgaben:** IlluPA 2026 A8 (Tulpensträuße) · ISB 2024 B AG2 #3 (Kennwörter) · ISB 2020 B AG2 #1a (Spielführer in Reihe).

---

## 3. Mehrstufige Zufallsexperimente — Baumdiagramm & Pfadregeln

**Pfadregel 1 (Multiplikation):** Wahrscheinlichkeiten **entlang eines Pfades** multiplizieren.

**Pfadregel 2 (Addition):** Wahrscheinlichkeiten **mehrerer Pfade** für dasselbe Ereignis addieren.

> **Beispiel:** Zwei Würfel werden geworfen. Wahrscheinlichkeit für „Augensumme $7$":
>
> $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$ — sechs Pfade, jeweils $\tfrac{1}{36}$ → $P(X=7) = \tfrac{6}{36} = \tfrac{1}{6}$.

**Mit/ohne Zurücklegen** unterscheiden:
- **Mit Zurücklegen:** Wahrscheinlichkeiten bleiben in jeder Stufe gleich.
- **Ohne Zurücklegen:** Nenner wird in jeder Stufe um $1$ kleiner.

> **Beispiel ohne Zurücklegen** (5 rote, 3 blaue Kugeln, zwei ziehen):
> $P(\text{beide rot}) = \dfrac{5}{8} \cdot \dfrac{4}{7} = \dfrac{20}{56} = \dfrac{5}{14}$.

**Aufgaben:** ISB 2020 A AG1 (Würfel + Glücksrad) · ISB 2024 A AG1 (Gewinnwahrscheinlichkeit $\tfrac14$) · ISB 2025 A (Würfelprodukt) · IlluPA 2026 A7 (drei Würfel).

---

## 4. Vierfeldertafel & bedingte Wahrscheinlichkeit

Das **Standard-Schema** für jede Aufgabe mit zwei Merkmalen.

| | $B$ | $\overline{B}$ | Summe |
|---|---|---|---|
| $A$ | $P(A \cap B)$ | $P(A \cap \overline{B})$ | $P(A)$ |
| $\overline{A}$ | $P(\overline{A} \cap B)$ | $P(\overline{A} \cap \overline{B})$ | $P(\overline{A})$ |
| Summe | $P(B)$ | $P(\overline{B})$ | $1$ |

**Vorgehen:** Gegebene Werte eintragen → fehlende Felder durch **Differenz zur Randsumme** ergänzen.

**Bedingte Wahrscheinlichkeit:**
$$P_A(B) = \frac{P(A \cap B)}{P(A)}$$

In Worten: Wahrscheinlichkeit von $B$, **gegeben dass** $A$ schon eingetreten ist.

> **Beispiel:** $P(A) = 0{,}3$, $P(A \cap B) = 0{,}12$ → $P_A(B) = \tfrac{0{,}12}{0{,}3} = 0{,}4$.

**Satz von Bayes** (umgekehrte Bedingung):
$$P_B(A) = \frac{P_A(B) \cdot P(A)}{P(B)}$$

> Bei Bayes-Aufgaben fast immer den Weg über die Vierfeldertafel gehen — schneller und weniger fehleranfällig.

**Aufgaben:** ISB 2020 B AG1 #1 (Internet/Streaming) · ISB 2024 B AG1 #1d (Retoure/Kleidung) · ISB 2025 B AG1 #2 (Kartenkauf) · ISB 2024 B AG2 #1 (Abonnenten/Alter) · IlluPA 2026 B3 #1 (Radfahrer/Helm).

---

## 5. Stochastische Unabhängigkeit

$A$ und $B$ sind **stochastisch unabhängig**, wenn gilt:
$$P(A \cap B) = P(A) \cdot P(B)$$

Äquivalent: $P_A(B) = P(B)$ — das Wissen um $A$ ändert nichts an der Wahrscheinlichkeit von $B$.

**Vorgehen bei „Untersuchen Sie auf Unabhängigkeit":**
1. $P(A)$, $P(B)$, $P(A \cap B)$ bestimmen (Vierfeldertafel).
2. Vergleichen: $P(A) \cdot P(B) \stackrel{?}{=} P(A \cap B)$.
3. Antwort im Klartext: „… sind (un)abhängig, weil …".

> **Falle:** „A und B sind disjunkt" $\neq$ „A und B sind unabhängig". Disjunkte Ereignisse mit $P(A), P(B) > 0$ sind sogar **immer abhängig**.

**Aufgaben:** ISB 2020 B AG1 #1 · ISB 2022 B AG2 #1a (Baumpatenschaft/Umweltwoche) · ISB 2023 B AG2 #2 (Glücksrad) · IlluPA 2026 B3 #1a.

---

## 6. Wahrscheinlichkeitsverteilung, Erwartungswert, Varianz

Eine **Zufallsgröße $X$** ordnet jedem Ergebnis eine Zahl zu. Die **Wahrscheinlichkeitsverteilung** zeigt, mit welcher Wahrscheinlichkeit jeder Wert vorkommt.

Tabellenform:

| Wert $x_i$ | $x_1$ | $x_2$ | $\dots$ | $x_n$ |
|---|---|---|---|---|
| $P(X=x_i)$ | $p_1$ | $p_2$ | $\dots$ | $p_n$ |

**Bedingung:** $\sum p_i = 1$.

**Erwartungswert** (im Mittel zu erwartender Wert):
$$E(X) = \sum_i x_i \cdot p_i$$

**Varianz** (durchschnittliche quadratische Abweichung):
$$\mathrm{Var}(X) = \sum_i (x_i - E(X))^2 \cdot p_i$$

**Standardabweichung:** $\sigma = \sqrt{\mathrm{Var}(X)}$.

> **Beispiel** (Glücksrad mit Auszahlung):
>
> | $k$ | $0$ | $5$ | $20$ |
> |---|---|---|---|
> | $P(X=k)$ | $\tfrac{1}{2}$ | $\tfrac{1}{3}$ | $\tfrac{1}{6}$ |
>
> $E(X) = 0 \cdot \tfrac12 + 5 \cdot \tfrac13 + 20 \cdot \tfrac16 = \tfrac{5}{3} + \tfrac{20}{6} = 5$.

**Faires Spiel:** Einsatz $=$ erwartete Auszahlung, also $E(\text{Gewinn}) = 0$.

**Aufgaben:** ISB 2020 A AG2 (Erwartungswert auflösen) · ISB 2020 B AG1 #3 (Verteilung mit Varianz) · ISB 2021 B AG2 #4 (Goldäpfel, relative Standardabweichung) · ISB 2022 B AG2 #2-3 (Glücksrad-Spiel „2022") · ISB 2024 B AG1 #2 (E und Var aus Gleichungssystem ablesen).

---

## 7. Bernoulli & Binomialverteilung — DAS zentrale Werkzeug

**Bernoulli-Experiment:** ein Versuch mit genau zwei Ausgängen (Treffer mit Wahrscheinlichkeit $p$, kein Treffer mit $1-p$).

**Bernoulli-Kette:** $n$-mal unabhängig hintereinander dasselbe Bernoulli-Experiment.

**Binomialverteilung** $X \sim B(n; p)$ — Anzahl der Treffer in $n$ Versuchen:

$$P(X = k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$$

| Größe | Formel |
|---|---|
| Erwartungswert | $E(X) = n \cdot p$ |
| Varianz | $\mathrm{Var}(X) = n \cdot p \cdot (1-p)$ |
| Standardabweichung | $\sigma = \sqrt{n \cdot p \cdot (1-p)}$ |

**Wann ist $X$ binomialverteilt?** Drei Bedingungen, alle drei nötig:
1. **fester** Stichprobenumfang $n$
2. nur zwei Ausgänge pro Versuch (Treffer / kein Treffer)
3. Versuche sind **unabhängig**, $p$ bleibt **gleich** (also „mit Zurücklegen" oder große Grundmenge)

### Stochastische Tabellen lesen (Teil B)

In den Tabellen steht die **kumulierte** Binomialverteilung $P(X \le k) = \sum_{i=0}^{k} \binom{n}{i} p^i (1-p)^{n-i}$.

| Gefragt | Umformung |
|---|---|
| $P(X = k)$ | $P(X \le k) - P(X \le k-1)$ |
| $P(X \le k)$ | direkt ablesen |
| $P(X < k)$ | $P(X \le k-1)$ |
| $P(X \ge k)$ | $1 - P(X \le k-1)$ |
| $P(X > k)$ | $1 - P(X \le k)$ |
| $P(a \le X \le b)$ | $P(X \le b) - P(X \le a-1)$ |

> **Faustregel:** „mindestens $k$" → $1 - P(X \le k-1)$. Das $-1$ ist die häufigste Falle.

### Mindestanzahl bestimmen

„Wie groß muss $n$ sein, damit $P(\text{mind. 1 Treffer}) > q$?"

$$P(X \ge 1) = 1 - P(X = 0) = 1 - (1-p)^n > q$$

Auflösen nach $n$:
$$(1-p)^n < 1-q \quad\Leftrightarrow\quad n > \frac{\ln(1-q)}{\ln(1-p)}$$

Ungleichungszeichen kehrt sich um, weil im letzten Schritt durch $\ln(1-p) < 0$ geteilt wird (Logarithmieren selbst erhält die Ungleichung).

> **Beispiel:** $p = 0{,}05$, $q = 0{,}99$ → $n > \tfrac{\ln 0{,}01}{\ln 0{,}95} \approx 89{,}8$ → $n = 90$.

**Aufgaben Binomial allgemein:** ISB 2020 B AG1 #2 (Internet, $n=10$, $p=0{,}2$) · ISB 2022 B AG1 #1 (Pflanzenschutz, $n=15$, $p=0{,}05$) · ISB 2025 B AG1 #1a (Brotzeitteller, $n=200$, $p=0{,}65$) · IlluPA 2026 B4 #1 (CDs, $n=12$, $p=0{,}6$).
**Aufgaben Mindestanzahl:** ISB 2020 B AG1 #2c · ISB 2022 B AG1 #1b · ISB 2024 B AG1 #1c · IlluPA 2026 B3 #2 (Reifenpanne).

---

## 8. Term-Interpretation (Pflichtskill Teil A)

„Beschreiben Sie ein Ereignis, dessen Wahrscheinlichkeit mit dem Term … berechnet werden kann."

Typische Musterterme zum Auswendiglernen:

| Term | Bedeutung |
|---|---|
| $\binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$ | „**genau** $k$ Treffer bei $n$ Versuchen", $p$ pro Versuch |
| $\displaystyle\sum_{k=0}^{m} \binom{n}{k} p^k (1-p)^{n-k}$ | „**höchstens** $m$ Treffer bei $n$ Versuchen" |
| $1 - \displaystyle\sum_{k=0}^{m} \binom{n}{k} p^k (1-p)^{n-k}$ | „**mehr als** $m$ Treffer bei $n$ Versuchen" |
| $1 - (1-p)^n$ | „**mindestens ein** Treffer bei $n$ Versuchen" |
| $p \cdot (1-p)^{k-1}$ | „erster Treffer **genau** beim $k$-ten Versuch" (geometrisch) |
| $\dfrac{a \cdot (a-1) \cdots}{N \cdot (N-1) \cdots}$ | Ziehen **ohne Zurücklegen**, in dieser Reihenfolge |
| $\dfrac{\binom{a}{k}\binom{N-a}{n-k}}{\binom{N}{n}}$ | $k$ Treffer in einer Stichprobe vom Umfang $n$ aus Urne mit $a$ Treffern und $N-a$ Nicht-Treffern (hypergeometrisch, §9) |

**Vorgehen beim Deuten:**
1. Welche Zahlen tauchen auf? $n$, $k$, $p$ identifizieren.
2. Welche Termstruktur? Binomialkoeffizient → Reihenfolge egal; Summe → „höchstens"; Differenz zu $1$ → Gegenereignis.
3. **Im Sachzusammenhang formulieren** — nicht nur „Anzahl Treffer", sondern „Anzahl der Pflanzen, die …".

> **Beispiel:** Term $\binom{5}{2} \cdot \left(\tfrac{1}{4}\right)^2 \cdot \left(\tfrac{3}{4}\right)^3$, im Kontext „Spiel wird $5$-mal gespielt, Gewinnwahrscheinlichkeit $\tfrac14$" → „Genau zweimal gewinnen bei fünf Spielen."

**Aufgaben:** ISB 2024 A AG1 (genau Term oben) · ISB 2023 A AG1 ($\left(\tfrac34\right)^5$, Tetraeder) · ISB 2020 B AG1 #2b ($0{,}2^{10} + 0{,}8^{10}$) · ISB 2020 B AG2 #3b (Summe von Produkten) · ISB 2024 B AG1 #1b · ISB 2025 B AG1 #1d (ohne Zurücklegen).

---

## 9. Hypergeometrische Verteilung — Ziehen ohne Zurücklegen

Urne mit $N$ Kugeln, davon $a$ „Treffer". Es werden $n$ Kugeln **ohne Zurücklegen** gezogen. Wahrscheinlichkeit für genau $k$ Treffer:

$$P(X = k) = \frac{\binom{a}{k} \cdot \binom{N-a}{n-k}}{\binom{N}{n}}$$

> **In den stochastischen Tabellen steht die hypergeometrische Verteilung nicht.** Werte direkt mit Binomialkoeffizienten ausrechnen.

**Faustregel:** Wenn $n$ klein ist gegenüber $N$ (etwa $n < 0{,}05 \cdot N$), kann das Ziehen ohne Zurücklegen näherungsweise binomial modelliert werden — sofern die Aufgabe nichts anderes vorgibt.

> **Falle:** Steht im Text „zufällig ausgewählt aus großer Grundmenge" → fast immer Binomial-Modell anwendbar. Steht „Urne mit $N$ Kugeln" und $n$ ist relativ groß → hypergeometrisch.

**Aufgaben:** ISB 2025 B AG1 #1b (5 Bücher aus 200 Gästen) · ISB 2024 B AG1 #1e-f (Pakete aus Transportkiste) · ISB 2023 B AG1 #1e (10 Plug-in aus 40) · ISB 2021 B AG2 #1 (drei Gummibärchen gleicher Farbe).

---

## 10. Geometrische Verteilung — Warten auf den ersten Treffer

$X$ = Nummer des Versuchs, bei dem **erstmals** ein Treffer fällt:

$$P(X = k) = (1-p)^{k-1} \cdot p$$

(Die ersten $k-1$ Versuche sind keine Treffer, der $k$-te ist ein Treffer.)

> **Beispiel:** Würfel, „bis zur ersten 6". $P(X = 4) = \left(\tfrac56\right)^3 \cdot \tfrac16 = \tfrac{125}{1296}$.

**Aufgaben:** ISB 2021 B AG1 #1b (5. Familie ist erste mit Bollerwagen) · ISB 2022 A AG2 #2a (Würfel bis zur ersten 1).

---

## 11. Sigma-Umgebung & Streumaße

**Faustregel** für binomialverteiltes $X$ mit $\sigma = \sqrt{n p (1-p)}$:

| Bereich | Wahrscheinlichkeit (ca.) |
|---|---|
| $[\mu - \sigma; \mu + \sigma]$ | $\approx 68\,\%$ |
| $[\mu - 2\sigma; \mu + 2\sigma]$ | $\approx 95\,\%$ |
| $[\mu - 3\sigma; \mu + 3\sigma]$ | $\approx 99{,}7\,\%$ |

(Gilt erst bei großen $n$ — als Sigma-Regeln.)

**Standardabweichung** ist immer die Wurzel aus der Varianz:
$$\sigma = \sqrt{\mathrm{Var}(X)}$$

**Aufgaben:** ISB 2021 B AG1 #1c (kleinster symm. Bereich um $\mu$ mit $P \ge 75\,\%$) · ISB 2022 B AG1 #1c (Standardabweichung in Bezug auf relative Häufigkeit).

---

## 12. Hypothesentest (einseitig)

Schema bei „Anteil ist höchstens $p_0$" / „Anteil ist mindestens $p_0$".

**Begriffe:**

| Begriff | Bedeutung |
|---|---|
| **Nullhypothese $H_0$** | zu prüfende Annahme; unter ihr werden die Wahrscheinlichkeiten berechnet. Verworfen wird $H_0$ nur bei hinreichend extremem Stichprobenergebnis |
| **Alternative $H_1$** | das Gegenteil von $H_0$; gilt als (vorläufig) plausibel, sobald $H_0$ verworfen wird |
| **Signifikanzniveau $\alpha$** | maximal akzeptierte Wahrscheinlichkeit, $H_0$ fälschlich abzulehnen |
| **Ablehnungsbereich** | Werte von $X$, bei denen $H_0$ verworfen wird |
| **Fehler 1. Art** | $H_0$ wird abgelehnt, obwohl sie **wahr** ist (Wahrscheinlichkeit $\le \alpha$) |
| **Fehler 2. Art** | $H_0$ wird **nicht** abgelehnt, obwohl sie **falsch** ist |

### Rechtsseitiger Test ($H_0: p \le p_0$)

Ablehnungsbereich: $\{k, k+1, \dots, n\}$ mit kleinstem $k$ so, dass
$$P_{p_0}(X \ge k) \le \alpha \quad\Leftrightarrow\quad 1 - P_{p_0}(X \le k-1) \le \alpha$$

### Linksseitiger Test ($H_0: p \ge p_0$)

Ablehnungsbereich: $\{0, 1, \dots, k\}$ mit größtem $k$ so, dass
$$P_{p_0}(X \le k) \le \alpha$$

### Fehler 2. Art berechnen

Bei tatsächlichem Anteil $p_1 \neq p_0$:
$$\beta = P_{p_1}(X \notin \text{Ablehnungsbereich})$$

> **Strategie in der Prüfung:** Hypothesentest-Aufgaben sind in 2024, 2025 und IlluPA 2026 alle dabei. Wenn die Zeit knapp ist: **Begriffe** ($H_0$, Ablehnungsbereich, Fehler 1./2. Art) verstehen und benennen können — schon für die Beschreibungs-Teilaufgaben gibt es 2–3 BE.

**Aufgaben:** ISB 2024 B AG2 #2 (Streamingdienst, kompletter Test) · ISB 2025 B AG2 #2c-d (Radausflügler, Entscheidungsregel + Fehler 2. Art) · IlluPA 2026 B4 #2 (CD-Hüllen).

---

## 13. Normalverteilung (neu im G9)

Eine **stetige** Zufallsgröße $X$ ist normalverteilt mit Erwartungswert $\mu$ und Standardabweichung $\sigma$, wenn ihre Dichtefunktion glockenförmig ist (Gauß-Kurve).

**68-95-99,7-Regel:**

| Bereich | Wahrscheinlichkeit |
|---|---|
| $[\mu - \sigma;\ \mu + \sigma]$ | $\approx 68\,\%$ |
| $[\mu - 2\sigma;\ \mu + 2\sigma]$ | $\approx 95\,\%$ |
| $[\mu - 3\sigma;\ \mu + 3\sigma]$ | $\approx 99{,}7\,\%$ |

**Symmetrie** der Dichtefunktion um $\mu$:
$$P(X > \mu + a) = P(X < \mu - a) = \frac{1 - P(\mu - a \le X \le \mu + a)}{2}$$

**Wirkung der Parameter** auf die Dichtekurve:
- Größeres $\sigma$ → flacher und breiter
- Verschiebung von $\mu$ → Kurve nach links/rechts verschoben

> **Beispiel** (IlluPA A3): $P(6 \le A \le 10) \approx 68\,\%$, also $\mu = 8$, $\sigma = 2$. Wahrscheinlichkeit $A > 10$:
>
> $P(A > 10) = \dfrac{1 - 0{,}68}{2} = 0{,}16 = 16\,\%$.

**Wenn mehr verlangt ist:** $\mu$ und $\sigma$ aus dem Dichteterm $\dfrac{1}{\sigma\sqrt{2\pi}}\,e^{-(x-\mu)^2 / (2\sigma^2)}$ ablesen. Intervallwahrscheinlichkeiten über die Verteilungsfunktion: $P(a \le X \le b) = F(b) - F(a)$ (mit MMS oder Tabelle).

**Aufgaben:** IlluPA 2026 A3 (einzige Aufgabe bisher; Pflichtteil A).

---

## 14. Lern-Checkliste vor der Prüfung

**Mechanische Skills (jede Prüfung):**
- [ ] Vierfeldertafel: Werte ergänzen mit Randsummen
- [ ] Bedingte Wahrscheinlichkeit: $P_A(B) = \dfrac{P(A\cap B)}{P(A)}$
- [ ] Unabhängigkeit prüfen: $P(A) \cdot P(B) \stackrel{?}{=} P(A \cap B)$
- [ ] Stochastische Tabellen lesen ($P(X=k)$, $P(X \ge k)$ richtig umformen — **Vorsicht** mit dem $-1$)
- [ ] Erwartungswert: $E(X) = \sum k \cdot P(X=k)$, bei Binomial: $E(X) = np$
- [ ] Mindestanzahl: $1 - (1-p)^n > q$ nach $n$ auflösen

**Term-Interpretation (Pflicht Teil A):**
- [ ] $\binom{n}{k} p^k (1-p)^{n-k}$ erkennen
- [ ] „mindestens / höchstens / genau" → richtige Termstruktur
- [ ] Im Sachzusammenhang formulieren, nicht abstrakt

**G9-Neuheiten:**
- [ ] 68-95-99,7-Regel der Normalverteilung
- [ ] Hypothesentest: Begriffe ($H_0$, Ablehnungsbereich, Fehler 1./2. Art) erklären können

**Fallen:**
- [ ] „mindestens $k$" $= 1 - P(X \le k - 1)$ — nicht $1 - P(X \le k)$
- [ ] Disjunkt $\neq$ unabhängig
- [ ] „ohne Zurücklegen" → Nenner wird kleiner; im Term tauchen Brüche wie $\tfrac{a-1}{N-1}$ auf
- [ ] Wahrscheinlichkeitsverteilung: Summe **muss** $1$ sein

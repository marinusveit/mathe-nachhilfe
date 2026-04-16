# Rezept: Operatoren im Abitur — Was wird erwartet?

## Warum das wichtig ist

Jede Abituraufgabe beginnt mit einem **Operator** (Aufgabenwort). Der Operator bestimmt, **wie ausführlich** und **in welcher Form** die Antwort sein muss. Wer den Operator falsch versteht, verliert Punkte — selbst wenn das Ergebnis stimmt.

## Die wichtigsten Operatoren

Alle Beispiele stammen aus dem echten bayerischen Abitur (Jahr in Klammern).

| Operator | Was der Korrektor erwartet | Beispiel aus dem Abitur |
|---|---|---|
| **Bestimmen** | Ergebnis selbst finden + vollständiger Rechenweg | „Bestimmen Sie rechnerisch die $x$-Koordinate von $W$ und beurteilen Sie, ob $W$ oberhalb der $x$-Achse liegt." (2025, Teil A) |
| **Ermitteln** | Wie „Bestimmen"; manchmal mit Abbildung/Kontrolle | „Ermitteln Sie $a$ und $b$." (2025, Teil A, nach Gleichungssystem) |
| **Berechnen** | Rechenweg besonders wichtig, numerisches Ergebnis | „Berechnen Sie den Wert des Integrals $\int_1^2 f(x)\,dx$." (2025, Teil A) |
| **Zeigen / Nachweisen** | Ergebnis ist **vorgegeben** — Rechenweg dahin lückenlos zeigen | „Zeigen Sie, dass $f'_a(0) = -a$ gilt." (2022, Teil A) · „Weisen Sie nach, dass $\frac{6-3x}{8\sqrt{6-x}}$ ein Term von $f'(x)$ ist." (2025, Teil B) |
| **Begründen** | Mathematisches Argument in Worten, ggf. kurze Rechnung | „Begründen Sie, dass die Funktion $f$ nicht umkehrbar, die Funktion $h$ jedoch umkehrbar ist." (2025, Teil B) |
| **Beschreiben** | In ganzen Sätzen formulieren, was man sieht oder tut | „Beschreiben Sie, wie man rechnerisch nachweisen kann, dass $2$ eine Wendestelle von $g$ ist." (2025, Teil A) |
| **Deuten / Interpretieren** | Ergebnis im Sachzusammenhang erklären (WARUM + WAS bedeutet das) | „Ermitteln Sie $\lim_{x \to 6} f'(x)$ und **deuten Sie das Ergebnis im Sachzusammenhang**." (2025, Teil B) |
| **Angeben** | Nur das Ergebnis, kein Rechenweg nötig | „Geben Sie $D_f$ und die Nullstellen von $f$ an." (2022, Teil A) |
| **Zeichnen / Einzeichnen** | Sauber ins Koordinatensystem eintragen (Lineal!) | „Zeichnen Sie den Graphen von $f$ für $-3 \leq x \leq 3$ in ein Koordinatensystem ein." (2025, Teil A) |
| **Skizzieren** | Grobe, aber korrekte Zeichnung; besondere Punkte markieren | seltener; oft in Kombination: „Zeigen Sie unter Verwendung einer geeigneten Skizze, dass …" (2025, Teil B) |
| **Beurteilen** | Aussage prüfen → wahr/falsch + mathematische Begründung | „Beurteilen Sie die folgende Aussage: $\int_0^{x_S} (g(x)-f(x))\,dx = 2 \cdot \int_0^{x_S} (x-f(x))\,dx$" (2025, Teil A) |

## Die drei wichtigsten Unterscheidungen

### 1. „Bestimmen" vs. „Zeigen"

| | Bestimmen | Zeigen |
|---|---|---|
| Ergebnis bekannt? | Nein — du findest es selbst | Ja — es steht in der Aufgabe |
| Was zählt? | Rechenweg + richtiges Ergebnis | Lückenloser Rechenweg zum gegebenen Ergebnis |
| Typischer Fehler | — | Ergebnis von hinten „einsetzen" statt herleiten |

### 2. „Begründen" vs. „Berechnen"

- **Begründen** = Argument (darf kurz sein, 1–3 Sätze + ggf. kleine Rechnung)
- **Berechnen** = vollständiger Rechenweg

Beispiel: „Begründen Sie, dass $f$ auf $[0;\infty)$ monoton steigend ist."
→ „$f'(x) = 2x + 1 > 0$ für alle $x \geq 0$, also ist $f$ dort streng monoton steigend." (Reicht!)

### 3. „Beschreiben" vs. „Erläutern"

- **Beschreiben** = WAS passiert
- **Erläutern** = WAS passiert + WARUM (im Sachkontext deuten)

## Allgemeine Tipps

- **Im Zweifel lieber zu viel schreiben** — fehlende Begründungen kosten Punkte, überflüssige nicht
- **Sachkontext-Aufgaben**: Immer mit Einheiten und Bezug zur Situation antworten, nicht nur Zahlen hinschreiben
- **„Zeigen Sie"**: Niemals das Ergebnis als Ausgangspunkt nehmen — immer von der gegebenen Funktion starten
- **Skizzen**: Achsenbeschriftung, besondere Punkte (Extrema, Wendepunkte, Nullstellen) markieren und beschriften
- **Antwortsatz**: Bei Sachkontext-Aufgaben immer einen Antwortsatz im Kontext der Aufgabe formulieren

## „Zeigen Sie" im Detail — der Operator mit dem höchsten Punkterisiko

**Die goldene Regel:** Starte bei der gegebenen Funktion und rechne vorwärts, bis der vorgegebene Term dasteht. Niemals rückwärts: „Wenn $f'(0) = -a$, dann …".

### Beispiel: Abitur 2022, Teil A (1 BE)

> Gegeben: $f_a(x) = a \cdot e^{-x} + 3$.
> **„Zeigen Sie, dass $f'_a(0) = -a$ gilt."**

**Richtige Lösung:**

$$f'_a(x) = a \cdot e^{-x} \cdot (-1) = -a \cdot e^{-x} \quad \text{(Kettenregel)}$$

$$f'_a(0) = -a \cdot e^0 = -a \cdot 1 = -a \quad \checkmark$$

**Typischer Fehler:** Nur „$f'_a(0) = -a$ ✓" ohne Herleitung — null Punkte, weil die Aufgabe genau den Weg dahin prüft.

### Beispiel: Abitur 2025, Teil B (6 BE)

> Gegeben: $f(x) = 0{,}25 \cdot (x+6) \cdot \sqrt{6-x}$.
> **„Weisen Sie nach, dass $\dfrac{6-3x}{8 \cdot \sqrt{6-x}}$ ein Term der ersten Ableitungsfunktion $f'$ von $f$ ist."**

**Vorgehen:**
1. Produktregel auf $f(x) = 0{,}25 \cdot (x+6) \cdot (6-x)^{1/2}$ anwenden
2. Gemeinsamen Nenner $\sqrt{6-x}$ bilden, Zähler zusammenfassen
3. Umformen, bis **genau der vorgegebene Term** dasteht

**Merke:** Die Zwischenschritte müssen für den Korrektor nachvollziehbar sein — auch ein kleiner ausgelassener Umformungsschritt kann BE kosten.

---
name: Lösungen Diagnosetest Sitzung 1
description: Musterlösungen + Bewertungsraster für den Diagnosetest der ersten Sitzung
---

# Lösungen — Diagnosetest Sitzung 1

> Für den Nachhilfelehrer. Neben jeder Aufgabe steht, **worauf typische Fehler hindeuten** — das hilft beim gezielten Nachfragen.

---

## Teil A: Ableitungen

### A1) Grundableitungen

**a)** f(x) = 3x⁴ − 2x² + 5x − 1
$$f'(x) = 12x^3 - 4x + 5$$
*Prüft: Potenzregel, Summenregel, Ableitung von Konstanten (−1 fällt weg).*

**b)** f(x) = √x = x^(1/2)
$$f'(x) = \tfrac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$$
*Prüft: Kann sie Wurzel als Potenz schreiben? Typischer Fehler: f'(x) = 1/(2x) oder gar nicht umgeschrieben.*

**c)** f(x) = 1/x² = x^(−2)
$$f'(x) = -2x^{-3} = -\frac{2}{x^3}$$
*Typischer Fehler: Vorzeichen vergessen oder Exponent falsch (−1 statt −3).*

---

### A2) Kettenregel

**a)** f(x) = (2x + 3)⁵
$$f'(x) = 5(2x+3)^4 \cdot 2 = 10(2x+3)^4$$
*Typischer Fehler: innere Ableitung (·2) vergessen.*

**b)** f(x) = e^(−2x)
$$f'(x) = e^{-2x} \cdot (-2) = -2e^{-2x}$$
*Typischer Fehler: Minus vergessen, oder e^(−2x) unverändert lassen.*

**c)** f(x) = sin(2x)
$$f'(x) = \cos(2x) \cdot 2 = 2\cos(2x)$$
*Prüft: sin' = cos **und** innere Ableitung nicht vergessen. Typische Fehler: f'(x) = cos(2x) (innere Ableitung vergessen), oder Vorzeichen von cos/sin verwechselt.*

---

### A3) Produkt- und Quotientenregel

**a)** f(x) = x² · eˣ
$$f'(x) = 2x \cdot e^x + x^2 \cdot e^x = (x^2 + 2x)\, e^x$$
*Merksatz: (u·v)' = u'v + uv'. Typischer Fehler: nur einzeln ableiten → 2x·eˣ.*

**b)** f(x) = x / (x² + 1)

Mit u = x, v = x² + 1, u' = 1, v' = 2x:
$$f'(x) = \frac{u'v - uv'}{v^2} = \frac{1 \cdot (x^2+1) - x \cdot 2x}{(x^2+1)^2} = \frac{1 - x^2}{(x^2+1)^2}$$
*Merksatz: (u/v)' = (u'v − uv') / v². Typische Fehler: Vorzeichen im Zähler verdreht (uv' − u'v), oder Nenner nicht quadriert.*

---

### A4) ln-Ableitung

f(x) = ln(3x)

**Weg 1 (Kettenregel):** f'(x) = (1/(3x)) · 3 = **1/x**
**Weg 2 (Logarithmengesetz):** ln(3x) = ln 3 + ln x → f'(x) = **1/x**

*Schön zum Diskutieren: Beide Wege führen zum selben Ergebnis — weil ln 3 eine Konstante ist.*

---

### A5) Höhere Ableitungen

f(x) = x³ − 6x² + 9x + 1
$$f'(x) = 3x^2 - 12x + 9$$
$$f''(x) = 6x - 12$$
*Prüft: Potenzregel mehrfach korrekt anwenden.*

---

### A6) Geometrische Bedeutung

**f'(x₀) ist die Steigung der Tangente an den Graphen von f im Punkt (x₀, f(x₀)).**

Akzeptable Antworten:
- „Steigung der Tangente"
- „momentane Änderungsrate von f bei x₀"
- „Grenzwert der Sekantensteigung"

*Wenn sie nur „Steigung" sagt: nachhaken „Steigung wovon?" — präzise Formulierung ist wichtig.*

---

## Teil B: Kurvendiskussion

### B1) f(x) = x³ − 3x

**a) Nullstellen:**
$$x^3 - 3x = 0 \iff x(x^2 - 3) = 0$$
$$\Rightarrow x_1 = 0,\ x_2 = \sqrt{3},\ x_3 = -\sqrt{3}$$

**b) Extrempunkte:**
f'(x) = 3x² − 3 = 0 → x² = 1 → x = ±1
f''(x) = 6x
- f''(−1) = −6 < 0 → **Hochpunkt** H(−1 | 2) (da f(−1) = −1 + 3 = 2)
- f''(1) = 6 > 0 → **Tiefpunkt** T(1 | −2) (da f(1) = 1 − 3 = −2)

**c) Wendepunkt:**
f''(x) = 6x = 0 → x = 0, f(0) = 0 → **WP(0 | 0)**
(f'''(0) = 6 ≠ 0 bestätigt den Wendepunkt.)

---

### B2) Skizze

Bedingungen: f'(2) = 0, f''(2) < 0, f(2) = 5

→ **Hochpunkt** bei (2 | 5). Graph: Parabel-artig nach unten geöffnet, Scheitel bei (2,5).

```
   y
 5 •-- H
   |  /|\
   | / | \
   |/  |  \
---+---+----→ x
   |   2
```

*Kernfrage: Erkennt sie, dass f''(x) < 0 „Rechtskrümmung" = Hochpunkt bedeutet?*

---

### B3) Graph von f' lesen

Gezeigt ist f'(x) = 4x − x² (Parabel, Nullstellen bei 0 und 4, Maximum bei x = 2):
- f'(x) < 0 für x < 0
- f'(x) > 0 für 0 < x < 4, Maximum bei x = 2 (dort f'(2) = 4)
- f'(x) < 0 für x > 4

**a) f monoton steigend:** dort wo f'(x) > 0 → **0 < x < 4**

**b) Lokales Maximum von f:** dort wo f' von + nach − wechselt → **bei x = 4**
*Achtung: Typischer Fehler — Schülerin sagt „bei x = 2", weil f' dort maximal ist. Das ist aber der Wendepunkt von f!*

**c) Wendepunkt von f:** dort wo f' ein Extremum hat (f'' = 0 mit Vorzeichenwechsel) → **bei x = 2**

*Diese Aufgabe ist erfahrungsgemäß die schwierigste im Test — das Unterscheiden von f und f' verlangt ein gutes Verständnis.*

---

## Teil C: Integralrechnung

### C1) Stammfunktionen

**a)** f(x) = 4x³ − 2x + 1
$$F(x) = x^4 - x^2 + x \ (+\, C)$$

**b)** f(x) = e^(2x)
$$F(x) = \tfrac{1}{2}\, e^{2x} \ (+\, C)$$
*Typischer Fehler: einfach F(x) = e^(2x) schreiben (faktor 1/2 vergessen).*

---

### C2) Bestimmtes Integral

$$\int_0^2 (x^2 + 1)\, dx = \left[\tfrac{x^3}{3} + x\right]_0^2 = \left(\tfrac{8}{3} + 2\right) - 0 = \tfrac{8}{3} + 2 = \tfrac{14}{3}$$

Ergebnis: **14/3 ≈ 4,67**

*Prüft: Stammfunktion + Einsetzen der Grenzen + Subtraktion.*

---

## Ergebnisse der Schülerin erfassen

### Vorgehen während der Auswertung

1. **Schülerin rechnet zuerst alleine**, du schaust nicht dabei — sonst korrigiert sie sich unbewusst.
2. **Danach gemeinsam durchgehen**, Aufgabe für Aufgabe. Sie erklärt ihren Weg.
3. **Auswertungsraster** (im `diagnosetest.md` unten) direkt während der Besprechung ausfüllen.

### Dreistufige Einschätzung pro Aufgabe

| Stufe | Bedeutung | Konsequenz |
|-------|-----------|------------|
| ✅ **sicher** | Ergebnis korrekt, Weg sauber, kann es erklären | In Phase 6 nicht extra üben |
| ⚠️ **unsicher** | Ergebnis teilweise richtig / Fehler bei Rechenschritten / kann es nur zögerlich erklären | In Phase 6 gezielt 1–2 Beispiele mehr |
| ❌ **nicht gekonnt** | Leer, fundamentaler Fehler, Regel unbekannt | Schwerpunkt heute; ggf. auf Sitzung 2 mitnehmen |

### Worauf besonders achten — Notizen machen

Notiere dir **nicht nur ja/nein**, sondern **was genau schiefging**. Beispiele:
- „A1c: Exponent falsch (−1 statt −3), Regel grundsätzlich klar"
- „A2b: Kettenregel innen vergessen — Muster"
- „A3: Produktregel unbekannt → heute Priorität"
- „B3b: f und f' verwechselt — häufiges Missverständnis"

Diese Notizen helfen dir **nach der Stunde** den Stundenplan anzupassen und beim nächsten Mal gezielt aufzugreifen.

### Quick-Heuristik zur Einordnung

| Bild | Interpretation | Handlung |
|------|----------------|----------|
| A1–A5 überwiegend ✅, B/C wacklig | Ableitungen sitzen, Fokus auf Kurvendiskussion/Integrale | Sitzung 2 planmäßig, Phase 6 kurz |
| A1 ✅, A2/A3 ⚠️/❌ | Grundlage da, Regel-Mix das Problem | Phase 6 **verlängern**, Regeln strukturiert wiederholen |
| A1 schon ❌ | Potenzregel/Umschreiben unsicher | Phase 6 komplett auf Basics, Sitzung 2 anpassen |
| B3 ❌, Rest ✅ | Nur das f/f'-Verständnis fehlt | Phase 5 intensiv nutzen, in Sitzung 2 nochmal aufgreifen |
| Alles ✅ (>80 %) | Solide Basis | Straffer durch Phasen 3–5, mehr anspruchsvolle Kombinationen in Phase 6, Vorgriff auf Kurvendiskussion |

### Nach der Stunde

- Notizen kurz in `sitzung_01/notizen_schuelerin.md` (neu anlegen) oder direkt im `stundenplan.md` ergänzen.
- Falls Schwerpunkt-Verschiebung nötig: `stundenplan.md` anpassen, bevor du Sitzung 2 vorbereitest.

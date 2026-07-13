# Cheatsheet: Kurvendiskussion

## Die Schritte im Überblick

### 1. Definitionsbereich
- Ganzrationale Funktionen: $D = \mathbb{R}$
- Brüche: Nenner $\neq 0$
- Wurzeln: Radikand $\geq 0$
- $\ln(x)$: Argument $> 0$

### 2. Symmetrie
| Test | Ergebnis | Art |
|------|----------|-----|
| $f(-x) = f(x)$ | achsensymmetrisch (y-Achse) | nur gerade Exponenten |
| $f(-x) = -f(x)$ | punktsymmetrisch (Ursprung) | nur ungerade Exponenten |

### 3. Nullstellen
$f(x) = 0$ lösen.
- Ausklammern, Substitution ($x^2 = z$), p-q-Formel, Polynomdivision

### 4. y-Achsenabschnitt
$f(0)$ berechnen → Punkt $(0 \mid f(0))$ eintragen.

### 5. Ableitungen
- $f'(x)$ berechnen (Potenz-, Ketten-, Produktregel)
- $f''(x)$ berechnen

### 6. Extremstellen

**Notwendige Bedingung:** $f'(x) = 0$

**Hinreichende Bedingung (2. Ableitung):**
| $f''(x_e)$ | Art |
|----------|-----|
| $< 0$ | **Hochpunkt (Maximum)** |
| $> 0$ | **Tiefpunkt (Minimum)** |
| $= 0$ | Vorzeichenwechsel von $f'$ prüfen! |

**Hinreichende Bedingung (VZW von $f'$):**
| $f'$ wechselt von | Art |
|-----------------|-----|
| $+ \to -$ | Hochpunkt |
| $- \to +$ | Tiefpunkt |
| kein VZW | Sattelpunkt |

y-Wert nicht vergessen: Punkt $= (x_e \mid f(x_e))$

### 7. Wendepunkte

**Notwendige Bedingung:** $f''(x) = 0$

**Hinreichende Bedingung:** $f'''(x_w) \neq 0$ (oder VZW von $f''$)

Punkt $= (x_w \mid f(x_w))$

Wendetangente: $t(x) = f'(x_w) \cdot (x - x_w) + f(x_w)$

### 8. Monotonie
| Bedingung | Verhalten |
|-----------|-----------|
| $f'(x) > 0$ | $f$ steigt ↗ |
| $f'(x) < 0$ | $f$ fällt ↘ |

Intervalle aus Nullstellen von $f'$ ablesen, Vorzeichen prüfen.

### 9. Krümmung
| Bedingung | Verhalten |
|-----------|-----------|
| $f''(x) > 0$ | linksgekrümmt (Tal) |
| $f''(x) < 0$ | rechtsgekrümmt (Berg) |

### 10. Verhalten für $x \to \pm\infty$
Höchste Potenz entscheidet:
- Gerader Grad, positiv: $f \to +\infty$ für $x \to \pm\infty$
- Gerader Grad, negativ: $f \to -\infty$ für $x \to \pm\infty$
- Ungerader Grad, positiv: $f \to -\infty$ (links), $f \to +\infty$ (rechts)
- Ungerader Grad, negativ: $f \to +\infty$ (links), $f \to -\infty$ (rechts)

### 11. Graph skizzieren
Alle Punkte eintragen, Verhalten beachten, verbinden!

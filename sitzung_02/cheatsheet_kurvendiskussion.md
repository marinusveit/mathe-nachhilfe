# Cheatsheet: Kurvendiskussion

## Die Schritte im Überblick

### 1. Definitionsbereich
- Ganzrationale Funktionen: D = ℝ
- Brüche: Nenner ≠ 0
- Wurzeln: Radikand ≥ 0
- ln(x): Argument > 0

### 2. Symmetrie
| Test | Ergebnis | Art |
|------|----------|-----|
| f(−x) = f(x) | achsensymmetrisch (y-Achse) | nur gerade Exponenten |
| f(−x) = −f(x) | punktsymmetrisch (Ursprung) | nur ungerade Exponenten |

### 3. Nullstellen
f(x) = 0 lösen.
- Ausklammern, Substitution (x² = z), p-q-Formel, Polynomdivision

### 4. y-Achsenabschnitt
f(0) berechnen → Punkt (0 | f(0)) eintragen.

### 5. Ableitungen
- f'(x) berechnen (Potenz-, Ketten-, Produktregel)
- f''(x) berechnen

### 6. Extremstellen

**Notwendige Bedingung:** f'(x) = 0

**Hinreichende Bedingung (2. Ableitung):**
| f''(xₑ) | Art |
|----------|-----|
| < 0 | **Hochpunkt (Maximum)** |
| > 0 | **Tiefpunkt (Minimum)** |
| = 0 | Vorzeichenwechsel von f' prüfen! |

**Hinreichende Bedingung (VZW von f'):**
| f' wechselt von | Art |
|-----------------|-----|
| + → − | Hochpunkt |
| − → + | Tiefpunkt |
| kein VZW | Sattelpunkt |

y-Wert nicht vergessen: Punkt = (xₑ | f(xₑ))

### 7. Wendepunkte

**Notwendige Bedingung:** f''(x) = 0

**Hinreichende Bedingung:** f'''(xw) ≠ 0 (oder VZW von f'')

Punkt = (xw | f(xw))

Wendetangente: t(x) = f'(xw) · (x − xw) + f(xw)

### 8. Monotonie
| Bedingung | Verhalten |
|-----------|-----------|
| f'(x) > 0 | f steigt ↗ |
| f'(x) < 0 | f fällt ↘ |

Intervalle aus Nullstellen von f' ablesen, Vorzeichen prüfen.

### 9. Krümmung
| Bedingung | Verhalten |
|-----------|-----------|
| f''(x) > 0 | linksgekrümmt (Tal) |
| f''(x) < 0 | rechtsgekrümmt (Berg) |

### 10. Verhalten für x → ±∞
Höchste Potenz entscheidet:
- Gerader Grad, positiv: f → +∞ für x → ±∞
- Gerader Grad, negativ: f → −∞ für x → ±∞
- Ungerader Grad, positiv: f → −∞ (links), f → +∞ (rechts)
- Ungerader Grad, negativ: f → +∞ (links), f → −∞ (rechts)

### 11. Graph skizzieren
Alle Punkte eintragen, Verhalten beachten, verbinden!

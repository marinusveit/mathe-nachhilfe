# Lösungen — Extremwertprobleme & Steckbriefaufgaben

## Teil A: Extremwertprobleme

**A1)** Rechteck aus 60 cm Draht

- Nebenbedingung: `2x + 2y = 60`, also `y = 30 - x`
- Flächenfunktion: `A(x) = x(30 - x) = 30x - x^2`
- Maximum bei `A'(x) = 30 - 2x = 0`, also `x = 15`
- Ergebnis: Quadrat mit `15 cm x 15 cm`

**A2)** Zylindrische Dose mit `V = 500 cm^3`

- Nebenbedingung: `pi r^2 h = 500`, also `h = 500 / (pi r^2)`
- Oberfläche: `O(r) = 2 pi r^2 + 2 pi r h = 2 pi r^2 + 1000 / r`
- Minimum bei `O'(r) = 4 pi r - 1000 / r^2 = 0`
- Optimaler Radius: `r = (250 / pi)^(1/3) ≈ 4,30 cm`
- Zugehörige Höhe: `h = 500 / (pi r^2) ≈ 8,60 cm`
- Verhältnis: `h / d = 1`

**A3)** Rechteck an einer Mauer mit 40 m Zaun

- Nebenbedingung: `2x + y = 40`, also `y = 40 - 2x`
- Flächenfunktion: `A(x) = x(40 - 2x) = 40x - 2x^2`
- Maximum bei `A'(x) = 40 - 4x = 0`, also `x = 10`
- Ergebnis: `x = 10 m`, `y = 20 m`, maximale Fläche `200 m^2`

**A4)** Offener Quader aus `20 cm x 20 cm`

- Volumenfunktion: `V(x) = x(20 - 2x)^2`
- Definitionsbereich: `0 <= x <= 10`
- Ableitung: `V'(x) = 12x^2 - 160x + 400`
- Kritische Stellen: `x = 10/3` und `x = 10`
- Maximum im Inneren bei `x = 10/3 cm`
- Maximales Volumen: `V(10/3) = 16000/27 ≈ 592,6 cm^3`

## Teil B: Steckbriefaufgaben

**B1)** Kubische Funktion mit

- `f(0) = 2`
- `f'(0) = 0`
- `f(2) = 0`
- `f'(2) = 0`

Ansatz: `f(x) = ax^3 + bx^2 + cx + d`

- Aus `f(0) = 2` folgt `d = 2`
- Aus `f'(0) = 0` folgt `c = 0`
- Aus `f(2) = 0` folgt `8a + 4b + 2 = 0`
- Aus `f'(2) = 0` folgt `12a + 4b = 0`

Lösung:

- `a = 1/2`
- `b = -3/2`
- `c = 0`
- `d = 2`

Also:

- `f(x) = 1/2 x^3 - 3/2 x^2 + 2`

**B2)** Quadratische Funktion mit Extremum bei `x = 1`, `f(1) = 4`, `f(0) = 3`

Ansatz: `f(x) = ax^2 + bx + c`

- `f'(1) = 0`
- `f(1) = 4`
- `f(0) = 3`

Lösung:

- `f(x) = -x^2 + 2x + 3`

**B3)** Achsensymmetrische Funktion 4. Grades

Ansatz wegen Achsensymmetrie:

- `f(x) = ax^4 + bx^2 + c`

Bedingungen:

- `f(0) = 1`, also `c = 1`
- `f(2) = 5`, also `16a + 4b + 1 = 5`
- `f'(2) = 8`, also `32a + 4b = 8`

Lösung:

- `a = 1/4`
- `b = 0`
- `c = 1`

Also:

- `f(x) = 1/4 x^4 + 1`

**B4)** Funktion höchstens 3. Grades

Ansatz: `f(x) = ax^3 + bx^2 + cx + d`

Bedingungen:

- `f(0) = 0`, also `d = 0`
- `f'(0) = 3`, also `c = 3`
- Wendepunkt bei `x = 2`, also `f''(2) = 0`
- `f(2) = 6`

Rechnung:

- `f''(x) = 6ax + 2b`
- `f''(2) = 12a + 2b = 0`, also `b = -6a`
- `f(2) = 8a + 4b + 6 = 6`, also `2a + b = 0`

Zusammen mit `b = -6a` folgt:

- `a = 0`
- `b = 0`

Also:

- `f(x) = 3x`

Hinweis:

- Die Bedingungen erzwingen hier keine echte kubische Funktion. Deshalb ist die Formulierung im Aufgabenblatt bewusst auf "höchstens dritten Grades" angepasst.

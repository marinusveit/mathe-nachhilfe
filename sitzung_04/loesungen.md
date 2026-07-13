# Lösungen — Extremwertprobleme & Steckbriefaufgaben

## Teil A: Extremwertprobleme

**A1)** Rechteck aus 60 cm Draht

- Nebenbedingung: $2x + 2y = 60$, also $y = 30 - x$
- Flächenfunktion: $A(x) = x(30 - x) = 30x - x^2$
- Maximum bei $A'(x) = 30 - 2x = 0$, also $x = 15$
- Ergebnis: Quadrat mit $15\ \mathrm{cm} \times 15\ \mathrm{cm}$

**A2)** Zylindrische Dose mit $V = 500\ \mathrm{cm}^3$

- Nebenbedingung: $\pi r^2 h = 500$, also $h = \frac{500}{\pi r^2}$
- Oberfläche: $O(r) = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \frac{1000}{r}$
- Minimum bei $O'(r) = 4\pi r - \frac{1000}{r^2} = 0$
- Optimaler Radius: $r = \left(\frac{250}{\pi}\right)^{1/3} \approx 4{,}30\ \mathrm{cm}$
- Zugehörige Höhe: $h = \frac{500}{\pi r^2} \approx 8{,}60\ \mathrm{cm}$
- Verhältnis: $h/d = 1$

**A3)** Rechteck an einer Mauer mit 40 m Zaun

- Nebenbedingung: $2x + y = 40$, also $y = 40 - 2x$
- Flächenfunktion: $A(x) = x(40 - 2x) = 40x - 2x^2$
- Maximum bei $A'(x) = 40 - 4x = 0$, also $x = 10$
- Ergebnis: $x = 10\ \mathrm{m}$, $y = 20\ \mathrm{m}$, maximale Fläche $200\ \mathrm{m}^2$

**A4)** Offener Quader aus $20\ \mathrm{cm} \times 20\ \mathrm{cm}$

- Volumenfunktion: $V(x) = x(20 - 2x)^2$
- Definitionsbereich: $0 \leq x \leq 10$
- Ableitung: $V'(x) = 12x^2 - 160x + 400$
- Kritische Stellen: $x = \tfrac{10}{3}$ und $x = 10$
- Maximum im Inneren bei $x = \tfrac{10}{3}\ \mathrm{cm}$
- Maximales Volumen: $V\!\left(\tfrac{10}{3}\right) = \tfrac{16000}{27} \approx 592{,}6\ \mathrm{cm}^3$

## Teil B: Steckbriefaufgaben

**B1)** Kubische Funktion mit

- $f(0) = 2$
- $f'(0) = 0$
- $f(2) = 0$
- $f'(2) = 0$

Ansatz: $f(x) = ax^3 + bx^2 + cx + d$

- Aus $f(0) = 2$ folgt $d = 2$
- Aus $f'(0) = 0$ folgt $c = 0$
- Aus $f(2) = 0$ folgt $8a + 4b + 2 = 0$
- Aus $f'(2) = 0$ folgt $12a + 4b = 0$

Lösung:

- $a = \tfrac{1}{2}$
- $b = -\tfrac{3}{2}$
- $c = 0$
- $d = 2$

Also:

- $f(x) = \tfrac{1}{2} x^3 - \tfrac{3}{2} x^2 + 2$

**B2)** Quadratische Funktion mit Extremum bei $x = 1$, $f(1) = 4$, $f(0) = 3$

Ansatz: $f(x) = ax^2 + bx + c$

- $f'(1) = 0$
- $f(1) = 4$
- $f(0) = 3$

Lösung:

- $f(x) = -x^2 + 2x + 3$

## Teil C: Rotationsvolumen

**C1)** $f(x) = \sqrt{x}$ auf $[0; 4]$, Rotation um x-Achse

- Formel: $V = \pi \cdot \int_0^4 [\sqrt{x}]^2\, dx = \pi \cdot \int_0^4 x\, dx$
- Stammfunktion: $F(x) = \tfrac{x^2}{2}$
- Einsetzen: $V = \pi \cdot \left[\tfrac{x^2}{2}\right]_0^4 = \pi \cdot \left(\tfrac{16}{2} - 0\right) =$ **$8\pi \approx 25{,}13$**
- Der Rotationskörper ist ein Paraboloid (bauchige Schale)

**C2)** $f(x) = x^2$ auf $[0; 2]$, Rotation um y-Achse

- Umkehrfunktion: $y = x^2 \Rightarrow x = \sqrt{y}$, also $f^{-1}(y) = \sqrt{y}$
- y-Grenzen: $c = f(0) = 0$, $d = f(2) = 4$
- $V = \pi \cdot \int_0^4 [\sqrt{y}]^2\, dy = \pi \cdot \int_0^4 y\, dy$
- Stammfunktion: $F(y) = \tfrac{y^2}{2}$
- Einsetzen: $V = \pi \cdot \left[\tfrac{y^2}{2}\right]_0^4 = \pi \cdot \left(\tfrac{16}{2} - 0\right) =$ **$8\pi \approx 25{,}13$**
- Bemerkung: Dass beide Ergebnisse gleich sind, ist hier Zufall — bei anderen Funktionen ergeben sich unterschiedliche Volumina!

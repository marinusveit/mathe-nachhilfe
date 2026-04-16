# Rezept: Extremwertprobleme (Optimierung)

> Aus einer realen Situation eine Zielgröße (Fläche, Volumen, Kosten, …) extremal machen: Nebenbedingung nutzen, um alles in einer Variablen auszudrücken, dann ableiten und nullsetzen.

## Typische Aufgabenstellung
> „Bestimmen Sie die Abmessungen des Rechtecks mit maximalem Flächeninhalt, das …"
> „Für welchen Wert von $x$ wird … maximal/minimal?"

## Schritt-für-Schritt

1. **Skizze anfertigen** und Variablen benennen ($x$, $y$, $r$, $h$, …)
2. **Zielfunktion** aufstellen: Was soll maximiert/minimiert werden?
   - z.B. $A(x, y) = x \cdot y$ (Fläche), $V(r, h) = \pi r^2 h$ (Volumen)
3. **Nebenbedingung** finden: Welche Einschränkung gibt es?
   - z.B. Umfang $= 20$ → $2x + 2y = 20$
4. **Nebenbedingung auflösen** und in Zielfunktion einsetzen → Zielfunktion in EINER Variable
   - $y = 10 - x \;\Rightarrow\; A(x) = x \cdot (10 - x) = 10x - x^2$
5. **Definitionsbereich** der Zielfunktion bestimmen ($x > 0$, $y > 0$, …)
6. **Ableitung $= 0$** setzen und lösen
7. **Nachweis** Extremum: $f''$ oder Randwertvergleich
8. **Antwort im Sachkontext** formulieren (Maße, Einheiten!)

## Häufige Fehler
- Nebenbedingung nicht gefunden oder falsch aufgestellt
- Definitionsbereich ignoriert → negativer Radius, negative Länge etc.
- Randwerte nicht geprüft: Maximum kann auch am Rand liegen
- Antwort ohne Einheiten oder ohne Rückbezug auf die Frage

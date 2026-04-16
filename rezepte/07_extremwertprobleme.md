# Rezept: Extremwertprobleme (Optimierung)

## Typische Aufgabenstellung
> „Bestimmen Sie die Abmessungen des Rechtecks mit maximalem Flächeninhalt, das …"
> „Für welchen Wert von x wird … maximal/minimal?"

## Schritt-für-Schritt

1. **Skizze anfertigen** und Variablen benennen (x, y, r, h, …)
2. **Zielfunktion** aufstellen: Was soll maximiert/minimiert werden?
   - z.B. A(x, y) = x · y (Fläche), V(r, h) = π r² h (Volumen)
3. **Nebenbedingung** finden: Welche Einschränkung gibt es?
   - z.B. Umfang = 20 → 2x + 2y = 20
4. **Nebenbedingung auflösen** und in Zielfunktion einsetzen → Zielfunktion in EINER Variable
   - y = 10 − x → A(x) = x · (10 − x) = 10x − x²
5. **Definitionsbereich** der Zielfunktion bestimmen (x > 0, y > 0, …)
6. **Ableitung = 0** setzen und lösen
7. **Nachweis** Extremum: f'' oder Randwertvergleich
8. **Antwort im Sachkontext** formulieren (Maße, Einheiten!)

## Häufige Fehler
- Nebenbedingung nicht gefunden oder falsch aufgestellt
- Definitionsbereich ignoriert → negativer Radius, negative Länge etc.
- Randwerte nicht geprüft: Maximum kann auch am Rand liegen
- Antwort ohne Einheiten oder ohne Rückbezug auf die Frage

# Rezept: Vollständige Kurvendiskussion

> Die systematische Untersuchung einer Funktion auf alle charakteristischen Eigenschaften: Definitionsbereich, Nullstellen, Symmetrie, Extrema, Wendepunkte, Verhalten im Unendlichen.

## Typische Aufgabenstellung
> „Untersuchen Sie $f$ auf Nullstellen, Extrema, Wendepunkte und skizzieren Sie den Graphen."

## Schritt-für-Schritt

1. **Definitionsbereich** bestimmen (Nenner $\neq 0$, Wurzel $\geq 0$, $\ln > 0$)
2. **Symmetrie** prüfen: $f(-x) = f(x)$ → achsensymmetrisch, $f(-x) = -f(x)$ → punktsymmetrisch
3. **Nullstellen**: $f(x) = 0$ lösen
4. **$y$-Achsenabschnitt**: $f(0)$ berechnen
5. **Ableitungen**: $f'(x)$ und $f''(x)$ berechnen
6. **Extremstellen**:
   - Notwendig: $f'(x) = 0$ lösen
   - Hinreichend: $f''(x_0) > 0$ → Minimum, $f''(x_0) < 0$ → Maximum
   - Alternative: Vorzeichenwechsel von $f'$ prüfen
7. **Wendepunkte**:
   - Notwendig: $f''(x) = 0$ lösen
   - Hinreichend: $f'''(x_0) \neq 0$ ODER Vorzeichenwechsel von $f''$
8. **Monotonie**: Vorzeichen von $f'$ in Intervallen → steigend/fallend
9. **Krümmung**: Vorzeichen von $f''$ → linksgekrümmt ($f'' > 0$) / rechtsgekrümmt ($f'' < 0$)
10. **Randverhalten**: $\lim_{x \to \pm\infty} f(x)$, ggf. $\lim$ an Polstellen
11. **Graph skizzieren**: alle Punkte eintragen, Monotonie/Krümmung beachten

## Häufige Fehler
- Hinreichende Bedingung vergessen (nur $f'=0$ reicht nicht!)
- Bei $f''(x_0) = 0$: Kein Extremum ausschließen, sondern VZW von $f'$ prüfen
- Definitionsbereich vergessen → falsche Nullstellen/Extrema
- Vorzeichen beim Randverhalten: $e^{-x} \to 0$ für $x \to \infty$, nicht $\to \infty$

## Operatoren-Hinweis
- „Untersuchen" = alle Schritte durchführen + begründen
- „Bestimmen" = Ergebnis berechnen + angeben
- „Zeigen/Nachweisen" = gegebene Aussage durch Rechnung bestätigen

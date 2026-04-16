# Rezept: Integrale im Sachkontext

## Typische Aufgabenstellung
> „Berechnen Sie die Gesamtänderung im Zeitraum [a; b]."
> „Bestimmen Sie den Bestand zum Zeitpunkt t."
> „Berechnen Sie den durchschnittlichen Funktionswert."

## Schritt-für-Schritt: Gesamtänderung

Wenn f'(t) die Änderungsrate beschreibt:
1. ∫ₐᵇ f'(t) dt = f(b) − f(a) = Gesamtänderung im Intervall [a;b]
2. **Einheit**: Das Integral hat die **Einheit von f**; anschaulich kürzt sich bei „Einheit von f pro Zeit" mal „Zeit" die Zeiteinheit weg
3. **Deutung**: „Im Zeitraum von a bis b hat sich … um … verändert."

## Schritt-für-Schritt: Bestandsrekonstruktion

Wenn Anfangsbestand f(a) und Änderungsrate f'(t) gegeben:
1. f(b) = f(a) + ∫ₐᵇ f'(t) dt
2. **Deutung**: „Zum Zeitpunkt b beträgt der Bestand …"

## Schritt-für-Schritt: Mittlere Änderungsrate

- Mittlere Änderungsrate = (f(b) − f(a)) / (b − a)
- **Achtung**: Das ist die Sekantensteigung, KEIN Integral

## Schritt-für-Schritt: Durchschnittlicher Funktionswert

- f̄ = 1/(b−a) · ∫ₐᵇ f(x) dx
- **Deutung**: „Im Durchschnitt betrug … im Zeitraum [a;b] den Wert …"

## Häufige Fehler
- Änderungsrate ≠ Bestand: f'(t) dt ≠ f(t)
- Einheiten falsch: „Liter pro Stunde" integriert → „Liter", nicht „Liter pro Stunde mal Stunden"
- Mittlere Änderungsrate und durchschnittlicher Funktionswert verwechselt
- Vorzeichen: negatives Integral = Abnahme, nicht Fehler

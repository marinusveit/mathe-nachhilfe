# Leitfaden — Sitzung 2: Kurvendiskussion komplett

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 1. Einstieg: Zusammenhang $f$, $f'$, $f''$ | ~15 Min | Manim-Animationen anschauen & besprechen | `manim/kurvendiskussion.py` (Scenes: `KurvendiskussionAnimation`, `WandernderPunkt`) |
| 2. Cheatsheet durchgehen | ~15 Min | Alle 11 Schritte der Kurvendiskussion systematisch | `cheatsheet_kurvendiskussion.md` |
| 3. Notebook interaktiv | ~25 Min | $f$/$f'$/$f''$-Zusammenhang, automatische Kurvendiskussion, Zuordnungsquiz | `kurvendiskussion_interaktiv.ipynb` (Abschnitte 1–4) |
| 4. Kurvendiskussion auf Papier | ~30 Min | Gemeinsam eine komplette Kurvendiskussion durchrechnen | Papier + Stift, Notebook-Aufgaben (Abschnitt 5) zur Kontrolle |
| 5. Puffer / Wiederholung | ~5 Min | Zusammenfassung, offene Fragen | Cheatsheet als Referenz |

---

## Phase 1: Manim-Animationen (~15 Min)

Animationen rendern und zeigen:
```bash
source .venv/bin/activate
cd sitzung_02/manim
manim -pql kurvendiskussion.py KurvendiskussionAnimation
manim -pql kurvendiskussion.py WandernderPunkt
```

**`KurvendiskussionAnimation`** zeigt an $f(x) = x^3 - 3x$:
1. Graph von $f(x)$ wird gezeichnet
2. $f'(x)$ erscheint darunter — Nullstellen von $f'$ werden per gestrichelter Linie mit den Extrema von $f$ verbunden
3. Monotoniebereiche werden farblich markiert (grün = steigend, rot = fallend)
4. $f''(x)$ erscheint — Nullstelle von $f''$ wird mit dem Wendepunkt von $f$ verbunden
5. Zusammenfassung der Regeln

**`WandernderPunkt`** vertieft das Verständnis:
- Ein Punkt wandert entlang $f(x)$ mit Tangente
- Synchron bewegen sich Punkte auf $f'(x)$ und $f''(x)$
- An besonderen Stellen (HOP bei $x = -1$, WP bei $x = 0$, TIP bei $x = 1$) erscheinen die zugehörigen Regeln

**Diskussionsfragen während der Animation:**
- "Was passiert mit der Tangente, wenn der Punkt das Maximum erreicht?"
- "Warum ist $f'(x) = 0$ nur eine *notwendige* Bedingung?"

---

## Phase 2: Cheatsheet besprechen (~15 Min)

Datei öffnen (am besten ausdrucken): `sitzung_02/cheatsheet_kurvendiskussion.md`

Die 11 Schritte systematisch durchgehen:
1. **Definitionsbereich** — Wann ist $D$ nicht gleich $\mathbb{R}$? (Brüche, Wurzeln, ln)
2. **Symmetrie** — $f(-x)$ einsetzen und vergleichen
3. **Nullstellen** — Methoden: Ausklammern, Substitution, p-q-Formel
4. **y-Achsenabschnitt** — $f(0)$ berechnen
5. **Ableitungen** — $f'(x)$ und $f''(x)$ bestimmen
6. **Extremstellen** — Notwendige Bedingung $f'(x) = 0$, hinreichend über $f''(x)$ oder VZW
7. **Wendepunkte** — $f''(x) = 0$ und $f'''(x) \neq 0$
8. **Monotonie** — Vorzeichen von $f'$ in Intervallen
9. **Krümmung** — Vorzeichen von $f''$ in Intervallen
10. **Verhalten für $x \to \pm\infty$** — Höchste Potenz entscheidet
11. **Graph skizzieren**

**Wichtig:** Die Tabellen zu Extremstellen (Schritt 6) und Krümmung (Schritt 9) betonen — das sind typische Abitur-Stolpersteine.

---

## Phase 3: Notebook interaktiv (~25 Min)

Notebook starten:
```bash
source .venv/bin/activate
jupyter lab sitzung_02/kurvendiskussion_interaktiv.ipynb
```

### Abschnitt 1 — $f$, $f'$ und $f''$ im Zusammenhang (~8 Min)
- Dropdown: verschiedene Funktionen auswählen ($x^3 - 3x$, $x^4 - 4x^2 + 1$, $x \cdot e^{-x}$, $\sin(x)$, ...)
- $f'$ und $f''$ einzeln ein-/ausblenden lassen
- **Aufgabe:** "Blende nur $f$ ein. Wo vermutest du die Extrema? Jetzt blende $f'$ ein und prüfe."
- Grüne Punkte = Extrema, orange Punkte = Wendepunkte

### Abschnitt 2 — Automatische Kurvendiskussion (~7 Min)
- Funktion `kurvendiskussion('x**3 - 3*x')` ausführen
- Alle Schritte erscheinen symbolisch berechnet (SymPy)
- Weitere Funktionen ausprobieren lassen: `x**4 - 4*x**2 + 1`, `x * exp(x)`, `x**2 * exp(-x)`
- **Nutzen:** Kontrolle für späteres Papierrechnen

### Abschnitt 3 — Zuordnungsquiz: $f$, $f'$ oder $f''$? (~5 Min)
- Drei Graphen in zufälliger Reihenfolge — welcher gehört zu $f$, $f'$, $f''$?
- Typische Abituraufgabe! Tipps werden eingeblendet.
- Lösung aufklappbar

### Abschnitt 4 — Monotonie und Krümmung mit Slider (~5 Min)
- Punkt auf $f(x) = x^3 - 3x$ verschieben
- Tangente, $f'(x_0)$, $f''(x_0)$ werden live angezeigt
- **Aufgabe:** Finde die zwei Extremstellen und den Wendepunkt durch Verschieben

---

## Phase 4: Kurvendiskussion auf Papier (~30 Min)

Gemeinsam am Beispiel **$f(x) = x^4 - 8x^2$** (Notebook Abschnitt 5, Aufgabe 1) alle Schritte durchrechnen:

1. $D = \mathbb{R}$ (ganzrationale Funktion)
2. Symmetrie: $f(-x) = f(x)$ — achsensymmetrisch
3. Nullstellen: $x^4 - 8x^2 = 0 \Rightarrow x^2(x^2 - 8) = 0$
4. Ableitungen: $f'(x) = 4x^3 - 16x$, $f''(x) = 12x^2 - 16$
5. Extremstellen: $f'(x) = 0 \Rightarrow x(4x^2 - 16) = 0 \Rightarrow x = 0,\ x = \pm 2$
6. Wendepunkte: $f''(x) = 0 \Rightarrow 12x^2 = 16$
7. Monotonie und Krümmung aus Vorzeichentabellen
8. Verhalten: $x^4$ dominiert → $f \to +\infty$ für $x \to \pm\infty$
9. Skizze anfertigen

**Falls Zeit bleibt:** Aufgabe 2 ($f(x) = x \cdot e^{-x}$) oder Aufgabe 3 ($f(x) = -x^3 + 3x^2$) bearbeiten.

Die Lösungen im Notebook (aufklappbar in Abschnitt 5) dienen zur Selbstkontrolle.

---

## Phase 5: Puffer / Zusammenfassung (~5 Min)

- Cheatsheet als Referenz für zu Hause mitgeben
- Die drei wichtigsten Regeln nochmal wiederholen:
  - $f'(x) = 0$ ist notwendig für Extremstellen
  - $f''(x_E) < 0$ → Maximum, $f''(x_E) > 0$ → Minimum
  - $f''(x) = 0$ und $f'''(x) \neq 0$ → Wendepunkt

---

## Tipps für die Durchführung

- **Wenn die Schülerin Ableitungen noch unsicher beherrscht:** Mehr Zeit in Phase 1 (Animationen) investieren und das Ableiten an einfachen Beispielen wiederholen — ggf. auch die Animation `AbleitungPotenzregel` aus `manim/ableitung_potenzregel.py` zeigen
- **Wenn Extremstellen/Wendepunkte gut sitzen:** Phase 4 verkürzen, stattdessen anspruchsvollere Funktionen (e-Funktionen) aus dem Notebook bearbeiten
- **Wenn das Zuordnungsquiz Schwierigkeiten macht:** Hier länger verweilen — "Graphen zuordnen" ist eine beliebte Abituraufgabe im hilfsmittelfreien Teil
- **Häufige Fehler:** y-Wert beim Extrempunkt vergessen, nur notwendige Bedingung prüfen (hinreichende vergessen), Monotonie-Intervalle falsch ablesen
- **Cheatsheet ausdrucken:** Das Cheatsheet eignet sich gut als Referenzblatt für die Hausarbeit zwischen den Sitzungen

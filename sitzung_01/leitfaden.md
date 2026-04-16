# Leitfaden — Sitzung 1: Diagnose + Ableitungen

**Dauer:** 90 Minuten

---

## Überblick

| Phase | Dauer | Inhalt | Material |
|-------|-------|--------|----------|
| 0. Organisatorisches & Kennenlernen | ~5 Min | Rahmenbedingungen klären (siehe unten) | — |
| 1. Diagnosetest | ~20 Min | 13 Aufgaben (A1–C2), hilfsmittelfrei | `diagnosetest.md` |
| 2. Auswertung & Lücken identifizieren | ~15 Min | Auswertungsraster ausfüllen, Schwerpunkte setzen | `diagnosetest.md` (Raster) |
| 3. Sekante → Tangente (Manim) | ~10 Min | Animation: geometrische Bedeutung der Ableitung | Manim `SekanteTangente` |
| 4. Tangente interaktiv erkunden | ~10 Min | Slider-Exploration am Notebook | Notebook Abschnitt 1 |
| 5. f und f' im Vergleich | ~10 Min | Zusammenhang Funktion ↔ Ableitung | Notebook Abschnitt 2 |
| 6. Ableitungsregeln üben | ~20 Min | Potenzregel, Ketten-, Produkt-, Quotientenregel, e/ln | Notebook Abschnitte 3–4 |
| 7. Freies Experimentieren & Ausblick | ~10 Min | Eigene Funktionen eingeben, Desmos-Tipp | Notebook Abschnitt 5 |

---

## Phase 0: Organisatorisches & Kennenlernen (~5 Min)

Bevor der Test beginnt, kurz **Rahmenbedingungen klären** — das beeinflusst, wie du die restlichen 7 Sitzungen und Teil B ausrichtest. Locker im Gespräch abfragen, nicht wie ein Interview.

**Fragen an die Schülerin:**

1. **Schriftlich oder Kolloquium?**
   Im G9 kann sie Deutsch **oder** Mathe schriftlich wählen; wer Mathe nicht schriftlich schreibt, hat ein mündliches Kolloquium (ebenfalls eA, 18.–22. Mai oder 8.–12. Juni 2026). → Schriftlich = Fokus auf Rechensicherheit + Formeldokument. Kolloquium = Fokus auf Erklärenkönnen + Begründungen.

2. **Taschenrechner-Variante: WTR oder MMS (CAS)?**
   Entscheidet die Schule. Macht einen großen Unterschied für Teil B: Mit MMS sind viele Rechnungen symbolisch lösbar, mit WTR muss mehr per Hand. → Unbedingt notieren, damit du bei Sitzung 5/6 die richtigen Lösungswege übst.

3. **IQB-Formeldokument schon bekannt?**
   Ersetzt die alte bayerische „Merkhilfe". Andere Notation. → Falls nein: sie soll es sich bis Sitzung 2 ausdrucken und mitbringen. Link in `abitur_info.md`.

4. **Aktueller Notenstand + Selbsteinschätzung**
   „Wie lief das letzte Halbjahr in Mathe? In welchen Themen fühlst du dich sicher, wo hast du Bauchschmerzen?" — informiert die Schwerpunktsetzung.

5. **Stochastik und Geometrie?**
   Unser Plan ist Analysis-fokussiert. In der Prüfung sind aber 5 BE (Teil A) + 20 BE (Teil B) je Stochastik/Geometrie. → Klären: Wird das in der Schule oder woanders abgedeckt, oder sollen wir später umplanen?

6. **Prüfungstermin-Realität: 6. Mai 2026.**
   Heute ist der 16. April — das sind **knapp 3 Wochen** bis zur schriftlichen Prüfung. Unser 4-Wochen-Plan läuft länger. → Entweder verdichten (Sitzung 7/8 vor der Prüfung) oder Sitzung 8 wird Nachbereitung/Kolloquiumsvorbereitung.

**Notiere die Antworten** in `sitzung_01/notizen_schuelerin.md` (neu anlegen) — brauchst du für die Plananpassung nach der Stunde.

---

## Phase 1: Diagnosetest (~20 Min)

**Material:** `diagnosetest.md` — ausdrucken oder auf dem Tablet zeigen.

**Durchführung:**
- Kein Taschenrechner, kein Formelblatt.
- Entspannte Atmosphäre schaffen: *„Es geht nicht um Noten, sondern darum, dass wir wissen, wo wir ansetzen."*
- Die Schülerin soll so weit kommen wie sie kann; nicht bei einzelnen Aufgaben hängenbleiben.

**Aufgabenüberblick:**
- **Teil A (Ableitungen):** A1 Grundableitungen (Potenz, Wurzel, 1/x²), A2 Kettenregel (Polynom, e-Funktion, **sin(2x)**), A3 Produkt- und **Quotientenregel**, A4 ln-Ableitung, A5 höhere Ableitungen, A6 geometrische Bedeutung
- **Teil B (Kurvendiskussion):** B1 Nullstellen/Extrema/Wendepunkt von x³−3x, B2 Skizze aus f'/f''-Bedingungen, B3 Graph von f' lesen
- **Teil C (Integralrechnung):** C1 Stammfunktionen, C2 bestimmtes Integral

**Worauf achten:**
- Kann sie Potenzen umschreiben (√x = x^(1/2), 1/x² = x^(-2))?
- Wendet sie Ketten-/Produktregel korrekt an oder verwechselt sie die Regeln?
- Versteht sie die geometrische Bedeutung der Ableitung (A6)?
- Teil B und C geben einen Vorgeschmack auf spätere Sitzungen — hier reicht eine grobe Einschätzung.

---

## Phase 2: Auswertung & Lücken identifizieren (~10 Min)

**Material:** Auswertungsraster in `diagnosetest.md` (unten).

- Raster direkt während der Besprechung ausfüllen (sicher / unsicher / nicht gekonnt).
- Lösungen gemeinsam durchgehen — nicht alles einzeln vorrechnen, sondern gezielt bei Fehlern einhaken.
- **Adaptive Entscheidung:** Je nach Ergebnis den Rest der Stunde anpassen:
  - **Grundableitungen unsicher (A1):** Mehr Zeit bei Phase 6 (Potenzregel-Slider), Grundrechenarten mit Potenzen wiederholen.
  - **Ketten-/Produktregel unsicher (A2/A3):** In Phase 6 gezielt diese Regeln in den Formel-Tester eingeben und üben.
  - **Alles sicher:** Phasen 3–5 zügig, mehr freies Rechnen in Phase 7.

---

## Phase 3: Sekante → Tangente — Manim-Animation (~10 Min)

**Starten:**
```bash
cd /home/marinusveit/Dokumente/isys_marinus/mathe_nachhilfe
source .venv/bin/activate
manim -pql sitzung_01/manim/sekante_tangente.py SekanteTangente
```
(Für 1080p: `-pqh` statt `-pql`)

**Was passiert in der Animation:**
1. Koordinatensystem mit f(x) = ½x² erscheint.
2. Fester Punkt P bei x₀ = 1,5 und beweglicher Punkt Q bei x₁ = 4.
3. Sekante durch P und Q mit Steigungsdreieck (Δx, Δy) und berechneter Sekantensteigung.
4. Frage: *„Was passiert, wenn x₁ immer näher an x₀ rückt?"*
5. Q wandert schrittweise zu P → Sekante wird zur Tangente.
6. Formel: f'(x₀) = lim (Differenzenquotient → Differentialquotient).

**Gesprächsimpulse:**
- *„Was fällt dir auf, wenn Q näher kommt?"*
- *„Warum wird das Steigungsdreieck immer kleiner?"*
- *„Was ist der Unterschied zwischen Sekantensteigung und Tangentensteigung?"*
- Bezug zu A6 im Diagnosetest herstellen: Die Ableitung f'(x₀) ist die Steigung der Tangente an x₀.

---

## Phase 4: Tangente interaktiv erkunden (~10 Min)

**Starten:**
```bash
cd /home/marinusveit/Dokumente/isys_marinus/mathe_nachhilfe
source .venv/bin/activate
jupyter lab sitzung_01/ableitungen_interaktiv.ipynb
```

**Abschnitt 1 im Notebook: „Tangente an einem Punkt"**
- Die Schülerin verschiebt den Slider für x₀ entlang der Kurve f(x) = x³ − 3x.
- Sie sieht die Tangente und deren Steigung in Echtzeit.

**Leitfragen:**
- *„Wo ist die Steigung positiv, wo negativ, wo null?"*
- *„Was passiert an den Stellen, wo die Steigung null ist?"* → Extremstellen!
- *„Schieb mal ganz langsam von links nach rechts — wann kippt die Steigung?"*

---

## Phase 5: f und f' im Vergleich (~10 Min)

**Abschnitt 2 im Notebook: „f(x) und f'(x) im Vergleich"**
- Dropdown-Menü mit verschiedenen Funktionen: x²−2x, x³−3x, sin(x), eˣ, ln(x).
- Oberer Plot zeigt f, unterer zeigt f' — grüne Punkte markieren Extrema/Nullstellen.

**Durchführung:**
- Mit x³−3x starten (bekannt aus Phase 4 und Diagnosetest B1).
- Dann eˣ zeigen: *„Was fällt dir auf?"* → Die Ableitung von eˣ ist wieder eˣ!
- Dann ln(x): *„Wo ist die Steigung am größten?"* → Nahe x = 0.

**Merkregeln gemeinsam formulieren:**
- f' > 0 → f steigt
- f' < 0 → f fällt
- f' = 0 → mögliches Extremum

---

## Phase 6: Ableitungsregeln üben (~20 Min)

**Abschnitt 3 im Notebook: „Ableitungsregeln live testen"**
- Eingabefeld, in das die Schülerin beliebige Funktionen eintippt → sympy berechnet die Ableitung symbolisch und plottet beides.

**Abschnitt 4: „Potenzregel — das Muster sehen"**
- Slider für den Exponenten n von −2 bis 5 → zeigt f(x) = xⁿ und f'(x) = n·xⁿ⁻¹.

**Übungsplan (an Diagnose-Ergebnis anpassen):**

| Regel | Eingabe zum Testen | Erwartung |
|-------|-------------------|-----------|
| Potenzregel | `x^4 - 2*x^2` | 4x³ − 4x |
| Kettenregel | `(2*x + 3)^5` | 10(2x+3)⁴ |
| sin/cos (mit Kette) | `sin(2*x)` | 2·cos(2x) |
| Produktregel | `x^2 * exp(x)` | (2x + x²)·eˣ |
| Quotientenregel | `x / (x^2 + 1)` | (1 − x²) / (x² + 1)² |
| e-Funktion | `exp(-2*x)` | −2·e^(−2x) |
| ln-Funktion | `ln(3*x)` | 1/x |
| Kombination | `x * ln(x)` | ln(x) + 1 |

**Vorgehen:**
1. Die Schülerin leitet erst **auf Papier** ab.
2. Dann tippt sie die Funktion ins Notebook ein und vergleicht.
3. Bei Fehlern: Gemeinsam die Regel nochmal durchgehen, visuell am Plot prüfen.

**Quotientenregel:** Im Diagnosetest (A3b) jetzt direkt geprüft. Bei Unsicherheit: Formel `(u/v)' = (u'v − uv') / v²` an Tafel/Papier, dann `x / (x^2 + 1)` ins Eingabefeld eintippen und mit dem Handrechenweg vergleichen.

---

## Phase 7: Freies Experimentieren & Ausblick (~10 Min)

**Abschnitt 5 im Notebook: Desmos-Verweis**
- Falls noch Zeit: Die Schülerin gibt eigene Funktionen ein oder probiert Desmos am Tablet.
- Link: [desmos.com/calculator](https://www.desmos.com/calculator)

**Desmos-Tipp:** `f(x) = x^3 - 3x` eingeben, dann `f'(x)` — Desmos berechnet die Ableitung automatisch.

**Ausblick auf Sitzung 2:**
- *„Nächstes Mal machen wir eine komplette Kurvendiskussion — Nullstellen, Extrema, Wendepunkte, Monotonie, das volle Programm."*
- Falls bestimmte Ableitungsregeln noch wackeln: als Hausaufgabe 3–4 Ableitungen auf Papier üben.

---

## Tipps für die Durchführung

**Falls der Diagnosetest sehr gut ausfällt (> 80 % sicher):**
- Phasen 3–5 straffen (je 5 Min), dafür mehr Zeit für anspruchsvollere Kombinationen in Phase 6 (z.B. verkettete e-Funktionen, Produkt aus ln und Polynom).
- Eventuell schon einen Vorgriff auf Kurvendiskussion (Sitzung 2) machen.

**Falls der Diagnosetest schlecht ausfällt (Grundableitungen unsicher):**
- Phase 3 (Manim) trotzdem zeigen — die geometrische Intuition hilft.
- Phase 6 verlängern: Mehr Grundbeispiele (Potenzregel-Slider intensiv nutzen, einfache Ableitungen üben).
- Ketten-/Produktregel ggf. auf Sitzung 2 verschieben und dort vor der Kurvendiskussion kurz wiederholen.

**Allgemein:**
- Immer erst die Schülerin rechnen lassen, dann mit dem Notebook überprüfen — nicht umgekehrt.
- Den Plot nutzen, um Rechenfehler zu finden: *„Die Ableitung müsste hier null sein — stimmt das mit deinem Ergebnis überein?"*
- Stundenplan nach dieser Sitzung ggf. anpassen (siehe Notiz in `stundenplan.md`).

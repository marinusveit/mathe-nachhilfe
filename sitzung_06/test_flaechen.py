"""
Tests für Sitzung 6: Flächen zwischen Kurven & Anwendungen.

Alle zu testenden Funktionen sind hier im Test-File definiert.
Ausführen mit: pytest sitzung_06/test_flaechen.py -v
"""

import math
import pytest


# ---------------------------------------------------------------------------
# Hilfsfunktionen (werden getestet)
# ---------------------------------------------------------------------------

def flaeche_zwischen_kurven(f, g, a, b, n=10_000):
    """Berechnet ∫_a^b |f(x) - g(x)| dx numerisch (Trapezregel)."""
    h = (b - a) / n
    summe = 0.5 * abs(f(a) - g(a)) + 0.5 * abs(f(b) - g(b))
    for i in range(1, n):
        x = a + i * h
        summe += abs(f(x) - g(x))
    return summe * h


def flaeche_zwischen_kurven_exakt(f_minus_g_stammfunktion, schnittpunkte):
    """Berechnet die Fläche über Teilintervalle mit Vorzeichenwechsel.

    f_minus_g_stammfunktion: Stammfunktion von f(x) - g(x)
    schnittpunkte: sortierte Liste der Schnittstellen [a, ..., b]
    """
    flaeche = 0.0
    for i in range(len(schnittpunkte) - 1):
        a, b = schnittpunkte[i], schnittpunkte[i + 1]
        teil = f_minus_g_stammfunktion(b) - f_minus_g_stammfunktion(a)
        flaeche += abs(teil)
    return flaeche


def schnittpunkte_polynome(koeffizienten_differenz):
    """Findet reelle Nullstellen eines Polynoms (numpy-frei, nur für Grad <= 2).

    koeffizienten_differenz: [a, b, c] für ax² + bx + c = 0
    """
    if len(koeffizienten_differenz) == 3:
        a, b, c = koeffizienten_differenz
        if a == 0:
            if b == 0:
                return []
            return [-c / b]
        diskriminante = b**2 - 4 * a * c
        if diskriminante < 0:
            return []
        elif diskriminante == 0:
            return [-b / (2 * a)]
        else:
            wurzel = math.sqrt(diskriminante)
            x1 = (-b - wurzel) / (2 * a)
            x2 = (-b + wurzel) / (2 * a)
            return sorted([x1, x2])
    elif len(koeffizienten_differenz) == 2:
        a, b = koeffizienten_differenz
        if a == 0:
            return []
        return [-b / a]
    return []


def mittelwert_funktion(f, a, b, n=10_000):
    """Berechnet den Mittelwert f̄ = 1/(b-a) · ∫_a^b f(x) dx numerisch."""
    h = (b - a) / n
    summe = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        x = a + i * h
        summe += f(x)
    return summe * h / (b - a)


def bestand_rekonstruktion(f0, rate, t, n=10_000):
    """Rekonstruiert den Bestand: F(t) = f0 + ∫_0^t rate(s) ds."""
    if t == 0:
        return f0
    h = t / n
    summe = 0.5 * rate(0) + 0.5 * rate(t)
    for i in range(1, n):
        s = i * h
        summe += rate(s)
    return f0 + summe * h


def bestimmtes_integral(f, a, b, n=10_000):
    """Berechnet ∫_a^b f(x) dx numerisch (Trapezregel)."""
    h = (b - a) / n
    summe = 0.5 * f(a) + 0.5 * f(b)
    for i in range(1, n):
        x = a + i * h
        summe += f(x)
    return summe * h


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestFlaecheZwischenKurven:
    """Tests für Flächenberechnungen zwischen zwei Kurven."""

    def test_flaeche_x_und_x_quadrat(self):
        """∫₀¹ (x - x²) dx = 1/6."""
        f = lambda x: x
        g = lambda x: x**2
        ergebnis = flaeche_zwischen_kurven(f, g, 0, 1)
        assert abs(ergebnis - 1 / 6) < 1e-4

    def test_flaeche_x_quadrat_minus1_und_minus_x_quadrat_plus3(self):
        """Fläche zwischen x²-1 und -x²+3: Schnittpunkte bei x = ±√2.
        ∫_{-√2}^{√2} (-2x² + 4) dx = 16√2/3 ≈ 7.5425."""
        f = lambda x: x**2 - 1
        g = lambda x: -x**2 + 3
        a = -math.sqrt(2)
        b = math.sqrt(2)
        ergebnis = flaeche_zwischen_kurven(f, g, a, b)
        exakt = 16 * math.sqrt(2) / 3
        assert abs(ergebnis - exakt) < 1e-3

    def test_flaeche_x_kubisch_und_x(self):
        """Fläche zwischen x³ und x auf [-1, 1]: zwei symmetrische Teilflächen.
        Gesamtfläche = 2 · ∫₀¹ (x - x³) dx = 2 · 1/4 = 1/2."""
        f = lambda x: x**3
        g = lambda x: x
        ergebnis = flaeche_zwischen_kurven(f, g, -1, 1)
        assert abs(ergebnis - 0.5) < 1e-4

    def test_flaeche_exp_und_1(self):
        """∫₀² (eˣ - 1) dx = e² - 3 ≈ 4.389."""
        f = lambda x: math.exp(x)
        g = lambda x: 1.0
        ergebnis = flaeche_zwischen_kurven(f, g, 0, 2)
        exakt = math.exp(2) - 3
        assert abs(ergebnis - exakt) < 1e-3


class TestFlaecheExakt:
    """Tests für die exakte Flächenberechnung über Teilintervalle."""

    def test_x_minus_x_quadrat(self):
        """Stammfunktion von (x - x²) ist x²/2 - x³/3, auf [0, 1]."""
        stammfkt = lambda x: x**2 / 2 - x**3 / 3
        ergebnis = flaeche_zwischen_kurven_exakt(stammfkt, [0, 1])
        assert abs(ergebnis - 1 / 6) < 1e-10

    def test_x_kubisch_minus_x_teilintervalle(self):
        """x³ - x auf [-1, 0, 1] → Gesamtfläche = 1/2."""
        stammfkt = lambda x: x**4 / 4 - x**2 / 2
        ergebnis = flaeche_zwischen_kurven_exakt(stammfkt, [-1, 0, 1])
        assert abs(ergebnis - 0.5) < 1e-10


class TestSchnittpunkte:
    """Tests für die Schnittpunktberechnung."""

    def test_x_und_x_quadrat(self):
        """x² - x = 0 → x(x-1) = 0 → x = 0, x = 1."""
        # Differenz: x² - x = 1·x² + (-1)·x + 0
        ergebnis = schnittpunkte_polynome([1, -1, 0])
        assert len(ergebnis) == 2
        assert abs(ergebnis[0] - 0) < 1e-10
        assert abs(ergebnis[1] - 1) < 1e-10

    def test_parabeln_gegenueber(self):
        """x²-1 = -x²+3 → 2x²-4 = 0 → x = ±√2."""
        ergebnis = schnittpunkte_polynome([2, 0, -4])
        assert len(ergebnis) == 2
        assert abs(ergebnis[0] - (-math.sqrt(2))) < 1e-10
        assert abs(ergebnis[1] - math.sqrt(2)) < 1e-10

    def test_keine_reellen_loesungen(self):
        """x² + 1 = 0 hat keine reellen Lösungen."""
        ergebnis = schnittpunkte_polynome([1, 0, 1])
        assert len(ergebnis) == 0


class TestMittelwert:
    """Tests für den Mittelwert einer Funktion."""

    def test_mittelwert_x_quadrat_0_bis_3(self):
        """f̄ = 1/3 · ∫₀³ x² dx = 1/3 · 9 = 3."""
        f = lambda x: x**2
        ergebnis = mittelwert_funktion(f, 0, 3)
        assert abs(ergebnis - 3.0) < 1e-3

    def test_mittelwert_konstante(self):
        """Mittelwert einer Konstanten = die Konstante selbst."""
        f = lambda x: 5.0
        ergebnis = mittelwert_funktion(f, -2, 7)
        assert abs(ergebnis - 5.0) < 1e-10

    def test_mittelwert_linear(self):
        """Mittelwert von f(x) = 2x auf [0, 4] ist 4."""
        f = lambda x: 2 * x
        ergebnis = mittelwert_funktion(f, 0, 4)
        assert abs(ergebnis - 4.0) < 1e-4


class TestBestandsrekonstruktion:
    """Tests für die Rekonstruktion von Beständen aus Änderungsraten."""

    def test_tank_fuellproblem(self):
        """z(t) = 6t - t², W(0) = 10.
        W(6) = 10 + ∫₀⁶ (6t - t²) dt = 10 + [3t² - t³/3]₀⁶ = 10 + 108 - 72 = 46."""
        rate = lambda t: 6 * t - t**2
        ergebnis = bestand_rekonstruktion(10, rate, 6)
        assert abs(ergebnis - 46.0) < 1e-2

    def test_anfangsbestand(self):
        """Bei t = 0 muss der Anfangsbestand zurückkommen."""
        rate = lambda t: 3 * t
        ergebnis = bestand_rekonstruktion(42, rate, 0)
        assert abs(ergebnis - 42.0) < 1e-10

    def test_konstante_rate(self):
        """Konstante Rate 5 über 10 Zeiteinheiten → Zunahme um 50."""
        rate = lambda t: 5.0
        ergebnis = bestand_rekonstruktion(0, rate, 10)
        assert abs(ergebnis - 50.0) < 1e-3


class TestBestimmtesIntegral:
    """Zusätzliche Tests für die numerische Integration."""

    def test_integral_x_quadrat_plus_1(self):
        """∫₀² (x² + 1) dx = [x³/3 + x]₀² = 8/3 + 2 = 14/3."""
        f = lambda x: x**2 + 1
        ergebnis = bestimmtes_integral(f, 0, 2)
        assert abs(ergebnis - 14 / 3) < 1e-4

    def test_integral_exp(self):
        """∫₀¹ eˣ dx = e - 1."""
        f = lambda x: math.exp(x)
        ergebnis = bestimmtes_integral(f, 0, 1)
        assert abs(ergebnis - (math.e - 1)) < 1e-4

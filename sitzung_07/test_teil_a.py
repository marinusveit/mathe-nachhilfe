"""
Tests für Sitzung 7: Hilfsmittelfreier Teil — Ableitungen, Stammfunktionen,
bestimmte Integrale und Graphen-Zuordnungslogik.

Ausführen mit:  pytest sitzung_07/test_teil_a.py -v
"""

import sympy as sp
import pytest

x = sp.Symbol('x')


# ---------------------------------------------------------------------------
# Hilfsfunktionen (identisch zur Notebook-Logik)
# ---------------------------------------------------------------------------

def ableitung(f_expr):
    """Berechnet die Ableitung und vereinfacht."""
    return sp.simplify(sp.diff(f_expr, x))


def stammfunktion(f_expr):
    """Berechnet eine Stammfunktion (ohne Integrationskonstante)."""
    return sp.integrate(f_expr, x)


def bestimmtes_integral(f_expr, a, b):
    """Berechnet das bestimmte Integral von a bis b."""
    return sp.integrate(f_expr, (x, a, b))


def ist_ableitung_von(f_expr, g_expr):
    """Prüft, ob g_expr die Ableitung von f_expr ist."""
    return sp.simplify(sp.diff(f_expr, x) - g_expr) == 0


# ---------------------------------------------------------------------------
# Tests: Ableitungen (symbolisch mit sympy)
# ---------------------------------------------------------------------------

class TestAbleitungen:
    """Diverse Ableitungen, wie sie im Teil A vorkommen."""

    def test_potenzregel_polynom(self):
        f = 5*x**3 - 4*x**2 + 2*x - 7
        assert ableitung(f) == sp.simplify(15*x**2 - 8*x + 2)

    def test_negative_potenz(self):
        # f(x) = 3/x = 3*x^(-1)  →  f'(x) = -3/x²
        f = 3 / x
        assert ableitung(f) == sp.simplify(-3 / x**2)

    def test_wurzel(self):
        # f(x) = 2*sqrt(x)  →  f'(x) = 1/sqrt(x)
        f = 2 * sp.sqrt(x)
        assert ableitung(f) == sp.simplify(1 / sp.sqrt(x))

    def test_kettenregel_potenz(self):
        # f(x) = (3x - 1)^4  →  f'(x) = 12*(3x - 1)^3
        f = (3*x - 1)**4
        assert ableitung(f) == sp.simplify(12 * (3*x - 1)**3)

    def test_kettenregel_exp(self):
        # f(x) = e^(-x²)  →  f'(x) = -2x * e^(-x²)
        f = sp.exp(-x**2)
        assert ableitung(f) == sp.simplify(-2*x * sp.exp(-x**2))

    def test_produktregel_x2_ln(self):
        # f(x) = x² · ln(x)  →  f'(x) = 2x·ln(x) + x
        f = x**2 * sp.log(x)
        erwartet = 2*x * sp.log(x) + x
        assert ableitung(f) == sp.simplify(erwartet)

    def test_produktregel_exp_sin(self):
        # f(x) = e^x · sin(x)  →  f'(x) = e^x·sin(x) + e^x·cos(x)
        f = sp.exp(x) * sp.sin(x)
        erwartet = sp.exp(x) * sp.sin(x) + sp.exp(x) * sp.cos(x)
        assert ableitung(f) == sp.simplify(erwartet)

    def test_trig_summe(self):
        # f(x) = sin(2x) + cos(x)  →  f'(x) = 2cos(2x) - sin(x)
        f = sp.sin(2*x) + sp.cos(x)
        erwartet = 2*sp.cos(2*x) - sp.sin(x)
        assert ableitung(f) == sp.simplify(erwartet)

    def test_exp_negativ(self):
        # f(x) = e^(-3x)  →  f'(x) = -3e^(-3x)
        f = sp.exp(-3*x)
        assert ableitung(f) == sp.simplify(-3*sp.exp(-3*x))

    def test_quotient_einfach(self):
        # f(x) = 1/(x² + 1)  →  f'(x) = -2x/(x² + 1)²
        f = 1 / (x**2 + 1)
        erwartet = -2*x / (x**2 + 1)**2
        assert ableitung(f) == sp.simplify(erwartet)


# ---------------------------------------------------------------------------
# Tests: Stammfunktionen
# ---------------------------------------------------------------------------

class TestStammfunktionen:
    """Stammfunktionen — Probe durch Ableitung."""

    def test_polynom(self):
        f = 6*x**2 - 4*x + 3
        F = stammfunktion(f)
        # Probe: F' muss f ergeben
        assert ist_ableitung_von(F, f)

    def test_exp_linear(self):
        f = sp.exp(2*x)
        F = stammfunktion(f)
        assert ist_ableitung_von(F, f)

    def test_eins_durch_x(self):
        f = 1/x
        F = stammfunktion(f)
        assert ist_ableitung_von(F, f)

    def test_cos(self):
        f = sp.cos(x)
        F = stammfunktion(f)
        assert ist_ableitung_von(F, f)

    def test_sin_linear(self):
        f = sp.sin(3*x)
        F = stammfunktion(f)
        assert ist_ableitung_von(F, f)

    def test_cos_doppelt(self):
        f = 4*sp.cos(2*x)
        F = stammfunktion(f)
        assert ist_ableitung_von(F, f)

    def test_potenz_negativ(self):
        # f(x) = x^(-2)  →  F(x) = -1/x
        f = x**(-2)
        F = stammfunktion(f)
        assert ist_ableitung_von(F, f)


# ---------------------------------------------------------------------------
# Tests: Bestimmte Integrale
# ---------------------------------------------------------------------------

class TestBestimmteIntegrale:
    """Bestimmte Integrale mit exakten (rationalen) Ergebnissen."""

    def test_linear(self):
        # ∫₀³ (2x+1) dx = [x²+x]₀³ = 9+3 = 12
        assert bestimmtes_integral(2*x + 1, 0, 3) == 12

    def test_quadratisch_0_2(self):
        # ∫₀² x² dx = [x³/3]₀² = 8/3
        assert bestimmtes_integral(x**2, 0, 2) == sp.Rational(8, 3)

    def test_quadratisch_1_2(self):
        # ∫₁² x² dx = 8/3 - 1/3 = 7/3
        assert bestimmtes_integral(x**2, 1, 2) == sp.Rational(7, 3)

    def test_kubisch(self):
        # ∫₀² x³ dx = [x⁴/4]₀² = 4
        assert bestimmtes_integral(x**3, 0, 2) == 4

    def test_exp_0_1(self):
        # ∫₀¹ eˣ dx = e - 1
        assert bestimmtes_integral(sp.exp(x), 0, 1) == sp.E - 1

    def test_symmetrisch_ungerade(self):
        # ∫₋₁¹ x³ dx = 0 (ungerade Funktion, symmetrisches Intervall)
        assert bestimmtes_integral(x**3, -1, 1) == 0

    def test_negatives_ergebnis(self):
        # ∫₀² (x² - 2x) dx = [x³/3 - x²]₀² = 8/3 - 4 = -4/3
        assert bestimmtes_integral(x**2 - 2*x, 0, 2) == sp.Rational(-4, 3)


# ---------------------------------------------------------------------------
# Tests: Graphen-Zuordnungslogik
# ---------------------------------------------------------------------------

class TestGraphenZuordnung:
    """Prüft die mathematische Logik hinter der Graphen-Zuordnung:
    Nullstellen von f' = Extrema von f, Nullstellen von f'' = Wendepunkte von f."""

    def test_extrema_aus_ableitung(self):
        """Nullstellen von f' sind Kandidaten für Extrema von f."""
        f = x**3 - 3*x
        fp = sp.diff(f, x)
        nullstellen_fp = sp.solve(fp, x)
        # f'(x) = 3x² - 3 = 0 → x = ±1
        assert set(nullstellen_fp) == {-1, 1}

    def test_art_der_extrema(self):
        """f''(x₀) entscheidet über Hoch-/Tiefpunkt."""
        f = x**3 - 3*x
        fp = sp.diff(f, x)
        fpp = sp.diff(f, x, 2)
        nullstellen = sp.solve(fp, x)
        arten = {}
        for x0 in nullstellen:
            wert = fpp.subs(x, x0)
            if wert > 0:
                arten[x0] = 'Tiefpunkt'
            elif wert < 0:
                arten[x0] = 'Hochpunkt'
            else:
                arten[x0] = 'unklar'
        assert arten[-1] == 'Hochpunkt'
        assert arten[1] == 'Tiefpunkt'

    def test_wendepunkt_aus_zweiter_ableitung(self):
        """Nullstellen von f'' mit VZW sind Wendepunkte."""
        f = x**3 - 3*x
        fpp = sp.diff(f, x, 2)  # 6x
        nullstellen_fpp = sp.solve(fpp, x)
        assert nullstellen_fpp == [0]
        # VZW prüfen: f''(-0.1) < 0, f''(0.1) > 0
        assert fpp.subs(x, sp.Rational(-1, 10)) < 0
        assert fpp.subs(x, sp.Rational(1, 10)) > 0

    def test_ableitung_ist_ableitung(self):
        """Konsistenzprüfung: Ableitung der gespeicherten f muss f' ergeben."""
        funktionen = [
            (x**3 - 3*x, 3*x**2 - 3, 6*x),
            (-x**4 + 4*x**2, -4*x**3 + 8*x, -12*x**2 + 8),
        ]
        for f_expr, fp_expr, fpp_expr in funktionen:
            assert sp.simplify(sp.diff(f_expr, x) - fp_expr) == 0
            assert sp.simplify(sp.diff(fp_expr, x) - fpp_expr) == 0

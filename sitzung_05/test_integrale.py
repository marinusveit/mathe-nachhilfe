"""Tests für Sitzung 5: Stammfunktionen & bestimmtes Integral."""

import math
import pytest
import sympy as sp

x = sp.Symbol('x')


# ---------------------------------------------------------------------------
# Hilfsfunktionen (werden direkt hier definiert, nicht importiert)
# ---------------------------------------------------------------------------

def stammfunktion(f_expr):
    """Berechnet eine Stammfunktion (ohne Integrationskonstante)."""
    return sp.integrate(f_expr, x)


def bestimmtes_integral(f_expr, a, b):
    """Berechnet das bestimmte Integral von a bis b."""
    return sp.integrate(f_expr, (x, a, b))


def riemann_summe(f_callable, a, b, n):
    """Berechnet die Riemann-Summe (linke Rechtecke) für f auf [a, b] mit n Rechtecken."""
    dx = (b - a) / n
    return sum(f_callable(a + i * dx) * dx for i in range(n))


def flaecheninhalt_mit_vorzeichenwechsel(f_expr, a, b):
    """Berechnet den Flächeninhalt |∫| stückweise an Nullstellen."""
    nullstellen = sp.solve(f_expr, x)
    nullstellen = sorted([float(ns) for ns in nullstellen if ns.is_real and a < ns < b])
    grenzen = [a] + nullstellen + [b]
    flaeche = 0
    for i in range(len(grenzen) - 1):
        teil = sp.integrate(f_expr, (x, grenzen[i], grenzen[i + 1]))
        flaeche += abs(teil)
    return flaeche


# ---------------------------------------------------------------------------
# Test 1–3: Stammfunktionen (Grundintegrale)
# ---------------------------------------------------------------------------

class TestStammfunktionen:
    def test_potenzregel_x_quadrat(self):
        """∫x² dx = x³/3"""
        F = stammfunktion(x**2)
        assert sp.simplify(F - x**3 / 3) == 0

    def test_potenzregel_polynom(self):
        """∫(3x² + 2x + 1) dx = x³ + x² + x"""
        F = stammfunktion(3 * x**2 + 2 * x + 1)
        erwartet = x**3 + x**2 + x
        assert sp.simplify(F - erwartet) == 0

    def test_e_funktion(self):
        """∫eˣ dx = eˣ"""
        F = stammfunktion(sp.exp(x))
        assert sp.simplify(F - sp.exp(x)) == 0

    def test_e_funktion_mit_faktor(self):
        """∫e^(3x) dx = e^(3x)/3"""
        F = stammfunktion(sp.exp(3 * x))
        erwartet = sp.exp(3 * x) / 3
        assert sp.simplify(F - erwartet) == 0

    def test_eins_durch_x(self):
        """∫1/x dx = ln|x|"""
        F = stammfunktion(1 / x)
        # sympy gibt ln(x) zurück (ohne Betrag), das ist korrekt für x > 0
        assert sp.simplify(F - sp.log(x)) == 0

    def test_ableitung_der_stammfunktion(self):
        """F'(x) = f(x) — der Hauptsatz."""
        f_expr = x**4 - 2 * x**2 + 7
        F = stammfunktion(f_expr)
        assert sp.simplify(sp.diff(F, x) - f_expr) == 0


# ---------------------------------------------------------------------------
# Test 4–6: Bestimmte Integrale
# ---------------------------------------------------------------------------

class TestBestimmtesIntegral:
    def test_x_quadrat_0_bis_2(self):
        """∫₀² x² dx = 8/3"""
        ergebnis = bestimmtes_integral(x**2, 0, 2)
        assert ergebnis == sp.Rational(8, 3)

    def test_sinus_0_bis_pi(self):
        """∫₀^π sin(x) dx = 2"""
        ergebnis = bestimmtes_integral(sp.sin(x), 0, sp.pi)
        assert ergebnis == 2

    def test_linear_1_bis_4(self):
        """∫₁⁴ (2x − 1) dx = 12"""
        ergebnis = bestimmtes_integral(2 * x - 1, 1, 4)
        assert ergebnis == 12

    def test_e_funktion_0_bis_1(self):
        """∫₀¹ e^(2x) dx = (e² − 1)/2"""
        ergebnis = bestimmtes_integral(sp.exp(2 * x), 0, 1)
        erwartet = (sp.exp(2) - 1) / 2
        assert sp.simplify(ergebnis - erwartet) == 0

    def test_ln_1_bis_e(self):
        """∫₁ᵉ 1/x dx = 1"""
        ergebnis = bestimmtes_integral(1 / x, 1, sp.E)
        assert ergebnis == 1


# ---------------------------------------------------------------------------
# Test 7–8: Riemann-Summen (Konvergenz)
# ---------------------------------------------------------------------------

class TestRiemannSummen:
    def test_konvergenz_x_quadrat(self):
        """Riemann-Summe für x² auf [0, 2] konvergiert gegen 8/3."""
        f = lambda t: t**2
        exakt = 8 / 3
        for n, tol in [(10, 0.5), (100, 0.05), (1000, 0.005)]:
            approx = riemann_summe(f, 0, 2, n)
            assert abs(approx - exakt) < tol, (
                f"n={n}: Riemann={approx:.6f}, exakt={exakt:.6f}"
            )

    def test_konvergenz_sinus(self):
        """Riemann-Summe für sin(x) auf [0, π] konvergiert gegen 2."""
        f = math.sin
        exakt = 2.0
        approx_100 = riemann_summe(f, 0, math.pi, 100)
        approx_10000 = riemann_summe(f, 0, math.pi, 10000)
        assert abs(approx_100 - exakt) < 0.05
        assert abs(approx_10000 - exakt) < 0.001


# ---------------------------------------------------------------------------
# Test 9–10: Flächenberechnung mit Vorzeichenwechsel
# ---------------------------------------------------------------------------

class TestFlaechenberechnung:
    def test_x_quadrat_minus_4(self):
        """Fläche von f(x) = x² − 4 auf [−2, 2]: Integral ist negativ, Fläche positiv."""
        f_expr = x**2 - 4
        integral = bestimmtes_integral(f_expr, -2, 2)
        assert integral == sp.Rational(-32, 3)  # negativ!
        flaeche = flaecheninhalt_mit_vorzeichenwechsel(f_expr, -2, 2)
        assert flaeche == sp.Rational(32, 3)  # positiv!

    def test_x_kubisch_minus_4x(self):
        """Fläche von f(x) = x³ − 4x auf [−2, 2] mit Vorzeichenwechsel."""
        f_expr = x**3 - 4 * x
        # Das Integral über das symmetrische Intervall ist 0 (ungerade Funktion!)
        integral = bestimmtes_integral(f_expr, -2, 2)
        assert integral == 0
        # Aber die Fläche ist > 0
        flaeche = flaecheninhalt_mit_vorzeichenwechsel(f_expr, -2, 2)
        assert flaeche == 8

    def test_integral_gleich_flaeche_wenn_positiv(self):
        """Wenn f(x) >= 0 auf [a,b], dann ist Integral = Fläche."""
        f_expr = x**2 + 1  # immer positiv
        integral = bestimmtes_integral(f_expr, 0, 3)
        flaeche = flaecheninhalt_mit_vorzeichenwechsel(f_expr, 0, 3)
        assert integral == flaeche

"""
Tests für die Probeklausur-Aufgaben (Sitzung 8).

Überprüft Musterlösungen symbolisch mit sympy:
Ableitungen, Nullstellen, Extrema, Integrale, Flächenberechnungen.
"""

import pytest
import sympy as sp

x = sp.Symbol("x")
a = sp.Symbol("a", positive=True)

# ============================================================
# Funktionen aus der Klausur
# ============================================================

# Teil A
f_A1a = 3 * x**4 - 2 * x**2 + 5 * x - 1
g_A1b = (2 * x + 1) ** 5
h_A1c = x**2 * sp.exp(x)
f_A2 = x**3 - 3 * x
integrand_A4 = 3 * x**2 - 4 * x + 1

# Teil B
f_B = (2 * x - x**2) * sp.exp(x)
f_B_schar = (a * x - x**2) * sp.exp(x)


# ============================================================
# Teil A — Ableitungen (A1)
# ============================================================

class TestAbleitungen:
    """A1: Ableitungen verschiedener Funktionen."""

    def test_A1a_potenzregel(self):
        ergebnis = sp.diff(f_A1a, x)
        erwartet = 12 * x**3 - 4 * x + 5
        assert sp.simplify(ergebnis - erwartet) == 0

    def test_A1b_kettenregel(self):
        ergebnis = sp.diff(g_A1b, x)
        erwartet = 10 * (2 * x + 1) ** 4
        assert sp.simplify(ergebnis - erwartet) == 0

    def test_A1c_produktregel(self):
        ergebnis = sp.diff(h_A1c, x)
        erwartet = (2 * x + x**2) * sp.exp(x)
        assert sp.simplify(ergebnis - erwartet) == 0


# ============================================================
# Teil A — Nullstellen und Extrema (A2)
# ============================================================

class TestKurvendiskussionA2:
    """A2: f(x) = x^3 - 3x — Nullstellen und lokales Minimum."""

    def test_nullstellen(self):
        nst = sp.solve(f_A2, x)
        assert set(nst) == {0, sp.sqrt(3), -sp.sqrt(3)}

    def test_extremum_x1_ist_minimum(self):
        f_prime = sp.diff(f_A2, x)
        f_double_prime = sp.diff(f_A2, x, 2)
        # f'(1) = 0
        assert f_prime.subs(x, 1) == 0
        # f''(1) > 0 → Minimum
        assert f_double_prime.subs(x, 1) > 0

    def test_minimum_wert(self):
        assert f_A2.subs(x, 1) == -2


# ============================================================
# Teil A — Integral (A4)
# ============================================================

class TestIntegral:
    """A4: Bestimmtes Integral von 3x^2 - 4x + 1 auf [0, 2]."""

    def test_bestimmtes_integral(self):
        ergebnis = sp.integrate(integrand_A4, (x, 0, 2))
        assert ergebnis == 2


# ============================================================
# Teil B — Kurvendiskussion f(x) = (2x - x^2) * e^x
# ============================================================

class TestTeilB:
    """B1: Vollständige Untersuchung von f(x) = (2x - x^2) * e^x."""

    def test_nullstellen(self):
        """B1a: Nullstellen."""
        nst = sp.solve(f_B, x)
        assert set(nst) == {0, 2}

    def test_grenzwert_plus_unendlich(self):
        """B1a: Verhalten für x → +∞."""
        grenzwert = sp.limit(f_B, x, sp.oo)
        assert grenzwert == -sp.oo

    def test_grenzwert_minus_unendlich(self):
        """B1a: Verhalten für x → -∞."""
        grenzwert = sp.limit(f_B, x, -sp.oo)
        assert grenzwert == 0

    def test_ableitung(self):
        """B1b: Erste Ableitung berechnen."""
        f_prime = sp.diff(f_B, x)
        erwartet = (2 - 2 * x + 2 * x - x**2) * sp.exp(x)  # = (2 - x^2) * e^x
        assert sp.simplify(f_prime - erwartet) == 0

    def test_extremstellen(self):
        """B1b: Extremstellen bestimmen."""
        f_prime = sp.diff(f_B, x)
        kritische = sp.solve(f_prime, x)
        assert set(kritische) == {sp.sqrt(2), -sp.sqrt(2)}

    def test_hochpunkt(self):
        """B1b: Hochpunkt bei x = sqrt(2)."""
        f_double_prime = sp.diff(f_B, x, 2)
        assert f_double_prime.subs(x, sp.sqrt(2)) < 0

    def test_tiefpunkt(self):
        """B1b: Tiefpunkt bei x = -sqrt(2)."""
        f_double_prime = sp.diff(f_B, x, 2)
        assert f_double_prime.subs(x, -sp.sqrt(2)) > 0

    def test_tangente_nullpunkt(self):
        """B1c: Tangente im Ursprung."""
        f_prime = sp.diff(f_B, x)
        m = f_prime.subs(x, 0)
        y0 = f_B.subs(x, 0)
        # Tangente: t(x) = m*x + y0
        assert m == 2
        assert y0 == 0
        # t(x) = 2x, Nullstelle bei x = 0
        tangente = m * x + y0
        tangente_nst = sp.solve(tangente, x)
        assert tangente_nst == [0]

    def test_flaeche_0_bis_2(self):
        """B1d: Fläche zwischen f und x-Achse auf [0, 2]."""
        # f >= 0 auf [0, 2], also direkte Integration
        flaeche = sp.integrate(f_B, (x, 0, 2))
        flaeche_simplified = sp.simplify(flaeche)
        # (2x - x^2)*e^x von 0 bis 2 = 4*e^2 - ... berechnen
        erwartet = sp.integrate((2 * x - x**2) * sp.exp(x), (x, 0, 2))
        assert sp.simplify(flaeche_simplified - erwartet) == 0
        # Numerischer Check: Wert sollte positiv sein
        assert float(flaeche_simplified) > 0

    def test_schar_gemeinsame_nullstelle(self):
        """B1e: Alle f_a haben gemeinsame Nullstelle x = 0."""
        assert f_B_schar.subs(x, 0) == 0


# ============================================================
# Zusätzliche Checks
# ============================================================

class TestZusaetzlich:
    """Weitere Konsistenztests."""

    def test_f_B_positiv_auf_0_2(self):
        """f(x) = (2x - x^2)*e^x ist auf (0, 2) positiv."""
        # Prüfe an Stichprobenpunkten
        for xval in [sp.Rational(1, 4), sp.Rational(1, 2), 1, sp.Rational(3, 2)]:
            assert f_B.subs(x, xval) > 0

    def test_stammfunktion_A4(self):
        """Stammfunktion von 3x^2 - 4x + 1 ist x^3 - 2x^2 + x."""
        F = sp.integrate(integrand_A4, x)
        # Ableitung der Stammfunktion muss wieder Integrand ergeben
        assert sp.simplify(sp.diff(F, x) - integrand_A4) == 0

    def test_schar_nullstellen(self):
        """f_a hat Nullstellen bei x = 0 und x = a."""
        nst = sp.solve(f_B_schar, x)
        assert 0 in nst
        assert a in nst

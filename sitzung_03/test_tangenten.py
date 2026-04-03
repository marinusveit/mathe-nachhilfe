"""Tests für die mathematischen Funktionen aus Sitzung 3 (Tangente, Normale, Funktionsscharen).

Die Rechenfunktionen sind hier direkt definiert (nicht aus dem Notebook importiert),
damit die Tests unabhängig laufen.
"""

import pytest
import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# Hilfsfunktionen (aus dem Notebook übernommen)
# ---------------------------------------------------------------------------

x_sym = sp.Symbol('x')


def tangentengleichung(f, f_prime, x0):
    """Berechnet die Tangente t(x) = f'(x0)·(x - x0) + f(x0) als lambda."""
    m = f_prime(x0)
    y0 = f(x0)
    return lambda x: m * (x - x0) + y0, m


def normalengleichung(f, f_prime, x0):
    """Berechnet die Normale n(x) = -1/f'(x0)·(x - x0) + f(x0) als lambda.

    Gibt (None, None) zurück wenn f'(x0) = 0 (senkrechte Normale).
    """
    m = f_prime(x0)
    y0 = f(x0)
    if abs(m) < 1e-12:
        return None, None
    m_n = -1 / m
    return lambda x: m_n * (x - x0) + y0, m_n


def tangente_symbolisch(f_sym, x0_wert):
    """Berechnet die Tangentengleichung symbolisch mit Sympy."""
    f_prime_sym = sp.diff(f_sym, x_sym)
    y0 = f_sym.subs(x_sym, x0_wert)
    m = f_prime_sym.subs(x_sym, x0_wert)
    tangente = sp.expand(m * (x_sym - x0_wert) + y0)
    return tangente, m, y0


def normale_symbolisch(f_sym, x0_wert):
    """Berechnet die Normalengleichung symbolisch mit Sympy."""
    f_prime_sym = sp.diff(f_sym, x_sym)
    y0 = f_sym.subs(x_sym, x0_wert)
    m = f_prime_sym.subs(x_sym, x0_wert)
    if m == 0:
        return None, None, y0
    m_n = -1 / m
    normale = sp.expand(m_n * (x_sym - x0_wert) + y0)
    return normale, m_n, y0


def extrempunkte_schar_kubisch(t):
    """Extrempunkte von f_t(x) = x³ - 3t²x.

    Returns: (x_hp, y_hp, x_tp, y_tp)
    """
    x_hp = -t
    y_hp = x_hp**3 - 3 * t**2 * x_hp  # = 2t³
    x_tp = t
    y_tp = x_tp**3 - 3 * t**2 * x_tp  # = -2t³
    return x_hp, y_hp, x_tp, y_tp


def ortskurve_kubisch(x_val):
    """Ortskurve der Extrempunkte von f_t(x) = x³ - 3t²x ist y = -2x³."""
    return -2 * x_val**3


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestTangente:
    """Tests für die Tangentenberechnung."""

    def test_tangente_kubisch_bei_x0_1(self):
        """f(x) = x³ - 3x bei x₀ = 1: Steigung = 0 (Extremstelle)."""
        f = lambda x: x**3 - 3*x
        f_prime = lambda x: 3*x**2 - 3
        t, m = tangentengleichung(f, f_prime, 1.0)
        assert m == pytest.approx(0.0)
        assert t(1.0) == pytest.approx(f(1.0))
        # Waagrechte Tangente: t(x) = -2 für alle x
        assert t(0.0) == pytest.approx(-2.0)
        assert t(5.0) == pytest.approx(-2.0)

    def test_tangente_exp_bei_x0_0(self):
        """f(x) = eˣ bei x₀ = 0: Steigung = 1, Tangente t(x) = x + 1."""
        f = np.exp
        f_prime = np.exp
        t, m = tangentengleichung(f, f_prime, 0.0)
        assert m == pytest.approx(1.0)
        assert t(0.0) == pytest.approx(1.0)
        assert t(1.0) == pytest.approx(2.0)

    def test_tangente_geht_durch_beruehrpunkt(self):
        """Die Tangente muss immer durch den Berührpunkt gehen."""
        f = lambda x: x**2
        f_prime = lambda x: 2*x
        for x0 in [-2.0, -1.0, 0.0, 0.5, 1.0, 3.0]:
            t, _ = tangentengleichung(f, f_prime, x0)
            assert t(x0) == pytest.approx(f(x0)), f"Tangente verfehlt Punkt bei x₀={x0}"

    def test_tangente_parabel_bei_x0_3(self):
        """f(x) = x² bei x₀ = 3: t(x) = 6x - 9."""
        f = lambda x: x**2
        f_prime = lambda x: 2*x
        t, m = tangentengleichung(f, f_prime, 3.0)
        assert m == pytest.approx(6.0)
        assert t(0.0) == pytest.approx(-9.0)
        assert t(3.0) == pytest.approx(9.0)


class TestNormale:
    """Tests für die Normalenberechnung."""

    def test_normale_steigung_negativ_reziprok(self):
        """Normale hat Steigung -1/m wenn m != 0."""
        f = lambda x: x**2
        f_prime = lambda x: 2*x
        _, m_n = normalengleichung(f, f_prime, 2.0)
        assert m_n == pytest.approx(-1 / 4.0)

    def test_normale_senkrecht_bei_waagrechter_tangente(self):
        """Wenn f'(x₀) = 0, ist die Normale senkrecht (None)."""
        f = lambda x: x**3 - 3*x
        f_prime = lambda x: 3*x**2 - 3
        n, m_n = normalengleichung(f, f_prime, 1.0)
        assert n is None
        assert m_n is None

    def test_normale_geht_durch_beruehrpunkt(self):
        """Die Normale muss durch den Berührpunkt gehen."""
        f = lambda x: x**2
        f_prime = lambda x: 2*x
        for x0 in [-2.0, -1.0, 0.5, 1.0, 3.0]:
            n, _ = normalengleichung(f, f_prime, x0)
            if n is not None:
                assert n(x0) == pytest.approx(f(x0)), \
                    f"Normale verfehlt Punkt bei x₀={x0}"

    def test_tangente_normale_orthogonal(self):
        """Produkt der Steigungen von Tangente und Normale ist -1."""
        f = lambda x: x**3
        f_prime = lambda x: 3*x**2
        for x0 in [0.5, 1.0, 2.0, -1.0]:
            _, m_t = tangentengleichung(f, f_prime, x0)
            _, m_n = normalengleichung(f, f_prime, x0)
            if m_n is not None:
                assert m_t * m_n == pytest.approx(-1.0), \
                    f"Nicht orthogonal bei x₀={x0}"


class TestSymbolisch:
    """Tests für die symbolische Berechnung mit Sympy."""

    def test_symbolisch_tangente_x_hoch_3(self):
        """f(x) = x³ bei x₀ = 2: t(x) = 12x - 16."""
        f_sym = x_sym**3
        tangente, m, y0 = tangente_symbolisch(f_sym, 2)
        assert m == 12
        assert y0 == 8
        assert tangente == 12 * x_sym - 16

    def test_symbolisch_normale_x_quadrat(self):
        """f(x) = x² bei x₀ = 1: Normale hat m_n = -1/2."""
        f_sym = x_sym**2
        normale, m_n, y0 = normale_symbolisch(f_sym, 1)
        assert m_n == sp.Rational(-1, 2)
        assert y0 == 1
        # n(x) = -1/2 (x - 1) + 1 = -x/2 + 3/2
        assert normale == -x_sym / 2 + sp.Rational(3, 2)

    def test_symbolisch_horizontale_tangente(self):
        """f(x) = x² bei x₀ = 0: Steigung 0, t(x) = 0."""
        f_sym = x_sym**2
        tangente, m, y0 = tangente_symbolisch(f_sym, 0)
        assert m == 0
        assert tangente == 0


class TestFunktionsscharen:
    """Tests für Funktionsscharen und Ortskurven."""

    def test_extrempunkte_kubisch_t1(self):
        """f_1(x) = x³ - 3x: HP(-1|2), TP(1|-2)."""
        x_hp, y_hp, x_tp, y_tp = extrempunkte_schar_kubisch(1.0)
        assert x_hp == pytest.approx(-1.0)
        assert y_hp == pytest.approx(2.0)
        assert x_tp == pytest.approx(1.0)
        assert y_tp == pytest.approx(-2.0)

    def test_extrempunkte_kubisch_t2(self):
        """f_2(x) = x³ - 12x: HP(-2|16), TP(2|-16)."""
        x_hp, y_hp, x_tp, y_tp = extrempunkte_schar_kubisch(2.0)
        assert x_hp == pytest.approx(-2.0)
        assert y_hp == pytest.approx(16.0)
        assert x_tp == pytest.approx(2.0)
        assert y_tp == pytest.approx(-16.0)

    def test_ortskurve_stimmt_mit_extrempunkten(self):
        """Die Ortskurve y = -2x³ geht durch alle Extrempunkte."""
        for t in [0.5, 1.0, 1.5, 2.0, 2.5]:
            x_hp, y_hp, x_tp, y_tp = extrempunkte_schar_kubisch(t)
            assert ortskurve_kubisch(x_hp) == pytest.approx(y_hp), \
                f"Ortskurve verfehlt HP bei t={t}"
            assert ortskurve_kubisch(x_tp) == pytest.approx(y_tp), \
                f"Ortskurve verfehlt TP bei t={t}"

    def test_ortskurve_formel(self):
        """y = -2x³ für konkrete Werte."""
        assert ortskurve_kubisch(0.0) == pytest.approx(0.0)
        assert ortskurve_kubisch(1.0) == pytest.approx(-2.0)
        assert ortskurve_kubisch(-1.0) == pytest.approx(2.0)
        assert ortskurve_kubisch(2.0) == pytest.approx(-16.0)

"""
Tests für die mathematischen Funktionen aus Sitzung 4:
Extremwertprobleme & Steckbriefaufgaben.

Die zu testenden Funktionen sind direkt hier definiert (kein Notebook-Import).
"""
import numpy as np
import pytest
import sympy as sp


# ============================================================
# Hilfsfunktionen — Dose-Optimierung
# ============================================================

def dose_oberflaeche(r: float, V: float = 500.0) -> float:
    """Oberfläche eines Zylinders bei gegebenem Volumen V und Radius r."""
    h = V / (np.pi * r**2)
    return 2 * np.pi * r**2 + 2 * np.pi * r * h


def dose_optimaler_radius(V: float = 500.0) -> float:
    """Optimaler Radius für minimale Oberfläche bei Volumen V."""
    # O(r) = 2πr² + 2V/r  →  O'(r) = 4πr − 2V/r² = 0  →  r = (V/(2π))^(1/3)
    return (V / (2 * np.pi)) ** (1 / 3)


def dose_optimale_hoehe(V: float = 500.0) -> float:
    """Optimale Höhe (h = V / (π r²)) beim optimalen Radius."""
    r = dose_optimaler_radius(V)
    return V / (np.pi * r**2)


# ============================================================
# Hilfsfunktionen — Zaun-Problem
# ============================================================

def zaun_flaeche(x: float, L: float = 40.0) -> float:
    """Fläche eines Rechtecks an einer Mauer.
    x = Seite senkrecht zur Mauer, L = verfügbarer Zaun.
    Nebenbedingung: 2x + y = L  →  y = L − 2x.
    """
    y = L - 2 * x
    return x * y


def zaun_optimale_seite(L: float = 40.0) -> float:
    """Optimale Seitenlänge x (senkrecht zur Mauer).
    A(x) = x(L − 2x) = Lx − 2x²  →  A'(x) = L − 4x = 0  →  x = L/4.
    """
    return L / 4


def zaun_max_flaeche(L: float = 40.0) -> float:
    """Maximale Fläche beim Zaun-Problem."""
    x = zaun_optimale_seite(L)
    return zaun_flaeche(x, L)


# ============================================================
# Hilfsfunktionen — Blech-Quader
# ============================================================

def blech_volumen(x: float, a: float = 20.0) -> float:
    """Volumen des offenen Quaders: V = x · (a−2x)²."""
    return x * (a - 2 * x) ** 2


def blech_optimales_x(a: float = 20.0) -> float:
    """Optimale Ausschnittgröße x für maximales Volumen.
    V(x) = x(a−2x)² →  V'(x) = (a−2x)(a−6x) = 0
    Lösungen: x = a/2 (Minimum, V=0) und x = a/6.
    """
    return a / 6


# ============================================================
# Hilfsfunktionen — Steckbrief-Löser
# ============================================================

def steckbrief_loesen(grad: int, bedingungen: list[tuple]) -> list[float]:
    """Löst eine Steckbriefaufgabe.

    Parameter:
        grad: Grad des Polynoms
        bedingungen: Liste von (typ, x_wert, y_wert) wobei
            typ = 0 → f(x_wert) = y_wert
            typ = 1 → f'(x_wert) = y_wert
            typ = 2 → f''(x_wert) = y_wert

    Rückgabe:
        Liste der Koeffizienten [a_n, a_{n-1}, ..., a_1, a_0]
        (höchster Grad zuerst, wie bei np.polyval).
    """
    x = sp.Symbol('x')
    koeffs = sp.symbols(f'a0:{grad + 1}')  # a0, a1, ..., a_n
    # Polynom: a0 + a1*x + a2*x² + ... + a_n*x^n
    poly = sum(koeffs[k] * x**k for k in range(grad + 1))

    gleichungen = []
    for typ, x_val, y_val in bedingungen:
        if typ == 0:
            expr = poly
        elif typ == 1:
            expr = sp.diff(poly, x)
        elif typ == 2:
            expr = sp.diff(poly, x, 2)
        else:
            raise ValueError(f"Unbekannter Typ: {typ}")
        gleichungen.append(sp.Eq(expr.subs(x, x_val), y_val))

    loesung = sp.solve(gleichungen, koeffs)
    if not loesung:
        raise ValueError("Gleichungssystem hat keine Lösung")

    # Koeffizienten in absteigender Reihenfolge (für np.polyval)
    result = [float(loesung[koeffs[k]]) for k in range(grad, -1, -1)]
    return result


# ============================================================
# Tests — Dose-Optimierung
# ============================================================

class TestDose:
    def test_optimaler_radius_V500(self):
        r = dose_optimaler_radius(500)
        expected = (250 / np.pi) ** (1 / 3)
        assert abs(r - expected) < 1e-10

    def test_oberflaeche_am_optimum_ist_minimum(self):
        r_opt = dose_optimaler_radius(500)
        O_opt = dose_oberflaeche(r_opt, 500)
        # Oberfläche bei leicht anderen Radien muss größer sein
        for delta in [0.5, 1.0, 2.0]:
            assert dose_oberflaeche(r_opt + delta, 500) > O_opt
            assert dose_oberflaeche(r_opt - delta * 0.5, 500) > O_opt

    def test_verhaeltnis_hoehe_durchmesser(self):
        """Beim optimalen Zylinder gilt h = d (Höhe = Durchmesser)."""
        r = dose_optimaler_radius(500)
        h = dose_optimale_hoehe(500)
        d = 2 * r
        assert abs(h / d - 1.0) < 1e-10

    def test_verschiedene_volumina(self):
        for V in [100, 330, 500, 1000]:
            r = dose_optimaler_radius(V)
            h = dose_optimale_hoehe(V)
            # Volumen muss stimmen
            assert abs(np.pi * r**2 * h - V) < 1e-8


# ============================================================
# Tests — Zaun-Problem
# ============================================================

class TestZaun:
    def test_optimale_seite_L40(self):
        assert abs(zaun_optimale_seite(40) - 10.0) < 1e-10

    def test_max_flaeche_L40(self):
        assert abs(zaun_max_flaeche(40) - 200.0) < 1e-10

    def test_flaeche_am_optimum_ist_maximum(self):
        x_opt = zaun_optimale_seite(40)
        A_opt = zaun_max_flaeche(40)
        for dx in [1, 2, 5]:
            assert zaun_flaeche(x_opt + dx, 40) < A_opt
            assert zaun_flaeche(x_opt - dx, 40) < A_opt

    def test_verschiedene_zaunlaengen(self):
        for L in [20, 40, 60, 100]:
            x = zaun_optimale_seite(L)
            A = zaun_max_flaeche(L)
            assert abs(x - L / 4) < 1e-10
            assert abs(A - L**2 / 8) < 1e-10


# ============================================================
# Tests — Blech-Quader
# ============================================================

class TestBlech:
    def test_optimales_x_a20(self):
        assert abs(blech_optimales_x(20) - 10 / 3) < 1e-10

    def test_volumen_am_optimum(self):
        x = blech_optimales_x(20)
        V = blech_volumen(x, 20)
        expected = (10 / 3) * (20 - 20 / 3) ** 2  # ≈ 592.6
        assert abs(V - expected) < 1e-8


# ============================================================
# Tests — Steckbrief-Löser
# ============================================================

class TestSteckbrief:
    def test_parabel_durch_drei_punkte(self):
        """f(x) = x² hat f(0)=0, f(1)=1, f(-1)=1."""
        koeffs = steckbrief_loesen(2, [
            (0, 0, 0),
            (0, 1, 1),
            (0, -1, 1),
        ])
        # koeffs = [1, 0, 0] → x²
        np.testing.assert_allclose(koeffs, [1, 0, 0], atol=1e-10)

    def test_B2_extremum_und_punkte(self):
        """B2: f'(1)=0, f(1)=4, f(0)=3 → f(x) = -x² + 2x + 3."""
        koeffs = steckbrief_loesen(2, [
            (1, 1, 0),   # f'(1) = 0
            (0, 1, 4),   # f(1) = 4
            (0, 0, 3),   # f(0) = 3
        ])
        np.testing.assert_allclose(koeffs, [-1, 2, 3], atol=1e-10)

    def test_kubisch_B1(self):
        """B1: f(0)=2, f'(0)=0, f(2)=0, f'(2)=0."""
        koeffs = steckbrief_loesen(3, [
            (0, 0, 2),   # f(0) = 2
            (1, 0, 0),   # f'(0) = 0
            (0, 2, 0),   # f(2) = 0
            (1, 2, 0),   # f'(2) = 0
        ])
        # Polynom: a3*x³ + a2*x² + a1*x + a0
        # Auswerten bei x=0 und x=2 zur Kontrolle
        assert abs(np.polyval(koeffs, 0) - 2) < 1e-10
        assert abs(np.polyval(koeffs, 2) - 0) < 1e-10
        # f'(0) = 0 → a1 = 0
        assert abs(koeffs[2]) < 1e-10  # a1 (zweitletzter Koeffizient)

    def test_gerade_aus_zwei_bedingungen(self):
        """f(x) = 2x + 1 hat f(0)=1 und f(1)=3."""
        koeffs = steckbrief_loesen(1, [
            (0, 0, 1),
            (0, 1, 3),
        ])
        np.testing.assert_allclose(koeffs, [2, 1], atol=1e-10)

    def test_wendepunkt_bedingung(self):
        """Funktion mit f''(1) = 0 (Wendepunkt-Bedingung)."""
        koeffs = steckbrief_loesen(3, [
            (0, 0, 0),   # f(0) = 0
            (0, 1, 1),   # f(1) = 1
            (1, 0, 1),   # f'(0) = 1
            (2, 1, 0),   # f''(1) = 0
        ])
        # Kontrolle: f(0)=0, f(1)=1
        assert abs(np.polyval(koeffs, 0) - 0) < 1e-10
        assert abs(np.polyval(koeffs, 1) - 1) < 1e-10


# ============================================================
# Tests — Sympy-basierte symbolische Verifikation
# ============================================================

class TestSympy:
    def test_dose_ableitung_nullstelle(self):
        """Symbolisch: O'(r) = 0 liefert r = (V/(2π))^(1/3)."""
        r, V = sp.symbols('r V', positive=True)
        h = V / (sp.pi * r**2)
        O = 2 * sp.pi * r**2 + 2 * sp.pi * r * h
        O_simplified = sp.simplify(O)
        dO = sp.diff(O_simplified, r)
        loesungen = sp.solve(dO, r)
        # Es gibt genau eine positive reelle Lösung
        assert len(loesungen) == 1
        # Prüfe, dass sie (V/(2π))^(1/3) entspricht
        expected = (V / (2 * sp.pi)) ** sp.Rational(1, 3)
        assert sp.simplify(loesungen[0] - expected) == 0

    def test_zaun_symbolisch(self):
        """Symbolisch: A(x) = x(L-2x), A'=0 → x = L/4."""
        x, L = sp.symbols('x L', positive=True)
        A = x * (L - 2 * x)
        dA = sp.diff(A, x)
        lsg = sp.solve(dA, x)
        assert len(lsg) == 1
        assert sp.simplify(lsg[0] - L / 4) == 0

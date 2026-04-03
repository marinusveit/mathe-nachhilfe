import json
import pathlib
import unittest
from functools import lru_cache
from unittest.mock import Mock, patch

import matplotlib
import numpy as np
import sympy as sp

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = pathlib.Path(__file__).resolve().parents[1]
NOTEBOOK_PATH = ROOT / "sitzung_01" / "ableitungen_interaktiv.ipynb"


def _strip_magics_and_interact_calls(source):
    cleaned_lines = []
    skip_interact = False
    paren_depth = 0

    for line in source.splitlines(True):
        stripped = line.lstrip()

        if stripped.startswith("%"):
            continue

        if not skip_interact and stripped.startswith("interact("):
            skip_interact = True
            paren_depth = line.count("(") - line.count(")")
            if paren_depth <= 0:
                skip_interact = False
            continue

        if skip_interact:
            paren_depth += line.count("(") - line.count(")")
            if paren_depth <= 0:
                skip_interact = False
            continue

        cleaned_lines.append(line)

    return "".join(cleaned_lines)


@lru_cache(maxsize=1)
def load_notebook_namespace():
    notebook = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    namespace = {"__name__": "__test__"}

    for cell in notebook["cells"]:
        if cell.get("cell_type") != "code":
            continue

        source = _strip_magics_and_interact_calls("".join(cell.get("source", [])))
        if not source.strip():
            continue

        exec(compile(source, str(NOTEBOOK_PATH), "exec"), namespace)

    return namespace


class AbleitungenInteraktivNotebookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ns = load_notebook_namespace()

    def tearDown(self):
        plt.close("all")

    def test_parse_formel_supports_power_e_and_ln_syntax(self):
        expr = self.ns["_parse_formel"]("e^x * ln(x)")
        expected = sp.E ** self.ns["_x"] * sp.log(self.ns["_x"])
        self.assertEqual(sp.simplify(expr - expected), 0)

    def test_parse_formel_supports_pi(self):
        expr = self.ns["_parse_formel"]("sin(pi*x)")
        expected = sp.sin(sp.pi * self.ns["_x"])
        self.assertEqual(sp.simplify(expr - expected), 0)

    def test_parse_formel_raises_for_invalid_input(self):
        with self.assertRaises(Exception):
            self.ns["_parse_formel"]("x***")

    def test_plot_werte_replaces_invalid_values_with_nan(self):
        expr = self.ns["_parse_formel"]("1/x")
        xs = np.array([-1.0, 0.0, 1.0])

        werte = self.ns["_plot_werte"](expr, xs)

        np.testing.assert_allclose(werte[[0, 2]], np.array([-1.0, 1.0]))
        self.assertTrue(np.isnan(werte[1]))

    def test_plot_werte_returns_nan_for_complex_results(self):
        expr = self.ns["_parse_formel"]("sqrt(x)")
        xs = np.array([-1.0, 0.0, 1.0])
        werte = self.ns["_plot_werte"](expr, xs)
        self.assertTrue(np.isnan(werte[0]))
        np.testing.assert_allclose(werte[2], 1.0)

    def test_plot_werte_broadcasts_constant_expressions(self):
        xs = np.linspace(-2.0, 2.0, 5)
        werte = self.ns["_plot_werte"](sp.Integer(5), xs)

        np.testing.assert_allclose(werte, np.full(xs.shape, 5.0))

    def test_ableitung_zeigen_displays_function_and_derivative(self):
        display_mock = Mock()

        with patch.dict(self.ns, {"display": display_mock}), patch.object(plt, "show"):
            self.ns["ableitung_zeigen"]("x^2")

        self.assertEqual(display_mock.call_count, 2)
        rendered = [getattr(call.args[0], "data", "") for call in display_mock.call_args_list]
        self.assertIn("x^{2}", rendered[0])
        self.assertIn("2 x", rendered[1])

    def test_ableitung_zeigen_prints_error_for_invalid_formula(self):
        with patch("builtins.print") as print_mock, patch.object(plt, "show") as show_mock:
            self.ns["ableitung_zeigen"]("x***")

        self.assertTrue(print_mock.called)
        self.assertIn("Fehler:", print_mock.call_args[0][0])
        show_mock.assert_not_called()

    def test_vergleich_marks_extremum_for_quadratic(self):
        with patch.object(plt, "show"):
            self.ns["vergleich"]("x\u00b2 \u2212 2x")

        fig = plt.gcf()
        _, ax_ableitung = fig.axes
        extremum_markers = [
            line for line in ax_ableitung.lines if line.get_marker() == "o"
        ]

        self.assertTrue(extremum_markers)
        marker_xs = np.concatenate([line.get_xdata() for line in extremum_markers])
        self.assertTrue(np.any(np.isclose(marker_xs, 1.0, atol=0.03)))

    def test_vergleich_limits_logarithm_to_positive_domain(self):
        with patch.object(plt, "show"):
            self.ns["vergleich"]("ln(x)")

        fig = plt.gcf()
        ax_funktion, ax_ableitung = fig.axes
        self.assertGreaterEqual(ax_funktion.lines[0].get_xdata().min(), 0.05)
        self.assertGreaterEqual(ax_ableitung.lines[0].get_xdata().min(), 0.05)

    def test_tangente_explorer_smoke_test(self):
        with patch.object(plt, "show"):
            self.ns["tangente_explorer"](2.0)

        ax = plt.gcf().axes[0]
        self.assertIn("9.00", ax.get_title())

    def test_potenzregel_visual_avoids_zero_for_negative_integer_exponents(self):
        with patch.object(plt, "show"):
            self.ns["potenzregel_visual"](-1.0)

        ax = plt.gcf().axes[0]
        xdata = ax.lines[0].get_xdata()
        self.assertTrue(np.all(np.abs(xdata) >= 0.08))

    def test_potenzregel_visual_uses_positive_domain_for_fractional_exponents(self):
        with patch.object(plt, "show"):
            self.ns["potenzregel_visual"](0.5)

        ax = plt.gcf().axes[0]
        xdata = ax.lines[0].get_xdata()
        self.assertGreaterEqual(xdata.min(), 0.01)


if __name__ == "__main__":
    unittest.main()

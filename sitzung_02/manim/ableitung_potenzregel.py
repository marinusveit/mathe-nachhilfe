"""
Manim-Animation: Ableitung mit der Potenzregel (Schritt für Schritt).

Zeigt visuell, wie der Exponent "herunterkommt" und mit dem Koeffizienten
multipliziert wird.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql ableitung_potenzregel.py AbleitungPotenzregel
    manim -pqh ableitung_potenzregel.py AbleitungPotenzregel   # 1080p
"""

import sys
from pathlib import Path

# Projektroot zum Python-Pfad hinzufügen (für utils-Import)
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from manim import *
from utils.ableitung_animation import AbleitungMixin

# 3b1b-Farbpalette
BLUE_3B1B = "#58C4DD"
YELLOW_3B1B = "#FFFF00"
GREEN_3B1B = "#83C167"
RED_3B1B = "#FC6255"
GREY_3B1B = "#888888"
ORANGE_3B1B = "#FF8C00"


class AbleitungPotenzregel(AbleitungMixin, Scene):
    def construct(self):
        # ── Titel ──────────────────────────────────────────────
        title = Text("Potenzregel", font_size=42, color=BLUE_3B1B)
        rule = MathTex(
            r"\left(", "a", r"\cdot", "x", "^{n}", r"\right)'",
            "=",
            "n", r"\cdot", "a", r"\cdot", "x", "^{n-1}",
            font_size=34,
        )
        rule[4].set_color(YELLOW_3B1B)    # n im Exponenten
        rule[7].set_color(YELLOW_3B1B)    # n als Faktor
        rule[12].set_color(GREEN_3B1B)    # n-1

        header = VGroup(title, rule).arrange(DOWN, buff=0.3).to_edge(UP, buff=0.5)
        header_bg = BackgroundRectangle(header, fill_opacity=0.8, buff=0.2)

        self.play(FadeIn(header_bg), Write(title), run_time=0.7)
        self.play(Write(rule), run_time=1)
        self.wait(0.5)

        # ── Beispiel 1:  2x³ → 6x² ───────────────────────────
        bsp1_title = Text("Beispiel 1", font_size=24, color=GREY_3B1B)
        bsp1_title.move_to(UP * 1.2 + LEFT * 4.5)
        self.play(FadeIn(bsp1_title))

        mobs1 = self.animate_potenzregel(coeff=2, exp=3, position=UP * 0.3)
        self.wait(1)

        # Aufräumen
        self.play(FadeOut(mobs1), FadeOut(bsp1_title))

        # ── Beispiel 2:  5x⁴ → 20x³ ──────────────────────────
        bsp2_title = Text("Beispiel 2", font_size=24, color=GREY_3B1B)
        bsp2_title.move_to(UP * 1.2 + LEFT * 4.5)
        self.play(FadeIn(bsp2_title))

        mobs2 = self.animate_potenzregel(coeff=5, exp=4, position=UP * 0.3)
        self.wait(1)

        self.play(FadeOut(mobs2), FadeOut(bsp2_title))

        # ── Beispiel 3:  -3x² → -6x ──────────────────────────
        bsp3_title = Text("Beispiel 3", font_size=24, color=GREY_3B1B)
        bsp3_title.move_to(UP * 1.2 + LEFT * 4.5)
        self.play(FadeIn(bsp3_title))

        mobs3 = self.animate_potenzregel(coeff=-3, exp=2, position=UP * 0.3)
        self.wait(1)

        self.play(FadeOut(mobs3), FadeOut(bsp3_title))

        # ── Zusammenfassung ────────────────────────────────────
        summary = VGroup(
            MathTex(r"2x^3", r"\;\to\;", r"6x^2", font_size=38),
            MathTex(r"5x^4", r"\;\to\;", r"20x^3", font_size=38),
            MathTex(r"-3x^2", r"\;\to\;", r"-6x", font_size=38),
        ).arrange(DOWN, buff=0.4).move_to(DOWN * 0.5)

        for row in summary:
            row[0].set_color(BLUE_3B1B)
            row[2].set_color(GREEN_3B1B)

        check = MathTex(r"\checkmark", font_size=48, color=GREEN_3B1B)
        check.next_to(summary, RIGHT, buff=0.8)

        self.play(
            *[Write(row) for row in summary],
            run_time=1.2,
        )
        self.play(FadeIn(check, scale=1.5))
        self.wait(2)

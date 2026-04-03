"""
Manim-Animation: Ortskurve der Extrempunkte einer Funktionsschar
Zeigt, wie die Extrempunkte von f_t(x) = x³ - 3t²x entlang y = -2x³ wandern.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql ortskurve.py OrtskurveAnimation
    manim -pqh ortskurve.py OrtskurveAnimation   # 1080p
"""

from manim import *
import numpy as np

# 3b1b-Farbpalette
BLUE_3B1B = "#58C4DD"
YELLOW_3B1B = "#FFFF00"
GREEN_3B1B = "#83C167"
RED_3B1B = "#FC6255"
GREY_3B1B = "#888888"
ORANGE_3B1B = "#FF8C00"


class OrtskurveAnimation(Scene):
    def construct(self):
        # --- Achsensystem ---
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-18, 18, 6],
            x_length=8,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "color": GREY_3B1B,
                "stroke_width": 1.5,
                "tick_size": 0.04,
            },
            tips=True,
        ).shift(DOWN * 0.3)

        # Titel
        title = MathTex(
            r"f_t(x) = x^3 - 3t^2 x", font_size=30, color=WHITE,
        ).to_corner(UL, buff=0.4)
        title_bg = BackgroundRectangle(title, fill_opacity=0.7, buff=0.15)

        self.play(Create(axes), FadeIn(title_bg), Write(title))
        self.wait(0.3)

        # --- Phase 1: Schar durchlaufen, Extrempunkte sammeln ---
        t_tracker = ValueTracker(0.5)

        def f_t(x, t):
            return x**3 - 3 * t**2 * x

        # Aktuelle Kurve
        graph = always_redraw(
            lambda: axes.plot(
                lambda x: f_t(x, t_tracker.get_value()),
                x_range=[-3.2, 3.2],
                color=BLUE_3B1B,
                stroke_width=3,
            )
        )

        # t-Label
        t_label = always_redraw(
            lambda: MathTex(
                rf"t = {t_tracker.get_value():.1f}",
                font_size=28,
                color=YELLOW_3B1B,
            ).to_corner(UR, buff=0.4).set_z_index(10)
        )
        t_label_bg = always_redraw(
            lambda: BackgroundRectangle(
                MathTex(
                    rf"t = {t_tracker.get_value():.1f}",
                    font_size=28,
                ).to_corner(UR, buff=0.4),
                fill_opacity=0.7, buff=0.15,
            )
        )

        # Extrempunkte
        hp_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    -t_tracker.get_value(),
                    f_t(-t_tracker.get_value(), t_tracker.get_value()),
                ),
                color=GREEN_3B1B,
                radius=0.1,
                z_index=5,
            )
        )
        tp_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    t_tracker.get_value(),
                    f_t(t_tracker.get_value(), t_tracker.get_value()),
                ),
                color=RED_3B1B,
                radius=0.1,
                z_index=5,
            )
        )

        hp_label_mob = always_redraw(
            lambda: MathTex(r"\text{HP}", font_size=20, color=GREEN_3B1B).next_to(
                Dot(axes.c2p(
                    -t_tracker.get_value(),
                    f_t(-t_tracker.get_value(), t_tracker.get_value()),
                )),
                UP, buff=0.15,
            )
        )
        tp_label_mob = always_redraw(
            lambda: MathTex(r"\text{TP}", font_size=20, color=RED_3B1B).next_to(
                Dot(axes.c2p(
                    t_tracker.get_value(),
                    f_t(t_tracker.get_value(), t_tracker.get_value()),
                )),
                DOWN, buff=0.15,
            )
        )

        self.play(Create(graph), FadeIn(t_label_bg), Write(t_label))
        self.play(FadeIn(hp_dot), FadeIn(tp_dot), Write(hp_label_mob), Write(tp_label_mob))
        self.wait(0.5)

        # Spur der Extrempunkte: traced paths
        hp_trace = TracedPath(
            lambda: axes.c2p(
                -t_tracker.get_value(),
                f_t(-t_tracker.get_value(), t_tracker.get_value()),
            ),
            stroke_color=GREEN_3B1B,
            stroke_width=2.5,
            stroke_opacity=0.7,
        )
        tp_trace = TracedPath(
            lambda: axes.c2p(
                t_tracker.get_value(),
                f_t(t_tracker.get_value(), t_tracker.get_value()),
            ),
            stroke_color=RED_3B1B,
            stroke_width=2.5,
            stroke_opacity=0.7,
        )

        self.add(hp_trace, tp_trace)

        # Einige Geisterkurven bei festen t-Werten als Orientierung
        ghost_ts = [0.5, 1.0, 1.5, 2.0, 2.5]
        ghosts = VGroup(*[
            axes.plot(
                lambda x, t=t: f_t(x, t),
                x_range=[-3.2, 3.2],
                color=BLUE_3B1B,
                stroke_width=0.8,
                stroke_opacity=0.2,
            )
            for t in ghost_ts
        ])
        self.play(FadeIn(ghosts), run_time=0.5)

        # t von 0.5 nach 2.5 animieren
        self.play(t_tracker.animate.set_value(2.5), run_time=5, rate_func=linear)
        self.wait(0.5)

        # --- Phase 2: Ortskurve einblenden ---
        ortskurve = axes.plot(
            lambda x: -2 * x**3,
            x_range=[-2.6, 2.6],
            color=YELLOW_3B1B,
            stroke_width=3,
        )
        ortskurve_label = MathTex(
            r"y = -2x^3", font_size=26, color=YELLOW_3B1B,
        ).next_to(axes.c2p(2.0, -16), RIGHT, buff=0.2)
        ortskurve_label_bg = BackgroundRectangle(ortskurve_label, fill_opacity=0.7, buff=0.1)

        self.play(
            Create(ortskurve, run_time=2),
            FadeIn(ortskurve_label_bg),
            Write(ortskurve_label),
        )
        self.wait(0.5)

        # Erklärung
        explanation = VGroup(
            MathTex(r"\text{Hochpunkte: } H(-t \mid 2t^3)", font_size=22, color=GREEN_3B1B),
            MathTex(r"\text{Tiefpunkte: } T(t \mid -2t^3)", font_size=22, color=RED_3B1B),
            MathTex(r"\text{Ortskurve: } y = -2x^3", font_size=22, color=YELLOW_3B1B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).to_corner(DL, buff=0.5)
        expl_bg = BackgroundRectangle(explanation, fill_opacity=0.7, buff=0.15)

        self.play(FadeIn(expl_bg), Write(explanation), run_time=2)
        self.wait(2)

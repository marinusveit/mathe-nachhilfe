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
            y_range=[-24, 24, 6],
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

        t_tracker = ValueTracker(0.5)

        def f_t(x, t):
            return x**3 - 3 * t**2 * x

        # ======================================================
        # Top-left: f_t Formeln (blau, wie der Graph)
        # ======================================================
        title = MathTex(
            r"f_t(x) = x^3 - 3t^2 x", font_size=30, color=BLUE_3B1B,
        ).to_corner(UL, buff=0.4)
        title_bg = BackgroundRectangle(title, fill_opacity=0.7, buff=0.15)

        def make_ft_sub():
            t = t_tracker.get_value()
            coeff = 3 * t**2
            tex = MathTex(
                rf"f_{{t={t:.1f}}}(x) = x^3 - 3 \cdot {t:.1f}^2 \cdot x"
                rf" = x^3 - {coeff:.2f}x",
                font_size=18, color=BLUE_3B1B,
            )
            tex.next_to(title, DOWN, aligned_edge=LEFT, buff=0.08)
            bg = BackgroundRectangle(tex, fill_opacity=0.7, buff=0.1)
            return VGroup(bg, tex)

        ft_sub = always_redraw(make_ft_sub)

        # ======================================================
        # Bottom-left: HP / TP Info-Block (von Anfang an sichtbar)
        # ======================================================
        def make_info_block():
            t = t_tracker.get_value()
            hp_x = -t
            hp_y = 2 * t**3
            tp_x = t
            tp_y = -2 * t**3

            hp1 = MathTex(
                r"\text{Hochpunkte: } H(-t \mid 2t^3)",
                font_size=22, color=GREEN_3B1B,
            )
            hp2 = MathTex(
                rf"H({hp_x:.1f} \mid {hp_y:.1f})",
                font_size=18, color=GREEN_3B1B,
            )
            tp1 = MathTex(
                r"\text{Tiefpunkte: } T(t \mid -2t^3)",
                font_size=22, color=RED_3B1B,
            )
            tp2 = MathTex(
                rf"T({tp_x:.1f} \mid {tp_y:.1f})",
                font_size=18, color=RED_3B1B,
            )

            block = VGroup(hp1, hp2, tp1, tp2).arrange(
                DOWN, aligned_edge=LEFT, buff=0.08,
            )
            block.to_corner(DL, buff=0.5)
            bg = BackgroundRectangle(block, fill_opacity=0.7, buff=0.15)
            return VGroup(bg, block)

        info_block = always_redraw(make_info_block)

        # ======================================================
        # t-Wert: unter der eingesetzten Gleichung (links, gut lesbar)
        # ======================================================
        def make_t_label():
            t = t_tracker.get_value()
            tex = MathTex(
                rf"t = {t:.1f}",
                font_size=24, color=YELLOW_3B1B,
            )
            # Links neben der x-Achse
            tex.next_to(axes.c2p(-3.5, 0), LEFT, buff=0.15)
            bg = BackgroundRectangle(tex, fill_opacity=0.7, buff=0.1)
            return VGroup(bg, tex).set_z_index(10)

        t_label = always_redraw(make_t_label)
        t_label_bg = VGroup()

        # ======================================================
        # Graph + Tag der dem Graphen folgt
        # ======================================================
        graph = always_redraw(
            lambda: axes.plot(
                lambda x: f_t(x, t_tracker.get_value()),
                x_range=[-3.2, 3.2],
                color=BLUE_3B1B,
                stroke_width=3,
            )
        )

        def make_graph_tag():
            t = t_tracker.get_value()
            for x_try in [2.2, 1.8, 1.5, 1.2, 0.8, 0.5]:
                y = f_t(x_try, t)
                if -14 < y < 14:
                    break
            else:
                x_try, y = 0.5, f_t(0.5, t)
            tex = MathTex(rf"f_{{{t:.1f}}}", font_size=20, color=BLUE_3B1B)
            tex.next_to(axes.c2p(x_try, y), UR, buff=0.08)
            bg = BackgroundRectangle(tex, fill_opacity=0.7, buff=0.06)
            return VGroup(bg, tex).set_z_index(8)

        graph_tag = always_redraw(make_graph_tag)

        # ======================================================
        # Extrempunkt-Dots + kleine Labels
        # ======================================================
        hp_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    -t_tracker.get_value(),
                    f_t(-t_tracker.get_value(), t_tracker.get_value()),
                ),
                color=GREEN_3B1B, radius=0.1, z_index=5,
            )
        )
        tp_dot = always_redraw(
            lambda: Dot(
                axes.c2p(
                    t_tracker.get_value(),
                    f_t(t_tracker.get_value(), t_tracker.get_value()),
                ),
                color=RED_3B1B, radius=0.1, z_index=5,
            )
        )

        hp_tag = always_redraw(
            lambda: MathTex(r"\text{HP}", font_size=18, color=GREEN_3B1B).next_to(
                axes.c2p(
                    -t_tracker.get_value(),
                    f_t(-t_tracker.get_value(), t_tracker.get_value()),
                ), UP, buff=0.12,
            ).set_z_index(6)
        )
        tp_tag = always_redraw(
            lambda: MathTex(r"\text{TP}", font_size=18, color=RED_3B1B).next_to(
                axes.c2p(
                    t_tracker.get_value(),
                    f_t(t_tracker.get_value(), t_tracker.get_value()),
                ), DOWN, buff=0.12,
            ).set_z_index(6)
        )

        # ======================================================
        # Spuren der Extrempunkte
        # ======================================================
        hp_trace = TracedPath(
            lambda: axes.c2p(
                -t_tracker.get_value(),
                f_t(-t_tracker.get_value(), t_tracker.get_value()),
            ),
            stroke_color=GREEN_3B1B, stroke_width=2.5, stroke_opacity=0.7,
        )
        tp_trace = TracedPath(
            lambda: axes.c2p(
                t_tracker.get_value(),
                f_t(t_tracker.get_value(), t_tracker.get_value()),
            ),
            stroke_color=RED_3B1B, stroke_width=2.5, stroke_opacity=0.7,
        )

        # ======================================================
        # Aufbau der Szene
        # ======================================================
        self.play(Create(axes), FadeIn(title_bg), Write(title))
        self.add(ft_sub)
        self.wait(0.3)

        self.play(Create(graph), FadeIn(t_label))
        self.add(graph_tag)

        # HP/TP sofort einblenden
        self.play(
            FadeIn(hp_dot), FadeIn(tp_dot),
            FadeIn(hp_tag), FadeIn(tp_tag),
            FadeIn(info_block),
        )
        self.add(hp_trace, tp_trace)
        self.wait(0.5)

        # Geisterkurven
        ghost_ts = [0.5, 1.0, 1.5, 2.0]
        ghosts = VGroup(*[
            axes.plot(
                lambda x, t=t: f_t(x, t),
                x_range=[-3.2, 3.2],
                color=BLUE_3B1B, stroke_width=0.8, stroke_opacity=0.2,
            )
            for t in ghost_ts
        ])
        self.play(FadeIn(ghosts), run_time=0.5)

        # t von 0.5 nach 2.0 animieren (HP bleibt im Viewport: 2·2³ = 16)
        self.play(
            t_tracker.animate.set_value(2.0), run_time=5, rate_func=linear,
        )
        self.wait(0.5)

        # ======================================================
        # Phase 2: Ortskurve einblenden
        # ======================================================
        ortskurve = axes.plot(
            lambda x: -2 * x**3,
            x_range=[-2.6, 2.6],
            color=YELLOW_3B1B, stroke_width=3,
        )
        ortskurve_label = MathTex(
            r"y = -2x^3", font_size=26, color=YELLOW_3B1B,
        ).next_to(axes.c2p(2.0, -16), RIGHT, buff=0.2)
        ortskurve_label_bg = BackgroundRectangle(
            ortskurve_label, fill_opacity=0.7, buff=0.1,
        )

        # Ortskurven-Zeile unter dem Info-Block
        ortskurve_info = MathTex(
            r"\text{Ortskurve: } y = -2x^3",
            font_size=22, color=YELLOW_3B1B,
        )
        # Positioniere relativ zum info_block (der ist always_redraw, daher manuell)
        current_info = make_info_block()
        ortskurve_info.next_to(current_info[1], DOWN, aligned_edge=LEFT, buff=0.12)
        ortskurve_info_bg = BackgroundRectangle(
            ortskurve_info, fill_opacity=0.7, buff=0.12,
        )

        self.play(
            Create(ortskurve, run_time=2),
            FadeIn(ortskurve_label_bg), Write(ortskurve_label),
            FadeIn(ortskurve_info_bg), Write(ortskurve_info),
        )
        self.wait(2)

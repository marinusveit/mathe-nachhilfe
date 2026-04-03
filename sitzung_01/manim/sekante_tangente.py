"""
Manim-Animation: Sekante wird zur Tangente
Zeigt visuell, wie der Differenzenquotient zum Differentialquotienten wird.
Inkl. Steigungsdreieck (Δy / Δx) und 3b1b-Style.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql sekante_tangente.py SekanteTangente
    manim -pqh sekante_tangente.py SekanteTangente   # 1080p
"""

from manim import *

# 3b1b-Farbpalette
BLUE_3B1B = "#58C4DD"
YELLOW_3B1B = "#FFFF00"
GREEN_3B1B = "#83C167"
RED_3B1B = "#FC6255"
PINK_3B1B = "#FF69B4"
GREY_3B1B = "#888888"


class SekanteTangente(Scene):
    def construct(self):
        # --- Koordinatensystem (3b1b-Style) ---
        # Achsen weiter nach oben, damit unten Platz für Text bleibt
        axes = Axes(
            x_range=[-0.5, 5.5, 1],
            y_range=[-0.5, 11, 2],
            x_length=9,
            y_length=5.5,
            axis_config={
                "include_numbers": True,
                "font_size": 22,
                "color": GREY_3B1B,
                "stroke_width": 2,
                "include_ticks": True,
                "tick_size": 0.05,
            },
            tips=True,
        ).shift(UP * 0.5 + LEFT * 0.5)

        # Dezente Achsen-Labels in LaTeX
        x_label = MathTex("x", font_size=28, color=WHITE).next_to(axes.x_axis, RIGHT, buff=0.15)
        y_label = MathTex("y", font_size=28, color=WHITE).next_to(axes.y_axis, UP, buff=0.15)

        # --- Funktion f(x) = 0.5x² ---
        def func(x):
            return 0.5 * x ** 2

        def func_prime(x):
            return x  # f'(x) = x

        graph = axes.plot(func, x_range=[0, 4.6], color=BLUE_3B1B, stroke_width=3)
        graph_label = MathTex(
            r"f(x) = \tfrac{1}{2}x^2", font_size=30, color=BLUE_3B1B
        ).move_to(axes.c2p(1.0, 8.5))

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1.5)
        self.play(Create(graph), Write(graph_label), run_time=1.5)
        self.wait(0.5)

        # --- Fester Punkt bei x0 ---
        x0 = 1.5
        y0 = func(x0)
        dot_P = Dot(axes.c2p(x0, y0), color=YELLOW_3B1B, radius=0.07, z_index=5)
        label_P = MathTex(r"f(x_0)", font_size=22, color=YELLOW_3B1B).next_to(dot_P, LEFT, buff=0.15)

        self.play(FadeIn(dot_P, scale=1.5), Write(label_P))

        # --- Beweglicher Punkt bei x1 ---
        x1_tracker = ValueTracker(4.0)

        dot_Q = always_redraw(
            lambda: Dot(
                axes.c2p(x1_tracker.get_value(), func(x1_tracker.get_value())),
                color=GREEN_3B1B, radius=0.07, z_index=5,
            )
        )
        label_Q = always_redraw(
            lambda: MathTex(r"f(x_1)", font_size=22, color=GREEN_3B1B).next_to(
                axes.c2p(x1_tracker.get_value(), func(x1_tracker.get_value())),
                UP, buff=0.15,
            )
        )

        self.play(FadeIn(dot_Q, scale=1.5), Write(label_Q))

        # --- Sekante durch P und Q ---
        def get_secant_line():
            x1 = x1_tracker.get_value()
            y1 = func(x1)
            if abs(x1 - x0) < 0.01:
                slope = func_prime(x0)
            else:
                slope = (y1 - y0) / (x1 - x0)
            # Linie weit genug verlängern, KEIN y-Clipping (das verfälscht die Richtung)
            x_left = -0.5
            x_right = 5.5
            return Line(
                axes.c2p(x_left, y0 + slope * (x_left - x0)),
                axes.c2p(x_right, y0 + slope * (x_right - x0)),
                color=RED_3B1B, stroke_width=2.5,
            )

        secant = always_redraw(get_secant_line)

        # --- Steigungsdreieck (Δx und Δy) + Lotlinien zur x-Achse ---
        def get_slope_triangle():
            x1 = x1_tracker.get_value()
            y1 = func(x1)
            if abs(x1 - x0) < 0.05:
                return VGroup()  # Zu klein, nicht zeigen

            # Horizontale Linie: P → (x1, y0) (Δx-Strecke)
            h_line = DashedLine(
                axes.c2p(x0, y0), axes.c2p(x1, y0),
                color=PINK_3B1B, stroke_width=2, dash_length=0.08,
            )
            # Vertikale Linie: (x1, y0) → Q (Δy-Strecke)
            v_line = DashedLine(
                axes.c2p(x1, y0), axes.c2p(x1, y1),
                color=YELLOW_3B1B, stroke_width=2, dash_length=0.08,
            )

            # Lotlinien von Punkten zur x-Achse
            lot_x0 = DashedLine(
                axes.c2p(x0, 0), axes.c2p(x0, y0),
                color=GREY_3B1B, stroke_width=1.5, dash_length=0.06,
            )
            lot_x1 = DashedLine(
                axes.c2p(x1, 0), axes.c2p(x1, y1),
                color=GREY_3B1B, stroke_width=1.5, dash_length=0.06,
            )

            # x₀ und x₁ Labels auf der x-Achse
            x0_label = MathTex(
                r"x_0", font_size=20, color=YELLOW_3B1B,
            ).next_to(axes.c2p(x0, 0), DOWN, buff=0.15)
            x1_label = MathTex(
                r"x_1", font_size=20, color=GREEN_3B1B,
            ).next_to(axes.c2p(x1, 0), DOWN, buff=0.15)

            # Δx und Δy Labels
            dx_label = MathTex(
                r"x_1 - x_0", font_size=22, color=PINK_3B1B,
            ).next_to(h_line, DOWN, buff=0.12)

            dy_label = MathTex(
                r"f(x_1) - f(x_0)", font_size=22, color=YELLOW_3B1B,
            ).next_to(v_line, RIGHT, buff=0.12)

            return VGroup(
                h_line, v_line, lot_x0, lot_x1,
                x0_label, x1_label, dx_label, dy_label,
            )

        triangle = always_redraw(get_slope_triangle)

        # --- Steigungsformel ---
        def get_slope_display():
            x1 = x1_tracker.get_value()
            y1 = func(x1)
            if abs(x1 - x0) < 0.01:
                slope = func_prime(x0)
            else:
                slope = (y1 - y0) / (x1 - x0)
            return MathTex(
                r"m_{\text{Sek}} = \frac{f(x_1) - f(x_0)}{x_1 - x_0} = "
                + f"{slope:.2f}",
                font_size=28, color=WHITE,
            ).to_corner(UR, buff=0.4).shift(DOWN * 0.3)

        slope_text = always_redraw(get_slope_display)

        sekante_label = MathTex(
            r"\text{Sekante}", font_size=26, color=RED_3B1B,
        ).to_corner(UL, buff=0.5)

        self.play(Create(secant), Create(triangle), Write(slope_text), Write(sekante_label))
        self.wait(1.5)

        # --- Frage (weit unter der x-Achse, eigener Bereich) ---
        title = MathTex(
            r"\text{Was passiert, wenn } Q \text{ immer näher an } P \text{ rückt?}",
            font_size=28,
        ).to_edge(DOWN, buff=0.3)
        title_bg = BackgroundRectangle(title, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(title_bg), Write(title))
        self.wait(1)

        # --- Q nähert sich P ---
        self.play(
            x1_tracker.animate.set_value(2.8),
            run_time=2.5, rate_func=smooth,
        )
        self.wait(0.5)

        self.play(
            x1_tracker.animate.set_value(2.0),
            run_time=2, rate_func=smooth,
        )
        self.wait(0.5)

        # --- Letzter Schritt: Q → P ---
        self.play(FadeOut(title_bg), FadeOut(title))

        tangente_title = MathTex(
            r"\text{Die Sekante wird zur Tangente!}",
            font_size=30, color=YELLOW_3B1B,
        ).to_edge(DOWN, buff=0.3)
        tangente_bg = BackgroundRectangle(tangente_title, fill_opacity=0.85, buff=0.15)
        self.play(FadeIn(tangente_bg), Write(tangente_title))

        self.play(
            x1_tracker.animate.set_value(x0 + 0.01),
            run_time=3, rate_func=smooth,
        )
        self.wait(0.5)

        # --- Umwandlung: Sekante → Tangente ---
        self.play(
            FadeOut(label_Q), FadeOut(dot_Q),
            FadeOut(slope_text), FadeOut(sekante_label),
            FadeOut(triangle),
        )

        tangente_label = MathTex(
            r"\text{Tangente}", font_size=26, color=YELLOW_3B1B,
        ).to_corner(UL, buff=0.5)

        ableitung_text = MathTex(
            r"f'(x_0) = \lim_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0}",
            font_size=30, color=YELLOW_3B1B,
        ).to_corner(UR, buff=0.4).shift(DOWN * 0.3)
        ableitung_bg = BackgroundRectangle(ableitung_text, fill_opacity=0.7, buff=0.15)

        steigung_konkret = MathTex(
            r"f'(1{,}5) = 1{,}5",
            font_size=26, color=WHITE,
        ).next_to(ableitung_text, DOWN, buff=0.2)
        steigung_bg = BackgroundRectangle(steigung_konkret, fill_opacity=0.7, buff=0.1)

        self.play(
            secant.animate.set_color(YELLOW_3B1B),
            Write(tangente_label),
        )
        self.play(FadeIn(ableitung_bg), Write(ableitung_text))
        self.play(FadeIn(steigung_bg), Write(steigung_konkret))
        self.wait(2)

        # --- Zusammenfassung ---
        self.play(FadeOut(tangente_bg), FadeOut(tangente_title))

        summary = MathTex(
            r"\text{Die Ableitung } f'(x_0) \text{ ist die Steigung der Tangente an } x_0.",
            font_size=28,
        ).to_edge(DOWN, buff=0.3)
        summary_bg = BackgroundRectangle(summary, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(summary_bg), Write(summary))
        self.wait(3)

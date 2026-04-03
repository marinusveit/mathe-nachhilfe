"""
Manim-Animation: Sekante wird zur Tangente
Zeigt visuell, wie der Differenzenquotient zum Differentialquotienten wird.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql sekante_tangente.py SekanteTangente
"""

from manim import *


class SekanteTangente(Scene):
    def construct(self):
        # --- Koordinatensystem ---
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 10, 2],
            x_length=8,
            y_length=5.5,
            axis_config={"include_numbers": True, "font_size": 24},
        ).shift(DOWN * 0.3)

        axis_labels = axes.get_axis_labels(x_label="x", y_label="y")

        # --- Funktion f(x) = 0.4x² ---
        def func(x):
            return 0.4 * x ** 2

        graph = axes.plot(func, x_range=[-0.5, 4.8], color=BLUE)
        graph_label = axes.get_graph_label(
            graph, label="f(x) = 0.4x^2", x_val=4, direction=UP + LEFT
        ).scale(0.7)

        self.play(Create(axes), Write(axis_labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(0.5)

        # --- Fester Punkt P ---
        x0 = 1.5
        y0 = func(x0)
        dot_P = Dot(axes.c2p(x0, y0), color=YELLOW, radius=0.08)
        label_P = MathTex("P", font_size=30, color=YELLOW).next_to(dot_P, DOWN + LEFT, buff=0.15)

        self.play(FadeIn(dot_P), Write(label_P))

        # --- Beweglicher Punkt Q ---
        x1_start = 4.0
        x1_tracker = ValueTracker(x1_start)

        dot_Q = always_redraw(
            lambda: Dot(
                axes.c2p(x1_tracker.get_value(), func(x1_tracker.get_value())),
                color=GREEN,
                radius=0.08,
            )
        )
        label_Q = always_redraw(
            lambda: MathTex("Q", font_size=30, color=GREEN).next_to(
                axes.c2p(x1_tracker.get_value(), func(x1_tracker.get_value())),
                UP + RIGHT,
                buff=0.15,
            )
        )

        self.play(FadeIn(dot_Q), Write(label_Q))

        # --- Sekante durch P und Q ---
        def get_secant_line():
            x1 = x1_tracker.get_value()
            y1 = func(x1)
            if abs(x1 - x0) < 0.01:
                # Tangente: benutze Ableitung
                slope = 0.8 * x0
            else:
                slope = (y1 - y0) / (x1 - x0)
            # Linie durch P mit Steigung
            x_left = -0.5
            x_right = 5.0
            p1 = axes.c2p(x_left, y0 + slope * (x_left - x0))
            p2 = axes.c2p(x_right, y0 + slope * (x_right - x0))
            return Line(p1, p2, color=RED, stroke_width=2.5)

        secant = always_redraw(get_secant_line)

        # --- Steigungsanzeige ---
        slope_text = always_redraw(
            lambda: MathTex(
                r"m_{\text{Sek}} = \frac{f(x_1) - f(x_0)}{x_1 - x_0} = "
                + f"{((func(x1_tracker.get_value()) - y0) / max(abs(x1_tracker.get_value() - x0), 0.01)):.2f}",
                font_size=28,
            ).to_corner(UR, buff=0.5)
        )

        sekante_label = Text("Sekante", font_size=22, color=RED).to_corner(UL, buff=0.5)

        self.play(Create(secant), Write(slope_text), Write(sekante_label))
        self.wait(1)

        # --- Titel: Differenzenquotient ---
        title = Text("Was passiert, wenn Q immer näher an P rückt?", font_size=26).to_edge(DOWN, buff=0.4)
        self.play(Write(title))
        self.wait(1)

        # --- Q nähert sich P (langsam) ---
        self.play(
            x1_tracker.animate.set_value(2.5),
            run_time=2,
            rate_func=smooth,
        )
        self.wait(0.5)

        self.play(
            x1_tracker.animate.set_value(1.8),
            run_time=2,
            rate_func=smooth,
        )
        self.wait(0.5)

        # --- Letzter Schritt: Q → P ---
        self.play(FadeOut(title))

        tangente_title = Text("Die Sekante wird zur Tangente!", font_size=28, color=YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(tangente_title))

        self.play(
            x1_tracker.animate.set_value(x0 + 0.01),
            run_time=3,
            rate_func=smooth,
        )

        # --- Umwandlung: Sekante → Tangente ---
        self.play(
            FadeOut(label_Q),
            FadeOut(dot_Q),
            FadeOut(slope_text),
            FadeOut(sekante_label),
        )

        tangente_label = Text("Tangente", font_size=22, color=YELLOW).to_corner(UL, buff=0.5)
        ableitung_text = MathTex(
            r"f'(x_0) = \lim_{x_1 \to x_0} \frac{f(x_1) - f(x_0)}{x_1 - x_0}",
            font_size=32,
            color=YELLOW,
        ).to_corner(UR, buff=0.5)

        steigung_konkret = MathTex(
            r"f'(1{,}5) = 0{,}8 \cdot 1{,}5 = 1{,}2",
            font_size=28,
        ).next_to(ableitung_text, DOWN, buff=0.3)

        self.play(
            secant.animate.set_color(YELLOW),
            Write(tangente_label),
        )
        self.play(Write(ableitung_text))
        self.play(Write(steigung_konkret))
        self.wait(2)

        # --- Zusammenfassung ---
        self.play(
            FadeOut(tangente_title),
        )

        summary = VGroup(
            Text("Die Ableitung f'(x₀) ist die Steigung", font_size=26),
            Text("der Tangente an der Stelle x₀.", font_size=26),
        ).arrange(DOWN, buff=0.15).to_edge(DOWN, buff=0.4)

        self.play(Write(summary))
        self.wait(3)

# manim -pql sitzung_05/manim/hauptsatz.py HauptsatzAnimation   # Preview
# manim -pqh sitzung_05/manim/hauptsatz.py HauptsatzAnimation   # HQ

from manim import *


class HauptsatzAnimation(Scene):
    """Visualisiert den Hauptsatz der Differential- und Integralrechnung.

    Linkes KS: f(x) = x², Fläche füllt sich von a=0 bis b=2.
    Rechtes KS: F(x) = x³/3, Punkt wandert synchron mit der Fläche.
    Am Ende: Formel ∫₀² x² dx = F(2) − F(0) = 8/3.
    """

    def construct(self):
        # ── Titel ──────────────────────────────────────────────────
        titel = Text("Hauptsatz der Differential- und Integralrechnung", font_size=36)
        self.play(Write(titel))
        self.wait()
        self.play(FadeOut(titel))

        # ── Koordinatensysteme nebeneinander ───────────────────────
        ax_links = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 5, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 24},
            tips=True,
        )
        labels_links = ax_links.get_axis_labels(
            x_label=MathTex("x"),
            y_label=MathTex("f(x)"),
        )
        titel_links = MathTex("f(x) = x^2", font_size=32, color=YELLOW)

        ax_rechts = Axes(
            x_range=[0, 2.5, 0.5],
            y_range=[0, 3.5, 1],
            x_length=5,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 24},
            tips=True,
        )
        labels_rechts = ax_rechts.get_axis_labels(
            x_label=MathTex("x"),
            y_label=MathTex("F(x)"),
        )
        titel_rechts = MathTex(r"F(x) = \tfrac{x^3}{3}", font_size=32, color=GREEN)

        # Gruppen bilden und positionieren
        gruppe_links = VGroup(ax_links, labels_links).shift(LEFT * 3.5)
        gruppe_rechts = VGroup(ax_rechts, labels_rechts).shift(RIGHT * 3.5)

        titel_links.next_to(ax_links, UP, buff=0.2)
        titel_rechts.next_to(ax_rechts, UP, buff=0.2)

        self.play(
            Create(ax_links), Write(labels_links), FadeIn(titel_links),
            Create(ax_rechts), Write(labels_rechts), FadeIn(titel_rechts),
            run_time=2,
        )

        # ── Graphen zeichnen ───────────────────────────────────────
        graph_f = ax_links.plot(lambda x: x ** 2, x_range=[0, 2.3], color=YELLOW)
        graph_F = ax_rechts.plot(lambda x: x ** 3 / 3, x_range=[0, 2.3], color=GREEN)

        self.play(Create(graph_f), Create(graph_F), run_time=2)
        self.wait(0.5)

        # ── ValueTracker für die obere Grenze b ───────────────────
        b_tracker = ValueTracker(0.01)  # Start knapp über 0

        # ── Fläche unter f(x) (links) ─────────────────────────────
        area = always_redraw(
            lambda: ax_links.get_area(
                graph_f,
                x_range=[0, b_tracker.get_value()],
                color=BLUE,
                opacity=0.5,
            )
        )

        # ── Vertikale Linie bei x = b (links) ─────────────────────
        v_line = always_redraw(
            lambda: ax_links.get_vertical_line(
                ax_links.c2p(b_tracker.get_value(), b_tracker.get_value() ** 2),
                color=WHITE,
                line_func=DashedLine,
            )
        )

        # ── Punkt auf F(x) (rechts) ───────────────────────────────
        dot_F = always_redraw(
            lambda: Dot(
                ax_rechts.c2p(
                    b_tracker.get_value(),
                    b_tracker.get_value() ** 3 / 3,
                ),
                color=RED,
                radius=0.08,
            )
        )

        # ── Label für den aktuellen Flächenwert ───────────────────
        area_label = always_redraw(
            lambda: MathTex(
                rf"A = {b_tracker.get_value() ** 3 / 3:.2f}",
                font_size=28,
                color=BLUE,
            ).add_background_rectangle(color=BLACK, opacity=0.7, buff=0.1)
            .next_to(ax_links, DOWN, buff=0.3)
        )

        # ── Label für F(b) ────────────────────────────────────────
        F_label = always_redraw(
            lambda: MathTex(
                rf"F(b) = {b_tracker.get_value() ** 3 / 3:.2f}",
                font_size=28,
                color=GREEN,
            ).add_background_rectangle(color=BLACK, opacity=0.7, buff=0.1)
            .next_to(ax_rechts, DOWN, buff=0.3)
        )

        # Alles einblenden
        self.play(
            FadeIn(area), FadeIn(v_line), FadeIn(dot_F),
            FadeIn(area_label), FadeIn(F_label),
        )

        # ── Synchrone Animation: b wandert von 0 nach 2 ──────────
        self.play(
            b_tracker.animate.set_value(2),
            run_time=6,
            rate_func=linear,
        )
        self.wait()

        # ── Endergebnis: Formel einblenden ─────────────────────────
        formel = MathTex(
            r"\int_0^2 x^2 \, dx",
            r"= F(2) - F(0)",
            r"= \frac{8}{3} - 0",
            r"= \frac{8}{3}",
            font_size=40,
        )
        formel[0].set_color(BLUE)
        formel[1].set_color(GREEN)
        formel[3].set_color(YELLOW)

        formel.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.2)
        formel.to_edge(DOWN, buff=0.5)

        # Alte Labels ausblenden, Formel einblenden
        self.play(
            FadeOut(area_label), FadeOut(F_label),
            FadeIn(formel, shift=UP),
            run_time=2,
        )
        self.wait(3)

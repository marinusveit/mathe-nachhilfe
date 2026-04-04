"""
Manim-Animation: Fläche zwischen zwei Kurven
Zeigt Riemann-Summen → exaktes Integral und das Vorzeichenwechsel-Problem.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql flaeche_zwischen_kurven.py FlaecheZwischenKurven
    manim -pql flaeche_zwischen_kurven.py VorzeichenwechselFlaeche
    manim -pqh flaeche_zwischen_kurven.py FlaecheZwischenKurven   # 1080p
"""

from manim import *

# 3b1b-Farbpalette
BLUE_3B1B = "#58C4DD"
YELLOW_3B1B = "#FFFF00"
GREEN_3B1B = "#83C167"
RED_3B1B = "#FC6255"
PINK_3B1B = "#FF69B4"
GREY_3B1B = "#888888"
ORANGE_3B1B = "#FF8C00"


class FlaecheZwischenKurven(Scene):
    def construct(self):
        # --- Phase 1: Koordinatensystem + Funktionen (2s) ---
        axes = Axes(
            x_range=[-0.3, 1.5, 0.5],
            y_range=[-0.3, 1.5, 0.5],
            x_length=8,
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
        ).shift(UP * 0.3)

        x_label = MathTex("x", font_size=28, color=WHITE).next_to(axes.x_axis, RIGHT, buff=0.15)
        y_label = MathTex("y", font_size=28, color=WHITE).next_to(axes.y_axis, UP, buff=0.15)

        def f(x):
            return x

        def g(x):
            return x ** 2

        graph_f = axes.plot(f, x_range=[0, 1.4], color=BLUE_3B1B, stroke_width=3)
        graph_g = axes.plot(g, x_range=[0, 1.25], color=RED_3B1B, stroke_width=3)

        label_f = MathTex(
            r"f(x) = x", font_size=28, color=BLUE_3B1B
        ).move_to(axes.c2p(1.25, 1.35))
        label_g = MathTex(
            r"g(x) = x^2", font_size=28, color=RED_3B1B
        ).move_to(axes.c2p(1.3, 0.85))

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1)
        self.play(
            Create(graph_f), Write(label_f),
            Create(graph_g), Write(label_g),
            run_time=1,
        )

        # --- Phase 2: Schnittpunkte markieren (1.5s) ---
        dot_0 = Dot(axes.c2p(0, 0), color=YELLOW_3B1B, radius=0.07, z_index=5)
        dot_1 = Dot(axes.c2p(1, 1), color=YELLOW_3B1B, radius=0.07, z_index=5)

        label_x0 = MathTex(r"x = 0", font_size=22, color=YELLOW_3B1B).next_to(dot_0, DL, buff=0.15)
        label_x1 = MathTex(r"x = 1", font_size=22, color=YELLOW_3B1B).next_to(dot_1, UR, buff=0.15)

        self.play(
            FadeIn(dot_0, scale=1.5), Write(label_x0),
            FadeIn(dot_1, scale=1.5), Write(label_x1),
            run_time=1.5,
        )

        # --- Phase 3: Riemann-Summe mit n=5 Streifen (3s) ---
        def create_riemann_rects(n):
            """Erzeugt Rechteck-Streifen zwischen f und g im Intervall [0,1]."""
            rects = VGroup()
            dx = 1.0 / n
            for i in range(n):
                x_i = i * dx
                x_mid = x_i + dx / 2  # Mittelpunkt für Höhe
                y_top = f(x_mid)
                y_bot = g(x_mid)
                if y_top <= y_bot:
                    continue
                # Rechteck von g(x_mid) bis f(x_mid)
                bottom_left = axes.c2p(x_i, y_bot)
                top_right = axes.c2p(x_i + dx, y_top)
                rect = Rectangle(
                    width=top_right[0] - bottom_left[0],
                    height=top_right[1] - bottom_left[1],
                    fill_color=GREEN_3B1B,
                    fill_opacity=0.5,
                    stroke_color=GREEN_3B1B,
                    stroke_width=1,
                )
                rect.move_to((np.array(bottom_left) + np.array(top_right)) / 2)
                rects.add(rect)
            return rects

        rects_5 = create_riemann_rects(5)
        n_label = MathTex(
            r"n = 5 \text{ Streifen}", font_size=26, color=WHITE
        ).to_corner(UR, buff=0.5)
        n_label_bg = BackgroundRectangle(n_label, fill_opacity=0.8, buff=0.12)

        self.play(
            FadeIn(rects_5, lag_ratio=0.15),
            FadeIn(n_label_bg), Write(n_label),
            run_time=2,
        )
        self.wait(1)

        # --- Phase 4: Anzahl erhöhen n=10, 30, 100 (4s) ---
        for n_val in [10, 30, 100]:
            new_rects = create_riemann_rects(n_val)
            new_n_label = MathTex(
                rf"n = {n_val} \text{{ Streifen}}", font_size=26, color=WHITE
            ).to_corner(UR, buff=0.5)
            new_n_label_bg = BackgroundRectangle(new_n_label, fill_opacity=0.8, buff=0.12)

            self.play(
                FadeOut(rects_5),
                FadeOut(n_label_bg), FadeOut(n_label),
                FadeIn(new_rects),
                FadeIn(new_n_label_bg), Write(new_n_label),
                run_time=1.2,
            )
            self.wait(0.2)

            rects_5 = new_rects
            n_label = new_n_label
            n_label_bg = new_n_label_bg

        self.wait(0.5)

        # --- Phase 5: Exakte Fläche (2s) ---
        area = axes.get_area(
            graph_f,
            x_range=[0, 1],
            bounded_graph=graph_g,
            color=GREEN_3B1B,
            opacity=0.5,
        )

        self.play(
            FadeOut(rects_5),
            FadeOut(n_label_bg), FadeOut(n_label),
            FadeIn(area),
            run_time=1,
        )

        formula = MathTex(
            r"A = \int_0^1 (x - x^2)\,dx = "
            r"\left[\frac{x^2}{2} - \frac{x^3}{3}\right]_0^1 = \frac{1}{6}",
            font_size=30,
            color=WHITE,
        ).to_edge(DOWN, buff=0.4)
        formula_bg = BackgroundRectangle(formula, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(formula_bg), Write(formula), run_time=1.5)
        self.wait(2)

        # --- Phase 6: Abschluss-Zusammenfassung (2s) ---
        self.play(FadeOut(formula_bg), FadeOut(formula))

        summary = MathTex(
            r"\text{Je mehr Streifen, desto genauer die Fläche!}",
            font_size=30,
        ).to_edge(DOWN, buff=0.4)
        summary_bg = BackgroundRectangle(summary, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(summary_bg), Write(summary))
        self.wait(2)


class VorzeichenwechselFlaeche(Scene):
    def construct(self):
        # --- Phase 1: Setup (2s) ---
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
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
        ).shift(UP * 0.3)

        x_label = MathTex("x", font_size=28, color=WHITE).next_to(axes.x_axis, RIGHT, buff=0.15)
        y_label = MathTex("y", font_size=28, color=WHITE).next_to(axes.y_axis, UP, buff=0.15)

        def f(x):
            return x ** 3

        def g(x):
            return x

        graph_f = axes.plot(f, x_range=[-1.3, 1.3], color=BLUE_3B1B, stroke_width=3)
        graph_g = axes.plot(g, x_range=[-1.4, 1.4], color=RED_3B1B, stroke_width=3)

        label_f = MathTex(
            r"f(x) = x^3", font_size=28, color=BLUE_3B1B
        ).move_to(axes.c2p(1.1, 1.4))
        label_g = MathTex(
            r"g(x) = x", font_size=28, color=RED_3B1B
        ).move_to(axes.c2p(1.35, 0.75))

        self.play(Create(axes), Write(x_label), Write(y_label), run_time=1)
        self.play(
            Create(graph_f), Write(label_f),
            Create(graph_g), Write(label_g),
            run_time=1,
        )

        # --- Phase 2: Schnittpunkte (1s) ---
        dots = VGroup(
            Dot(axes.c2p(-1, -1), color=YELLOW_3B1B, radius=0.07, z_index=5),
            Dot(axes.c2p(0, 0), color=YELLOW_3B1B, radius=0.07, z_index=5),
            Dot(axes.c2p(1, 1), color=YELLOW_3B1B, radius=0.07, z_index=5),
        )
        dot_labels = VGroup(
            MathTex(r"x = -1", font_size=20, color=YELLOW_3B1B).next_to(dots[0], DL, buff=0.12),
            MathTex(r"x = 0", font_size=20, color=YELLOW_3B1B).next_to(dots[1], DL, buff=0.12),
            MathTex(r"x = 1", font_size=20, color=YELLOW_3B1B).next_to(dots[2], UR, buff=0.12),
        )

        self.play(
            *[FadeIn(d, scale=1.5) for d in dots],
            *[Write(l) for l in dot_labels],
            run_time=1,
        )

        # --- Phase 3: Naives Integral (3s) ---
        # Auf [-1, 0]: x³ >= x (also f oben, g unten)
        # Auf [0, 1]: x >= x³ (also g oben, f unten)
        # Wir zeigen die Fläche naiv als ein Stück
        area_left_naive = axes.get_area(
            graph_f,
            x_range=[-1, 0],
            bounded_graph=graph_g,
            color=GREEN_3B1B,
            opacity=0.4,
        )
        area_right_naive = axes.get_area(
            graph_g,
            x_range=[0, 1],
            bounded_graph=graph_f,
            color=GREEN_3B1B,
            opacity=0.4,
        )
        naive_area = VGroup(area_left_naive, area_right_naive)

        self.play(FadeIn(naive_area), run_time=1)

        naive_formula = MathTex(
            r"\int_{-1}^{1} (x^3 - x)\,dx = 0",
            font_size=30,
            color=WHITE,
        ).to_edge(DOWN, buff=0.6)
        naive_formula_bg = BackgroundRectangle(naive_formula, fill_opacity=0.85, buff=0.15)

        falsch_text = MathTex(
            r"\text{Falsch! Die Flächen heben sich auf.}",
            font_size=28,
            color=RED_3B1B,
        ).next_to(naive_formula, DOWN, buff=0.15)
        falsch_bg = BackgroundRectangle(falsch_text, fill_opacity=0.85, buff=0.12)

        self.play(
            FadeIn(naive_formula_bg), Write(naive_formula),
            run_time=1,
        )
        self.play(FadeIn(falsch_bg), Write(falsch_text), run_time=1)
        self.wait(1)

        # --- Phase 4: Korrekte Aufteilung (4s) ---
        self.play(
            FadeOut(naive_area),
            FadeOut(naive_formula_bg), FadeOut(naive_formula),
            FadeOut(falsch_bg), FadeOut(falsch_text),
            run_time=0.8,
        )

        # [-1, 0]: f(x)=x³ liegt über g(x)=x
        area_1 = axes.get_area(
            graph_f,
            x_range=[-1, 0],
            bounded_graph=graph_g,
            color=ORANGE_3B1B,
            opacity=0.5,
        )
        # [0, 1]: g(x)=x liegt über f(x)=x³
        area_2 = axes.get_area(
            graph_g,
            x_range=[0, 1],
            bounded_graph=graph_f,
            color=GREEN_3B1B,
            opacity=0.5,
        )

        self.play(FadeIn(area_1), FadeIn(area_2), run_time=1)

        # Annotationen für die Teilflächen
        ann_1 = MathTex(
            r"\text{Teilfläche 1} = \tfrac{1}{4}",
            font_size=24, color=ORANGE_3B1B,
        ).move_to(axes.c2p(-0.55, -0.55))
        ann_1_bg = BackgroundRectangle(ann_1, fill_opacity=0.8, buff=0.1)

        ann_2 = MathTex(
            r"\text{Teilfläche 2} = \tfrac{1}{4}",
            font_size=24, color=GREEN_3B1B,
        ).move_to(axes.c2p(0.55, 0.55))
        ann_2_bg = BackgroundRectangle(ann_2, fill_opacity=0.8, buff=0.1)

        self.play(
            FadeIn(ann_1_bg), Write(ann_1),
            FadeIn(ann_2_bg), Write(ann_2),
            run_time=1,
        )

        correct_formula = MathTex(
            r"A = |A_1| + |A_2| = \frac{1}{4} + \frac{1}{4} = \frac{1}{2}",
            font_size=30,
            color=WHITE,
        ).to_edge(DOWN, buff=0.4)
        correct_formula_bg = BackgroundRectangle(correct_formula, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(correct_formula_bg), Write(correct_formula), run_time=1.5)
        self.wait(2)

        # --- Phase 5: Merksatz (2s) ---
        self.play(FadeOut(correct_formula_bg), FadeOut(correct_formula))

        merksatz = MathTex(
            r"\text{Betrag nicht vergessen! Immer an Schnittpunkten aufteilen.}",
            font_size=28,
        ).to_edge(DOWN, buff=0.4)
        merksatz_bg = BackgroundRectangle(merksatz, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(merksatz_bg), Write(merksatz))
        self.wait(2)

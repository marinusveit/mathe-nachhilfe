"""
Manim-Animation: Zusammenhang f, f', f''
Zeigt visuell, wie Monotonie, Extrema, Wendepunkte und Krümmung zusammenhängen.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql kurvendiskussion.py KurvendiskussionAnimation
    manim -pqh kurvendiskussion.py KurvendiskussionAnimation   # 1080p
"""

from manim import *
import numpy as np

# 3b1b-Farbpalette
BLUE_3B1B = "#58C4DD"
YELLOW_3B1B = "#FFFF00"
GREEN_3B1B = "#83C167"
RED_3B1B = "#FC6255"
PINK_3B1B = "#FF69B4"
GREY_3B1B = "#888888"
ORANGE_3B1B = "#FF8C00"


class KurvendiskussionAnimation(Scene):
    def construct(self):
        # f(x) = x³ - 3x  (schöne Extrema und Wendepunkt)
        def f(x):
            return x ** 3 - 3 * x

        def f_prime(x):
            return 3 * x ** 2 - 3

        def f_double_prime(x):
            return 6 * x

        # --- Drei Achsensysteme untereinander ---
        axes_config = {
            "x_range": [-2.5, 2.5, 1],
            "x_length": 5,
            "axis_config": {
                "include_numbers": True,
                "font_size": 18,
                "color": GREY_3B1B,
                "stroke_width": 1.5,
                "tick_size": 0.04,
            },
            "tips": True,
        }

        axes_f = Axes(y_range=[-4, 4, 2], y_length=2.2, **axes_config)
        axes_fp = Axes(y_range=[-4, 10, 2], y_length=2.2, **axes_config)
        axes_fpp = Axes(y_range=[-16, 16, 8], y_length=2.2, **axes_config)

        # Anordnen
        all_axes = VGroup(axes_f, axes_fp, axes_fpp).arrange(DOWN, buff=0.4).shift(LEFT * 0.3)

        # Labels
        f_label = MathTex(r"f(x)", font_size=26, color=BLUE_3B1B).next_to(axes_f, LEFT, buff=0.3)
        fp_label = MathTex(r"f'(x)", font_size=26, color=RED_3B1B).next_to(axes_fp, LEFT, buff=0.3)
        fpp_label = MathTex(r"f''(x)", font_size=26, color=ORANGE_3B1B).next_to(axes_fpp, LEFT, buff=0.3)

        # Funktionsname
        func_name = MathTex(
            r"f(x) = x^3 - 3x", font_size=28, color=WHITE,
        ).to_corner(UR, buff=0.4)
        func_bg = BackgroundRectangle(func_name, fill_opacity=0.7, buff=0.15)

        # --- Phase 1: f(x) zeichnen ---
        graph_f = axes_f.plot(f, x_range=[-2.05, 2.05], color=BLUE_3B1B, stroke_width=3)

        self.play(Create(axes_f), Write(f_label), FadeIn(func_bg), Write(func_name))
        self.play(Create(graph_f), run_time=1.5)
        self.wait(0.5)

        # Extrema markieren: f'(x) = 0 → x = -1, x = 1
        dot_max = Dot(axes_f.c2p(-1, f(-1)), color=GREEN_3B1B, radius=0.07, z_index=5)
        dot_min = Dot(axes_f.c2p(1, f(1)), color=GREEN_3B1B, radius=0.07, z_index=5)
        max_label = MathTex(r"\text{HOP}", font_size=18, color=GREEN_3B1B).next_to(dot_max, UP, buff=0.1)
        min_label = MathTex(r"\text{TIP}", font_size=18, color=GREEN_3B1B).next_to(dot_min, DOWN, buff=0.1)

        # Wendepunkt: f''(x) = 0 → x = 0
        dot_wp = Dot(axes_f.c2p(0, f(0)), color=ORANGE_3B1B, radius=0.07, z_index=5)
        wp_label = MathTex(r"\text{WP}", font_size=18, color=ORANGE_3B1B).next_to(dot_wp, UR, buff=0.1)

        # --- Phase 2: f'(x) zeichnen ---
        graph_fp = axes_fp.plot(f_prime, x_range=[-2.05, 2.05], color=RED_3B1B, stroke_width=3)

        self.play(Create(axes_fp), Write(fp_label))
        self.play(Create(graph_fp), run_time=1.5)
        self.wait(0.5)

        # Nullstellen von f' markieren → Extrema von f
        dot_fp_null1 = Dot(axes_fp.c2p(-1, 0), color=GREEN_3B1B, radius=0.07, z_index=5)
        dot_fp_null2 = Dot(axes_fp.c2p(1, 0), color=GREEN_3B1B, radius=0.07, z_index=5)

        # Vertikale Verbindungslinien
        vline1 = DashedLine(
            axes_fp.c2p(-1, 0), axes_f.c2p(-1, f(-1)),
            color=GREEN_3B1B, stroke_width=1.5, dash_length=0.06,
        )
        vline2 = DashedLine(
            axes_fp.c2p(1, 0), axes_f.c2p(1, f(1)),
            color=GREEN_3B1B, stroke_width=1.5, dash_length=0.06,
        )

        # Erklärungstext
        erkl_1 = MathTex(
            r"f'(x) = 0 \;\Rightarrow\; \text{Kandidat für Extremstelle}",
            font_size=24, color=GREEN_3B1B,
        ).to_corner(UL, buff=0.4)
        erkl_1_bg = BackgroundRectangle(erkl_1, fill_opacity=0.7, buff=0.1)

        self.play(
            FadeIn(dot_fp_null1), FadeIn(dot_fp_null2),
            Create(vline1), Create(vline2),
            FadeIn(dot_max), FadeIn(dot_min),
            Write(max_label), Write(min_label),
            FadeIn(erkl_1_bg), Write(erkl_1),
        )
        self.wait(1.5)

        # Monotonie-Bereiche einfärben
        # f' > 0: x < -1 und x > 1 (steigend)
        # f' < 0: -1 < x < 1 (fallend)
        area_pos_left = axes_fp.get_area(
            graph_fp, x_range=[-2.05, -1], color=GREEN_3B1B, opacity=0.2,
        )
        area_neg = axes_fp.get_area(
            graph_fp, x_range=[-1, 1], color=RED_3B1B, opacity=0.2,
        )
        area_pos_right = axes_fp.get_area(
            graph_fp, x_range=[1, 2.05], color=GREEN_3B1B, opacity=0.2,
        )

        mono_text = VGroup(
            MathTex(r"f' > 0 \;\Rightarrow\; f \text{ steigt}", font_size=22, color=GREEN_3B1B),
            MathTex(r"f' < 0 \;\Rightarrow\; f \text{ fällt}", font_size=22, color=RED_3B1B),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(erkl_1, DOWN, buff=0.3, aligned_edge=LEFT)
        mono_bg = BackgroundRectangle(mono_text, fill_opacity=0.7, buff=0.1)

        self.play(
            FadeIn(area_pos_left), FadeIn(area_neg), FadeIn(area_pos_right),
            FadeIn(mono_bg), Write(mono_text),
        )
        self.wait(2)

        # --- Phase 3: f''(x) zeichnen ---
        graph_fpp = axes_fpp.plot(f_double_prime, x_range=[-2.05, 2.05], color=ORANGE_3B1B, stroke_width=3)

        self.play(Create(axes_fpp), Write(fpp_label))
        self.play(Create(graph_fpp), run_time=1.5)
        self.wait(0.5)

        # Nullstelle von f'' → Wendepunkt von f
        dot_fpp_null = Dot(axes_fpp.c2p(0, 0), color=ORANGE_3B1B, radius=0.07, z_index=5)
        vline_wp = DashedLine(
            axes_fpp.c2p(0, 0), axes_f.c2p(0, f(0)),
            color=ORANGE_3B1B, stroke_width=1.5, dash_length=0.06,
        )

        self.play(FadeOut(erkl_1_bg), FadeOut(erkl_1), FadeOut(mono_bg), FadeOut(mono_text))

        erkl_2 = MathTex(
            r"f''(x) = 0 \;\Rightarrow\; \text{Kandidat für Wendepunkt}",
            font_size=24, color=ORANGE_3B1B,
        ).to_corner(UL, buff=0.4)
        erkl_2_bg = BackgroundRectangle(erkl_2, fill_opacity=0.7, buff=0.1)

        kruemm_text = VGroup(
            MathTex(r"f'' > 0 \;\Rightarrow\; \text{linksgekrümmt}", font_size=22, color=ORANGE_3B1B),
            MathTex(r"f'' < 0 \;\Rightarrow\; \text{rechtsgekrümmt}", font_size=22, color=YELLOW_3B1B),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT).next_to(erkl_2, DOWN, buff=0.3, aligned_edge=LEFT)
        kruemm_bg = BackgroundRectangle(kruemm_text, fill_opacity=0.7, buff=0.1)

        self.play(
            FadeIn(dot_fpp_null), Create(vline_wp), FadeIn(dot_wp), Write(wp_label),
            FadeIn(erkl_2_bg), Write(erkl_2),
            FadeIn(kruemm_bg), Write(kruemm_text),
        )
        self.wait(2)

        # --- Zusammenfassung ---
        self.play(
            FadeOut(erkl_2_bg), FadeOut(erkl_2),
            FadeOut(kruemm_bg), FadeOut(kruemm_text),
        )

        summary = VGroup(
            MathTex(r"f'(x) = 0", font_size=22, color=GREEN_3B1B),
            MathTex(r"\Rightarrow", font_size=22),
            MathTex(r"\text{Kandidat für Extremstelle}", font_size=22, color=GREEN_3B1B),
        ).arrange(RIGHT, buff=0.15)

        summary2 = VGroup(
            MathTex(r"f''(x) = 0", font_size=22, color=ORANGE_3B1B),
            MathTex(r"\Rightarrow", font_size=22),
            MathTex(r"\text{Kandidat für Wendepunkt}", font_size=22, color=ORANGE_3B1B),
        ).arrange(RIGHT, buff=0.15)

        summary3 = VGroup(
            MathTex(r"f''(x_E) < 0", font_size=22, color=YELLOW_3B1B),
            MathTex(r"\Rightarrow", font_size=22),
            MathTex(r"\text{Maximum}", font_size=22, color=YELLOW_3B1B),
            MathTex(r"\quad f''(x_E) > 0", font_size=22, color=PINK_3B1B),
            MathTex(r"\Rightarrow", font_size=22),
            MathTex(r"\text{Minimum}", font_size=22, color=PINK_3B1B),
        ).arrange(RIGHT, buff=0.15)

        all_summary = VGroup(summary, summary2, summary3).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT,
        ).to_corner(UL, buff=0.4)
        sum_bg = BackgroundRectangle(all_summary, fill_opacity=0.8, buff=0.15)

        self.play(FadeIn(sum_bg), Write(all_summary))
        self.wait(4)


class WandernderPunkt(Scene):
    """
    Ein Punkt wandert entlang f(x) = x³ - 3x mit Tangente.
    Korrespondierende Punkte auf f'(x) und f''(x) bewegen sich synchron.
    Bei besonderen Punkten (Extrema, WP) werden Regeln links eingeblendet.

    Rendern mit:
        manim -pql kurvendiskussion.py WandernderPunkt
        manim -pqh kurvendiskussion.py WandernderPunkt   # 1080p
    """

    def construct(self):
        # --- Funktionen ---
        def f(x):
            return x ** 3 - 3 * x

        def f_prime(x):
            return 3 * x ** 2 - 3

        def f_double_prime(x):
            return 6 * x

        # --- Hilfsfunktion: Tangente an f bei x0 ---
        def make_tangent(x0, dx=0.6):
            slope = f_prime(x0)
            x1, x2 = x0 - dx, x0 + dx
            y1 = f(x0) + slope * (x1 - x0)
            y2 = f(x0) + slope * (x2 - x0)
            return Line(
                axes_f.c2p(x1, y1), axes_f.c2p(x2, y2),
                color=YELLOW_3B1B, stroke_width=2.5,
            )

        # --- Drei Achsensysteme untereinander ---
        axes_config = {
            "x_range": [-2.5, 2.5, 1],
            "x_length": 5,
            "axis_config": {
                "include_numbers": True,
                "font_size": 18,
                "color": GREY_3B1B,
                "stroke_width": 1.5,
                "tick_size": 0.04,
            },
            "tips": True,
        }

        axes_f = Axes(y_range=[-4, 4, 2], y_length=2.2, **axes_config)
        axes_fp = Axes(y_range=[-4, 10, 2], y_length=2.2, **axes_config)
        axes_fpp = Axes(y_range=[-16, 16, 8], y_length=2.2, **axes_config)

        all_axes = VGroup(axes_f, axes_fp, axes_fpp).arrange(DOWN, buff=0.4)

        # --- Labels RECHTS mit vollen Formeln ---
        f_label = MathTex(
            r"f(x) = x^3 - 3x", font_size=22, color=BLUE_3B1B,
        ).next_to(axes_f, RIGHT, buff=0.3)
        fp_label = MathTex(
            r"f'(x) = 3x^2 - 3", font_size=22, color=RED_3B1B,
        ).next_to(axes_fp, RIGHT, buff=0.3)
        fpp_label = MathTex(
            r"f''(x) = 6x", font_size=22, color=ORANGE_3B1B,
        ).next_to(axes_fpp, RIGHT, buff=0.3)

        # --- Graphen ---
        graph_f = axes_f.plot(f, x_range=[-2.05, 2.05], color=BLUE_3B1B, stroke_width=3)
        graph_fp = axes_fp.plot(f_prime, x_range=[-2.05, 2.05], color=RED_3B1B, stroke_width=3)
        graph_fpp = axes_fpp.plot(f_double_prime, x_range=[-2.05, 2.05], color=ORANGE_3B1B, stroke_width=3)

        # Alles einblenden
        self.play(
            Create(axes_f), Create(axes_fp), Create(axes_fpp),
            Write(f_label), Write(fp_label), Write(fpp_label),
        )
        self.play(
            Create(graph_f), Create(graph_fp), Create(graph_fpp),
            run_time=2,
        )
        self.wait(0.5)

        # --- ValueTracker und wandernde Punkte ---
        tracker = ValueTracker(-2.2)

        dot_f = always_redraw(
            lambda: Dot(
                axes_f.c2p(tracker.get_value(), f(tracker.get_value())),
                color=YELLOW_3B1B, radius=0.08, z_index=5,
            )
        )
        dot_fp = always_redraw(
            lambda: Dot(
                axes_fp.c2p(tracker.get_value(), f_prime(tracker.get_value())),
                color=YELLOW_3B1B, radius=0.08, z_index=5,
            )
        )
        dot_fpp = always_redraw(
            lambda: Dot(
                axes_fpp.c2p(tracker.get_value(), f_double_prime(tracker.get_value())),
                color=YELLOW_3B1B, radius=0.08, z_index=5,
            )
        )

        # --- Tangente an f(x) ---
        tangent = always_redraw(lambda: make_tangent(tracker.get_value()))

        # --- Vertikale gestrichelte Verbindungslinien ---
        vline_f_fp = always_redraw(
            lambda: DashedLine(
                axes_f.c2p(tracker.get_value(), f(tracker.get_value())),
                axes_fp.c2p(tracker.get_value(), f_prime(tracker.get_value())),
                color=GREY_3B1B, stroke_width=1.5, dash_length=0.06,
            )
        )
        vline_fp_fpp = always_redraw(
            lambda: DashedLine(
                axes_fp.c2p(tracker.get_value(), f_prime(tracker.get_value())),
                axes_fpp.c2p(tracker.get_value(), f_double_prime(tracker.get_value())),
                color=GREY_3B1B, stroke_width=1.5, dash_length=0.06,
            )
        )

        # Dots, Tangente und Linien einblenden
        self.play(
            FadeIn(dot_f), FadeIn(dot_fp), FadeIn(dot_fpp),
            Create(tangent),
            Create(vline_f_fp), Create(vline_fp_fpp),
        )
        self.wait(0.5)

        # ============================================================
        # Phase 1: x = -2.2 → -1 (f steigt, f' > 0)
        # ============================================================
        rule_steigt = MathTex(
            r"f'(x) > 0 \;\Rightarrow\; f \text{ steigt}",
            font_size=22, color=GREEN_3B1B,
        ).to_corner(UL, buff=0.4)
        rule_steigt_bg = BackgroundRectangle(rule_steigt, fill_opacity=0.8, buff=0.1)

        self.play(FadeIn(rule_steigt_bg), Write(rule_steigt))
        self.play(tracker.animate.set_value(-1), run_time=3, rate_func=linear)
        self.play(FadeOut(rule_steigt_bg), FadeOut(rule_steigt))

        # ============================================================
        # Halt bei x = -1: Hochpunkt (HOP)
        # ============================================================
        hop_dot = Dot(axes_f.c2p(-1, f(-1)), color=GREEN_3B1B, radius=0.07, z_index=6)
        hop_label = MathTex(r"\text{HOP}", font_size=20, color=GREEN_3B1B).next_to(hop_dot, UP, buff=0.12)

        rule_hop = VGroup(
            MathTex(r"f'(-1) = 0", font_size=22, color=GREEN_3B1B),
            MathTex(r"\Rightarrow\;\text{Extremstelle}", font_size=22, color=GREEN_3B1B),
        ).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.4)
        rule_hop_2 = MathTex(
            r"f''(-1) = -6 < 0 \;\Rightarrow\; \text{Maximum}",
            font_size=22, color=YELLOW_3B1B,
        ).next_to(rule_hop, DOWN, buff=0.15, aligned_edge=LEFT)
        rule_hop_group = VGroup(rule_hop, rule_hop_2)
        rule_hop_bg = BackgroundRectangle(rule_hop_group, fill_opacity=0.8, buff=0.12)

        self.play(
            FadeIn(hop_dot), Write(hop_label),
            FadeIn(rule_hop_bg), Write(rule_hop_group),
        )
        self.wait(2.5)
        self.play(FadeOut(rule_hop_bg), FadeOut(rule_hop_group))

        # ============================================================
        # Phase 2: x = -1 → 0 (f fällt, f' < 0)
        # ============================================================
        rule_faellt = MathTex(
            r"f'(x) < 0 \;\Rightarrow\; f \text{ fällt}",
            font_size=22, color=RED_3B1B,
        ).to_corner(UL, buff=0.4)
        rule_faellt_bg = BackgroundRectangle(rule_faellt, fill_opacity=0.8, buff=0.1)

        self.play(FadeIn(rule_faellt_bg), Write(rule_faellt))
        self.play(tracker.animate.set_value(0), run_time=2.5, rate_func=linear)
        self.play(FadeOut(rule_faellt_bg), FadeOut(rule_faellt))

        # ============================================================
        # Halt bei x = 0: Wendepunkt (WP)
        # ============================================================
        wp_dot = Dot(axes_f.c2p(0, f(0)), color=ORANGE_3B1B, radius=0.07, z_index=6)
        wp_label = MathTex(r"\text{WP}", font_size=20, color=ORANGE_3B1B).next_to(wp_dot, UR, buff=0.12)

        rule_wp = VGroup(
            MathTex(r"f''(0) = 0", font_size=22, color=ORANGE_3B1B),
            MathTex(r"\Rightarrow\;\text{Wendepunkt}", font_size=22, color=ORANGE_3B1B),
        ).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.4)
        rule_wp_2 = MathTex(
            r"\text{Krümmung wechselt hier das Vorzeichen}",
            font_size=20, color=ORANGE_3B1B,
        ).next_to(rule_wp, DOWN, buff=0.15, aligned_edge=LEFT)
        rule_wp_group = VGroup(rule_wp, rule_wp_2)
        rule_wp_bg = BackgroundRectangle(rule_wp_group, fill_opacity=0.8, buff=0.12)

        self.play(
            FadeIn(wp_dot), Write(wp_label),
            FadeIn(rule_wp_bg), Write(rule_wp_group),
        )
        self.wait(2.5)
        self.play(FadeOut(rule_wp_bg), FadeOut(rule_wp_group))

        # ============================================================
        # Phase 3: x = 0 → 1 (f fällt weiter, f' < 0)
        # ============================================================
        rule_faellt2 = MathTex(
            r"f'(x) < 0 \;\Rightarrow\; f \text{ fällt}",
            font_size=22, color=RED_3B1B,
        ).to_corner(UL, buff=0.4)
        rule_faellt2_bg = BackgroundRectangle(rule_faellt2, fill_opacity=0.8, buff=0.1)

        self.play(FadeIn(rule_faellt2_bg), Write(rule_faellt2))
        self.play(tracker.animate.set_value(1), run_time=2.5, rate_func=linear)
        self.play(FadeOut(rule_faellt2_bg), FadeOut(rule_faellt2))

        # ============================================================
        # Halt bei x = 1: Tiefpunkt (TIP)
        # ============================================================
        tip_dot = Dot(axes_f.c2p(1, f(1)), color=GREEN_3B1B, radius=0.07, z_index=6)
        tip_label = MathTex(r"\text{TIP}", font_size=20, color=GREEN_3B1B).next_to(tip_dot, DOWN, buff=0.12)

        rule_tip = VGroup(
            MathTex(r"f'(1) = 0", font_size=22, color=GREEN_3B1B),
            MathTex(r"\Rightarrow\;\text{Extremstelle}", font_size=22, color=GREEN_3B1B),
        ).arrange(RIGHT, buff=0.1).to_corner(UL, buff=0.4)
        rule_tip_2 = MathTex(
            r"f''(1) = 6 > 0 \;\Rightarrow\; \text{Minimum}",
            font_size=22, color=PINK_3B1B,
        ).next_to(rule_tip, DOWN, buff=0.15, aligned_edge=LEFT)
        rule_tip_group = VGroup(rule_tip, rule_tip_2)
        rule_tip_bg = BackgroundRectangle(rule_tip_group, fill_opacity=0.8, buff=0.12)

        self.play(
            FadeIn(tip_dot), Write(tip_label),
            FadeIn(rule_tip_bg), Write(rule_tip_group),
        )
        self.wait(2.5)
        self.play(FadeOut(rule_tip_bg), FadeOut(rule_tip_group))

        # ============================================================
        # Phase 4: x = 1 → 2.2 (f steigt, f' > 0)
        # ============================================================
        rule_steigt2 = MathTex(
            r"f'(x) > 0 \;\Rightarrow\; f \text{ steigt}",
            font_size=22, color=GREEN_3B1B,
        ).to_corner(UL, buff=0.4)
        rule_steigt2_bg = BackgroundRectangle(rule_steigt2, fill_opacity=0.8, buff=0.1)

        self.play(FadeIn(rule_steigt2_bg), Write(rule_steigt2))
        self.play(tracker.animate.set_value(2.2), run_time=3, rate_func=linear)
        self.play(FadeOut(rule_steigt2_bg), FadeOut(rule_steigt2))

        # ============================================================
        # Zusammenfassung
        # ============================================================
        summary_title = Text(
            "Kurvendiskussion auf einen Blick",
            font_size=22, color=WHITE, weight=BOLD,
        )
        summary_rules = VGroup(
            MathTex(r"f'(x) = 0 \;\Rightarrow\; \text{Extremstelle}", font_size=22, color=GREEN_3B1B),
            MathTex(r"f''(x_E) < 0 \;\Rightarrow\; \text{Maximum}", font_size=22, color=YELLOW_3B1B),
            MathTex(r"f''(x_E) > 0 \;\Rightarrow\; \text{Minimum}", font_size=22, color=PINK_3B1B),
            MathTex(r"f''(x) = 0 \;\Rightarrow\; \text{Wendepunkt}", font_size=22, color=ORANGE_3B1B),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        summary = VGroup(summary_title, summary_rules).arrange(
            DOWN, buff=0.25, aligned_edge=LEFT,
        ).to_corner(UL, buff=0.4)
        sum_bg = BackgroundRectangle(summary, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(sum_bg), Write(summary))
        self.wait(4)

"""
Manim-Animation: Zusammenhang f <-> f' <-> f''
Kompakte Visualisierung fuer den hilfsmittelfreien Teil (Sitzung 7).
Zeigt Extrema, Nullstellen von f', Wendepunkt und Nullstelle von f''
sowie Vorzeichen-Bereiche von f'.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql zusammenhang_f_fp_fpp.py ZusammenhangFFpFpp
    manim -pqh zusammenhang_f_fp_fpp.py ZusammenhangFFpFpp   # 1080p
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


class ZusammenhangFFpFpp(Scene):
    def construct(self):
        # --- Funktionen ---
        def f(x):
            return x ** 3 - 3 * x

        def fp(x):
            return 3 * x ** 2 - 3

        def fpp(x):
            return 6 * x

        # --- Drei Achsensysteme untereinander ---
        axes_config = {
            "x_range": [-2.5, 2.5, 1],
            "x_length": 5.5,
            "axis_config": {
                "include_numbers": True,
                "font_size": 18,
                "color": GREY_3B1B,
                "stroke_width": 1.5,
                "tick_size": 0.04,
            },
            "tips": True,
        }

        axes_f = Axes(y_range=[-4, 4, 2], y_length=2.0, **axes_config)
        axes_fp = Axes(y_range=[-4, 10, 2], y_length=2.0, **axes_config)
        axes_fpp = Axes(y_range=[-16, 16, 8], y_length=2.0, **axes_config)

        all_axes = VGroup(axes_f, axes_fp, axes_fpp).arrange(DOWN, buff=0.35)

        # Labels links neben den Achsen
        label_f = MathTex(r"f(x)", font_size=24, color=BLUE_3B1B).next_to(
            axes_f, LEFT, buff=0.25
        )
        label_fp = MathTex(r"f'(x)", font_size=24, color=RED_3B1B).next_to(
            axes_fp, LEFT, buff=0.25
        )
        label_fpp = MathTex(r"f''(x)", font_size=24, color=ORANGE_3B1B).next_to(
            axes_fpp, LEFT, buff=0.25
        )

        # Funktionsname oben rechts
        func_name = MathTex(
            r"f(x) = x^3 - 3x", font_size=26, color=WHITE
        ).to_corner(UR, buff=0.4)
        func_bg = BackgroundRectangle(func_name, fill_opacity=0.7, buff=0.15)

        # --- Phase 1: f(x) zeichnen ---
        graph_f = axes_f.plot(f, x_range=[-2.2, 2.2], color=BLUE_3B1B, stroke_width=3)

        self.play(
            Create(axes_f),
            Write(label_f),
            FadeIn(func_bg),
            Write(func_name),
            run_time=1,
        )
        self.play(Create(graph_f), run_time=1.2)
        self.wait(0.3)

        # --- Phase 2: f'(x) zeichnen ---
        graph_fp = axes_fp.plot(
            fp, x_range=[-2.2, 2.2], color=RED_3B1B, stroke_width=3
        )

        fp_eq = MathTex(
            r"f'(x) = 3x^2 - 3", font_size=22, color=RED_3B1B
        ).next_to(func_name, DOWN, buff=0.15, aligned_edge=RIGHT)
        fp_eq_bg = BackgroundRectangle(fp_eq, fill_opacity=0.7, buff=0.1)

        self.play(Create(axes_fp), Write(label_fp), run_time=0.8)
        self.play(
            Create(graph_fp),
            FadeIn(fp_eq_bg),
            Write(fp_eq),
            run_time=1.2,
        )
        self.wait(0.3)

        # --- Phase 3: f''(x) zeichnen ---
        graph_fpp = axes_fpp.plot(
            fpp, x_range=[-2.2, 2.2], color=ORANGE_3B1B, stroke_width=3
        )

        fpp_eq = MathTex(
            r"f''(x) = 6x", font_size=22, color=ORANGE_3B1B
        ).next_to(fp_eq, DOWN, buff=0.15, aligned_edge=RIGHT)
        fpp_eq_bg = BackgroundRectangle(fpp_eq, fill_opacity=0.7, buff=0.1)

        self.play(Create(axes_fpp), Write(label_fpp), run_time=0.8)
        self.play(
            Create(graph_fpp),
            FadeIn(fpp_eq_bg),
            Write(fpp_eq),
            run_time=1.2,
        )
        self.wait(0.5)

        # --- Phase 4: Extrema von f <-> Nullstellen von f' ---
        # Punkte auf f
        dot_hp = Dot(
            axes_f.c2p(-1, f(-1)), color=GREEN_3B1B, radius=0.07, z_index=5
        )
        dot_tp = Dot(
            axes_f.c2p(1, f(1)), color=GREEN_3B1B, radius=0.07, z_index=5
        )
        hp_label = MathTex(
            r"\text{HP}", font_size=18, color=GREEN_3B1B
        ).next_to(dot_hp, UP, buff=0.1)
        tp_label = MathTex(
            r"\text{TP}", font_size=18, color=GREEN_3B1B
        ).next_to(dot_tp, DOWN, buff=0.1)

        # Nullstellen-Punkte auf f'
        dot_fp_n1 = Dot(
            axes_fp.c2p(-1, 0), color=GREEN_3B1B, radius=0.07, z_index=5
        )
        dot_fp_n2 = Dot(
            axes_fp.c2p(1, 0), color=GREEN_3B1B, radius=0.07, z_index=5
        )

        # Gestrichelte vertikale Verbindungslinien
        vline_hp = DashedLine(
            axes_f.c2p(-1, f(-1)),
            axes_fp.c2p(-1, 0),
            color=GREEN_3B1B,
            stroke_width=1.5,
            dash_length=0.06,
        )
        vline_tp = DashedLine(
            axes_f.c2p(1, f(1)),
            axes_fp.c2p(1, 0),
            color=GREEN_3B1B,
            stroke_width=1.5,
            dash_length=0.06,
        )

        # Erklaerungs-Text
        text_ext = MathTex(
            r"\text{Extremum von } f",
            r"\;\leftrightarrow\;",
            r"\text{Nullstelle von } f'",
            font_size=22,
        ).to_corner(UL, buff=0.4)
        text_ext[0].set_color(GREEN_3B1B)
        text_ext[2].set_color(GREEN_3B1B)
        text_ext_bg = BackgroundRectangle(text_ext, fill_opacity=0.8, buff=0.12)

        self.play(
            FadeIn(dot_hp),
            FadeIn(dot_tp),
            Write(hp_label),
            Write(tp_label),
            FadeIn(dot_fp_n1),
            FadeIn(dot_fp_n2),
            Create(vline_hp),
            Create(vline_tp),
            FadeIn(text_ext_bg),
            Write(text_ext),
            run_time=1.5,
        )
        self.wait(1.5)

        # --- Phase 5: Vorzeichen-Bereiche von f' ---
        area_pos_l = axes_fp.get_area(
            graph_fp, x_range=[-2.2, -1], color=GREEN_3B1B, opacity=0.2
        )
        area_neg = axes_fp.get_area(
            graph_fp, x_range=[-1, 1], color=RED_3B1B, opacity=0.2
        )
        area_pos_r = axes_fp.get_area(
            graph_fp, x_range=[1, 2.2], color=GREEN_3B1B, opacity=0.2
        )

        mono_text = VGroup(
            MathTex(
                r"f' > 0 \;\Rightarrow\; f \text{ steigt}",
                font_size=20,
                color=GREEN_3B1B,
            ),
            MathTex(
                r"f' < 0 \;\Rightarrow\; f \text{ fällt}",
                font_size=20,
                color=RED_3B1B,
            ),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        mono_text.next_to(text_ext, DOWN, buff=0.2, aligned_edge=LEFT)
        mono_bg = BackgroundRectangle(mono_text, fill_opacity=0.8, buff=0.1)

        self.play(
            FadeIn(area_pos_l),
            FadeIn(area_neg),
            FadeIn(area_pos_r),
            FadeIn(mono_bg),
            Write(mono_text),
            run_time=1,
        )
        self.wait(1.5)

        # --- Phase 6: Wendepunkt von f <-> Nullstelle von f'' ---
        # Aufraeumen: Monotonie-Texte ausblenden
        self.play(
            FadeOut(text_ext_bg),
            FadeOut(text_ext),
            FadeOut(mono_bg),
            FadeOut(mono_text),
            run_time=0.6,
        )

        # Wendepunkt auf f
        dot_wp = Dot(
            axes_f.c2p(0, f(0)), color=ORANGE_3B1B, radius=0.07, z_index=5
        )
        wp_label = MathTex(
            r"\text{WP}", font_size=18, color=ORANGE_3B1B
        ).next_to(dot_wp, UR, buff=0.1)

        # Nullstelle auf f''
        dot_fpp_n = Dot(
            axes_fpp.c2p(0, 0), color=ORANGE_3B1B, radius=0.07, z_index=5
        )

        # Gestrichelte Linie von f-Wendepunkt bis f''-Nullstelle
        vline_wp = DashedLine(
            axes_f.c2p(0, f(0)),
            axes_fpp.c2p(0, 0),
            color=ORANGE_3B1B,
            stroke_width=1.5,
            dash_length=0.06,
        )

        text_wp = MathTex(
            r"\text{Wendepunkt von } f",
            r"\;\leftrightarrow\;",
            r"\text{Nullstelle von } f''",
            font_size=22,
        ).to_corner(UL, buff=0.4)
        text_wp[0].set_color(ORANGE_3B1B)
        text_wp[2].set_color(ORANGE_3B1B)
        text_wp_bg = BackgroundRectangle(text_wp, fill_opacity=0.8, buff=0.12)

        self.play(
            FadeIn(dot_wp),
            Write(wp_label),
            FadeIn(dot_fpp_n),
            Create(vline_wp),
            FadeIn(text_wp_bg),
            Write(text_wp),
            run_time=1.5,
        )
        self.wait(1.5)

        # --- Phase 7: Zusammenfassung ---
        self.play(
            FadeOut(text_wp_bg),
            FadeOut(text_wp),
            run_time=0.5,
        )

        summary_1 = MathTex(
            r"f'(x_0) = 0",
            r"\;\Leftrightarrow\;",
            r"\text{Extremstelle bei } x_0",
            font_size=22,
        )
        summary_1[0].set_color(GREEN_3B1B)
        summary_1[2].set_color(GREEN_3B1B)

        summary_2 = MathTex(
            r"f''(x_0) = 0",
            r"\;\Leftrightarrow\;",
            r"\text{Wendepunkt bei } x_0",
            font_size=22,
        )
        summary_2[0].set_color(ORANGE_3B1B)
        summary_2[2].set_color(ORANGE_3B1B)

        all_summary = VGroup(summary_1, summary_2).arrange(
            DOWN, buff=0.2, aligned_edge=LEFT
        ).to_corner(UL, buff=0.4)
        sum_bg = BackgroundRectangle(all_summary, fill_opacity=0.85, buff=0.15)

        self.play(FadeIn(sum_bg), Write(all_summary), run_time=1)
        self.wait(3)

"""
Manim-Animation: Ortskurve der Extrempunkte einer Funktionsschar
Zeigt, wie die Extrempunkte von f_t(x) = x³ - 3t²x entlang y = -2x³ wandern,
dann eine Schritt-für-Schritt-Musterlösung.

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
        # ==============================================================
        #  PHASE 1 + 2: Visualisierung (wie bisher)
        # ==============================================================
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

        # --- Top-left: f_t Formeln (blau) ---
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

        # --- Bottom-left: HP / TP Info-Block ---
        def make_info_block():
            t = t_tracker.get_value()
            hp_x, hp_y = -t, 2 * t**3
            tp_x, tp_y = t, -2 * t**3
            hp1 = MathTex(r"\text{Hochpunkte: } H(-t \mid 2t^3)", font_size=22, color=GREEN_3B1B)
            hp2 = MathTex(rf"H({hp_x:.1f} \mid {hp_y:.1f})", font_size=18, color=GREEN_3B1B)
            tp1 = MathTex(r"\text{Tiefpunkte: } T(t \mid -2t^3)", font_size=22, color=RED_3B1B)
            tp2 = MathTex(rf"T({tp_x:.1f} \mid {tp_y:.1f})", font_size=18, color=RED_3B1B)
            block = VGroup(hp1, hp2, tp1, tp2).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
            block.to_corner(DL, buff=0.5)
            bg = BackgroundRectangle(block, fill_opacity=0.7, buff=0.15)
            return VGroup(bg, block)

        info_block = always_redraw(make_info_block)

        # --- t-Wert: links neben x-Achse ---
        def make_t_label():
            t = t_tracker.get_value()
            tex = MathTex(rf"t = {t:.1f}", font_size=24, color=YELLOW_3B1B)
            tex.next_to(axes.c2p(-3.5, 0), LEFT, buff=0.15)
            bg = BackgroundRectangle(tex, fill_opacity=0.7, buff=0.1)
            return VGroup(bg, tex).set_z_index(10)

        t_label = always_redraw(make_t_label)

        # --- Graph + Tag ---
        graph = always_redraw(
            lambda: axes.plot(
                lambda x: f_t(x, t_tracker.get_value()),
                x_range=[-3.2, 3.2], color=BLUE_3B1B, stroke_width=3,
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

        # --- Extrempunkt-Dots ---
        hp_dot = always_redraw(lambda: Dot(
            axes.c2p(-t_tracker.get_value(), f_t(-t_tracker.get_value(), t_tracker.get_value())),
            color=GREEN_3B1B, radius=0.1, z_index=5,
        ))
        tp_dot = always_redraw(lambda: Dot(
            axes.c2p(t_tracker.get_value(), f_t(t_tracker.get_value(), t_tracker.get_value())),
            color=RED_3B1B, radius=0.1, z_index=5,
        ))
        hp_tag = always_redraw(
            lambda: MathTex(r"\text{HP}", font_size=18, color=GREEN_3B1B).next_to(
                axes.c2p(-t_tracker.get_value(), f_t(-t_tracker.get_value(), t_tracker.get_value())),
                UP, buff=0.12,
            ).set_z_index(6)
        )
        tp_tag = always_redraw(
            lambda: MathTex(r"\text{TP}", font_size=18, color=RED_3B1B).next_to(
                axes.c2p(t_tracker.get_value(), f_t(t_tracker.get_value(), t_tracker.get_value())),
                DOWN, buff=0.12,
            ).set_z_index(6)
        )

        # --- Spuren ---
        hp_trace = TracedPath(
            lambda: axes.c2p(-t_tracker.get_value(), f_t(-t_tracker.get_value(), t_tracker.get_value())),
            stroke_color=GREEN_3B1B, stroke_width=2.5, stroke_opacity=0.7,
        )
        tp_trace = TracedPath(
            lambda: axes.c2p(t_tracker.get_value(), f_t(t_tracker.get_value(), t_tracker.get_value())),
            stroke_color=RED_3B1B, stroke_width=2.5, stroke_opacity=0.7,
        )

        # --- Aufbau ---
        self.play(Create(axes), FadeIn(title_bg), Write(title))
        self.add(ft_sub)
        self.wait(0.3)
        self.play(Create(graph), FadeIn(t_label))
        self.add(graph_tag)
        self.play(
            FadeIn(hp_dot), FadeIn(tp_dot),
            FadeIn(hp_tag), FadeIn(tp_tag),
            FadeIn(info_block),
        )
        self.add(hp_trace, tp_trace)
        self.wait(0.5)

        ghost_ts = [0.5, 1.0, 1.5, 2.0]
        ghosts = VGroup(*[
            axes.plot(lambda x, t=t: f_t(x, t), x_range=[-3.2, 3.2],
                      color=BLUE_3B1B, stroke_width=0.8, stroke_opacity=0.2)
            for t in ghost_ts
        ])
        self.play(FadeIn(ghosts), run_time=0.5)
        self.play(t_tracker.animate.set_value(2.0), run_time=5, rate_func=linear)
        self.wait(0.5)

        # --- Ortskurve einblenden ---
        ortskurve = axes.plot(lambda x: -2 * x**3, x_range=[-2.6, 2.6],
                              color=YELLOW_3B1B, stroke_width=3)
        ortskurve_label = MathTex(r"y = -2x^3", font_size=26, color=YELLOW_3B1B)
        ortskurve_label.next_to(axes.c2p(2.0, -16), RIGHT, buff=0.2)
        ortskurve_label_bg = BackgroundRectangle(ortskurve_label, fill_opacity=0.7, buff=0.1)

        current_info = make_info_block()
        ortskurve_info = MathTex(r"\text{Ortskurve: } y = -2x^3", font_size=22, color=YELLOW_3B1B)
        ortskurve_info.next_to(current_info[1], DOWN, aligned_edge=LEFT, buff=0.12)
        ortskurve_info_bg = BackgroundRectangle(ortskurve_info, fill_opacity=0.7, buff=0.12)

        self.play(
            Create(ortskurve, run_time=2),
            FadeIn(ortskurve_label_bg), Write(ortskurve_label),
            FadeIn(ortskurve_info_bg), Write(ortskurve_info),
        )
        self.wait(1.5)

        # ==============================================================
        #  PHASE 3: Verkleinern → Musterlösung
        # ==============================================================

        # Updater stoppen, damit scale funktioniert
        for mob in self.mobjects:
            mob.clear_updaters()

        everything = Group(*self.mobjects)
        self.play(
            everything.animate.scale(0.28).to_corner(UR, buff=0.15),
            run_time=1.5,
        )

        # Rahmen um die Mini-Vorschau
        mini_border = SurroundingRectangle(
            everything, color=GREY_3B1B, stroke_width=1, buff=0.08,
        )
        self.play(Create(mini_border), run_time=0.3)

        # ----------------------------------------------------------
        #  Schritt 1: Ableitungen bilden
        # ----------------------------------------------------------
        header = Text("Musterlösung: Ortskurve bestimmen", font_size=28, color=WHITE)
        header.to_edge(UP, buff=0.3).to_edge(LEFT, buff=0.5)
        ul = Underline(header, color=YELLOW_3B1B, stroke_width=2)
        self.play(Write(header), Create(ul))

        s1_lab = MathTex(r"\textbf{1. Ableitungen bilden:}", font_size=24, color=GREY_3B1B)
        s1_lab.next_to(header, DOWN, aligned_edge=LEFT, buff=0.35)

        s1_f = MathTex(r"f_t(x)", r"=", r"x^3", r"-", r"3t^2 x", font_size=28, color=BLUE_3B1B)
        s1_f.next_to(s1_lab, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(s1_lab), Write(s1_f))
        self.wait(0.3)

        # f'_t direkt darunter (ohne Pfeil)
        s1_fp = MathTex(r"f'_t(x)", r"=", r"3x^2", r"-", r"3t^2", font_size=28, color=RED_3B1B)
        s1_fp.next_to(s1_f, DOWN, aligned_edge=LEFT, buff=0.15)

        # Terme einzeln transformieren
        self.play(
            TransformFromCopy(s1_f[0], s1_fp[0]),
            TransformFromCopy(s1_f[1], s1_fp[1]),
        )
        self.play(TransformFromCopy(s1_f[2], s1_fp[2]), run_time=1)
        self.play(
            TransformFromCopy(s1_f[3], s1_fp[3]),
            TransformFromCopy(s1_f[4], s1_fp[4]),
            run_time=1,
        )
        self.wait(0.5)

        # f''_t für HP/TP-Nachweis
        s1_fpp = MathTex(r"f''_t(x)", r"=", r"6x", font_size=28, color=ORANGE_3B1B)
        s1_fpp.next_to(s1_fp, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(TransformFromCopy(s1_fp[0], s1_fpp[0]),
                  TransformFromCopy(s1_fp[1], s1_fpp[1]))
        self.play(TransformFromCopy(s1_fp[2], s1_fpp[2]), run_time=1)
        self.wait(0.8)

        # ----------------------------------------------------------
        #  Schritt 2: Extremstellen (f' = 0)
        # ----------------------------------------------------------
        s2_lab = MathTex(r"\textbf{2. Extremstellen } (f'_t = 0)\textbf{:}",
                         font_size=24, color=GREY_3B1B)
        s2_lab.next_to(s1_fpp, DOWN, aligned_edge=LEFT, buff=0.3)

        s2_eq1 = MathTex(r"3x^2 - 3t^2 = 0", font_size=28)
        s2_eq1.next_to(s2_lab, DOWN, aligned_edge=LEFT, buff=0.15)

        s2_eq2 = MathTex(r"x^2 = t^2", font_size=28)
        s2_eq2.next_to(s2_eq1, DOWN, aligned_edge=LEFT, buff=0.1)

        s2_result = MathTex(
            r"x_1 = t", r",\quad", r"x_2 = -t",
            font_size=28, color=YELLOW_3B1B,
        )
        s2_result.next_to(s2_eq2, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(s2_lab))
        self.play(Write(s2_eq1))
        self.play(Write(s2_eq2))
        self.wait(0.3)
        self.play(Write(s2_result))
        self.wait(0.8)

        # ----------------------------------------------------------
        #  Schritt 3: HP/TP-Nachweis mit f''
        # ----------------------------------------------------------
        s3_lab = MathTex(r"\textbf{3. Art der Extrema } (f''_t)\textbf{:}",
                         font_size=24, color=GREY_3B1B)
        s3_lab.next_to(s2_result, DOWN, aligned_edge=LEFT, buff=0.3)

        s3_tp = MathTex(
            r"f''_t(t) = 6t > 0 \text{ für } t > 0",
            font_size=26, color=RED_3B1B,
        )
        s3_tp.next_to(s3_lab, DOWN, aligned_edge=LEFT, buff=0.15)
        s3_tp_tag = MathTex(r"\Rightarrow \text{Tiefpunkt}", font_size=24, color=RED_3B1B)
        s3_tp_tag.next_to(s3_tp, RIGHT, buff=0.3)

        s3_hp = MathTex(
            r"f''_t(-t) = -6t < 0 \text{ für } t > 0",
            font_size=26, color=GREEN_3B1B,
        )
        s3_hp.next_to(s3_tp, DOWN, aligned_edge=LEFT, buff=0.1)
        s3_hp_tag = MathTex(r"\Rightarrow \text{Hochpunkt}", font_size=24, color=GREEN_3B1B)
        s3_hp_tag.next_to(s3_hp, RIGHT, buff=0.3)

        self.play(Write(s3_lab))
        self.play(Write(s3_tp), Write(s3_tp_tag))
        self.play(Write(s3_hp), Write(s3_hp_tag))
        self.wait(1)

        # ----------------------------------------------------------
        #  Seite 2: y-Werte + Parameter eliminieren
        # ----------------------------------------------------------
        page1 = VGroup(
            s1_lab, s1_f, s1_fp, s1_fpp,
            s2_lab, s2_eq1, s2_eq2, s2_result,
            s3_lab, s3_tp, s3_tp_tag, s3_hp, s3_hp_tag,
        )
        self.play(FadeOut(page1), run_time=0.8)

        # ----------------------------------------------------------
        #  Schritt 4: y-Werte berechnen
        # ----------------------------------------------------------
        s4_lab = MathTex(r"\textbf{4. y-Werte berechnen:}", font_size=24, color=GREY_3B1B)
        s4_lab.next_to(header, DOWN, aligned_edge=LEFT, buff=0.35)

        # Tiefpunkt
        s4_tp_title = MathTex(r"\text{Tiefpunkt } (x = t):", font_size=22, color=RED_3B1B)
        s4_tp_title.next_to(s4_lab, DOWN, aligned_edge=LEFT, buff=0.2)

        s4_tp1 = MathTex(r"f_t(t)", r"=", r"t^3 - 3t^2 \cdot t", font_size=26)
        s4_tp1.next_to(s4_tp_title, DOWN, aligned_edge=LEFT, buff=0.1)

        s4_tp2 = MathTex(r"=", r"t^3 - 3t^3", r"=", r"-2t^3", font_size=26)
        s4_tp2[3].set_color(RED_3B1B)
        s4_tp2.next_to(s4_tp1[1], DOWN, aligned_edge=LEFT, buff=0.1)

        s4_tp_res = MathTex(
            r"\Rightarrow\;", r"T(t \mid -2t^3)",
            font_size=26, color=RED_3B1B,
        )
        s4_tp_res.next_to(s4_tp2, RIGHT, buff=0.4)

        self.play(Write(s4_lab))
        self.play(Write(s4_tp_title))
        self.play(Write(s4_tp1))
        self.play(Write(s4_tp2), Write(s4_tp_res))
        self.wait(0.5)

        # Hochpunkt
        s4_hp_title = MathTex(r"\text{Hochpunkt } (x = -t):", font_size=22, color=GREEN_3B1B)
        s4_hp_title.next_to(s4_tp2, DOWN, aligned_edge=LEFT, buff=0.25)
        s4_hp_title.align_to(s4_tp_title, LEFT)

        s4_hp1 = MathTex(r"f_t(-t)", r"=", r"(-t)^3 - 3t^2 \cdot (-t)", font_size=26)
        s4_hp1.next_to(s4_hp_title, DOWN, aligned_edge=LEFT, buff=0.1)

        s4_hp2 = MathTex(r"=", r"-t^3 + 3t^3", r"=", r"2t^3", font_size=26)
        s4_hp2[3].set_color(GREEN_3B1B)
        s4_hp2.next_to(s4_hp1[1], DOWN, aligned_edge=LEFT, buff=0.1)

        s4_hp_res = MathTex(
            r"\Rightarrow\;", r"H(-t \mid 2t^3)",
            font_size=26, color=GREEN_3B1B,
        )
        s4_hp_res.next_to(s4_hp2, RIGHT, buff=0.4)

        self.play(Write(s4_hp_title))
        self.play(Write(s4_hp1))
        self.play(Write(s4_hp2), Write(s4_hp_res))
        self.wait(1)

        # ----------------------------------------------------------
        #  Seite 3: Parameter eliminieren
        # ----------------------------------------------------------
        page2 = VGroup(
            s4_lab, s4_tp_title, s4_tp1, s4_tp2, s4_tp_res,
            s4_hp_title, s4_hp1, s4_hp2, s4_hp_res,
        )
        self.play(FadeOut(page2), run_time=0.8)

        # ----------------------------------------------------------
        #  Schritt 5: Parameter eliminieren → Ortskurve
        # ----------------------------------------------------------
        s5_lab = MathTex(
            r"\textbf{5. Parameter eliminieren:}",
            font_size=24, color=GREY_3B1B,
        )
        s5_lab.next_to(header, DOWN, aligned_edge=LEFT, buff=0.35)

        s5_intro = MathTex(
            r"\text{Aus } T(t \mid -2t^3) \text{ lesen wir ab:}",
            font_size=24,
        )
        s5_intro.next_to(s5_lab, DOWN, aligned_edge=LEFT, buff=0.2)

        s5_eq1 = MathTex(r"x = t", r"\quad\Rightarrow\quad", r"t = x",
                         font_size=28, color=RED_3B1B)
        s5_eq1.next_to(s5_intro, DOWN, aligned_edge=LEFT, buff=0.15)

        s5_sub = MathTex(r"\text{Einsetzen in } y = -2t^3:", font_size=24)
        s5_sub.next_to(s5_eq1, DOWN, aligned_edge=LEFT, buff=0.2)

        s5_result1 = MathTex(r"y = -2(x)^3 = -2x^3", font_size=28, color=YELLOW_3B1B)
        s5_result1.next_to(s5_sub, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(s5_lab))
        self.play(Write(s5_intro))
        self.play(Write(s5_eq1))
        self.wait(0.3)
        self.play(Write(s5_sub))
        self.play(Write(s5_result1))
        self.wait(0.5)

        # Probe mit Hochpunkt
        s5_probe = MathTex(
            r"\text{Probe mit } H(-t \mid 2t^3):",
            font_size=24,
        )
        s5_probe.next_to(s5_result1, DOWN, aligned_edge=LEFT, buff=0.3)

        s5_eq2 = MathTex(r"x = -t", r"\;\Rightarrow\;", r"t = -x",
                         font_size=28, color=GREEN_3B1B)
        s5_eq2.next_to(s5_probe, DOWN, aligned_edge=LEFT, buff=0.15)

        s5_result2 = MathTex(
            r"y = 2t^3 = 2(-x)^3 = -2x^3 \;\checkmark",
            font_size=28, color=YELLOW_3B1B,
        )
        s5_result2.next_to(s5_eq2, DOWN, aligned_edge=LEFT, buff=0.15)

        self.play(Write(s5_probe))
        self.play(Write(s5_eq2))
        self.play(Write(s5_result2))
        self.wait(0.8)

        # ----------------------------------------------------------
        #  Endergebnis hervorheben
        # ----------------------------------------------------------
        final_box_content = MathTex(
            r"\text{Ortskurve: } y = -2x^3",
            font_size=36, color=YELLOW_3B1B,
        )
        final_box_content.next_to(s5_result2, DOWN, buff=0.5)
        final_box_content.shift(LEFT * 0.5)
        final_box = SurroundingRectangle(
            final_box_content, color=YELLOW_3B1B, stroke_width=2.5, buff=0.2,
        )

        self.play(Write(final_box_content), Create(final_box), run_time=1.5)
        self.wait(2.5)

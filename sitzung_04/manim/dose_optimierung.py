"""
Manim-Animation: Zylindrische Dose — Minimale Oberflaече
Zeigt, wie sich Radius und Hoehe bei konstantem Volumen aendern
und wo die Oberflaeche minimal wird.

Rendern mit:
    source ../../.venv/bin/activate
    manim -pql dose_optimierung.py DoseOptimierung
    manim -pqh dose_optimierung.py DoseOptimierung   # 1080p
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

# Physikalische Konstanten
V = 500  # Volumen in cm^3
# h = V / (pi * r^2)
# O(r) = 2*pi*r^2 + 2*pi*r*h = 2*pi*r^2 + 2V/r = 2*pi*r^2 + 1000/r
# O'(r) = 4*pi*r - 1000/r^2 = 0  =>  r^3 = 250/pi  =>  r_opt ≈ 4.3 cm
R_OPT = (250 / np.pi) ** (1 / 3)  # ≈ 4.301


def h_of_r(r):
    """Hoehe aus Volumen-Nebenbedingung."""
    return V / (np.pi * r**2)


def O_of_r(r):
    """Oberflaeche als Funktion von r."""
    return 2 * np.pi * r**2 + 2 * V / r


class DoseOptimierung(Scene):
    def construct(self):
        # ============================================================
        # 1) Titel
        # ============================================================
        titel = Tex(
            r"Zylindrische Dose --- Minimale Oberfl\"ache",
            font_size=44,
            color=WHITE,
        )
        titel_bg = BackgroundRectangle(titel, fill_opacity=0.8, buff=0.2)
        self.play(FadeIn(titel_bg), Write(titel), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(titel_bg), FadeOut(titel))

        # ============================================================
        # 2) Layout: Zylinder links, Graph rechts
        # ============================================================

        # --- ValueTracker fuer den Radius ---
        r_min, r_max = 2.0, 8.0
        r_tracker = ValueTracker(r_min)

        # --- Rechte Seite: Graph O(r) ---
        axes = Axes(
            x_range=[1, 9, 1],
            y_range=[0, 700, 100],
            x_length=5.5,
            y_length=5,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
                "color": GREY_3B1B,
                "stroke_width": 1.5,
                "tick_size": 0.05,
            },
            tips=True,
        ).shift(RIGHT * 3)

        axes_label_x = axes.get_x_axis_label(
            MathTex(r"r", font_size=28), edge=RIGHT, direction=DOWN, buff=0.2
        )
        axes_label_y = axes.get_y_axis_label(
            MathTex(r"O(r)", font_size=28), edge=UP, direction=LEFT, buff=0.2
        )

        graph = axes.plot(
            O_of_r, x_range=[1.8, 8.5], color=BLUE_3B1B, stroke_width=3
        )

        formel = MathTex(
            r"O(r) = 2\pi r^2 + \frac{1000}{r}",
            font_size=26,
            color=BLUE_3B1B,
        ).next_to(axes, UP, buff=0.25)
        formel_bg = BackgroundRectangle(formel, fill_opacity=0.7, buff=0.12)

        # Roter Punkt auf der Kurve
        dot_graph = always_redraw(
            lambda: Dot(
                axes.c2p(r_tracker.get_value(), O_of_r(r_tracker.get_value())),
                color=RED_3B1B,
                radius=0.08,
                z_index=5,
            )
        )

        # O-Wert Label am Punkt
        dot_label = always_redraw(
            lambda: MathTex(
                rf"O \approx {O_of_r(r_tracker.get_value()):.0f}",
                font_size=20,
                color=RED_3B1B,
            ).next_to(
                axes.c2p(r_tracker.get_value(), O_of_r(r_tracker.get_value())),
                UR,
                buff=0.15,
            )
        )

        # --- Linke Seite: Zylinder-Seitenansicht ---
        # Skalierung: 1 cm -> scale_factor Manim-Einheiten
        CYL_CENTER = LEFT * 3.5
        SCALE = 0.15  # Manim-Einheiten pro cm

        def build_cylinder(r_val):
            """Erzeugt die Zylinder-Seitenansicht (Rechteck + Ellipsen)."""
            h_val = h_of_r(r_val)
            w = r_val * SCALE * 2  # Breite in Manim-Einheiten
            h_draw = h_val * SCALE  # Hoehe in Manim-Einheiten

            # Begrenzung fuer die Darstellung
            w = np.clip(w, 0.3, 5.0)
            h_draw = np.clip(h_draw, 0.3, 5.0)

            # Rechteck (Mantelflaeche)
            rect = Rectangle(
                width=w,
                height=h_draw,
                color=BLUE_3B1B,
                fill_color=BLUE_3B1B,
                fill_opacity=0.15,
                stroke_width=2.5,
            ).move_to(CYL_CENTER)

            # Ellipsen oben und unten (Deckel/Boden)
            ellipse_h = w * 0.25  # Ellipsen-Hoehe fuer 3D-Effekt
            top_ellipse = Ellipse(
                width=w,
                height=ellipse_h,
                color=BLUE_3B1B,
                stroke_width=2.5,
            ).move_to(rect.get_top())

            bot_ellipse = Ellipse(
                width=w,
                height=ellipse_h,
                color=BLUE_3B1B,
                stroke_width=2.5,
            ).move_to(rect.get_bottom())

            # Gestrichelte hintere Haelfte der unteren Ellipse
            bot_back = DashedVMobject(
                Ellipse(width=w, height=ellipse_h, color=BLUE_3B1B, stroke_width=1.5),
                num_dashes=12,
            ).move_to(rect.get_bottom())

            return VGroup(rect, bot_back, bot_ellipse, top_ellipse)

        def build_labels(r_val):
            """Beschriftungen r und h."""
            h_val = h_of_r(r_val)
            w = np.clip(r_val * SCALE * 2, 0.3, 5.0)
            h_draw = np.clip(h_val * SCALE, 0.3, 5.0)

            # r-Pfeil (horizontaler Radius oben)
            r_start = CYL_CENTER + UP * h_draw / 2
            r_end = r_start + RIGHT * w / 2
            r_arrow = DoubleArrow(
                r_start, r_end,
                buff=0,
                color=YELLOW_3B1B,
                stroke_width=2,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.4,
            )
            r_text = MathTex(
                rf"r = {r_val:.1f}",
                font_size=22,
                color=YELLOW_3B1B,
            ).next_to(r_arrow, UP, buff=0.1)

            # h-Pfeil (vertikal rechts)
            h_top = CYL_CENTER + UP * h_draw / 2 + RIGHT * w / 2 + RIGHT * 0.25
            h_bot = CYL_CENTER + DOWN * h_draw / 2 + RIGHT * w / 2 + RIGHT * 0.25
            h_arrow = DoubleArrow(
                h_bot, h_top,
                buff=0,
                color=ORANGE_3B1B,
                stroke_width=2,
                tip_length=0.15,
                max_tip_length_to_length_ratio=0.4,
            )
            h_text = MathTex(
                rf"h = {h_val:.1f}",
                font_size=22,
                color=ORANGE_3B1B,
            ).next_to(h_arrow, RIGHT, buff=0.1)

            return VGroup(r_arrow, r_text, h_arrow, h_text)

        # always_redraw Zylinder und Labels
        cylinder = always_redraw(lambda: build_cylinder(r_tracker.get_value()))
        cyl_labels = always_redraw(lambda: build_labels(r_tracker.get_value()))

        # Volumen-Hinweis
        vol_text = MathTex(
            r"V = \pi r^2 h = 500\,\text{cm}^3",
            font_size=24,
            color=WHITE,
        ).move_to(CYL_CENTER + DOWN * 3.2)
        vol_bg = BackgroundRectangle(vol_text, fill_opacity=0.7, buff=0.1)

        # ============================================================
        # 3) Alles einblenden
        # ============================================================
        self.play(
            Create(axes),
            Write(axes_label_x),
            Write(axes_label_y),
            run_time=1,
        )
        self.play(
            Create(graph),
            FadeIn(formel_bg),
            Write(formel),
            run_time=1.5,
        )
        self.play(
            FadeIn(cylinder),
            FadeIn(cyl_labels),
            FadeIn(dot_graph),
            FadeIn(dot_label),
            FadeIn(vol_bg),
            Write(vol_text),
            run_time=1,
        )
        self.wait(0.5)

        # ============================================================
        # 4) Animation: r von klein nach optimal
        # ============================================================
        self.play(
            r_tracker.animate.set_value(R_OPT),
            run_time=4,
            rate_func=smooth,
        )
        self.wait(0.5)

        # --- Minimum markieren ---
        star = Star(
            n=5,
            outer_radius=0.2,
            inner_radius=0.1,
            color=GREEN_3B1B,
            fill_opacity=1,
            fill_color=GREEN_3B1B,
            z_index=10,
        ).move_to(axes.c2p(R_OPT, O_of_r(R_OPT)))

        min_text = MathTex(
            r"\text{Minimum: } h = 2r",
            font_size=26,
            color=GREEN_3B1B,
        ).next_to(star, DOWN + LEFT, buff=0.25)
        min_bg = BackgroundRectangle(min_text, fill_opacity=0.8, buff=0.12)

        self.play(FadeIn(star, scale=2), run_time=0.6)
        self.play(FadeIn(min_bg), Write(min_text), run_time=1)
        self.wait(1.5)

        # ============================================================
        # 5) Weiterfahren bis r gross
        # ============================================================
        self.play(
            r_tracker.animate.set_value(r_max),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(0.5)

        # ============================================================
        # 6) Zurueck zum Optimum
        # ============================================================
        self.play(
            r_tracker.animate.set_value(R_OPT),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(2)

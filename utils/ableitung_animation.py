"""
Utility-Mixin: Potenzregel-Ableitung animieren.

Nutzung in einer Manim-Szene:

    from utils.ableitung_animation import AbleitungMixin

    class MeineScene(AbleitungMixin, Scene):
        def construct(self):
            mobs = self.animate_potenzregel(coeff=2, exp=3, position=ORIGIN)
            self.play(FadeOut(mobs))
"""

from manim import *

# 3b1b-Farbpalette
BLUE_3B1B = "#58C4DD"
YELLOW_3B1B = "#FFFF00"
GREEN_3B1B = "#83C167"
RED_3B1B = "#FC6255"
GREY_3B1B = "#888888"
ORANGE_3B1B = "#FF8C00"


class AbleitungMixin:
    """Mixin für Manim-Szenen: animiert Ableitungen mit der Potenzregel."""

    def animate_potenzregel(
        self,
        coeff: int,
        exp: int,
        position=ORIGIN,
        font_size: int = 48,
        show_labels: bool = True,
        wait_time: float = 0.5,
    ) -> VGroup:
        """
        Animiert die Ableitung eines Monoms  coeff · x^exp  nach der Potenzregel.

        Ein-Schritt-Animation:
            Zeile 1:  f(x) = ax^n         (oben, bleibt stehen)
                         ↓  Formel „fällt" herunter, dabei:
                            • Exponent n spaltet sich: Kopie fliegt zum Koeff,
                              Original wird zu n-1
                            • Exponent-Kopie verschmilzt mit Koeff → n·a
            Zeile 2:  f'(x) = (n·a) x^{n-1}  (unten, Ergebnis)

        Returns:
            VGroup mit line1 und line2 (zum Aufräumen / FadeOut).
        """
        new_coeff = coeff * exp
        new_exp = exp - 1
        all_mobs = VGroup()
        coeff_str = self._coeff_str(coeff)
        has_visible_coeff = abs(coeff) != 1

        # ── Zeile 1: Originalterm ──────────────────────────────
        if show_labels:
            line1 = MathTex(
                "f(x)", "=", coeff_str, "x", f"^{{{exp}}}",
                font_size=font_size,
            )
            line1[0].set_color(BLUE_3B1B)
            ci, xi, ei = 2, 3, 4
        else:
            line1 = MathTex(
                coeff_str, "x", f"^{{{exp}}}",
                font_size=font_size,
            )
            ci, xi, ei = 0, 1, 2

        line1.move_to(position)
        all_mobs.add(line1)

        self.play(Write(line1))
        self.wait(0.3)

        # Exponent hervorheben
        self.play(line1[ei].animate.set_color(YELLOW_3B1B))
        self.wait(0.2)

        # ── Zeile 2 (Ergebnis) aufbauen ───────────────────────
        line2, l2_ci, l2_xi, l2_ei = self._build_result_line(
            new_coeff, new_exp, show_labels, font_size,
        )
        line2.next_to(line1, DOWN, buff=1.2)
        # Koeffizient zunächst unsichtbar — wird durch Merge enthüllt
        line2[l2_ci].set_opacity(0)
        all_mobs.add(line2)

        # ── Ghost-Objekte für die Verschmelzung ───────────────
        # Merge-Ziel: sieht aus wie der finale Koeffizient
        merge_target = line2[l2_ci].copy().set_opacity(1).set_color(GREEN_3B1B)

        exp_ghost = MathTex(str(exp), font_size=font_size, color=YELLOW_3B1B)
        exp_ghost.move_to(line1[ei])
        self.add(exp_ghost)

        if has_visible_coeff:
            coeff_ghost = line1[ci].copy()
            self.add(coeff_ghost)

        # ── Haupt-Animation: Formel fällt herunter ────────────
        # Ghosts transformieren sich WÄHREND des Fallens zum Ergebnis —
        # wenn alles unten ankommt, ist die Verschmelzung bereits fertig.
        anims = [
            Transform(exp_ghost, merge_target),
        ]
        if has_visible_coeff:
            anims.append(Transform(coeff_ghost, merge_target.copy()))

        # Strukturteile kopieren sich nach unten
        if show_labels:
            anims.append(TransformFromCopy(line1[0], line2[0]))   # f(x) → f'(x)
            anims.append(TransformFromCopy(line1[1], line2[1]))   # =  → =

        if l2_xi is not None:
            anims.append(TransformFromCopy(line1[xi], line2[l2_xi]))  # x → x

        if l2_ei is not None:
            anims.append(TransformFromCopy(line1[ei], line2[l2_ei]))  # ^n → ^{n-1}

        self.play(*anims, run_time=2)

        # Ghost NICHT entfernen — er IST jetzt der sichtbare Koeffizient.
        # Nur den zweiten Ghost (coeff_ghost) entfernen, da er deckungsgleich ist.
        if has_visible_coeff:
            self.remove(coeff_ghost)
        all_mobs.add(exp_ghost)

        self.wait(wait_time)
        return all_mobs

    # ── Hilfsfunktionen ───────────────────────────────────────

    @staticmethod
    def _coeff_str(c: int) -> str:
        """Koeffizient als String (1 → '', -1 → '-')."""
        if c == 1:
            return ""
        if c == -1:
            return "-"
        return str(c)

    @staticmethod
    def _build_result_line(
        new_coeff: int,
        new_exp: int,
        show_labels: bool,
        font_size: int,
    ) -> tuple:
        """
        Baut die Ergebnis-Zeile  f'(x) = (n·a) x^{n-1}.

        Returns:
            (MathTex, coeff_idx, x_idx_or_None, exp_idx_or_None)
        """
        nc = str(new_coeff)

        if show_labels:
            if new_exp == 0:
                line = MathTex("f'(x)", "=", nc, font_size=font_size)
                ci, xi, ei = 2, None, None
            elif new_exp == 1:
                line = MathTex("f'(x)", "=", nc, "x", font_size=font_size)
                ci, xi, ei = 2, 3, None
            else:
                line = MathTex(
                    "f'(x)", "=", nc, "x", f"^{{{new_exp}}}",
                    font_size=font_size,
                )
                ci, xi, ei = 2, 3, 4
            line[0].set_color(RED_3B1B)
        else:
            if new_exp == 0:
                line = MathTex(nc, font_size=font_size)
                ci, xi, ei = 0, None, None
            elif new_exp == 1:
                line = MathTex(nc, "x", font_size=font_size)
                ci, xi, ei = 0, 1, None
            else:
                line = MathTex(nc, "x", f"^{{{new_exp}}}", font_size=font_size)
                ci, xi, ei = 0, 1, 2

        return line, ci, xi, ei

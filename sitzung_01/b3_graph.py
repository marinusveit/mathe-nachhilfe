"""Erzeugt die Grafik f'(x) für Aufgabe B3 des Diagnosetests."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['mathtext.fontset'] = 'cm'

fig, ax = plt.subplots(figsize=(6, 4))

x = np.linspace(-1.5, 5.5, 400)
y = 4 * x - x**2  # f'(x) = 4x - x^2 = -x(x-4)

ax.plot(x, y, linewidth=2.2, color='#1f77b4', label=r"$f'(x)$")
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)

ax.set_xticks([-1, 0, 1, 2, 3, 4, 5])
ax.set_yticks([-4, -2, 0, 2, 4])
ax.set_xlim(-1.5, 5.5)
ax.set_ylim(-6, 5)
ax.grid(True, linestyle=':', alpha=0.5)
ax.set_xlabel('x')
ax.legend(loc='upper left')
ax.set_title(r"Graph von $f'(x)$ (nicht $f$!)")

plt.tight_layout()
output_path = Path(__file__).with_name("b3_graph.png")
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f"saved {output_path}")

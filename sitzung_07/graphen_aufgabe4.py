"""
Erzeugt die Graphen für Aufgabe 4 des Diagnosetests (Sitzung 7).

Funktion: f(x) = x²(4−x)² / 4
  → Nullstellen bei x = 0 und x = 4, Maximum bei x = 2 mit f(2) = 4

f'(x) = x(4−x)(2−x)
  → Nullstellen bei x = 0, 2, 4; VZW von + nach − bei x = 2

f''(x) = 3x² − 12x + 8
  → Nach oben geöffnete Parabel, Minimum bei x = 2 mit f''(2) = −4

Zuordnung (nicht im Diagnosetest verraten!):
  Graph A = f''   |   Graph B = f   |   Graph C = f'
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 11

x = np.linspace(-1, 5, 500)

# f(x) = x²(4-x)² / 4
f = x**2 * (4 - x)**2 / 4

# f'(x) = x(4-x)(2-x)
f_prime = x * (4 - x) * (2 - x)

# f''(x) = 3x² - 12x + 8
f_double_prime = 3 * x**2 - 12 * x + 8

# Zuordnung: A = f'', B = f, C = f'
graphs = [
    ("Graph A", f_double_prime),
    ("Graph B", f),
    ("Graph C", f_prime),
]

fig, axes = plt.subplots(1, 3, figsize=(14, 4))

for ax, (title, y) in zip(axes, graphs):
    ax.plot(x, y, color='#2d70b3', linewidth=2)
    ax.axhline(0, color='black', linewidth=0.6)
    ax.axvline(0, color='black', linewidth=0.6)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    ax.set_xlim(-1, 5)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('auto')

# y-Limits individuell anpassen
axes[0].set_ylim(-6, 15)   # f''
axes[1].set_ylim(-1, 5.5)  # f
axes[2].set_ylim(-5, 5)    # f'

fig.tight_layout()

out = Path(__file__).parent / "graphen_aufgabe4.png"
fig.savefig(out, dpi=200, bbox_inches='tight')
print(f"Gespeichert: {out}")

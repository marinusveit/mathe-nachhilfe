"""
Generates static PNGs for rezepte visualisations.
Run: python generate_plots.py
Output: PNG files in the same directory.
Convention (siehe CLAUDE.md): mathtext.fontset='cm', LaTeX in Legenden.
"""
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.family'] = 'serif'

OUT = Path(__file__).parent


def plot_graphen_zuordnen():
    x = np.linspace(-2.2, 2.2, 400)
    f = x**3 - 3 * x
    fp = 3 * x**2 - 3
    fpp = 6 * x
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.8), sharex=True)
    data = [(f, r'$f(x) = x^3 - 3x$'),
            (fp, r"$f'(x) = 3x^2 - 3$"),
            (fpp, r"$f''(x) = 6x$")]
    for ax, (y, title) in zip(axes, data):
        ax.plot(x, y, linewidth=2)
        ax.axhline(0, color='black', linewidth=0.6)
        ax.axvline(0, color='black', linewidth=0.6)
        ax.grid(True, alpha=0.3)
        ax.set_title(title, fontsize=13)
        ax.set_ylim(-6, 6)
    plt.tight_layout()
    plt.savefig(OUT / 'graphen_zuordnen.png', dpi=120, bbox_inches='tight')
    plt.close()


def plot_gebrochen_rational():
    def f(x):
        return (x**2 + 1) / (x**2 - 4)
    x_left = np.linspace(-5, -2.05, 300)
    x_mid = np.linspace(-1.95, 1.95, 300)
    x_right = np.linspace(2.05, 5, 300)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(x_left, f(x_left), 'C0', linewidth=2)
    ax.plot(x_mid, f(x_mid), 'C0', linewidth=2,
            label=r'$f(x) = \dfrac{x^2 + 1}{x^2 - 4}$')
    ax.plot(x_right, f(x_right), 'C0', linewidth=2)
    ax.axvline(-2, color='red', linestyle='--', alpha=0.7,
               label=r'senkrechte Asymptoten $x = \pm 2$')
    ax.axvline(2, color='red', linestyle='--', alpha=0.7)
    ax.axhline(1, color='green', linestyle='--', alpha=0.7,
               label=r'waagrechte Asymptote $y = 1$')
    ax.axhline(0, color='black', linewidth=0.6)
    ax.axvline(0, color='black', linewidth=0.6)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-8, 8)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=11)
    plt.tight_layout()
    plt.savefig(OUT / 'gebrochen_rational.png', dpi=120, bbox_inches='tight')
    plt.close()


def plot_umkehrfunktion():
    x1 = np.linspace(-2, 2.5, 400)
    x2 = np.linspace(0.05, 7, 400)
    fig, ax = plt.subplots(figsize=(6.5, 6.5))
    ax.plot(x1, np.exp(x1), 'C0', linewidth=2, label=r'$f(x) = e^x$')
    ax.plot(x2, np.log(x2), 'C2', linewidth=2, label=r'$f^{-1}(x) = \ln(x)$')
    diag = np.linspace(-2, 7, 10)
    ax.plot(diag, diag, color='gray', linestyle='--', alpha=0.7,
            label=r'$y = x$ (Spiegelachse)')
    ax.axhline(0, color='black', linewidth=0.6)
    ax.axvline(0, color='black', linewidth=0.6)
    ax.set_xlim(-2, 7)
    ax.set_ylim(-2, 7)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right', fontsize=11)
    plt.tight_layout()
    plt.savefig(OUT / 'umkehrfunktion.png', dpi=120, bbox_inches='tight')
    plt.close()


def plot_rotationsvolumen():
    fig = plt.figure(figsize=(10, 4.5))

    ax1 = fig.add_subplot(121)
    x = np.linspace(0, 4, 400)
    y = np.sqrt(x)
    ax1.plot(x, y, 'C0', linewidth=2, label=r'$f(x) = \sqrt{x}$')
    ax1.fill_between(x, 0, y, alpha=0.3, color='C0')
    ax1.axhline(0, color='black', linewidth=0.8)
    ax1.axvline(0, color='black', linewidth=0.8)
    ax1.set_xlim(-0.3, 4.3)
    ax1.set_ylim(-2.3, 2.3)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend(fontsize=11)
    ax1.set_title('Fläche unter dem Graphen')

    ax2 = fig.add_subplot(122, projection='3d')
    u = np.linspace(0, 4, 60)
    v = np.linspace(0, 2 * np.pi, 60)
    U, V = np.meshgrid(u, v)
    X = U
    Y = np.sqrt(U) * np.cos(V)
    Z = np.sqrt(U) * np.sin(V)
    ax2.plot_surface(X, Y, Z, alpha=0.7, color='C0', edgecolor='none')
    ax2.set_xlabel(r'$x$')
    ax2.set_ylabel(r'$y$')
    ax2.set_zlabel(r'$z$')
    ax2.set_title(r'Rotationskörper um $x$-Achse')

    plt.tight_layout()
    plt.savefig(OUT / 'rotationsvolumen.png', dpi=120, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    plot_graphen_zuordnen()
    plot_gebrochen_rational()
    plot_umkehrfunktion()
    plot_rotationsvolumen()
    print('Generated 4 PNGs in', OUT)

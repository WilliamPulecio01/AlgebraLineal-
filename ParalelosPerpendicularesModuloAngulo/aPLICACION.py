"""
=============================================================
  APLICACIÓN PRÁCTICA: ANÁLISIS DE FUERZAS EN UNA ESTRUCTURA
  Equilibrio Estático de un Puente Colgante (simplificado)
=============================================================
Problema: Un punto de unión de un puente colgante soporta
  una carga vertical W = 500 N. Dos cables salen del punto
  con ángulos θ1 = 30° y θ2 = 45° respecto a la horizontal.
  Hallar las tensiones T1 y T2 en cada cable para que el
  sistema esté en equilibrio.

Bibliotecas: NumPy, Matplotlib, SciPy, SymPy
=============================================================
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
from scipy.linalg import solve
import sympy as sp

# ─────────────────────────────────────────────────────────────
#  DATOS DEL PROBLEMA
# ─────────────────────────────────────────────────────────────
W = 500.0          # Carga en Newtons (vertical, hacia abajo)
theta1_deg = 30.0  # Ángulo del cable 1 con la horizontal (°)
theta2_deg = 45.0  # Ángulo del cable 2 con la horizontal (°)

theta1 = np.radians(theta1_deg)
theta2 = np.radians(theta2_deg)

print("="*65)
print("   APLICACIÓN PRÁCTICA: EQUILIBRIO DE FUERZAS EN PUENTE")
print("="*65)
print(f"\n  Carga vertical: W = {W} N")
print(f"  Ángulo cable 1: θ₁ = {theta1_deg}°")
print(f"  Ángulo cable 2: θ₂ = {theta2_deg}°")

# ─────────────────────────────────────────────────────────────
#  PLANTEAMIENTO VECTORIAL
#  Condición de equilibrio: ΣF = 0
#  → T1·cos(θ1) - T2·cos(θ2) = 0       [eje X]
#  → T1·sin(θ1) + T2·sin(θ2) - W = 0   [eje Y]
# ─────────────────────────────────────────────────────────────
print("\n" + "-"*65)
print("  PLANTEAMIENTO MATRICIAL (AX = b)")
print("-"*65)

# Matriz de coeficientes A y vector b
A = np.array([
    [ np.cos(theta1), -np.cos(theta2)],
    [ np.sin(theta1),  np.sin(theta2)]
])
b = np.array([0.0, W])

print(f"\n  Matriz A:\n{A}")
print(f"\n  Vector b: {b}")

# ─────────────────────────────────────────────────────────────
#  SOLUCIÓN CON SCIPY
# ─────────────────────────────────────────────────────────────
print("\n" + "-"*65)
print("  SOLUCIÓN CON SCIPY (scipy.linalg.solve)")
print("-"*65)

T = solve(A, b)
T1, T2 = T

print(f"\n  T1 (cable 30°) = {T1:.4f} N")
print(f"  T2 (cable 45°) = {T2:.4f} N")

# ─────────────────────────────────────────────────────────────
#  VERIFICACIÓN CON NUMPY
# ─────────────────────────────────────────────────────────────
print("\n" + "-"*65)
print("  VERIFICACIÓN CON NUMPY (np.linalg.solve)")
print("-"*65)

T_np = np.linalg.solve(A, b)
print(f"\n  T1 (NumPy) = {T_np[0]:.4f} N")
print(f"  T2 (NumPy) = {T_np[1]:.4f} N")
print(f"  Coincidencia con SciPy: {np.allclose(T, T_np)}")

# ─────────────────────────────────────────────────────────────
#  SOLUCIÓN SIMBÓLICA CON SYMPY
# ─────────────────────────────────────────────────────────────
print("\n" + "-"*65)
print("  SOLUCIÓN SIMBÓLICA CON SYMPY")
print("-"*65)

T1s, T2s = sp.symbols('T1 T2', positive=True)
theta1_s = sp.Rational(30) * sp.pi / 180
theta2_s = sp.Rational(45) * sp.pi / 180
Ws = sp.Integer(500)

eq1 = sp.Eq(T1s * sp.cos(theta1_s) - T2s * sp.cos(theta2_s), 0)
eq2 = sp.Eq(T1s * sp.sin(theta1_s) + T2s * sp.sin(theta2_s), Ws)

print(f"\n  Ecuación 1: {eq1}")
print(f"  Ecuación 2: {eq2}")

sol = sp.solve([eq1, eq2], [T1s, T2s])
print(f"\n  Solución exacta:")
print(f"  T1 = {sol[T1s]} ≈ {float(sol[T1s]):.4f} N")
print(f"  T2 = {sol[T2s]} ≈ {float(sol[T2s]):.4f} N")

# ─────────────────────────────────────────────────────────────
#  VECTORES DE FUERZA
# ─────────────────────────────────────────────────────────────
print("\n" + "-"*65)
print("  VECTORES DE FUERZA RESULTANTES")
print("-"*65)

# Cable 1: va hacia arriba-izquierda
F1 = np.array([-T1 * np.cos(theta1), T1 * np.sin(theta1)])
# Cable 2: va hacia arriba-derecha
F2 = np.array([ T2 * np.cos(theta2), T2 * np.sin(theta2)])
# Carga
Fw = np.array([0.0, -W])

print(f"\n  F1 (cable 30°) = [{F1[0]:.4f}, {F1[1]:.4f}] N")
print(f"  F2 (cable 45°) = [{F2[0]:.4f}, {F2[1]:.4f}] N")
print(f"  Fw (carga)     = [{Fw[0]:.4f}, {Fw[1]:.4f}] N")

F_resultante = F1 + F2 + Fw
print(f"\n  Resultante (debe ser ≈ 0): [{F_resultante[0]:.6f}, {F_resultante[1]:.6f}] N")
print(f"  |Resultante| = {np.linalg.norm(F_resultante):.6e} N  ✅ Equilibrio verificado")

# ─────────────────────────────────────────────────────────────
#  GRÁFICA
# ─────────────────────────────────────────────────────────────
print("\n" + "-"*65)
print("  GENERANDO GRÁFICA DE LA APLICACIÓN...")
print("-"*65)

fig, axes = plt.subplots(1, 2, figsize=(15, 7))
fig.suptitle("Aplicación Práctica: Equilibrio de Fuerzas en Puente Colgante",
             fontsize=14, fontweight='bold', y=1.01)

# ── SUBPLOT 1: Diagrama de cuerpo libre ──
ax1 = axes[0]
escala = 0.002  # escala de los vectores

origin = np.array([0, 0])
ax1.annotate('', xy=(F1[0]*escala, F1[1]*escala), xytext=origin,
             arrowprops=dict(arrowstyle='->', color='#e74c3c', lw=3,
                             mutation_scale=20))
ax1.text(F1[0]*escala*1.05, F1[1]*escala*1.0,
         f'T₁ = {T1:.1f} N\n(θ₁ = {theta1_deg}°)',
         color='#e74c3c', fontsize=11, fontweight='bold')

ax1.annotate('', xy=(F2[0]*escala, F2[1]*escala), xytext=origin,
             arrowprops=dict(arrowstyle='->', color='#3498db', lw=3,
                             mutation_scale=20))
ax1.text(F2[0]*escala*1.05, F2[1]*escala*1.0,
         f'T₂ = {T2:.1f} N\n(θ₂ = {theta2_deg}°)',
         color='#3498db', fontsize=11, fontweight='bold')

ax1.annotate('', xy=(0, -W*escala), xytext=origin,
             arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=3,
                             mutation_scale=20))
ax1.text(0.05, -W*escala, f'  W = {W:.0f} N', color='#2ecc71',
         fontsize=11, fontweight='bold')

# Punto de unión
ax1.plot(0, 0, 'ko', markersize=10, zorder=5)
ax1.text(0.05, 0.02, 'Punto de\nunión', fontsize=9, ha='left')

# Ejes de referencia
ax1.axhline(0, color='gray', lw=0.5, linestyle='--')
ax1.axvline(0, color='gray', lw=0.5, linestyle='--')
ax1.set_xlim(-1.3, 1.3)
ax1.set_ylim(-1.3, 1.3)
ax1.set_xlabel('Componente X (N × 10⁻² escala)', fontsize=10)
ax1.set_ylabel('Componente Y (N × 10⁻² escala)', fontsize=10)
ax1.set_title('Diagrama de Cuerpo Libre\nVectores de Fuerza', fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_aspect('equal')
leyenda = [
    mpatches.Patch(color='#e74c3c', label=f'T₁ = {T1:.2f} N'),
    mpatches.Patch(color='#3498db', label=f'T₂ = {T2:.2f} N'),
    mpatches.Patch(color='#2ecc71', label=f'W = {W:.0f} N'),
]
ax1.legend(handles=leyenda, loc='lower right', fontsize=10)

# ── SUBPLOT 2: Esquema del puente ──
ax2 = axes[1]
ax2.set_xlim(-3, 3)
ax2.set_ylim(-1.5, 3)
ax2.set_aspect('equal')
ax2.set_title('Esquema del Puente Colgante', fontweight='bold')
ax2.grid(True, alpha=0.2)

# Techo/anclajes
ax2.fill_between([-3, 3], [2.8, 2.8], [3.0, 3.0], color='#7f8c8d', alpha=0.8)
ax2.text(0, 2.9, 'ESTRUCTURA SUPERIOR', ha='center', va='center',
         fontsize=9, color='white', fontweight='bold')

# Cables
px, py = 0, 0  # Punto de unión
ax2.plot([px, -2.5], [py, 2.8], color='#e74c3c', lw=3, label=f'Cable 1 (T₁={T1:.1f} N)')
ax2.plot([px,  2.0], [py, 2.8], color='#3498db', lw=3, label=f'Cable 2 (T₂={T2:.1f} N)')

# Ángulos
import matplotlib.patches as patches
arc1 = patches.Arc((px, py), 0.8, 0.8, angle=0,
                   theta1=90, theta2=90+theta1_deg, color='#e74c3c', lw=1.5)
arc2 = patches.Arc((px, py), 0.6, 0.6, angle=0,
                   theta1=90-theta2_deg, theta2=90, color='#3498db', lw=1.5)
ax2.add_patch(arc1)
ax2.add_patch(arc2)
ax2.text(-0.55, 0.5, f'{theta1_deg}°', color='#e74c3c', fontsize=10, fontweight='bold')
ax2.text(0.2, 0.45, f'{theta2_deg}°', color='#3498db', fontsize=10, fontweight='bold')

# Nodo
circle = plt.Circle((px, py), 0.12, color='#2c3e50', zorder=5)
ax2.add_patch(circle)

# Carga vertical
ax2.annotate('', xy=(0, -1.2), xytext=(0, -0.15),
             arrowprops=dict(arrowstyle='->', color='#2ecc71', lw=2.5,
                             mutation_scale=18))
rect = plt.Rectangle((-0.6, -1.5), 1.2, 0.3, color='#27ae60', alpha=0.8)
ax2.add_patch(rect)
ax2.text(0, -1.35, f'W = {W:.0f} N', ha='center', va='center',
         color='white', fontsize=10, fontweight='bold')

ax2.legend(loc='lower left', fontsize=9)
ax2.set_xlabel('Posición (m)', fontsize=10)
ax2.set_ylabel('Altura (m)', fontsize=10)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/aplicacion_puente.png", dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ Gráfica guardada: aplicacion_puente.png")

# ─────────────────────────────────────────────────────────────
#  RESUMEN FINAL
# ─────────────────────────────────────────────────────────────
print("\n" + "="*65)
print("  RESUMEN DE RESULTADOS")
print("="*65)
print(f"\n  Tensión T1 en cable (θ₁=30°): {T1:.4f} N")
print(f"  Tensión T2 en cable (θ₂=45°): {T2:.4f} N")
print(f"  Carga soportada W:             {W:.4f} N")
print(f"\n  Verificación de equilibrio:")
print(f"    ΣFx = {F1[0]:.4f} + {F2[0]:.4f} = {F1[0]+F2[0]:.6f} ≈ 0 ✅")
print(f"    ΣFy = {F1[1]:.4f} + {F2[1]:.4f} - {W:.4f} = {F1[1]+F2[1]-W:.6f} ≈ 0 ✅")
print("\n  Bibliotecas usadas: NumPy, SciPy, SymPy, Matplotlib")
print("="*65)
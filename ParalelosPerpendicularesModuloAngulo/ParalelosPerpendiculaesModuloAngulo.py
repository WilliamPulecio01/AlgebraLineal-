"""
=============================================================
  EJERCICIOS DE VECTORES EN PYTHON
  Vectores: Paralelos, Perpendiculares, Módulo y Ángulo
=============================================================
Bibliotecas: NumPy, Matplotlib, SymPy
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import sympy as sp

# ─────────────────────────────────────────────────────────────
#  UTILIDADES
# ─────────────────────────────────────────────────────────────
def modulo(v):
    """Calcula el módulo (norma) de un vector."""
    return np.linalg.norm(v)

def angulo_entre(v1, v2, grados=True):
    """Calcula el ángulo entre dos vectores."""
    cos_theta = np.dot(v1, v2) / (modulo(v1) * modulo(v2))
    cos_theta = np.clip(cos_theta, -1.0, 1.0)  # Evitar errores numéricos
    theta = np.arccos(cos_theta)
    return np.degrees(theta) if grados else theta

def son_paralelos(v1, v2, tol=1e-9):
    """Comprueba si dos vectores son paralelos (producto cruzado ≈ 0)."""
    if len(v1) == 2:
        cross = abs(v1[0]*v2[1] - v1[1]*v2[0])
    else:
        cross = np.linalg.norm(np.cross(v1, v2))
    return cross < tol

def son_perpendiculares(v1, v2, tol=1e-9):
    """Comprueba si dos vectores son perpendiculares (producto punto ≈ 0)."""
    return abs(np.dot(v1, v2)) < tol

def encabezado(titulo):
    print("\n" + "="*60)
    print(f"  {titulo}")
    print("="*60)

def separador():
    print("-"*60)


# ═══════════════════════════════════════════════════════════════
#  SECCIÓN 1: VECTORES PARALELOS
# ═══════════════════════════════════════════════════════════════
encabezado("SECCIÓN 1: VECTORES PARALELOS")

paralelos = [
    (np.array([2, 4]), np.array([1, 2]),     "a=[2,4], b=[1,2]"),
    (np.array([3, -6, 9]), np.array([-1, 2, -3]), "a=[3,-6,9], b=[-1,2,-3]"),
    (np.array([5, 0]), np.array([-10, 0]),   "a=[5,0], b=[-10,0]"),
]

for i, (v1, v2, desc) in enumerate(paralelos, 1):
    separador()
    print(f"  Ejercicio P{i}: {desc}")
    print(f"  Vector a = {v1}")
    print(f"  Vector b = {v2}")
    if len(v1) == 2:
        cross = abs(v1[0]*v2[1] - v1[1]*v2[0])
        print(f"  Producto cruzado (escalar 2D) = {cross:.4f}")
    else:
        cross = np.cross(v1, v2)
        print(f"  Producto cruzado 3D = {cross}")
    resultado = son_paralelos(v1, v2)
    print(f"  ¿Son paralelos? → {'✅ SÍ' if resultado else '❌ NO'}")
    ang = angulo_entre(v1, v2)
    print(f"  Ángulo entre ellos = {ang:.2f}° (paralelos: 0° o 180°)")

# ═══════════════════════════════════════════════════════════════
#  SECCIÓN 2: VECTORES PERPENDICULARES
# ═══════════════════════════════════════════════════════════════
encabezado("SECCIÓN 2: VECTORES PERPENDICULARES")

perpendiculares = [
    (np.array([1, 0]), np.array([0, 1]),      "a=[1,0], b=[0,1]"),
    (np.array([3, 4]), np.array([-4, 3]),     "a=[3,4], b=[-4,3]"),
    (np.array([1, -2, 1]), np.array([2, 1, 0]), "a=[1,-2,1], b=[2,1,0]"),
]

for i, (v1, v2, desc) in enumerate(perpendiculares, 1):
    separador()
    print(f"  Ejercicio Perp{i}: {desc}")
    print(f"  Vector a = {v1}")
    print(f"  Vector b = {v2}")
    dot = np.dot(v1, v2)
    print(f"  Producto punto a·b = {dot:.4f}")
    resultado = son_perpendiculares(v1, v2)
    print(f"  ¿Son perpendiculares? → {'✅ SÍ' if resultado else '❌ NO'}")
    ang = angulo_entre(v1, v2)
    print(f"  Ángulo entre ellos = {ang:.2f}° (perpendiculares: 90°)")

# ═══════════════════════════════════════════════════════════════
#  SECCIÓN 3: MÓDULO DE VECTORES
# ═══════════════════════════════════════════════════════════════
encabezado("SECCIÓN 3: MÓDULO DE UN VECTOR")

modulos = [
    (np.array([3, 4]),        "v=[3,4]",      "√(3²+4²)=5"),
    (np.array([1, 2, 2]),     "v=[1,2,2]",    "√(1+4+4)=3"),
    (np.array([-5, 12]),      "v=[-5,12]",    "√(25+144)=13"),
]

for i, (v, desc, formula) in enumerate(modulos, 1):
    separador()
    print(f"  Ejercicio M{i}: {desc}")
    print(f"  Vector v = {v}")
    mod = modulo(v)
    print(f"  Fórmula: |v| = {formula}")
    print(f"  |v| con NumPy = {mod:.6f}")
    # Verificar con SymPy
    v_sym = sp.Matrix(v.tolist())
    mod_sym = sp.sqrt(sum(x**2 for x in v))
    print(f"  |v| con SymPy = {mod_sym} ≈ {float(mod_sym):.6f}")

# ═══════════════════════════════════════════════════════════════
#  SECCIÓN 4: ÁNGULO ENTRE DOS VECTORES
# ═══════════════════════════════════════════════════════════════
encabezado("SECCIÓN 4: ÁNGULO ENTRE DOS VECTORES")

angulos = [
    (np.array([1, 0]), np.array([0, 1]),   "a=[1,0], b=[0,1]"),
    (np.array([1, 1]), np.array([1, 0]),   "a=[1,1], b=[1,0]"),
    (np.array([2, 3, 1]), np.array([1, -1, 2]), "a=[2,3,1], b=[1,-1,2]"),
]

for i, (v1, v2, desc) in enumerate(angulos, 1):
    separador()
    print(f"  Ejercicio A{i}: {desc}")
    print(f"  Vector a = {v1}")
    print(f"  Vector b = {v2}")
    dot = np.dot(v1, v2)
    mag1, mag2 = modulo(v1), modulo(v2)
    cos_theta = dot / (mag1 * mag2)
    ang = angulo_entre(v1, v2)
    print(f"  a · b = {dot:.4f}")
    print(f"  |a| = {mag1:.4f},  |b| = {mag2:.4f}")
    print(f"  cos θ = (a·b)/(|a||b|) = {cos_theta:.6f}")
    print(f"  θ = arccos({cos_theta:.6f}) = {ang:.4f}°")


# ═══════════════════════════════════════════════════════════════
#  GRÁFICA RESUMEN
# ═══════════════════════════════════════════════════════════════
encabezado("GENERANDO GRÁFICA DE VECTORES...")

fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("Ejercicios de Vectores: Resumen Gráfico", fontsize=15, fontweight='bold', y=0.98)

colores = ['#e74c3c', '#3498db', '#2ecc71']

# --- Paralelos ---
ax = axes[0, 0]
pares_2d = [(np.array([2, 4]), np.array([1, 2])),
            (np.array([4, -2]), np.array([2, -1])),
            (np.array([5, 0]), np.array([-10, 0]))]

origins = [(0, 0), (2, 0), (0, 2)]
for idx, ((v1, v2), (ox, oy)) in enumerate(zip(pares_2d, origins)):
    sc = 0.4
    ax.annotate('', xy=(ox+v1[0]*sc, oy+v1[1]*sc), xytext=(ox, oy),
                arrowprops=dict(arrowstyle='->', color=colores[idx], lw=2))
    ax.annotate('', xy=(ox+v2[0]*sc, oy+v2[1]*sc), xytext=(ox, oy),
                arrowprops=dict(arrowstyle='->', color=colores[idx], lw=2, linestyle='dashed'))
    ax.text(ox+v1[0]*sc, oy+v1[1]*sc, f' P{idx+1}', color=colores[idx], fontsize=9)

ax.set_xlim(-2, 4); ax.set_ylim(-2, 4)
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.set_title("Vectores Paralelos", fontweight='bold')
ax.grid(True, alpha=0.3)
p = [mpatches.Patch(color=c, label=f'Par {i+1}') for i, c in enumerate(colores)]
ax.legend(handles=p, fontsize=8)

# --- Perpendiculares ---
ax = axes[0, 1]
pares_perp = [(np.array([1, 0]), np.array([0, 1])),
              (np.array([3, 4]), np.array([-4, 3])),
              (np.array([2, -1]), np.array([1, 2]))]

origins = [(0, 0), (0, 0), (0, 0)]
escalas = [1.0, 0.3, 0.8]
for idx, ((v1, v2), sc) in enumerate(zip(pares_perp, escalas)):
    ax.annotate('', xy=(v1[0]*sc, v1[1]*sc), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=colores[idx], lw=2))
    ax.annotate('', xy=(v2[0]*sc, v2[1]*sc), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=colores[idx], lw=2, linestyle='dashed'))

ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.set_title("Vectores Perpendiculares", fontweight='bold')
ax.grid(True, alpha=0.3)
p = [mpatches.Patch(color=c, label=f'Par {i+1} (90°)') for i, c in enumerate(colores)]
ax.legend(handles=p, fontsize=8)

# --- Módulos ---
ax = axes[1, 0]
vecs = [np.array([3, 4]), np.array([1, 2]), np.array([-5, 12])]
escalas_m = [1.0, 1.0, 0.2]
for idx, (v, sc) in enumerate(zip(vecs, escalas_m)):
    ax.annotate('', xy=(v[0]*sc, v[1]*sc), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=colores[idx], lw=2.5))
    mod_v = modulo(v)
    ax.text(v[0]*sc, v[1]*sc, f"  |v|={mod_v:.1f}", color=colores[idx], fontsize=9)

ax.set_xlim(-1.5, 4); ax.set_ylim(-0.5, 3)
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.set_title("Módulo de Vectores", fontweight='bold')
ax.grid(True, alpha=0.3)

# --- Ángulos ---
ax = axes[1, 1]
pairs_ang = [(np.array([1, 0]), np.array([0, 1])),
             (np.array([1, 1]), np.array([1, 0])),
             (np.array([2, 1]), np.array([-1, 2]))]

for idx, (v1, v2) in enumerate(pairs_ang):
    sc = 1.2
    v1n = v1 / modulo(v1) * sc
    v2n = v2 / modulo(v2) * sc
    ax.annotate('', xy=(v1n[0], v1n[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=colores[idx], lw=2))
    ax.annotate('', xy=(v2n[0], v2n[1]), xytext=(0, 0),
                arrowprops=dict(arrowstyle='->', color=colores[idx], lw=2, linestyle='dashed'))
    ang = angulo_entre(v1, v2)
    mid = (v1n + v2n) / 2 * 0.6
    ax.text(mid[0], mid[1], f"{ang:.1f}°", fontsize=8, color=colores[idx],
            ha='center', bbox=dict(boxstyle='round,pad=0.2', fc='white', alpha=0.7))

ax.set_xlim(-1.5, 1.5); ax.set_ylim(-0.5, 1.5)
ax.axhline(0, color='k', lw=0.5); ax.axvline(0, color='k', lw=0.5)
ax.set_title("Ángulo entre Vectores", fontweight='bold')
ax.grid(True, alpha=0.3)




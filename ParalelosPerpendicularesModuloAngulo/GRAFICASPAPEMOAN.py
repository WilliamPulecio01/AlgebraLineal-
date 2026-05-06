# ============================================================
# GRAFICACIÓN 3D DE VECTORES EN R3
# Paralelos, Perpendiculares, Módulo y Ángulo
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# FUNCIONES
# ============================================================

def dibujar_vectores_3d(v1, v2=None, titulo=""):
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')

    # Vector 1
    ax.quiver(0,0,0, v1[0], v1[1], v1[2], linewidth=2)

    # Vector 2 (si existe)
    if v2 is not None:
        ax.quiver(0,0,0, v2[0], v2[1], v2[2], linestyle='dashed', linewidth=2)

    # Límites
    lim = 10
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])
    ax.set_zlim([-lim, lim])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(titulo)

    plt.show()

# ============================================================
# PARALELOS
# ============================================================

def graficar_paralelos():
    vectores = [
        (np.array([2,4,6]), np.array([1,2,3])),
        (np.array([3,-6,9]), np.array([-1,2,-3])),
        (np.array([5,0,0]), np.array([-10,0,0]))
    ]

    for i, (v1, v2) in enumerate(vectores, 1):
        dibujar_vectores_3d(v1, v2, f"Paralelos {i}")

# ============================================================
# PERPENDICULARES
# ============================================================

def graficar_perpendiculares():
    vectores = [
        (np.array([1,0,0]), np.array([0,1,0])),
        (np.array([1,2,3]), np.array([2,-1,0])),
        (np.array([2,-2,1]), np.array([1,1,0]))
    ]

    for i, (v1, v2) in enumerate(vectores, 1):
        dibujar_vectores_3d(v1, v2, f"Perpendiculares {i}")

# ============================================================
# MÓDULO
# ============================================================

def graficar_modulos():
    vectores = [
        np.array([3,4,12]),
        np.array([1,2,2]),
        np.array([-5,12,0])
    ]

    for i, v in enumerate(vectores, 1):
        dibujar_vectores_3d(v, None, f"Módulo {i}")

# ============================================================
# ÁNGULO
# ============================================================

def graficar_angulos():
    vectores = [
        (np.array([1,0,0]), np.array([0,1,0])),
        (np.array([1,1,0]), np.array([1,0,0])),
        (np.array([2,3,1]), np.array([1,-1,2]))
    ]

    for i, (v1, v2) in enumerate(vectores, 1):
        dibujar_vectores_3d(v1, v2, f"Ángulo {i}")

# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    graficar_paralelos()
    graficar_perpendiculares()
    graficar_modulos()
    graficar_angulos()

    print("\nSe generaron todas las gráficas en 3D correctamente.")

# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    main()
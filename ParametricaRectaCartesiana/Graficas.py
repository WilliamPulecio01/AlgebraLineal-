# ============================================================
# GRAFICAS COMPLETAS: RECTAS + PLANOS + INTERSECCIÓN
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# FUNCION PARA GRAFICAR RECTAS
# ============================================================

def graficar_rectas():
    print("\nGraficando 5 rectas...")

    rectas = [
        ((1,2,3), (2,-1,1)),
        ((0,1,-1), (1,2,3)),
        ((2,0,1), (3,1,-2)),
        ((-1,2,0), (1,-1,2)),
        ((3,-2,1), (2,2,1))
    ]

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(-5,5,100)

    for i, (P, v) in enumerate(rectas):
        P = np.array(P)
        v = np.array(v)

        x = P[0] + v[0]*t
        y = P[1] + v[1]*t
        z = P[2] + v[2]*t

        ax.plot(x, y, z, label=f'Recta {i+1}')
        ax.scatter(P[0], P[1], P[2])

    ax.set_title("5 Rectas en R3")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.legend()
    plt.show()

# ============================================================
# FUNCION PARA GRAFICAR PLANO
# ============================================================

def graficar_plano(p1, p2, p3, titulo):

    print(f"\nGraficando {titulo}...")

    P = np.array(p1)
    Q = np.array(p2)
    R = np.array(p3)

    v1 = Q - P
    v2 = R - P

    normal = np.cross(v1, v2)

    xx, yy = np.meshgrid(np.linspace(-5,5,20), np.linspace(-5,5,20))

    # Evitar división por 0
    if normal[2] != 0:
        zz = (-normal[0]*(xx-P[0]) - normal[1]*(yy-P[1]))/normal[2] + P[2]
    else:
        zz = np.zeros_like(xx)

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(xx, yy, zz, alpha=0.5)

    # Puntos
    ax.scatter(P[0], P[1], P[2], label='P')
    ax.scatter(Q[0], Q[1], Q[2], label='Q')
    ax.scatter(R[0], R[1], R[2], label='R')

    ax.set_title(titulo)
    ax.legend()
    plt.show()

# ============================================================
# INTERSECCIÓN RECTA - PLANO
# ============================================================

def graficar_interseccion():

    print("\nGraficando intersección...")

    P = np.array([1,-1,2])
    v = np.array([1,2,3])
    Q = np.array([1,-1,1])

    t = np.linspace(-2,2,100)

    x = P[0] + v[0]*t
    y = P[1] + v[1]*t
    z = P[2] + v[2]*t

    # Plano
    normal = v  # perpendicular a N
    xx, yy = np.meshgrid(np.linspace(-5,5,20), np.linspace(-5,5,20))
    zz = (-normal[0]*(xx-Q[0]) - normal[1]*(yy-Q[1]))/normal[2] + Q[2]

    # Intersección (calculada)
    t0 = -1/3
    punto = P + t0*v

    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')

    # Recta
    ax.plot(x,y,z, label='Recta')

    # Plano
    ax.plot_surface(xx,yy,zz, alpha=0.5)

    # Punto intersección
    ax.scatter(punto[0], punto[1], punto[2],
               s=80, label='Intersección')

    ax.set_title("Intersección Recta - Plano")
    ax.legend()
    plt.show()

# ============================================================
# EJECUCIÓN
# ============================================================

graficar_rectas()

# Plano a
graficar_plano((1,-2,3),(4,6,1),(-2,1,1),"Plano a")

# Plano b
graficar_plano((1,-1,1),(2,3,5),(6,-4,3),"Plano b")

# Intersección
graficar_interseccion()
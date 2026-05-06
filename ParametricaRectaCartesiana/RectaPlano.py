# ============================================================
# TRABAJO: RECTAS Y PLANOS EN R3 (VERSIÓN COMPLETA EXPLICADA)
# ============================================================

import sympy as sp

x, y, z, t = sp.symbols('x y z t')

# ============================================================
# DEFINICIÓN: RECTAS
# ============================================================

print("\n" + "="*70)
print("DEFINICIÓN: ECUACIÓN PARAMÉTRICA DE LA RECTA")
print("="*70)
print("""
Una ecuación paramétrica de la recta en R3 permite representar todos los puntos
de una recta usando un punto inicial y un vector dirección.

Se expresa como:
r(t) = r0 + t*v

Donde:
- r0 es un punto de la recta
- v es el vector dirección
- t es un parámetro real
""")

# ============================================================
# 1. RECTAS EN R3
# ============================================================

print("\n" + "="*70)
print("1. RECTAS EN R3 - PASO A PASO")
print("="*70)

def recta_explicada(P, v):
    x0, y0, z0 = P
    a, b, c = v
    
    print("\n--------------------------------------------------")
    print(f"Punto: {P}")
    print(f"Vector dirección: {v}")
    
    print("\nPASO 1: Paramétricas")
    print(f"x = {x0} + {a}t")
    print(f"y = {y0} + {b}t")
    print(f"z = {z0} + {c}t")
    
    print("\nPASO 2: Despejar t")
    print(f"t = (x - {x0})/{a}")
    print(f"t = (y - {y0})/{b}")
    print(f"t = (z - {z0})/{c}")
    
    print("\nPASO 3: Forma cartesiana")
    print(f"(x - {x0})/{a} = (y - {y0})/{b} = (z - {z0})/{c}")
    
    print("\nINTERPRETACIÓN:")
    print("Describe todos los puntos de la recta en el espacio.")

rectas = [
    ((1,2,3), (2,-1,1)),
    ((0,1,-1), (1,2,3)),
    ((2,0,1), (3,1,-2)),
    ((-1,2,0), (1,-1,2)),
    ((3,-2,1), (2,2,1))
]

for i, (P, v) in enumerate(rectas, 1):
    print(f"\n=========== EJERCICIO {i} ===========")
    recta_explicada(P, v)

# ============================================================
# DEFINICIÓN: PLANO
# ============================================================

print("\n" + "="*70)
print("DEFINICIÓN: ECUACIÓN DEL PLANO")
print("="*70)
print("""
Un plano en R3 es una superficie definida por tres puntos no colineales.

Se obtiene calculando dos vectores en el plano y su producto cruz,
el cual genera un vector normal.

Ecuación general:
Ax + By + Cz + D = 0
""")

# ============================================================
# 2. PLANOS
# ============================================================

print("\n" + "="*70)
print("2. PLANOS - PASO A PASO")
print("="*70)

def plano_explicado(origen, p2, p3):
    O = sp.Matrix(origen)
    A = sp.Matrix(p2)
    B = sp.Matrix(p3)
    
    print("\n--------------------------------------------------")
    print(f"Origen: {origen}")
    
    print("\nPASO 1: Vectores del plano")
    v1 = A - O
    v2 = B - O
    print("v1:", v1)
    print("v2:", v2)
    
    print("\nPASO 2: Producto cruz")
    n = v1.cross(v2)
    print("Vector normal:", n)
    
    print("\nPASO 3: Ecuación del plano")
    eq = n[0]*(x-O[0]) + n[1]*(y-O[1]) + n[2]*(z-O[2])
    eq_s = sp.simplify(eq)
    print(eq_s, "= 0")
    
    print("\nINTERPRETACIÓN:")
    print("El vector normal es perpendicular al plano.")
    
    return eq_s

# Plano a
P = (1,-2,3)
Q = (4,6,1)
R = (-2,1,1)

print("\n=========== PLANO a ===========")
plano_explicado(P, Q, R)
plano_explicado(Q, P, R)
plano_explicado(R, P, Q)

# Plano b
S = (1,-1,1)
T = (2,3,5)
U = (6,-4,3)

print("\n=========== PLANO b ===========")
plano_explicado(S, T, U)
plano_explicado(T, S, U)
plano_explicado(U, S, T)

# ============================================================
# DEFINICIÓN: INTERSECCIÓN
# ============================================================

print("\n" + "="*70)
print("DEFINICIÓN: INTERSECCIÓN RECTA - PLANO")
print("="*70)
print("""
Consiste en encontrar el punto donde una recta corta un plano.

Se sustituye la recta en el plano y se resuelve el parámetro.
""")

# ============================================================
# 3. INTERSECCIÓN
# ============================================================

print("\n" + "="*70)
print("3. INTERSECCIÓN RECTA - PLANO")
print("="*70)

Q = (1,-1,1)
P = (1,-1,2)
N = (1,2,3)

print("\nPASO 1: Recta")
xr = P[0] + N[0]*t
yr = P[1] + N[1]*t
zr = P[2] + N[2]*t

print("x =", xr)
print("y =", yr)
print("z =", zr)

print("\nPASO 2: Sustituir en plano")
eq = N[0]*(xr - Q[0]) + N[1]*(yr - Q[1]) + N[2]*(zr - Q[2])
print(eq)

print("\nPASO 3: Resolver t")
sol = sp.solve(eq, t)
print("t =", sol)

print("\nPASO 4: Punto de intersección")
px = xr.subs(t, sol[0])
py = yr.subs(t, sol[0])
pz = zr.subs(t, sol[0])

print((px, py, pz))

print("\nINTERPRETACIÓN:")
print("Es el punto donde la recta intersecta el plano.")

# ============================================================
# REFLEXIÓN FINAL
# ============================================================

print("\n" + "="*70)
print("REFLEXIÓN FINAL")
print("="*70)
print("""
Al desarrollar este programa se pudo evidenciar que las ecuaciones de rectas
y planos son herramientas fundamentales en el análisis del espacio tridimensional.

El uso de Python permitió automatizar los cálculos y comprender mejor
los procedimientos matemáticos.

Además, estas herramientas tienen múltiples aplicaciones en áreas como
ingeniería, física y programación.

Esto demuestra la importancia de integrar matemáticas con programación.
""")

# ============================================================
print("\n" + "="*70)
print("PROGRAMA FINALIZADO")
print("="*70)
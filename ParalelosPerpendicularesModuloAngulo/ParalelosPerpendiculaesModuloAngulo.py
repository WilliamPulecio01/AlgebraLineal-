# ============================================================
# EJERCICIOS DE VECTORES EN R3 (PASO A PASO)
# Paralelos, Perpendiculares, Módulo y Ángulo
# ============================================================

import numpy as np

# ============================================================
# FUNCIONES BASE
# ============================================================

def modulo(v):
    """Calcula el módulo de un vector"""
    return np.linalg.norm(v)

def angulo(v1, v2):
    """Calcula el ángulo entre dos vectores en grados"""
    cos_theta = np.dot(v1, v2) / (modulo(v1) * modulo(v2))
    cos_theta = np.clip(cos_theta, -1, 1)
    return np.degrees(np.arccos(cos_theta))

def son_paralelos(v1, v2):
    """Dos vectores son paralelos si su producto cruz es cero"""
    cruz = np.cross(v1, v2)
    return np.allclose(cruz, [0,0,0])

def son_perpendiculares(v1, v2):
    """Dos vectores son perpendiculares si su producto punto es 0"""
    return np.isclose(np.dot(v1, v2), 0)

# ============================================================
# SECCIÓN 1: PARALELOS
# ============================================================

print("\n" + "="*60)
print("SECCIÓN 1: VECTORES PARALELOS")
print("="*60)

paralelos = [
    (np.array([2,4,6]), np.array([1,2,3])),
    (np.array([3,-6,9]), np.array([-1,2,-3])),
    (np.array([5,0,0]), np.array([-10,0,0]))
]

for i, (v1, v2) in enumerate(paralelos, 1):
    print("\n--- Ejercicio", i, "---")
    print("Vectores:")
    print("v1 =", v1)
    print("v2 =", v2)

    print("\nPaso 1: Calcular producto cruz")
    cruz = np.cross(v1, v2)
    print("v1 x v2 =", cruz)

    print("\nPaso 2: Analizar resultado")
    if son_paralelos(v1, v2):
        print("Los vectores SON paralelos (producto cruz = 0)")
    else:
        print("NO son paralelos")

    print("\nPaso 3: Ángulo")
    ang = angulo(v1, v2)
    print("Ángulo =", ang, "grados (paralelos: 0° o 180°)")

# ============================================================
# SECCIÓN 2: PERPENDICULARES
# ============================================================

print("\n" + "="*60)
print("SECCIÓN 2: VECTORES PERPENDICULARES")
print("="*60)

perp = [
    (np.array([1,0,0]), np.array([0,1,0])),
    (np.array([1,2,3]), np.array([2,-1,0])),
    (np.array([2,-2,1]), np.array([1,1,0]))
]

for i, (v1, v2) in enumerate(perp, 1):
    print("\n--- Ejercicio", i, "---")
    print("v1 =", v1)
    print("v2 =", v2)

    print("\nPaso 1: Producto punto")
    dot = np.dot(v1, v2)
    print("v1 · v2 =", dot)

    print("\nPaso 2: Analizar")
    if son_perpendiculares(v1, v2):
        print("Son perpendiculares (producto punto = 0)")
    else:
        print("NO son perpendiculares")

    print("\nPaso 3: Ángulo")
    ang = angulo(v1, v2)
    print("Ángulo =", ang, "grados (perpendiculares: 90°)")

# ============================================================
# SECCIÓN 3: MÓDULO
# ============================================================

print("\n" + "="*60)
print("SECCIÓN 3: MÓDULO DE VECTORES")
print("="*60)

modulos = [
    np.array([3,4,12]),
    np.array([1,2,2]),
    np.array([-5,12,0])
]

for i, v in enumerate(modulos, 1):
    print("\n--- Ejercicio", i, "---")
    print("Vector v =", v)

    print("\nPaso 1: Aplicar fórmula")
    print("|v| = sqrt(x² + y² + z²)")

    resultado = modulo(v)

    print("\nPaso 2: Resultado")
    print("|v| =", resultado)

# ============================================================
# SECCIÓN 4: ÁNGULO ENTRE VECTORES
# ============================================================

print("\n" + "="*60)
print("SECCIÓN 4: ÁNGULO ENTRE VECTORES")
print("="*60)

angulos = [
    (np.array([1,0,0]), np.array([0,1,0])),
    (np.array([1,1,0]), np.array([1,0,0])),
    (np.array([2,3,1]), np.array([1,-1,2]))
]

for i, (v1, v2) in enumerate(angulos, 1):
    print("\n--- Ejercicio", i, "---")
    print("v1 =", v1)
    print("v2 =", v2)

    print("\nPaso 1: Producto punto")
    dot = np.dot(v1, v2)
    print("v1 · v2 =", dot)

    print("\nPaso 2: Módulos")
    m1 = modulo(v1)
    m2 = modulo(v2)
    print("|v1| =", m1)
    print("|v2| =", m2)

    print("\nPaso 3: Fórmula")
    print("cosθ = (v1·v2) / (|v1||v2|)")

    cos_theta = dot / (m1*m2)

    print("\nPaso 4: Ángulo")
    ang = angulo(v1, v2)
    print("θ =", ang, "grados")

# ============================================================
# REFLEXIÓN FINAL
# ============================================================

print("\n" + "="*60)
print("REFLEXIÓN FINAL")
print("="*60)

print("""
Al desarrollar estos ejercicios se pudo comprender que los vectores
permiten modelar relaciones geométricas en el espacio tridimensional.

Se observó que:
- Los vectores paralelos tienen la misma dirección
- Los vectores perpendiculares forman 90 grados
- El módulo representa la magnitud del vector
- El ángulo permite analizar la relación entre vectores

El uso de Python facilita estos cálculos y permite verificar resultados
de manera rápida y precisa, lo cual es fundamental en ingeniería.
""")
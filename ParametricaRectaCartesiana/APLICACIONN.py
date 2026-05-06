# ============================================================
# APLICACIÓN AVANZADA:
# INTERSECCIÓN RECTA - PLANO EN R3
# NIVEL: INGENIERÍA DE SISTEMAS (COMPLETO)
# ============================================================

import sympy as sp
import numpy as np

# ============================================================
# DEFINICIÓN TEÓRICA
# ============================================================

def definicion():
    print("\n" + "="*80)
    print("MODELADO MATEMÁTICO: RECTA Y PLANO EN R3")
    print("="*80)
    print("""
En geometría analítica, una recta puede representarse mediante una ecuación
paramétrica, mientras que un plano se describe mediante una ecuación cartesiana.

Recta:
    r(t) = P + t·v

Plano:
    Ax + By + Cz + D = 0

El problema de intersección consiste en determinar si existe un valor de t tal
que el punto de la recta satisfaga la ecuación del plano.
""")

# ============================================================
# DATOS DEL PROBLEMA
# ============================================================

def datos():
    # Punto inicial de la recta
    P = sp.Matrix([0, 2, 1])
    
    # Vector dirección de la recta
    v = sp.Matrix([3, 1, 2])
    
    # Plano
    A, B, C, D = 1, 2, 1, -10
    
    return P, v, A, B, C, D

# ============================================================
# ECUACIÓN DE LA RECTA
# ============================================================

def ecuacion_recta(P, v):
    t = sp.symbols('t')
    r = P + t*v
    
    print("\n--- ECUACIÓN DE LA RECTA ---")
    print("Forma vectorial: r(t) = P + t·v")
    
    print(f"\nPunto P: {P}")
    print(f"Vector dirección v: {v}")
    
    print("\nEcuaciones paramétricas:")
    print(f"x(t) = {r[0]}")
    print(f"y(t) = {r[1]}")
    print(f"z(t) = {r[2]}")
    
    return r, t

# ============================================================
# ECUACIÓN DEL PLANO
# ============================================================

def ecuacion_plano(A, B, C, D):
    print("\n--- ECUACIÓN DEL PLANO ---")
    print(f"{A}x + {B}y + {C}z + {D} = 0")
    
    normal = sp.Matrix([A, B, C])
    print("Vector normal del plano:", normal)
    
    return normal

# ============================================================
# ANÁLISIS PREVIO (IMPORTANTE)
# ============================================================

def analisis_geometrico(v, normal):
    print("\n--- ANÁLISIS GEOMÉTRICO ---")
    
    producto = v.dot(normal)
    
    print("Producto punto (v · n) =", producto)
    
    if producto == 0:
        print("La recta es PARALELA al plano (no hay intersección o hay infinitas).")
    else:
        print("La recta INTERSECTA el plano en un punto único.")

# ============================================================
# INTERSECCIÓN
# ============================================================

def calcular_interseccion(r, t, A, B, C, D):
    
    print("\n--- CÁLCULO DE INTERSECCIÓN ---")
    
    eq = A*r[0] + B*r[1] + C*r[2] + D
    
    print("\nSustituyendo la recta en el plano:")
    print(eq)
    
    sol = sp.solve(eq, t)
    
    if not sol:
        print("\nNo hay solución → recta paralela")
        return None
    
    t_val = sol[0]
    print("\nValor de t:", t_val)
    
    punto = r.subs(t, t_val)
    
    print("\nPunto de intersección:")
    print(punto)
    
    return punto

# ============================================================
# VERIFICACIÓN NUMÉRICA
# ============================================================

def verificacion(punto, A, B, C, D):
    
    print("\n--- VERIFICACIÓN NUMÉRICA ---")
    
    px, py, pz = float(punto[0]), float(punto[1]), float(punto[2])
    
    resultado = A*px + B*py + C*pz + D
    
    print(f"Evaluación: {resultado}")
    
    if abs(resultado) < 1e-6:
        print("El punto pertenece al plano ✅")
    else:
        print("Error en cálculo ❌")

# ============================================================
# DISTANCIA (ANÁLISIS EXTRA PRO)
# ============================================================

def distancia_punto_plano(punto, A, B, C, D):
    
    print("\n--- DISTANCIA PUNTO-PLANO ---")
    
    px, py, pz = punto
    
    numerador = abs(A*px + B*py + C*pz + D)
    denominador = np.sqrt(A**2 + B**2 + C**2)
    
    distancia = numerador / denominador
    
    print(f"Distancia = {distancia}")
    
    return distancia

# ============================================================
# INTERPRETACIÓN INGENIERIL
# ============================================================

def interpretacion(punto):
    
    print("\n--- INTERPRETACIÓN INGENIERIL ---")
    
    print(f"""
El punto {punto} representa el punto exacto donde una trayectoria lineal
(interpretable como una rampa, cable o trayectoria de movimiento)
intersecta una superficie plana.

Aplicaciones:
- Diseño de estructuras
- Modelado 3D
- Simulación de trayectorias
- Ingeniería civil y mecánica

Este tipo de análisis permite garantizar precisión y seguridad
en el diseño de sistemas reales.
""")

# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    definicion()
    
    P, v, A, B, C, D = datos()
    
    r, t = ecuacion_recta(P, v)
    
    normal = ecuacion_plano(A, B, C, D)
    
    analisis_geometrico(v, normal)
    
    punto = calcular_interseccion(r, t, A, B, C, D)
    
    if punto:
        verificacion(punto, A, B, C, D)
        distancia_punto_plano(punto, A, B, C, D)
        interpretacion(punto)
    
    print("\n" + "="*80)
    print("REFLEXIÓN FINAL")
    print("="*80)
    print("""
Este desarrollo demuestra cómo la integración entre matemáticas y programación
permite resolver problemas complejos de manera estructurada.

El uso de SymPy facilita el cálculo simbólico, mientras que NumPy permite
validaciones numéricas eficientes.

Esto es fundamental en áreas como:
- Inteligencia artificial
- Simulación
- Ingeniería estructural
- Computación gráfica

La modelación matemática es una herramienta clave en la ingeniería moderna.
""")

# ============================================================
# EJECUCIÓN
# ============================================================

if __name__ == "__main__":
    main()
import pandas as pd
import numpy as np

# ============================================================
# PROYECTO: APLICACIÓN DEL ÁLGEBRA LINEAL EN SALUD
# Tema: Predicción de la presión arterial de un estudiante
# usando matrices y sistemas de ecuaciones.
#
# Ecuación general del modelo:
# Presion = a + b(Sueno) + c(Ejercicio) + d(Estres)
# ============================================================

# ------------------------------------------------------------
# 1. REGISTRAR LOS DATOS
# ------------------------------------------------------------
# Cada fila corresponde a un día.
#
# Sueno      -> Horas dormidas
# Ejercicio  -> Minutos de ejercicio realizados
# Estres     -> Nivel de estrés de 1 a 10
# Presion    -> Presión arterial medida
# ------------------------------------------------------------

datos = pd.DataFrame({
    "Sueno": [8, 6, 7, 5, 8],
    "Ejercicio": [30, 10, 20, 0, 40],
    "Estres": [2, 8, 5, 9, 3],
    "Presion": [118, 140, 130, 150, 120]
})

print("=" * 60)
print("DATOS REGISTRADOS")
print("=" * 60)
print(datos)
print()

# ------------------------------------------------------------
# 2. CONSTRUIR LA MATRIZ A Y EL VECTOR B
# ------------------------------------------------------------
# Se agrega una primera columna de 1 porque corresponde al
# término independiente de la ecuación.
#
# Matriz A:
# [1, sueño, ejercicio, estrés]
#
# Vector B:
# [presión]
# ------------------------------------------------------------

A = np.array([
    [1, 8, 30, 2],
    [1, 6, 10, 8],
    [1, 7, 20, 5],
    [1, 5, 0, 9],
    [1, 8, 40, 3]
])

B = np.array([118, 140, 130, 150, 120])

print("=" * 60)
print("MATRIZ A")
print("=" * 60)
print(A)
print()

print("VECTOR B")
print(B)
print()

# ------------------------------------------------------------
# 3. CALCULAR LOS COEFICIENTES
# ------------------------------------------------------------
# Fórmula de álgebra lineal:
# X = (A^T * A)^(-1) * A^T * B
#
# El vector X contiene:
# X[0] = a
# X[1] = b
# X[2] = c
# X[3] = d
# ------------------------------------------------------------

X = np.linalg.inv(A.T @ A) @ A.T @ B

# Guardar los coeficientes en variables con nombres claros
intercepto = X[0]
coef_sueno = X[1]
coef_ejercicio = X[2]
coef_estres = X[3]

print("=" * 60)
print("COEFICIENTES DEL MODELO")
print("=" * 60)
print(f"a (intercepto) = {intercepto:.2f}")
print(f"b (sueño)      = {coef_sueno:.2f}")
print(f"c (ejercicio)  = {coef_ejercicio:.2f}")
print(f"d (estrés)     = {coef_estres:.2f}")
print()

# Mostrar la ecuación final de manera legible
print("ECUACIÓN OBTENIDA:")
print(
    f"Presión = {intercepto:.2f} "
    f"{coef_sueno:+.2f}(Sueño) "
    f"{coef_ejercicio:+.2f}(Ejercicio) "
    f"{coef_estres:+.2f}(Estrés)"
)
print()

# ------------------------------------------------------------
# 4. FUNCIÓN PARA ESTIMAR LA PRESIÓN ARTERIAL
# ------------------------------------------------------------
# Esta función recibe horas de sueño, ejercicio y estrés,
# y devuelve la presión arterial estimada.
# ------------------------------------------------------------

def estimar_presion(sueno, ejercicio, estres):
    return (
        intercepto
        + coef_sueno * sueno
        + coef_ejercicio * ejercicio
        + coef_estres * estres
    )

# ------------------------------------------------------------
# 5. COMPARAR DOS CASOS
# ------------------------------------------------------------
# Caso 1: Semana normal
# Caso 2: Semana de exámenes
# ------------------------------------------------------------

presion_normal = estimar_presion(8, 30, 3)
presion_examenes = estimar_presion(5, 0, 9)

print("=" * 60)
print("COMPARACIÓN DE CASOS")
print("=" * 60)

print("Semana normal:")
print("- 8 horas de sueño")
print("- 30 minutos de ejercicio")
print("- Estrés = 3")
print(f"Presión estimada: {presion_normal:.2f}")
print()

print("Semana de exámenes:")
print("- 5 horas de sueño")
print("- 0 minutos de ejercicio")
print("- Estrés = 9")
print(f"Presión estimada: {presion_examenes:.2f}")
print()

# ------------------------------------------------------------
# 6. INTERPRETAR LOS RESULTADOS
# ------------------------------------------------------------

print("=" * 60)
print("INTERPRETACIÓN")
print("=" * 60)
print(
    f"Cada hora adicional de sueño cambia la presión en {coef_sueno:.2f}."
)
print(
    f"Cada minuto adicional de ejercicio cambia la presión en {coef_ejercicio:.2f}."
)
print(
    f"Cada punto adicional de estrés cambia la presión en {coef_estres:.2f}."
)

if presion_examenes > presion_normal:
    diferencia = presion_examenes - presion_normal
    print()
    print(
        f"La presión en semana de exámenes es aproximadamente "
        f"{diferencia:.2f} puntos mayor que en una semana normal."
    )

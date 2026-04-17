# ==========================================================
# INSTALACIÓN DE LA BIBLIOTECA NECESARIA
# ==========================================================
# Antes de ejecutar este programa en la terminal o consola,
# debes instalar NumPy con el siguiente comando:
#
# pip install numpy
#
# NumPy se utiliza para trabajar fácilmente con vectores.

# Importamos la biblioteca NumPy y le damos el nombre corto np
import numpy as np

# ==========================================================
# 5 EJERCICIOS DE SUMA DE VECTORES EN R3
# ==========================================================

print("========== SUMAS ==========")

# ----------------------------------------------------------
# SUMA 1
# ----------------------------------------------------------

# Creamos los dos vectores
v1 = np.array([3, -2, 5])
v2 = np.array([4, 1, -3])

# Sumamos los vectores componente por componente
r1 = v1 + v2

# Mostramos el procedimiento y el resultado
print("\nSUMA 1")
print("Vectores:", v1, "+", v2)
print("Procedimiento: (3+4, -2+1, 5+(-3))")
print("Resultado:", r1)

# ----------------------------------------------------------
# SUMA 2
# ----------------------------------------------------------

v3 = np.array([-6, 8, 2])
v4 = np.array([5, -3, 7])

r2 = v3 + v4

print("\nSUMA 2")
print("Vectores:", v3, "+", v4)
print("Procedimiento: (-6+5, 8+(-3), 2+7)")
print("Resultado:", r2)

# ----------------------------------------------------------
# SUMA 3
# ----------------------------------------------------------

v5 = np.array([1, 4, -2])
v6 = np.array([7, -5, 3])

r3 = v5 + v6

print("\nSUMA 3")
print("Vectores:", v5, "+", v6)
print("Procedimiento: (1+7, 4+(-5), -2+3)")
print("Resultado:", r3)

# ----------------------------------------------------------
# SUMA 4
# ----------------------------------------------------------

v7 = np.array([9, 0, -1])
v8 = np.array([-2, 6, 8])

r4 = v7 + v8

print("\nSUMA 4")
print("Vectores:", v7, "+", v8)
print("Procedimiento: (9+(-2), 0+6, -1+8)")
print("Resultado:", r4)

# ----------------------------------------------------------
# SUMA 5
# ----------------------------------------------------------

v9 = np.array([-4, -7, 5])
v10 = np.array([3, 2, -9])

r5 = v9 + v10

print("\nSUMA 5")
print("Vectores:", v9, "+", v10)
print("Procedimiento: (-4+3, -7+2, 5+(-9))")
print("Resultado:", r5)


# ==========================================================
# 5 EJERCICIOS DE RESTA DE VECTORES EN R3
# ==========================================================

print("\n========== RESTAS ==========")

# ----------------------------------------------------------
# RESTA 1
# ----------------------------------------------------------

v11 = np.array([9, -4, 6])
v12 = np.array([2, 5, -1])

# Restamos el segundo vector al primero
r6 = v11 - v12

print("\nRESTA 1")
print("Vectores:", v11, "-", v12)
print("Procedimiento: (9-2, -4-5, 6-(-1))")
print("Resultado:", r6)

# ----------------------------------------------------------
# RESTA 2
# ----------------------------------------------------------

v13 = np.array([-3, 7, -8])
v14 = np.array([4, -2, 5])

r7 = v13 - v14

print("\nRESTA 2")
print("Vectores:", v13, "-", v14)
print("Procedimiento: (-3-4, 7-(-2), -8-5)")
print("Resultado:", r7)

# ----------------------------------------------------------
# RESTA 3
# ----------------------------------------------------------

v15 = np.array([10, 3, -6])
v16 = np.array([1, 8, 2])

r8 = v15 - v16

print("\nRESTA 3")
print("Vectores:", v15, "-", v16)
print("Procedimiento: (10-1, 3-8, -6-2)")
print("Resultado:", r8)

# ----------------------------------------------------------
# RESTA 4
# ----------------------------------------------------------

v17 = np.array([-5, -9, 4])
v18 = np.array([-2, 1, -7])

r9 = v17 - v18

print("\nRESTA 4")
print("Vectores:", v17, "-", v18)
print("Procedimiento: (-5-(-2), -9-1, 4-(-7))")
print("Resultado:", r9)

# ----------------------------------------------------------
# RESTA 5
# ----------------------------------------------------------

v19 = np.array([8, 2, 0])
v20 = np.array([6, -4, 9])

r10 = v19 - v20

print("\nRESTA 5")
print("Vectores:", v19, "-", v20)
print("Procedimiento: (8-6, 2-(-4), 0-9)")
print("Resultado:", r10)


# ==========================================================
# 5 EJERCICIOS DE PRODUCTO DE UN ESCALAR POR UN VECTOR
# ==========================================================

print("\n========== PRODUCTO POR ESCALAR ==========")

# ----------------------------------------------------------
# ESCALAR 1
# ----------------------------------------------------------

# Definimos un escalar y un vector
k1 = 3
v21 = np.array([2, -1, 4])

# Multiplicamos cada componente del vector por el escalar
r11 = k1 * v21

print("\nESCALAR 1")
print("Escalar:", k1)
print("Vector:", v21)
print("Procedimiento: (3*2, 3*(-1), 3*4)")
print("Resultado:", r11)

# ----------------------------------------------------------
# ESCALAR 2
# ----------------------------------------------------------

k2 = -2
v22 = np.array([5, 3, -6])

r12 = k2 * v22

print("\nESCALAR 2")
print("Escalar:", k2)
print("Vector:", v22)
print("Procedimiento: (-2*5, -2*3, -2*(-6))")
print("Resultado:", r12)

# ----------------------------------------------------------
# ESCALAR 3
# ----------------------------------------------------------

k3 = 4
v23 = np.array([-1, 7, 2])

r13 = k3 * v23

print("\nESCALAR 3")
print("Escalar:", k3)
print("Vector:", v23)
print("Procedimiento: (4*(-1), 4*7, 4*2)")
print("Resultado:", r13)

# ----------------------------------------------------------
# ESCALAR 4
# ----------------------------------------------------------

k4 = 5
v24 = np.array([0, -3, 8])

r14 = k4 * v24

print("\nESCALAR 4")
print("Escalar:", k4)
print("Vector:", v24)
print("Procedimiento: (5*0, 5*(-3), 5*8)")
print("Resultado:", r14)

# ----------------------------------------------------------
# ESCALAR 5
# ----------------------------------------------------------

k5 = -3
v25 = np.array([6, -2, 1])

r15 = k5 * v25

print("\nESCALAR 5")
print("Escalar:", k5)
print("Vector:", v25)
print("Procedimiento: (-3*6, -3*(-2), -3*1)")
print("Resultado:", r15)
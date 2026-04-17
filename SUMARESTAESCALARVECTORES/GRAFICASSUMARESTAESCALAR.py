# ==========================================================
# INSTALACIÓN DE LIBRERÍAS
# ==========================================================
# Ejecuta esto antes de correr el programa:
#
# pip install numpy matplotlib
#
# numpy: para trabajar con vectores
# matplotlib: para crear las gráficas

import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# FUNCIÓN PARA GRAFICAR Y GUARDAR EL VECTOR RESULTANTE
# ==========================================================

def graficar_vector(vector, titulo):
    # Crear figura y ejes 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dibujar el vector desde el origen
    ax.quiver(
        0, 0, 0,
        vector[0], vector[1], vector[2],
        color='blue',
        arrow_length_ratio=0.1
    )

    # Ajustar el tamaño de los ejes
    limite = max(abs(vector)) + 2
    ax.set_xlim([-limite, limite])
    ax.set_ylim([-limite, limite])
    ax.set_zlim([-limite, limite])

    # Etiquetas
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # Título y cuadrícula
    ax.set_title(titulo)
    ax.grid(True)

    # Guardar la imagen
    nombre_archivo = titulo + ".png"
    plt.savefig(nombre_archivo)

    # Cerrar la figura para no acumular memoria
    plt.close()

    print("Gráfica guardada:", nombre_archivo)


# ==========================================================
# 5 GRÁFICAS DE SUMAS
# ==========================================================

# Suma 1
r1 = np.array([7, -1, 2])
graficar_vector(r1, "Suma_1")

# Suma 2
r2 = np.array([-1, 5, 9])
graficar_vector(r2, "Suma_2")

# Suma 3
r3 = np.array([8, -1, 1])
graficar_vector(r3, "Suma_3")

# Suma 4
r4 = np.array([7, 6, 7])
graficar_vector(r4, "Suma_4")

# Suma 5
r5 = np.array([-1, -5, -4])
graficar_vector(r5, "Suma_5")


# ==========================================================
# 5 GRÁFICAS DE RESTAS
# ==========================================================

# Resta 1
r6 = np.array([7, -9, 7])
graficar_vector(r6, "Resta_1")

# Resta 2
r7 = np.array([-7, 9, -13])
graficar_vector(r7, "Resta_2")

# Resta 3
r8 = np.array([9, -5, -8])
graficar_vector(r8, "Resta_3")

# Resta 4
r9 = np.array([-3, -10, 11])
graficar_vector(r9, "Resta_4")

# Resta 5
r10 = np.array([2, 6, -9])
graficar_vector(r10, "Resta_5")


# ==========================================================
# 5 GRÁFICAS DE PRODUCTO POR ESCALAR
# ==========================================================

# Producto por escalar 1
r11 = np.array([6, -3, 12])
graficar_vector(r11, "Producto_Escalar_1")

# Producto por escalar 2
r12 = np.array([-10, -6, 12])
graficar_vector(r12, "Producto_Escalar_2")

# Producto por escalar 3
r13 = np.array([-4, 28, 8])
graficar_vector(r13, "Producto_Escalar_3")

# Producto por escalar 4
r14 = np.array([0, -15, 40])
graficar_vector(r14, "Producto_Escalar_4")

# Producto por escalar 5
r15 = np.array([-18, 6, -3])
graficar_vector(r15, "Producto_Escalar_5")

print("\nTodas las gráficas fueron guardadas correctamente.")
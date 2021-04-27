"""Modulo que contiene el Metodo de Eliminacion Gaussiana"""
# Este programa no intercambia las filas, asi que puede causar errores si el primer elemento de la matriz es cero

import numpy as np

def Metodo_Eliminacion_Gaussiana(orden):
    """Funcion que llevara a cabo el Metodo de Eliminacion Gaussiana"""
    # Crea una matriz sin valores asignados para almacenar numeros de tipo 'float'
    A = np.empty((orden, orden + 1), dtype = 'f')

    # Bucle anidado para almacenar los valores ingresados por el usuario en la matriz
    for i in range(orden):
        for j in range(orden + 1):
            if j == orden:
                A[i, j] = float(input(f"Ingrese el resultado de la ecuacion {i + 1}: "))
            else:
                A[i, j] = float(input(f"Ingrese el elemento {i + 1, j + 1}: "))

    # Bucle anidado que llevara a cabo el metodo
    for k in range(1, orden):  # Comienza desde la segunda ecuacion de la matriz
        for l in range(k, orden):  # Bucle que convierte en cero los elementos por debajo del pivote
            # Calcula el numero que se usara para la conversion de los numeros debajo del pivote
            multiplicador = A[l, k - 1] / A[k - 1, k - 1]
            # Realiza las operaciones con los renglones de la matriz para convertir los numeros debajo del pivote en cero
            A[l] = (-1 * (multiplicador * A[k - 1])) + A[l]

    print("\n", A)

    x = np.zeros(orden)  # Vector solucion
    # Bucle que llenara el vector solucion haciendo el despeje hacia atras
    for n in range(orden - 1, -1, -1):
        sumatoria = 0
        for m in range(orden - 1, -1, -1):
            sumatoria += (-1) * (x[m]) * (A[n, m])
        x[n] = (1 / A[n, n]) * (A[n, orden] + sumatoria)

    print("\nVector solucion:\n", np.transpose(x).reshape(orden, 1))


if __name__ == "__main__":
    orden = int(input("Ingrese la cantidad de ecuaciones: "))
    Metodo_Eliminacion_Gaussiana(orden)
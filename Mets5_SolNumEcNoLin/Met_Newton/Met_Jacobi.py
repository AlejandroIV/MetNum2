"""Modulo que contiene el Metodo de Jacobi"""

from ModulosAdicionales import MatDiagDom
import numpy as np
import math
import sys

def Jacobi(tolerancia, limite, A, x):
    """Funcion que llevara a cabo el Metodo de Jacobi"""
    # Manda a llamar a la funcion para hacer el intercambio de los renglones necesarios, de tal manera que la matriz resultante sea una matriz diagonal dominante
    A = MatDiagDom.Matriz_Diagonal_Dominante(A)

    # Bucle anidado que modifica la matriz A para poder aplicar el metodo de Jacobi
    for fil in range(A.shape[0]):
        denominador = A[fil, fil]
        for col in range(A.shape[1]):
            # Condicional para cambiar la componente de la diagonal por cero
            if col == fil:
                A[fil, col] = 0
            else:
                if (col + 1) == A.shape[1]:
                    A[fil, col] /= denominador
                else:
                    A[fil, col] /= -denominador

    T = np.copy(A[:, :A.shape[0]])

    c = np.copy(A[:, A.shape[0]:])

    # Calcula la norma de 'x'
    normaX1 = np.linalg.norm(x)

    cont = 0

    # Bucle que se repetira hasta que el error sea menor o igual al permitido
    while True:
        # Multiplica la matriz 'T' por el vector 'x' y le suma el vector 'c'
        x = np.matmul(T, np.reshape(x, (A.shape[0], 1))) + np.reshape(c, (A.shape[0], 1))

        cont += 1

        # Calcula la norma de 'x'
        normaX2 = np.linalg.norm(x)

        # Calcula el error aproximado porcentual y almacena el resultado en la variable 'errorAproxPorcen'
        errorAproxPorcen = ((normaX2 - normaX1) / normaX2) * 100

        if abs(errorAproxPorcen) < tolerancia:
            break

        if cont == limite:
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no se ha determinado el resultado y se detiene la ejecucion del programa
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado un posible ", end = "")
            print("resultado aplicando el Metodo de Jacobi para resolver el sistema de ecuaciones lineales")
            print("Pruebe con otro vector inicial o ingrese un limite de iteraciones mayor\n\n")
            sys.exit(1)

        # Se copia el valor de 'normaX2' en la variable 'normaX1' para que en la siguiente iteracion se considere la norma que se acaba de calcular
        normaX1 = normaX2

    return x

def Metodo_de_Jacobi(orden):
    # Crea una matriz sin valores asignados para almacenar numeros de tipo 'float'
    matriz = np.empty((orden, orden + 1), dtype = 'f')

    print()
    # Bucle anidado para almacenar los valores ingresados por el usuario en la matriz
    for i in range(orden):
        for j in range(orden + 1):
            if j == orden:
                matriz[i, j] = float(input(f"Ingrese el resultado de la ecuacion {i + 1}: "))
            else:
                matriz[i, j] = float(input(f"Ingrese el elemento {i + 1, j + 1}: "))

    print("\nIngrese el vector incial para comenzar con el metodo\n")
    # Crea el vector inicial para comenzar con el metdo y se llena en el bucle for
    vectorIn = np.empty(orden, dtype = 'f')
    for comp in range(orden):
        vectorIn[comp] = float(input(f"Ingrese la componente {comp + 1} del vector: "))

    # Pide al usuario los valores necesarios para el metodo
    error = float(input("Ingrese el error de tolerancia: "))
    limite = float(input("Ingrese el limite de iteraciones: "))
    print()

    vectorSol = Jacobi(error, limite, matriz, vectorIn)

    print("\nEl posible vector solucion es:\n", np.transpose(vectorSol).reshape(orden, 1))

if __name__ == "__main__":
    orden = int(input("Ingrese la cantidad de ecuaciones: "))
    Metodo_de_Jacobi(orden)
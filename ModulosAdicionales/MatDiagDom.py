"""Modulo que cotiene lo necesario para hacer una Matriz Diagonal Dominante"""

import numpy as np

def Matriz_Diagonal_Dominante(matriz):
    """Funcion que cambiara los renglones de la matriz para que sea una Matriz Diagonal Positiva"""
    # Crea el vector de indices y lo llena en el bucle
    vectorIndices = np.empty(matriz.shape[0], dtype = 'i1')
    for cantFilas in range(matriz.shape[0]):
        vectorIndices[cantFilas] = cantFilas

    # Bucle que recorre las filas de la matriz
    for fil in range(matriz.shape[0]):
        # Bucle que recorre las filas que no se han usado para determinar las componentes de las digonales
        for diag in vectorIndices:
            sumatoria = 0
            # Bucle que recorre las columnas para sumar las componetes excepto el elemento de la diagonal
            for col in range(matriz.shape[1] - 1):
                # Condicional para no considera la componente de la matriz que esta en la posicion de la componente de la diagonal
                if col == fil:
                    continue
                else:
                    sumatoria += abs(matriz[diag, col])
            
            # Condicional que se ejecutara en caso de que se cumpla la condicion de que el elemento
            # de la diagonal es mayor que la sumatoria de los demas componentes en esa misma fila
            if abs(matriz[diag, fil]) > sumatoria:
                vectorIndices = np.delete(vectorIndices, np.where(vectorIndices == fil))
                # Se intercambian las filas
                vectFilaAux = np.copy(matriz[fil, :])
                matriz[fil, :] = np.copy(matriz[diag, :])
                matriz[diag, :] = vectFilaAux
                # Se para el bucle para seguir con las demas filas
                break

    # Al final regresa la matriz diagonal dominante
    return matriz

if __name__ == "__main__":
    orden = int(input("Ingrese la cantidad de ecuaciones: "))

    # Crea una matriz sin valores asignados para almacenar numeros de tipo 'float'
    A = np.empty((orden, orden + 1), dtype = 'f')

    # Bucle anidado para almacenar los valores ingresados por el usuario en la matriz
    for i in range(orden):
        for j in range(orden + 1):
            if j == orden:
                A[i, j] = float(input(f"Ingrese el resultado de la ecuacion {i + 1}: "))
            else:
                A[i, j] = float(input(f"Ingrese el elemento {i + 1, j + 1}: "))

    print(A)

    print(Matriz_Diagonal_Dominante(A))
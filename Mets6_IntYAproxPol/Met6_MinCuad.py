"""Modulo que contiene el codigo para construir el Polinomio Discreto de Minimos Cuadrados"""

from sage.all import SR, sage, round, ln, var
import sys
import numpy as np
from Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, RelacionMinCuad

def Interpolacion_Minimos_Cuadrados(nombre):
    """Funcion que construira el Polinomio Interpolante usando Minimos Cuadrados"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    # Pide al usuario que indique si la relacion de los datos es exponencial
    relacionExp = RelacionMinCuad()

    # Si la relacion de los datos es exponencial
    if relacionExp:
        # Calcula los valores de las columnas (ln y, x^2, x * ln y) que se agregaran a la matriz 'matDatos' [Burden p. 492]
        vetcAux = np.copy(ln(matDatos[:, 1]))
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)
        vetcAux = np.copy(matDatos[:, 0] * matDatos[:, 0])
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)
        vetcAux = np.copy(matDatos[:, 0] * matDatos[:, 2])
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)
    # Si la relacion de los datos no es exponencial
    else:
        # Calcula los valores de las columnas (x^2, x * y) que se agregaran a la matriz 'matDatos' [Burden p. 487]
        vetcAux = np.copy(matDatos[:, 0] * matDatos[:, 0])
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)
        vetcAux = np.copy(matDatos[:, 0] * matDatos[:, 1])
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)

    np.set_printoptions(precision = 6, suppress = True)

    print(f"\n{matDatos}\n")

    # Crea la variable que contendra el polinomio en formato'str'
    polinomio = ''
    # Constuiye el polinomio usando como coeficientes las sumatorias  tomando en [Burden pp. 487, 492]
    # Si la relacion de los datos es exponencial
    if relacionExp:
        valor1 = ((matDatos.shape[0] * np.sum(matDatos[:, 4])) - (np.sum(matDatos[:, 0]) * np.sum(matDatos[:, 2])))
        valor1 /= ((matDatos.shape[0] * np.sum(matDatos[:, 3])) - (np.sum(matDatos[:, 0]) ** 2))
        valor2 = ((np.sum(matDatos[:, 3]) * np.sum(matDatos[:, 2])) - (np.sum(matDatos[:, 4]) * np.sum(matDatos[:, 0])))
        valor2 /=((matDatos.shape[0] * np.sum(matDatos[:, 3])) - (np.sum(matDatos[:, 0]) ** 2))
        polinomio = f"(e ** {valor2}) * (e ** ({valor1} * x))"
    # Si la relacion de los datos no es exponencial
    else:
        valor1 = ((np.sum(matDatos[:, 2]) * np.sum(matDatos[:, 1])) - (np.sum(matDatos[:, 0]) * np.sum(matDatos[:, 3])))
        valor1 /= ((matDatos.shape[0] * np.sum(matDatos[:, 2])) - (np.sum(matDatos[:, 0]) ** 2))
        valor2 = ((matDatos.shape[0] * np.sum(matDatos[:, 3])) - (np.sum(matDatos[:, 0]) * np.sum(matDatos[:, 1])))
        valor2 /= ((matDatos.shape[0] * np.sum(matDatos[:, 2])) - (np.sum(matDatos[:, 0]) ** 2))
        polinomio = f"({valor2} * x) + {valor1}"

    polinomio = SR(polinomio)

    print(f"\nEl Polinomio Interpolante es: {polinomio}")

    a = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa

    # Declara la variable simbolica
    x = var('x')

    # Simplifica el resultado y lo imprime redondeandolo a 8 decimales
    print(f"\n\nEl valor de la funcion en el punto {x} es aproximadamente: {round(polinomio.subs(x = a).simplify_full(), 8)}\n")

def MinimosCuadrados():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Interpolacion_Minimos_Cuadrados(fNombre)

if __name__ == "__main__":
    Interpolacion_Minimos_Cuadrados("prueba")
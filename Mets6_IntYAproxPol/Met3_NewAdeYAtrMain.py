"""Modulo que contiene el codigo para aplicar las Formulas de Interpolacion de Newton: hacia adelante y hacia atras"""

from sage.all import SR, sage, round
import sys
import numpy as np
from Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, AlgoritmoNet, Modificar_Matriz_DifRegr

def Interpolacion_Newton_Adelante_Atras(nombre):
    """Funcion que construira la tabla de las diferencias para aplicar la Formula de las Diferencias de Newton"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)
    # Une la matriz 'matDatos' con otra matriz de ceros de orden n x n - 1, donde n es el numero de datos
    matDatos = np.copy(np.append(matDatos, np.zeros((matDatos.shape[0], (matDatos.shape[0] - 1)), dtype = 'f'), axis = 1))

    # Bucle que se repetira hasta calcular la ultima diferencia posible
    # Este contador se utilizara para indexar los valores de las columnas de 'matDatos'
    for cont1 in range(1, matDatos.shape[0]):
        #  Este contador se utilizara para indexar los valores de las filas de 'matDatos'
        cont2 = 0
        # Bucle que calcula los elementos de la tabla de diferencias
        for iteracion in range(cont1, matDatos.shape[0]):
            matDatos[cont2, (cont1 + 1)] = matDatos[(cont2 + 1), cont1] - matDatos[cont2, cont1]
            cont2 += 1

    np.set_printoptions(precision = 6, suppress = True)

    # Pide al usuario que elija una opcion
    opcion = AlgoritmoNet()

    # Si el usuario elije aplicar la interpolacion de newton hacia adelante entonces necesitamos indexar los valores de la primera fila de la matriz 'matDatos'
    if opcion == 1:
        fila = 0

    # Si el usuario elije aplicar la interpolacion de newton hacia atras entonces necesitamos indexar los valores de la ultima fila de la matriz 'matDatos'
    else:
        fila = matDatos.shape[0] - 1
        matDatos = Modificar_Matriz_DifRegr(matDatos)

    print(f"\n{matDatos}\n")

    # Pide al usuario el grado del polinomio
    while True:
        try:
            num = int(input("Ingrese el grado del polinomio que quiera usar para el calculo: "))
            if num > 0 and num < (matDatos.shape[1] - 1):
                break
            print("Entrada invalida")
        except:
            print("Entrada invalida")

    # Calcula 's'
    x = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa
    s = (x - matDatos[fila, 0]) / (matDatos[1, 0] - matDatos[0, 0])

    # Crea la variable que contendra el polinomio en formato'str'
    polinomio = f"({round(matDatos[fila, 1], 8)})+"  # Primero agrega el primer termino del polinomio (constante)
    # Lista que contendra los terminos lineales que se multiplicaran por las deltas
    terminos = ['s']   # Almacena el elemento 's' en la lista
    # Bucle que recorrera las columnas de la fila con la que se desee trabajar (la primera o la ultima)
    for deltas in range(1, num + 1):
        polinomio += f"(({round(matDatos[fila, (deltas + 1)], 8)}"
        # Bucle que agregara los terminos
        for termino in terminos:
            polinomio += f" * {termino}"
        polinomio += f") / (factorial({deltas})))+"

        # Agrega un nuevo termino a la lista
        # Si el usuario eligio aplicar la interpolacion de newton hacia adelante se agregan terminos de la forma: (s - n) [Burden p. 126]
        if opcion == 1:
            terminos.append(f"(s - {deltas})")

        # Si el usuario eligio plicar la interpolacion de newton hacia atras se agregan terminos de la forma: (s + n) [Burden p. 127]
        else:
            terminos.append(f"(s + {deltas})")

    # Elimina el ultimo signo '+' que esta en la cadena que contiene el polinomio
    polinomio = polinomio[:(len(polinomio) - 1)]

    # Sustituye 's' por el valor que se calculo
    polinomio = polinomio.replace('s', f"({str(s)})")

    print(f"\nEl Polinomio Interpolante es: {polinomio}")

    polinomio = SR(polinomio)

    # Simplifica el resultado y lo imprime redondeandolo a 8 decimales
    print(f"\n\nEl valor de la funcion en el punto {x} es aproximadamente: {round(polinomio.simplify_full(), 8)}\n")

def NewtonInterpolacion():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Interpolacion_Newton_Adelante_Atras(fNombre)

if __name__ == "__main__":
    Interpolacion_Newton_Adelante_Atras("prueba")
"""Modulo que contiene el codigo para aplicar las Formulas de Interpolacion de Newton: hacia adelante y hacia atras"""

from sage.all import *
import sys
import numpy as np
from Mets6_IntYAproxPol.Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, OpcionesNet, Modificar_Matriz

def Interpolacion_Newton_Adelante_Atras(nombre):
    """Funcion que construira la tabla de las diferencias para aplciar la Formula de Interpolacion de Newton"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    # Crea un vector columna auxiliar para ir guardando lo resultados que se almacenaran en a tabla
    vectResultadosAux = np.empty((matDatos.shape[0], 1), dtype = 'f')
    # Contador que se usara para saber que columna de 'matDatos' se va a utilizar para calcular el numerador
    cont1 = 1
    # Bucle que se repetira hasta calcular la ultima diferencia posible
    for diferencia in range(matDatos.shape[0] - 1):
        cont2 = 0  # Contador que se va a usar para indexar a 'vectResultadosAux'
        # Bucle que calcula los elementos de la tabla de diferencias
        for iteraciones in range(cont1, matDatos.shape[0]):
            # La variable 'iteraciones' se va a utilizar para idexar las filas que se van a usar de la matriz 'matDatos'
            resultado = matDatos[(cont2 + 1), cont1] - matDatos[cont2, cont1]
            vectResultadosAux[cont2, 0] = resultado
            cont2 += 1

        # Bucle que agregara ceros al resto de filas del vector
        for ceros in range(cont1):
            vectResultadosAux[cont2, 0] = 0
            cont2 += 1

        cont1 += 1

        # Agrega la columna que se calculo a la matriz
        matDatos = np.append(matDatos, vectResultadosAux, axis = 1)

    np.set_printoptions(precision = 6, suppress = True)

    # Pide al usuario que elija aplicar el metodo de newton hacia adelante o ahacia atras
    opcion = OpcionesNet()

    # Si el usuario elije aplicar la interpolacion de newton hacia adelante entonces necesitamos indexar los valores de la primera fila de la matriz 'matDatos'
    if opcion == 1:
        fila = 0
        # Calcula 's'
        x = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa
        s = (x - matDatos[fila, 0]) / (matDatos[1, 0] - matDatos[0, 0])
        print(f"\n{matDatos}\n")

    # Si el usuario elije aplicar la interpolacion de newton hacia atras entonces necesitamos indexar los valores de la ultima fila de la matriz 'matDatos'
    else:
        fila = matDatos.shape[0] - 1
        # Calcula 's'
        x = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa
        s = (x - matDatos[fila, 0]) / (matDatos[1, 0] - matDatos[0, 0])
        matDatos = Modificar_Matriz(matDatos)
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

    # Crea la variable que contendra el polinomio en formato'str'
    polinomio = ''
    # Lista que contendra los terminos lineales que se multiplicaran por las deltas
    terminos = []
    # Bucle que recorrera las columnas de la fila con la que se desee trabajar (la primera o la ultima)
    for deltas in range(num + 1):
        polinomio += f"(({round(matDatos[fila, (deltas + 1)], 8)}"
        if deltas == 0:
            polinomio += "))+"
            # Agrega un nuevo termino a la lista
            terminos.append('s')
            continue
        # Bucle que agregara los terminos
        for termino in terminos:
            polinomio += f" * {termino}"
        polinomio += f") / (factorial({deltas})))+"

        # Si el usuario eligio aplicar la interpolacion de newton hacia adelante se agregan terminos como: (s - n)
        if opcion == 1:
            # Agrega un nuevo termino a la lista
            terminos.append(f"(s - {deltas})")

        # Si el usuario eligio plicar la interpolacion de newton hacia atras se agregan terminos como: (s + n)
        else:
            # Agrega un nuevo termino
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
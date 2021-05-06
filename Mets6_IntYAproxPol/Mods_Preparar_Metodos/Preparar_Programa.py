"""Modulo que contiene las funciones necesarias para preparar el codigo para el modulo 'Met1_PolInterLagMain.py'"""

from sage.all import *
import sys
import numpy as np

def LLenar_Matriz_Datos(nombreArchTxt):
    """Funcion que lee un archivo de texto, extrae los datos ingresados y las almacena en una matriz"""
    try:
        archDts = open(f"{nombreArchTxt}.txt", "r")
    except:
        print("\nNo es posible abrir el archivo")
        print("Crea un archivo de texto e ingresa los datos ahí, guardalo con el formato 'txt' y vuelve a correr el programa\n")
        sys.exit(1)

    dts = ""
    # Bucle que recorre todo el archivo
    for parr in archDts:
        # Guarda el la variable 'dts' la cadena de texto con los datos que hay en el archivo de texto en formato 'str'
        dts += parr

    # Separa los datos delimitados por comas
    dts = dts.split(' ')

    # Crea una matriz para almacenar los datos extraidos del archivo de texto
    matDts = np.empty((len(dts), 2), dtype = 'f')

    cont = 0
    # Bucle que recorre la lista con todos los datos ingresados por el usuario en el archivo de texto para separarlos
    for dato in dts:
        # Variables auxiliares el indice de los caracteres que se usan para delimitar los datos y hacer las separacion de los mismos
        indParentesis1 = dato.find("(")
        indParentesis2 = dato.find(")")
        indComa = dato.find(",")
        
        # Trata de convertir los datos en formato 'double' y los almacena en 'matDts'
        try:
            matDts[cont, 0] = float(dato[(indParentesis1 + 1):indComa])
            matDts[cont, 1] = float(dato[(indComa + 1):indParentesis2])
        except:
            print("\nAlguno de los datos no se ha podido convertir en un formato compatible que pueda usar el programa")
            print("Debe ingresar numeros para poder continuar\n")
            sys.exit(1)
        cont += 1

    # Cierra el archivo
    archDts.close()

    # Regresa la matriz con los datos leidos desde el archivo de texto
    return matDts

def OpcionesLag(matDats):
    """Funcion que pedira al usuario elegir una opcion en la que se aplica la formula de lagrange"""
    # Pide al usuario que elija una de las siguientes opciones
    print("\n1.- Construir el Polinomio Interpolante de Lagrange")
    print("2.- Aproximar la funcion en un punto usando la Formula de Lagrange")
    #print("3.- Aplicar el Metodo de Neville")

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 3:  # Aqui va un '4' si se programa el metodo de Neville y se descomentan las lineas para correrlo
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Si el usuario selecciona la opcion 1 o 2 entonces se imprimen los datos
    if op > 0 and op < 3:
        print("\nLos datos ingresados son los siguientes:\n")
        # Bucle que recorre la matriz que contiene los datos y los imprime de manera enumerada para que el usuario elija los datos que desee utilizar
        cont = 0
        for elem in range(matDats.shape[0]):
            print((cont + 1), end = "   -   ")
            print(matDats[cont])
            cont += 1

    # Crea la variable 'indiceFilas' para saber cuales son los datos que el usuario desea utilizar y la opcion que elije el usuario
    indicesFilas = list()

    # Si el usuario elige la opcion 1 entonces se construye el polinomio interpolante de lagrange
    if op == 1 or op == 2:
        # Bucle para pedir al usuario que ingrese la cantidad de elementos que desee utilizar
        while True:
            try:
                cantDts = int(input("\nIngrese la cantidad de datos que desee usar: "))
                if cantDts > 0 and cantDts < (matDats.shape[0] + 1):
                    break
                print("Cantidad de elementos invalida!!!")
            except:
                print("Entrada invalida!!!")

        # Agrega a la lista la opcion elegida por el usuario
        indicesFilas.append(op)

        # Si el usuario decide usar todos los datos entonces crea una lista para poder acceder a todas las filas de la matriz 'matDatos'
        if cantDts == matDats.shape[0]:
            for ind in range(cantDts):
                indicesFilas.append(ind)

        # Si el usuario no decide usar todos los datos, entonces crea una lista para poder acceder a las filas de la matriz 'matDatos'
        else:
            for elem in range(cantDts):
                # Pide al usuario los numeros de los datos que desea utilizar
                while True:
                    try:
                        num = int(input(f"Ingresa el dato {(elem + 1)} que desee usar: "))
                        if num > 0 and num < (matDats.shape[0] + 1):
                            break
                        print("Entrada invalida")
                    except:
                        print("Entrada invalida")
                indicesFilas.append(num - 1)

    #elif op == 3:
    #    indicesFilas.append(op)
    #    print()
    #    print("Neville")

    return indicesFilas

def OpcionesDifDiv():
    """Funcion que pedira al usuario elegir una opcion en la que se aplican las diferencias divididas"""
    # Pide al usuario que elija una de las siguientes opciones
    print("\n1.- Construir el Polinomio Interpolante de Newton")
    print("2.- Aproximar la funcion en un punto usando las Diferencias Divididas")

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 3:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    return op

def OpcionesNet():
    """Funcion que pedira al usuario elegir una opcion en la que se aplica la interpolacion de newton"""
    # Pide al usuario que lija una de las siguientes opciones
    print("\n1.- Aplicar la Formula de Interpolacion de Newton hacia adelante")
    print("2.- Aplicar la Formula de Interpolacion de Newton hacia atras")

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 3:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    return op

def Modificar_Matriz(matriz):
    """Funcion que modifica la matriz para poder aplicar la formula de interpolacion de newton hacia atras"""
    # Se crea una matriz auxiliar para ir almacenando los datos de la matriz en forma modificada
    matAux = np.empty((matriz.shape[0], 1), dtype = 'f')
    # Crea un vector auxiliar para ir almacenando las columnas modificadas de la matriz
    vectAux = np.empty((matriz.shape[0], 1), dtype = 'f')
    # Contador auxiliar que se usara para saber hasta que fila recorrer de la matriz
    contAux = matriz.shape[1] - 2
    # Bucle que recorrera las columnas de la matriz, las modificara y las almacenara en 'matAux'
    for iteracion in range(matriz.shape[1] - 2):
        # Variable que se usara para indexar a 'vectAux'
        indexAux = 0
        # Bucle que llenara de ceros las primeras filas de 'vectAux'
        for cero in (range(iteracion + 1)):
            vectAux[cero, 0] = 0
            indexAux += 1

        vectAux[indexAux:, 0] = matriz[:(matriz.shape[0] - indexAux), (iteracion + 2)]
        # Agrega la columna que se calculo a la matriz auxiliar
        matAux = np.append(matAux, vectAux, axis = 1)

    # Actualiza la matriz a su forma modificada
    matriz = np.append(matriz[:, :2], matAux[:, 1:], axis = 1)

    return matriz

if __name__ == "__main__":
    print(LLenar_Vector_Datos("prueba"))
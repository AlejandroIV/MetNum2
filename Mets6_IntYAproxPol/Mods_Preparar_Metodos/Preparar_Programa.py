"""Modulo que contiene las funciones necesarias para preparar los modulos que contienen los metodos de interpolacion"""

from sage.all import *
import sys
import numpy as np

def LLenar_Matriz_Datos(nombreArchTxt):
    """Funcion que lee un archivo de texto, extrae los datos ingresados y los almacena en una matriz para aplicar los metodos de interpolacion"""
    try:
        archDts = open(f"{nombreArchTxt}.txt", "r")
    except:
        print("\nNo es posible abrir el archivo")
        print("Crea un archivo de texto e ingresa los datos ahí, guardalo con el formato 'txt' y vuelve a correr el programa\n")
        sys.exit(1)

    dts = ""
    # Bucle que recorre todo el archivo
    for parr in archDts:
        # Guarda en la variable 'dts' la cadena de texto con los datos que hay en el archivo de texto en formato 'str'
        dts += parr

    # Separa los datos delimitados por espacios
    dts = dts.split(' ')

    # Crea una matriz para almacenar los datos extraidos del archivo de texto
    matDts = np.empty((len(dts), 2), dtype = 'f')

    cont = 0
    # Bucle que recorre la lista con todos los datos ingresados por el usuario en el archivo de texto para separarlos
    for dato in dts:
        # Variables auxiliares que son los indices de los caracteres que se usan para delimitar los datos y separarlos
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

    # Regresa la matriz con los datos extraidos desde el archivo de texto
    return matDts

def LLenar_Matriz_Datos_Hermite(nombreArchTxt):
    """Funcion que lee un archivo de texto, extrae los datos ingresados y los almacena en una matriz para aplicar el metodo de Interpolacion de Hermite"""
    try:
        archDts = open(f"{nombreArchTxt}.txt", "r")
    except:
        print("\nNo es posible abrir el archivo")
        print("Crea un archivo de texto e ingresa los datos ahí, guardalo con el formato 'txt' y vuelve a correr el programa\n")
        sys.exit(1)

    dts = ""
    # Bucle que recorre todo el archivo
    for parr in archDts:
        # Guarda en la variable 'dts' la cadena de texto con los datos que hay en el archivo de texto en formato 'str'
        dts += parr

    # Separa los datos delimitados por espacios
    dts = dts.split(' ')

    # Crea una matriz para almacenar los datos extraidos del archivo de texto
    matDts = np.zeros(((len(dts) * 2), 3), dtype = 'f')

    cont = 0
    # Bucle que recorre la lista con todos los datos ingresados por el usuario en el archivo de texto para separarlos
    for dato in dts:
        # Variables auxiliares que son los indices de los caracteres que se usan para delimitar los datos y separarlos
        indParentesis1 = dato.find("(")
        indParentesis2 = dato.find(")")
        indComa1 = dato.find(",")
        indComa2 = dato.find(",", (indComa1 + 1))

        # Trata de convertir los datos en formato 'double' y los almacena en 'matDts'
        try:
            matDts[cont:(cont + 2), 0] = float(dato[(indParentesis1 + 1):indComa1])
            matDts[cont:(cont + 2), 1] = float(dato[(indComa1 + 1):indComa2])
            matDts[cont, 2] = float(dato[(indComa2 + 1):indParentesis2])
        except:
            print("\nAlguno de los datos no se ha podido convertir en un formato compatible que pueda usar el programa")
            print("Debe ingresar numeros para poder continuar\n")
            sys.exit(1)
        cont += 2

    # Cierra el archivo
    archDts.close()

    # Regresa la matriz con los datos extraidos desde el archivo de texto
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

    # Si el usuario elige usar la formula de lagrange
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

def OpcionesHer():
    """Funcion que pedira al usuario elegir una opcion en la que se aplica la interpolacion de hermite"""
    # Pide al usuario que elija una de las siguiente opciones
    print("\n1.- Construir el Polinomio Interpolante de Hermite")
    print("2.- Aproximar la funcion en un punto usando el Polinomio Oscultante")

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 3:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    return op

def Modificar_Matriz_DifRegr(matriz):
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

def AlgoritmoNet():
    """Funcion que pedira al usuario elegir que algoritmo de diferencias divididas de newton aplicar"""
    # Pide al usuario que elija una de las siguientes opciones
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

def AlgoritmoTraz():
    """Funcion que pedira al usuario elegir que algoritmo de trazador cubico aplicar"""
    # Pide al usuario que elija una de las siguientes opciones
    print("\nElija el algoritmo que desee aplicar")
    print("1.- Trazador cubico natural")
    print("2.- Trazador cubico sujeto")
    # Crea la lista que contendra los valores que ingrese el usuario para aplicar el metodo de trazadores cubicos
    lista = []

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 3:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Ingresa la opcion elegida por el usuario en la lista 'lista'
    lista.append(op)

    # Si el usuario elije usar el algoritmo para construir la tabla aplicando el algoritmo de trazador cubico sujeto
    if op == 2:
        contAux = 0
        # Tupla que almacenara los valores de las derivadas
        tupla = ()
        derAux = ["inferior", "superior"]
        while contAux < 2:
            try:
                deriv = float(input(f"\nIngrese la derivada del punto {derAux[contAux]}: "))
                contAux += 1
                # Agrega el valor de la derivada que ingresa el usuario a la tupla 'tupla'
                tupla += (deriv,)
            except:
                print("Ingrese un valor numerico!!!")
        # Ingresa los valores de las derivadas a la lista 'lista'
        lista.append(tupla)

    return lista

def RelacionMinCuad():
    """Funcion que pedira al usuario que indique si los datos tienen una relacion exponencial"""
    # Pide al usuario que indique si los datos tiene una relacion exponencial
    while True:
        try:
            op = int(input("Los datos tienen relacion exponencial?\nSi - 1    No - 0: "))
            if op > -1 and op < 2:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    return op

if __name__ == "__main__":
    print(LLenar_Matriz_Datos_Hermite("prueba"))
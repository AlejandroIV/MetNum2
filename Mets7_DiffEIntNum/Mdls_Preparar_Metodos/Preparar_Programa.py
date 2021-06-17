"""Modulo que contiene las funciones necesarias para preparar los modulos que contiene los metodos de derivacion e integracion numerica"""

from sage.all import SR, sage, round
import sys
import numpy as np

def LLenar_Matriz_Datos(nombreArchTxt):
    """Funcion que lee un archivo de texto, extrae los datos ingresados y los almacena en una matriz para aplicar las formulas de derivacion o integracion"""
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
        # Intenta convertir la primera cadena de texto a formato 'SR' (caso de las integrales)
        try:
            # Variable que contendra la funcion
            funcion = SR(dts)
             # Cierra el archivo
            archDts.close()
            # Regresa la funcion en formato 'SR'
            return funcion
        except:
            continue

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

def FormulasDer(matriz):
    """Funcion que pedira al usuario elegir que formula de derivacion numerica aplicar"""
    # Pide al usuario que elija una de las siguientes opciones
    print("\n1.- Derivacion numerica hacia adelante")
    print("2.- Derivacion numerica hacia atras")
    print("3.- Derivacion numerica centrada")
    # Crea la lista que contendra los valores que ingrese el usuario para aplicar las formulas de derivacion numerica
    lista = []

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 4:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Agrega la opcion elegida por el usuario a la lista 'lista'
    lista.append(op)

    np.set_printoptions(precision = 6, suppress = True)

    # Imprime los datos
    print("\nLos datos ingresados son los siguientes:\n")
    # Bucle que recorre la matriz que contiene los datos y los imprime de manera enumerada para que el usuario elija los datos que desee utilizar
    for elem in range(matriz.shape[0]):
        print((elem + 1), end = "   -   ")
        print(matriz[elem, :])

    # Pide al usuario elegir que datos elegir cuantos datos elegir
    while True:
        try:
            op = int(input("\nCuantos valores desea usar (3 o 5)? "))
            if op == 3 or op == 5:
                break
            elif op > matriz.shape[0]:
                print(f"\nNo es posible usar {op} valores porque solo se han ingresado {matriz.shape[0]} valores de entrada")
                print("Agregue mas datos al archivo de texto y vuelve a correr el programa\n")
                sys.exit(1)
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Agrega la opcion elegida por el usuario a la lista 'lista'
    lista.append(op)

    # Crea el vector auxiliar que contendra los valores que se usaran en las formulas
    vectAux = np.empty((op, 2), dtype = 'f')

    # Pide al usuario elegir que datos usar
    for indice in range(op):
        while True:
            try:
                dato = int(input(f"Elije el dato {indice + 1} que desee usar: "))
                if dato > 0 and dato <= matriz.shape[0]:
                    vectAux[indice] = matriz[dato - 1]
                    break
                print("Entrada invalida")
            except:
                print("Entrada invalida")

    # Pide al usuario que ingrese un valor para 'h' positivo
    while True:
        try:
            h = float(input("\nIngrese un valor para 'h': "))
            if h > 0:
                break
            print("Entrada invalida")
        except:
            print("Entrada invalida")

    # Agrega el valor de 'h' ingresado por el usuario a la lista 'lista'
    lista.append(round(h, 6))

    # Extrae un valor dependiendo el tipo de formula que elijio el usuario
    if lista[0] == 1:  # Caso en el que se decide usar la formula hacia adelante
        lista.append(vectAux[0, 0])

    if lista[0] == 2:  # Caso en el que se decide usar la formula hacia atras
        lista.append(vectAux[(vectAux.shape[0] - 1), 0])

    else:  # Caso en el que se decide usar la formula centrada
        if lista[1] == 3:  # Caso en el que se decide usar 3 puntos
            lista.append(vectAux[1, 0])
        
        else:  # Caso en el que se decide usar 5 puntos
            lista.append(vectAux[2, 0])

    # Regresa el vector con los datos que se usaran en la formula y 
    # la lista con los valores [formula, cantidad de valores, el valor de h, punto al que se le va a calcular la derivada]
    return(vectAux, lista)

def FormulasInt_Datos(matriz):
    """Funcion que pedira al usuario elegir que formula de integracion numerica aplicar si ingreso los valores de 'x' y 'y'"""
    # Pide al usuario que elija una de las siguientes opciones
    print("\n1.- Regla del trapecio")
    print("2.- Regla de simpson 1/3")
    print("3.- Regla de simpson 3/8")
    print("4.- Regla del punto medio")
    # Crea la lista que contendra los valores que ingrese el usuario para aplicar las formulas de integracion numerica
    lista = []

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 5:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Agrega la opcion elegida por el usuario a la lista 'lista'
    lista.append(op)

    np.set_printoptions(precision = 6, suppress = True)

    # Imprime los datos
    print("\nLos datos ingresados son los siguientes:\n")
    # Bucle que recorre la matriz que contiene los datos y los imprime de manera enumerada para que el usuario elija los datos que desee utilizar
    for elem in range(matriz.shape[0]):
        print((elem + 1), end = "   -   ")
        print(matriz[elem, :])

    # Pide al usuario elegir que datos elegir cuantos datos elegir
    while True:
        try:
            op = int(input("\nCuantos valores desea usar? "))
            if op > 1 and op <= matriz.shape[0]:
                lista.append(op)
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Crea el vector auxiliar que contendra los valores que se usaran en las formulas
    vectAux = np.empty((op, 2), dtype = 'f')

    # Si el usuario decide usar todos los datos
    if op == matriz.shape[0]:
        vectAux = matriz
    
    # Si el usuario decide no usar todos los datos
    else:
        # Pide al usuario elegir que datos usar
        for indice in range(op):
            while True:
                try:
                    dato = int(input(f"Elije el dato {indice + 1} que desee usar: "))
                    if dato > 0 and dato <= matriz.shape[0]:
                        vectAux[indice] = matriz[dato - 1]
                        break
                    print("Entrada invalida")
                except:
                    print("Entrada invalida")

    # Pide al usuario que ingrese un valor para 'h' positivo
    while True:
        try:
            h = float(input("\nIngrese un valor para 'h': "))
            if h > 0:
                break
            print("Entrada invalida")
        except:
            print("Entrada invalida")

    # Agrega el valor de 'h' ingresado por el usuario a la lista 'lista'
    lista.append(round(h, 6))

    # Regresa el vector con los datos que se usaran en la formula y 
    # la lista con los valores [formula, cantidad de valores, el valor de h]
    return(vectAux, lista)

def FormulasInt_Funcion(funcion):
    """Funcion que pedira al usuario elegir que formula de integracion numerica aplicar si ingreso una funcion"""
    # Pide al usuario que elija una de las siguientes opciones
    print("\n1.- Regla del trapecio")
    print("2.- Regla de simpson 1/3")
    print("3.- Regla de simpson 3/8")
    print("4.- Regla del punto medio")

    # Crea la lista que contendra los valores que ingrese el usuario para aplicar las formulas de integracion numerica
    lista = []

    while True:
        try:
            op = int(input("\nElija una opcion: "))
            if op > 0 and op < 5:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Agrega la opcion elegida por el usuario a la lista 'lista'
    lista.append(op)

    np.set_printoptions(precision = 6, suppress = True)

    while True:
        try:
            x1 = float(input("Ingrese el valor del limite inferior de la integral: "))
            break
        except:
            print("Entrada invalida")

    while True:
        try:
            x2 = float(input("Ingrese el valor del limite superior de la integral: "))
            if x2 > x1:
                break
            print("Entrada invalida")
        except:
            print("Entrada invalida")

    while True:
        try:
            op = int(input("\nCuantos subintervalos desea usar? "))
            if op > 0:
                lista.append(op + 1)
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Calcula el valor de 'h' [Burden p. 197]
    h = (x2 - x1) / op
    # Agrega el valor de 'h' a la lista 'lista'
    lista.append(round(h, 6))

    # Crea la matriz que contendra los valores de 'x' y 'y'
    matDatos = np.empty(((op + 1), 2), dtype = 'f')

    # Primero llena la primera columna con los valores de 'x'
    for priCol in range(op + 1):
        matDatos[priCol, 0] = round(x1 + (h * priCol), 6)

    # Evalua la funcion en cada punto de 'x' y lo almacena en la segunda columna
    for segCol in range(op + 1):
        matDatos[segCol, 1] = funcion.subs(x = matDatos[segCol, 0])

    # Regresa el vector columna con los datos que se usaran en la formula y 
    # la lista con los valores [formula, cantidad de valores, el valor de h]
    return(matDatos, lista)

def IntegralRom():
    """Funcion que pedira al usuario elegir los cantidad los datos necesarios para aplicar la inegral de Romberg"""
    # Crea la lista que contendra los valores que ingrese el usuario para aplicar las formulas de integracion numerica
    lista = []

    print()

    np.set_printoptions(precision = 6, suppress = True)

    while True:
        try:
            x1 = float(input("Ingrese el valor del limite inferior de la integral: "))
            if x1 != '':
                lista.append(x1)
                break
        except:
            print("Entrada invalida")

    while True:
        try:
            x2 = float(input("Ingrese el valor del limite superior de la integral: "))
            if x2 > x1:
                lista.append(x2)
                break
            print("Entrada invalida")
        except:
            print("Entrada invalida")

    while True:
        try:
            op = int(input("\nCuantas aproximaciones iniciales desea usar? "))
            if op > 0:
                lista.append(op)
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    # Regresa la lista con los valores [limite inferior, limite superior, cantidad de iteraciones iniciales]
    return lista

def EvalRom_Funcion(funcion, h, n, inferior):
    """Funcion que evaluara funcion para aplicar la regla del trapecio"""
    # Crea la matriz que contendra los valores de 'x' y 'y'
    matDatos = np.empty(((n + 1), 2), dtype = 'f')

    # Primero llena la primera columna con los valores de 'x'
    for priCol in range(n + 1):
        matDatos[priCol, 0] = round(inferior + (h * priCol), 6)

    # Evalua la funcion en cada punto de 'x' y lo almacena en la segunda columna
    for segCol in range(n + 1):
        matDatos[segCol, 1] = funcion.subs(x = matDatos[segCol, 0])

    # Regresa la matriz con los datos que se usaran aplicando la regla del trapecio
    return matDatos
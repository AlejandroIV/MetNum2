"""Modulo que contiene el Metodo de Broyden para la solucion de sistemas de ecuaciones no lineales"""

from sage.all import *
import sys
import numpy as np
import Preparar_Programa

def Metodo_Broyden(tolerancia, limite, nombre):
    """Funcion que llevara a cabo el Metodo de Broyden"""
    # Primero llena un vector columna con las funciones contenidas en el documento de texto
    vectFun = Preparar_Programa.Llenar_Vector_Funciones(nombre)
    # Despues crea un vector de flotantes que contendra los valores de las variables dados por el usuario   
    vectSol = np.array([4, 2, -3], dtype = 'f')  # LINEA INGRESADA POR EL PROGRAMA
    vectSol = np.reshape(vectSol, (vectSol.shape[0], 1))
    # Declara las variables para poder calcular el jacobiano
    x, y, z = var('x', 'y', 'z')  # LINEA INGRESADA POR EL PROGRAMA

    # Crea la matriz que contendra el jacobiano de las funciones
    matJac = np.empty(0, dtype = type(SR()))
    # Bucle que recorre todo el vector de funciones para calcular la matriz jacobiana y almacenarla en matJac
    for funcion in vectFun:
        # Ira calculando el jacobiano de cada fila
        filaJac = jacobian(funcion[0], (x, y, z))  # LINEA INGRESADA POR EL PROGRAMA
        # Bucle que ira agregando las funciones una por una para separarlas
        for derPar in filaJac[0]:
            matJac = np.append(matJac, derPar)

    # Se usa para considerar una presicion de 6
    np.set_printoptions(precision = 6, suppress = True)

    matJac = np.reshape(matJac, ((vectFun.shape[0]), (vectFun.shape[0])))

    # Crea la matriz que se mandara como parametro para la funcion que va a calcular 'y' (aplicando el Metodo de Jacobi)
    mtrzA = np.empty((matJac.shape[0], (matJac.shape[0])), dtype = 'f')

    # Calcula la norma de 'vectSol'
    normaX1 = np.linalg.norm(vectSol)

    # Crea la matriz que contendra los valores obtenidos en cada iteracion para poder imprimirlos
    matIter = np.copy(vectSol)
    matIter = np.append(matIter, 0)

    # SENTENCIAS INGRESADAS POR EL PROGRAMA
    print('-' * (15 * vectSol.shape[0]))
    print((' ' * 5) + 'x' + (' ' * 4), sep = '', end = '')
    print((' ' * 5) + 'y' + (' ' * 4), sep = '', end = '')
    print((' ' * 5) + 'y' + (' ' * 4), sep = '', end = '')
    print((' ' * 6) + 'error')

    # Declara las variables que se usaran para almacenar las evaluaciones de las funciones
    evalFun1X = np.empty((matJac.shape[0], 1), dtype = 'f')
    evalFun2X = np.empty((matJac.shape[0], 1), dtype = 'f')

    # Bucle anidado que evaluara cada una de las funciones que hay en la matriz jacobiana y cada una que hay
    # en el vector columna que tiene las funciones y los resultados los ira almacenando en la matriz 'mtrzA'
    for cont1 in range(matJac.shape[0]):
        for cont2 in range(matJac.shape[0]):
            mtrzA[cont1, cont2] = matJac[cont1, cont2].subs(x = vectSol[0, 0], y = vectSol[1, 0], z = vectSol[2, 0])  # LINEA INGRESADA POR EL PROGRAMA

    # Almacena en "evalFun1X" la primera evaluacion de las funciones
    for contFun in range(vectFun.shape[0]):
            evalFun1X[contFun, 0] = vectFun[contFun][0].subs(x = vectSol[0, 0], y = vectSol[1, 0], z = vectSol[2, 0])  # LINEA INGRESADA POR EL PROGRAMA
    # Calula la inversa del jacobiano, lo multiplica por el vector que contiene por valores las funciones evaluadas y cambia el signo a negativo
    mtrzA = np.linalg.inv(mtrzA)  # Almacena la inversa del jacobiano en "mtrzA"
    vectS = -(np.matmul(mtrzA, evalFun1X))

    # Calcula la norma de 'vectSol'
    normaX1 = np.linalg.norm(vectSol)

    vectSol += vectS

    # Calcula la norma de 'vectSol'
    normaX2 = np.linalg.norm(vectSol)

    # Ingresa el vector 'vectSol' en una nueva columna de la matriz 'matIter'
    matIter = np.append(matIter, vectSol)

    # Calcula el error aproximado porcentual y almacena el resultado en la variable 'errorAproxPorcen'
    errorAproxPorcen = ((normaX2 - normaX1) / normaX2) * 100

    matIter = np.append(matIter, abs(errorAproxPorcen))

    # Se copia el valor de 'normaX2' en la variable 'normaX1' para que en la siguiente iteracion se considere la norma que se acaba de calcular
    normaX1 = normaX2

    contIt = 1
    # Bucle que se repetira hasta que el error sea menor o igual al permitido
    while(True):
        # Almacena la evaluacion anterior y lo vuelve a evaluar
        evalFun2X = np.copy(evalFun1X)
        for contFun in range(matJac.shape[0]):
            evalFun1X[contFun, 0] = vectFun[contFun][0].subs(x = vectSol[0, 0], y = vectSol[1, 0], z = vectSol[2, 0])  # LINEA INGRESADA POR EL PROGRAMA
        # Almacena la diferencia de las evaluaciones en "diferEval"
        diferEval = evalFun1X - evalFun2X

        # Multiplica la matriz por la diferencia de las funciones y cambia el signo a negativo
        vectZ = -(np.matmul(mtrzA, diferEval))
        # Multiplica "vectS" traspuesto por "vectZ" y lo cambia de signo a negativo
        numP = -(np.matmul(np.reshape(vectS, (1, matJac.shape[0])), np.reshape(vectZ, (matJac.shape[0], 1))))
        # Multiplica "vectS" traspuesto por la matriz "mtrzA"
        vectUTransp = np.matmul(np.reshape(vectS, (1, matJac.shape[0])), mtrzA)

        # Determina el nuevo valor de la matriz "mtrzA"
        mtrzA = mtrzA + np.matmul(((1 / numP) * (vectS + vectZ)), vectUTransp)

        # Determina el nuevo valor para "vectS"
        vectS = -(np.matmul(mtrzA, evalFun1X))

        vectSol += vectS

        contIt += 1

        # Ingresa el vector 'vectSol' en una nueva columna de la matriz 'matIter'
        matIter = np.append(matIter, vectSol)

        # Calcula la norma de 'vectSol'
        normaX2 = np.linalg.norm(vectSol)

        # Calcula el error aproximado porcentual y almacena el resultado en la variable 'errorAproxPorcen'
        errorAproxPorcen = ((normaX2 - normaX1) / normaX2) * 100

        matIter = np.append(matIter, abs(errorAproxPorcen))

        if abs(errorAproxPorcen) < tolerancia:
            break

        if contIt == limite:
            matIter = np.reshape(matIter, ((contIt + 1), (vectSol.shape[0] + 1)))
            print("-" * (15 * vectSol.shape[0]))
            # Se imprimen los resultados por cada iteracion
            print(matIter)
            print("-" * (15 * vectSol.shape[0]))
            # En caso que se hayan hecho 'x' iteraciones, entonces suponemos que
            # no se ha determinado el resultado y se detiene la ejecucion del programa
            print("\n\nSe ha llegado al limite de iteraciones y no se ha encontrado un posible resultado")
            print("Pruebe con otro vector inicial\n\n")
            sys.exit(1)

        # Se copia el valor de 'normaX2' en la variable 'normaX1' para que en la siguiente iteracion se considere la norma que se acaba de calcular
        normaX1 = normaX2

    matIter = np.reshape(matIter, ((contIt + 1), (vectSol.shape[0] + 1)))

    print("-" * (15 * vectSol.shape[0]))
    # Se imprimen los resultados por cada iteracion
    print(matIter)
    print("-" * (15 * vectSol.shape[0]))
    print("\nSe contaron ", contIt, "iteraciones\n")

    # Regresa la solucion aproximada
    return vectSol

def Broy(FNombre):
    error = float(input("Ingresa la tolerancia: "))
    lim = float(input("Ingresa el limite de iteraciones: "))
    print()
    print(Metodo_Broyden(error, lim, FNombre))

if __name__ == "__main__":
    error = float(input("Ingresa la tolerancia: "))
    lim = float(input("Ingresa el limite de iteraciones: "))
    FNombre = input("Ingresa el nombre del archivo: ")
    print()
    print(Metodo_Broyden(error, lim, FNombre))
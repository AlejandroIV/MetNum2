"""Modulo que contiene las formulas de la Integracion Numerica (Integral de Romberg)"""

from sage.all import SR, sage, round
import numpy as np
import sys
from Mdls_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, IntegralRom, EvalRom_Funcion

def Integracion_Romberg(nombre):
    """Funcion que llevara a cabo la Integral de Romberg"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    funcion = LLenar_Matriz_Datos(nombre)

    # Si el usuario ingreso datos
    if type(funcion) != type(SR()):
        print("\n\nDebe ingresar una funcion\n\n")
        sys.exit(1)

    # Primero pide los datos al usuario
    datosUsr = IntegralRom()

    # Crea la matriz que contendra los valores de las iteraciones de la integral de Romberg
    matRom = np.zeros((datosUsr[2], datosUsr[2]), dtype = 'f')

    # Bucle que calculara las primeras aproximaciones
    for cont in range(datosUsr[2]):
        # Llama a la funcion para realizar las evaluaciones necesarias y los almacena en la matriz 'matDatos'
        matDatos = EvalRom_Funcion(funcion, ((datosUsr[1] - datosUsr[0]) / (2 ** cont)), (2 ** cont), datosUsr[0])

        # Termino que multiplica a las sumas
        integral = ((datosUsr[1] - datosUsr[0]) / (2 ** cont)) / 2
        # Termino de las sumas
        sumatoria = matDatos[-1, 1] + matDatos[0, 1]
        for suma in range(1, (2 ** cont)):
            sumatoria += 2 * matDatos[suma, 1]

        integral *= sumatoria

        # Almacena los valores de las primeras aproximaciones en la primera columna de la matriz 'matDatos'
        matRom[cont, 0] = integral

    # Bucle anidado que aplicara la formula para la integral del Romberg [Burden p. 209]
    for col in range(1, matRom.shape[0]):
        for fila in range(col, matRom.shape[0]):
            matRom[fila, col] = (((4 ** col) * matRom[fila, (col - 1)]) - matRom[(fila - 1), (col - 1)]) / ((4 ** col) - 1)

    # Crea el vector que contendra los errores de las integrales de Romberg
    vectErr = np.zeros((matRom.shape[0], 1), dtype = 'f')
    # Bucle que recorre todas los elementos de la diagonal
    for error in range(1, matRom.shape[0]):
        vectErr[error] = abs(matRom[error, error] - matRom[(error - 1), (error - 1)])

    # Anexa los valores de los errores a la matriz 'matRom'
    matRom = np.append(matRom, vectErr, axis = 1)

    # Imprime la matriz 'matRom'
    print("\n" + "\n".join([''.join(['{:13}'.format(round(val, 8)) for val in fila]) for fila in matRom]) + "\n")

    print(f"\nUsando la integracion de Romberg")
    print(f"La aproximacion de la integral de x = {datosUsr[0]} a x = {datosUsr[1]}", end = " ")
    print(f"con {datosUsr[2]} iteraciones es: {round(matRom[-1, -2], 8)}, con un error de: {round(matRom[-1, -1], 8)}\n\n")

def IntegracionRomberg():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Integracion_Romberg(fNombre)

if __name__ == "__main__":
    Integracion_Romberg("prueba")
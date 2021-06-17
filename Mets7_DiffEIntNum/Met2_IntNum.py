"""Modulo que contiene las formulas de la Integracion Numerica (Newton Cotes)"""

from sage.all import SR, sage, round
import numpy as np
import sys
from Mdls_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, FormulasInt_Funcion, FormulasInt_Datos

def Integracion_Numerica(nombre):
    """Funcion que aplicara las formulas de Integracion Numerica"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatosOFuncion = LLenar_Matriz_Datos(nombre)

    # Si el usuario ingreso la funcion
    if type(matDatosOFuncion) == type(SR()):
        dtsFormulas = FormulasInt_Funcion(matDatosOFuncion)
    
    # Si el usuario ingreso valores de 'x' y 'y'
    else:
        # Pide al usuario una opcion
        dtsFormulas = FormulasInt_Datos(matDatosOFuncion)

    # Si el usuario decide usar la regla del trapecio [Burden p. 192]
    if dtsFormulas[1][0] == 1:  # Aplicable con cualquier cantidad de datos
        # Termino que multiplica a las sumas
        integral = dtsFormulas[1][2] / 2
        # Termino de las sumas
        sumatoria = dtsFormulas[0][0, 1] + dtsFormulas[0][(dtsFormulas[1][1] - 1), 1]
        for suma in range(1, (dtsFormulas[1][1] - 1)):
            sumatoria += 2 * dtsFormulas[0][suma, 1]

    # Si el usuario decide usar la regla de simpson 1/3
    elif dtsFormulas[1][0] == 2 and (dtsFormulas[1][1] - 1) % 2 == 0:  # Aplicable solo cuando la cantidad de subintervalos es par
        # Termino que multiplica a las sumas
        integral = (dtsFormulas[1][2] / 3)
        # Termino de las sumas
        sumatoria = dtsFormulas[0][0, 1] + dtsFormulas[0][(dtsFormulas[1][1] - 1), 1]
        for suma in range(1, (dtsFormulas[1][1] - 1)):
            # Terminos con indice impar
            if suma % 2 != 0:
                sumatoria += 4 * dtsFormulas[0][suma, 1]
            # Terminos con indice par
            else:
                sumatoria += 2 * dtsFormulas[0][suma, 1]

    # Si el usuario decide usar la regla de simpson 3/8
    elif dtsFormulas[1][0] == 3 and (dtsFormulas[1][1] - 1) % 3 == 0:  # Aplicable solo cuando la cantidad de subintervalos es multiplo de 3
        # Termino que multiplica a las sumas
        integral = ((3 * dtsFormulas[1][2]) / 8)
        # Termino de las sumas
        sumatoria = dtsFormulas[0][0, 1] + dtsFormulas[0][(dtsFormulas[1][1] - 1), 1]
        for suma in range(1, (dtsFormulas[1][1] - 1)):
            # Terminos con indice multiplo de 3
            if suma % 3 == 0:
                sumatoria += 2 * dtsFormulas[0][suma, 1]
            # Terminos con los indices restantes
            else:
                sumatoria += 3 * dtsFormulas[0][suma, 1]

    # Si el usuario decide usar la regla del punto medio
    elif dtsFormulas[1][0] == 4 and (dtsFormulas[1][1] - 1) % 2 == 0:  # Aplicable solo cuando la cantidad de subintervalos es par
        # Termino que multiplica a las sumas
        integral = 2 * dtsFormulas[1][2]
        # Termino de las sumas
        sumatoria = 0
        for suma in range(1, (dtsFormulas[1][1] - 1)):
            # Terminos con indice impar
            if suma % 2 != 0:
                sumatoria += dtsFormulas[0][suma, 1]

    # Si no hay cantidad suficiente de subintervalos
    else:
        print(f"\nSe requiere que la cantidad de subintervalos sea compatible con la formula que se desea usar")
        print("Revise su entrada\n")
        sys.exit(1)

    integral *= sumatoria

    # Imprime el resultado
    listaAux = ["regla del trapecio", "regla de simpson 1/3", "regla de simpson 3/8", "regla del punto medio"]
    print(f"\n\nUsando la formula de integracion numerica {listaAux[dtsFormulas[1][0] - 1]} y con h = {dtsFormulas[1][2]}")
    print(f"La aproximacion de la integral de x = {dtsFormulas[0][0, 0]} a x = {dtsFormulas[0][(dtsFormulas[1][1] - 1), 0]}", end = " ")
    print(f"con {dtsFormulas[1][1] - 1} subintervalos es: {round(integral, 7)}\n\n")

def IntegracionNumerica():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Integracion_Numerica(fNombre)

if __name__ == "__main__":
    Integracion_Numerica("prueba")
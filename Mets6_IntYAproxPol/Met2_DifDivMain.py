"""Modulo que contiene el codigo para construir el Polinomio Interpolante de Newton"""

from sage.all import *
import sys
import numpy as np
from Mets6_IntYAproxPol.Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, OpcionesDifDiv

def Interpolacion_Diferencias_Divididas(nombre):
    """Funcion que construira el Polinomio Interpolante de Newton"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    # Crea un vector columna auxiliar para ir guardando lo resultados que se almacenaran en a tabla
    vectResultadosAux = np.empty((matDatos.shape[0], 1), dtype = 'f')
    # Contador que se usara para saber que columna de 'matDatos' se va a utilizar para calcular el numerador
    cont1 = 1
    # Bucle que se repetira hasta calcular la ultima diferencia dividida posible
    for diferenciaDividida in range(matDatos.shape[0] - 1):
        # Contador que se va a usar para saber que fila de 'matDatos' se va a utilizar para calcular el sustraendo del denominador
        cont2 = 0  # Este contador tambien se va a utilizar para indexar a 'vectResultadosAux'
        # Bucle que calcula los elementos de la tabla de diferencias divididas
        for elemRengl in range(cont1, matDatos.shape[0]):
            # La variable 'elemRengl' va a indexar la fila del valor de x que se va a usar en el minuendo (primer elemento de la resta)
            resultado = (matDatos[(cont2 + 1), cont1] - matDatos[(cont2), cont1]) / (matDatos[elemRengl, 0] - matDatos[cont2, 0])
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
    # Lista que contendra los terminos lineales
    terLin = []
    # Bucle que construye el polinomio usando como coeficientes los elementos de la primera fila de la matriz
    for coeficientes in range(num + 1):
        polinomio += f"({round(matDatos[0, (coeficientes + 1)], 8)}"
        if coeficientes == 0:
            polinomio += ")+"
            # Agrega un nuevo termino a la lista
            terLin.append(f"(x - {round(matDatos[coeficientes, 0], 6)})")
            continue
        # Bucle que agregara los terminos lineales al polinomio
        for terminosLineales in terLin:
            polinomio += f" * {terminosLineales}"
        polinomio += ")+"

        # Agrega un nuevo termino a la lista de terminos lineales
        terLin.append(f"(x - {round(matDatos[coeficientes, 0], 6)})")

        cont1 += 1  # No se usa BORRAR

    # Elimina el ultimo signo '+' que esta en la cadena que contiene el polinomio
    polinomio = polinomio[:(len(polinomio) - 1)]

    opcion = OpcionesDifDiv()

    if opcion == 1:
        # Imprime el polinomio interpolante
        print(f"\n\nEl Polinomio Interpolante es: {polinomio}\n")

        while True:
            print("Desea simplificar? Si - 1, No - 2: ", end = '')
            try:
                opcion = int(input())
                if opcion > 0 and opcion < 3:
                    print()
                    break
                print("Opcion invalida!!!")
            except:
                print("Opcion invalida!!!")

        # Si el usuario desea simplificar el polinomio lo convierte a formato sagemath y lo simplifica
        if opcion == 1:
            polinomio = SR(polinomio)

            # Simplifica el polinomio resultante y lo imprime
            print(f"\n\nEl Polinomio Interpolante es: {polinomio.simplify_full()}\n")

    else:  # Sustituye el punto que se quiere calcular por las 'x' que aparecen en la cadena de caracteres que contiene el polinomio
        x = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa
        polinomio = polinomio.replace('x', str(x))
        polinomio = SR(polinomio)

        # Simplifica el resultado y lo imprime redondeandolo a 8 decimales
        print(f"\n\nEl valor de la funcion en el punto {x} es aproximadamente: {round(polinomio.simplify_full(), 8)}\n")

def DiferenciasDivididas():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Interpolacion_Diferencias_Divididas(fNombre)

if __name__ == "__main__":
    Diferencias_Divididas("prueba")
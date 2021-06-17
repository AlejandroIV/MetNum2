"""Modulo que contiene el codigo para construir el Polinomio Interpolante de Newton"""

from sage.all import SR, sage, round
import sys
import numpy as np
from Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, OpcionesDifDiv

def Interpolacion_Diferencias_Divididas(nombre):
    """Funcion que construira el Polinomio Interpolante de Newton"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)
    # Une la matriz 'matDatos' con otra matriz de ceros de orden n x n - 1, donde n es el numero de datos
    matDatos = np.copy(np.append(matDatos, np.zeros((matDatos.shape[0], (matDatos.shape[0] - 1)), dtype = 'f'), axis = 1))

    # Bucle que se repetira hasta calcular la ultima diferencia dividida posible
    # Este contador se utilizara para indexar los valores de las columnas de 'matDatos' [Burden p. 124]
    for cont1 in range(1, matDatos.shape[0]):
        #  Este contador se utilizara para indexar los valores de las filas de 'matDatos'
        cont2 = 0
        # Bucle que calcula los elementos de la tabla de diferencias divididas
        for elemRengl in range(cont1, matDatos.shape[0]):
            # La variable 'elemRengl' va a indexar la fila del valor de x que se va a usar en el minuendo (primer elemento de la resta)
            matDatos[cont2, (cont1 + 1)] = (matDatos[(cont2 + 1), cont1] - matDatos[cont2, cont1]) / (matDatos[elemRengl, 0] - matDatos[cont2, 0])
            cont2 += 1

    np.set_printoptions(precision = 6, suppress = True)

    # Imprime la matriz 'matDatos'
    print("\n" + "\n".join([''.join(['{:12}'.format(round(val, 6)) for val in fila]) for fila in matDatos]) + "\n")

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
    polinomio = f"({round(matDatos[0, 1], 8)})+"  # Primero agrega el primer termino del polinomio (constante)
    # Lista que contendra los terminos lineales
    terLin = [f"(x - {round(matDatos[0, 0], 6)})"]  # Almacena el primer termino lineal en la lista
    # Bucle que construye el polinomio usando como coeficientes los elementos de la primera fila de la matriz
    for coeficientes in range(1, num + 1):
        polinomio += f"({round(matDatos[0, (coeficientes + 1)], 8)}"
        # Bucle que agregara los terminos lineales al polinomio
        for terminosLineales in terLin:
            polinomio += f" * {terminosLineales}"
        polinomio += ")+"

        # Agrega un nuevo termino a la lista de terminos lineales
        terLin.append(f"(x - {round(matDatos[coeficientes, 0], 6)})")

    # Elimina el ultimo signo '+' que esta en la cadena que contiene el polinomio
    polinomio = polinomio[:(len(polinomio) - 1)]

    # Pide al usuario que elija una opcion
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
    Interpolacion_Diferencias_Divididas("prueba")
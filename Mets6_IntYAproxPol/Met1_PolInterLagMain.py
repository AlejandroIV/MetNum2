"""Modulo que contiene el codigo para construir el Polinomio Interpolante de Lagrange y el Método de Neville"""

from sage.all import *
import sys
import numpy as np
from Mets6_IntYAproxPol.Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, OpcionesLag

def Interpolacion_Lagrange(nombre):
    """Funcion que construira el Polinomio Interpolante de Lagrange"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    # Manda a llamar a la funcion 'Opciones' para pedir al usuario que elija una opcion para usar la formula de lagrange, saber cuales son
    # los datos que el usuario desea elegir y para almacenar los indices de las filas de 'matDatos' que se van a usar en 'indicesDatos'
    indicesDatos = OpcionesLag(matDatos)

    # Revisa el contenido del primer elemento de 'indicesDatos' para saber que opcion eligio el usuario
    if indicesDatos[0] == 1 or indicesDatos[0] == 2:  # Construye el Polinomio Interpolante de Lagrange
        opcionAux = indicesDatos[0]
        # Elimina el primer elemento de 'indicesDatos'
        indicesDatos = indicesDatos[1:]
        # Ordena los indices de forma ascendente y elimina los valores duplicados
        indicesDatos = list(set(indicesDatos))

        # Crea la lista que contendra los polinomios de lagrange
        PolinomiosInterLag = list()

        # Declara las variables que contendran la expresiones que estaran en el numerador y en el denominador de cada polinomio de lagrange
        numerador = ""
        denominador = ""

        cont = 0
        # Bucle que construye el polinomio interpolante de lagrange
        for elemento in indicesDatos:
            # Bucle que construira el numerador
            for elemNum in indicesDatos:
                # Condicional que se saltara este paso en caso de que lleguemos al elemento que no ira en el numerdor
                if elemNum == elemento:
                    # Almacena en la variable 'elemFunAux' el indice del valor que estamos saltando para despues
                    # usarlo al multiplicar los polinomio interpolantes por el valor de la funcion en ese punto
                    elemFunAux = elemNum
                    continue
                else:
                    numerador += f"(x - {matDatos[elemNum, 0]})*"
            # Elimina el ultimo signo '*' de la cadena almacenada en la variable 'numerador'
            numerador = "(" + numerador[:(len(numerador) - 1)] + ")"

            # Bulce que construira el denominador
            for elemDen in indicesDatos:
                # Condicional que se saltara este paso en caso de que lleguemos al elemento que no ira en el numerdor
                if elemDen == elemento:
                    continue
                else:
                    denominador += f"({matDatos[elemento, 0]} - {matDatos[elemDen, 0]})*"
            # Elimina el ultimo signo '*' de la cadena almacenada en la variable 'denominador'
            denominador = "(" + denominador[:(len(denominador) - 1)] + ")"

            # Agrega a la lista de polinomio el polinomio que se forma con el numerador y el denominador de los bucles anteriores
            PolinomiosInterLag.append(f"{numerador} / {denominador}")

            numerador = ""
            denominador = ""

            # Multiplica el polinomio interpolante de lagrange por el valor de la funcion 
            PolinomiosInterLag[cont] = "(" + f"({round(matDatos[elemFunAux, 1], 6)}) * " + f"({PolinomiosInterLag[cont]})" + ")"

            cont += 1

        # Declara variable que contendra el polinomio aplicando la formula de lagrange
        polinomio = ""

        # Bucle que convertira de formato 'srt' a formato de sagemath los polinomios obtenidos por los bucles anteriores y los sumara
        for pol in PolinomiosInterLag:
            polinomio += pol + "+"

        # Elimina el ultimo signo '+' de la cadena almacenada en la variable 'polinomio'
        polinomio = polinomio[:(len(polinomio) - 1)]

        if opcionAux == 1:  # Convierte la cadena de caracteres que contiene el polinomio en formato de sagemath
            polinomio = SR(polinomio)

            # Simplifica el polinomio resultante y lo imprime
            print(f"\n\nEl Polinomio Interpolante es: {polinomio.simplify_full()}\n")

        else:  # Sustituye el punto que se quiere calcular por las 'x' que aparecen en la cadena de caracteres que contiene el polinomio
            x = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa
            polinomio = polinomio.replace('x', str(x))
            polinomio = SR(polinomio)

            # Simplifica el resultado y lo imprime redondeandolo a 8 decimales
            print(f"\n\nEl valor de la funcion en el punto {x} es aproximadamente: {round(polinomio.simplify_full(), 8)}\n")

    #elif indicesDatos[0] == 3:  # Aplica el metodo de Neville
    #    print("nada")

def Lagrange():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Interpolacion_Lagrange(fNombre)

if __name__ == "__main__":
    Interpolacion_Lagrange("prueba")
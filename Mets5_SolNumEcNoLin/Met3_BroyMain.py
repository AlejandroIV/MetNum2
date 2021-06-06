"""Modulo que coordina: pide los datos al usuario para poder correr el programa que contiene el Metodo de Broyden"""

from Met_Broyden.Preparar_Programa import Identificar_Variables, Escribir_Programa

def Broyden():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    listaVars = Identificar_Variables(fNombre)
    print("\nElije alguna de las siguientes opciones: ")
    print("1 - Usar el Metodo de Jacobi para determinar el valor del vector 's'")
    print("2 - Calcular la inversa de la matriz jacobiana para determinar el valor del vector 's'")
    opc = int(input("Opcion: "))
    print()
    Escribir_Programa(listaVars)
    from Met3_Broyden import Broy
    Broy(fNombre, opc)
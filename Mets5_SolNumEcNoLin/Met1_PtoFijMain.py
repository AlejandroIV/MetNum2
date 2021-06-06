"""Modulo que coordina: pide los datos al usuario para poder correr el programa que contiene el Metodo del Punto Fijo"""

from Met_Punto_Fijo.Preparar_Programa import Identificar_Variables, Escribir_Programa

def Punto_Fijo():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    listaVars = Identificar_Variables(fNombre)
    Escribir_Programa(listaVars)
    from Met1_PuntoFijo import Pto_Fij
    Pto_Fij(fNombre)
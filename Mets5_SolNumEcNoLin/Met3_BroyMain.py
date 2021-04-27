"""Modulo que coordina: pide los datos al usuario para poder correr el programa que contiene el Metodo de Broyden"""

from Mets5_SolNumEcNoLin.Met_Broyden.Preparar_Programa import Identificar_Variables, Escribir_Programa

def Broyden():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    listaVars = Identificar_Variables(fNombre)
    Escribir_Programa(listaVars)
    from Mets5_SolNumEcNoLin.Met3_Broyden import Broy
    Broy(fNombre)

if __name__ == "__main__":
    Broyden()
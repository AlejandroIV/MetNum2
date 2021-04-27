"""Modulo que coordina: pide los datos al usuario para poder correr el programa que contiene el Metodo de Newton"""

from Mets5_SolNumEcNoLin.Met_Newton.Preparar_Programa import Identificar_Variables, Escribir_Programa

def Newton():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    listaVars = Identificar_Variables(fNombre)
    print("\nElije alguna de las siguientes opciones: ")
    print("1 - Usar el Metodo de Jacobi para determinar el valor del vector 'y'")
    print("2 - Calcular la inversa de la matriz jacobiana para determinar el valor del vector 'y'")
    opc = int(input("Opcion: "))
    print()
    Escribir_Programa(listaVars, opc)
    from Mets5_SolNumEcNoLin.Met2_Newton import Newt
    Newt(fNombre, opc)

if __name__ == "__main__":
    Newton()
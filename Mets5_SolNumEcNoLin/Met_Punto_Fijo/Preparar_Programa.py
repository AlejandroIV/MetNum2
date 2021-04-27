"""Modulo que contiene las funciones necesarias para preparar el codigo para el modulo 'Met1_PuntoFijo.py'"""

from sage.all import *
import sys
import numpy as np

def Llenar_Vector_Funciones(nombreArchTxt):
    """Funcion que lee un archivo de texto, extrae las expresiones que estan despues de un signo '=' y las almacena en un vector columna"""
    try:
        # Se ubica a dos directorios anteriores porque esta funcion es llamada desde un programa en el directorio donde esta la funcion principal
        archFun = open(f"{nombreArchTxt}.txt", "r")  
    except:
        print("\nNo es posible abrir el archivo")
        print("Crea un archivo de texto nuevo e ingresa las funciones ahí, guardalo con el formato 'txt' vuelve a correr el programa\n")
        sys.exit(1)

    contFun = 0
    # Bucle que recorre todo el archivo y cuenta cuantas expresiones hay en el archivo
    for parr in archFun:
        contFun += 1

    # Crea vector que contendra las expresiones que escriba el usuario en el archivo de texto
    matFun = np.empty((contFun, 1), dtype = type(SR()))

    # Regresa al principio del documento
    archFun.seek(0)

    contFun = 0
    # Bucle que recorre todo el archivo para extraer las expresiones que aparecen despues del signo '=' en cada linea
    for linea in archFun:
        indIn = linea.find("=")
        # Intenta pasar cada linea del archivo de texto a formato de funciones de sagemath
        try:
            matFun[contFun, 0] = SR(linea[(indIn + 1):])
        except:
            print("\nNo ha sido posible convertir alguna de las expresiones en un formato compatible con el programa")
            print("Revise la documentacion de SageMath para ver como se pueden ingresar las expresiones\n")
            sys.exit(1)
        contFun += 1

    # Cierra el archivo
    archFun.close()

    # Regresa el vector columna con las expresiones leidas desde el archivo de texto
    return matFun

def Identificar_Variables(nombreArchTxt):
    """Funcion que leera el documento de texto de nuevo para identificar las variables y le pedira al usuario los valores iniciales para cada una"""
    try:
        arch = open(f"{nombreArchTxt}.txt", "r")
    except:
        print("\nNo es posible abrir el archivo")
        print("Crea un archivo de texto nuevo e ingresa las funciones ahí, guardalo con el formato 'txt' vuelve a correr el programa\n")
        sys.exit(1)

    # Crea la lista que contendra los nombres de las variables
    listaVar = []

    # Bucle que recorre todo el archivo para extraer las variables
    for linea in arch:
        indIn = linea.find("=")
        # Intenta pasar cada linea del archivo de texto a formato de funciones de sagemath
        try:
            listaVar.append(linea[:(indIn + 1)])
        except:
            print("\nNo ha sido posible identificar las variables en el archivo de texto")
            print("Asegurese de escribir en el archivo de texto lo siguiente:")
            print("'Nombre de variable' = 'Expresion'\n")
            sys.exit(1)

    print("\nSe han identificado las siguientes variables: ", end = "")
    # Bucle que imprimira las variables que se han identificado
    for variables in listaVar:
        print(variables[0], end = "  ")
    print()

    # Sentencias para verificar si las variables identificadas por el programa son las que se necesitan para hacer los calculos
    verificacion = input("Es correcta la identificacion de variables? (S/N): ")
    if verificacion == "N":
        print("\nPor favor revisa el archivo de texto donde ingreso las expresiones y comprueba que las expresiones tengan la siguiente estructura: ")
        print("'Nombre de variable' = 'Expresion'\n")
        sys.exit(1)

    cont = 0

    # Bucle que recorrera la lista de variables y le pedira un valor al usuario
    for var in listaVar:
        valIn = input(f"Ingresa el valor para la variable {listaVar[cont][0]}: ")
        listaVar[cont] = listaVar[cont] + " " + valIn
        cont += 1

    return listaVar

def Escribir_Programa(listaVariables):
    # Abre el archivo de texto con el codigo en modo lectura
    fin = open("Mets5_SolNumEcNoLin/Met_Punto_Fijo/Codigo.txt", "r")
    # Abre el archivo '.py' para escribir el codigo en modo escritura
    fout = open("Mets5_SolNumEcNoLin/Met1_PuntoFijo.py", "w")

    contLinea = 0
    # Bucle que recorre todas las lineas del documento de texto
    for linea in fin:
        # Agrega la primera fila que se debe modificar
        if linea.startswith("PRIMERA1"):
            cadena = "    vectSol = np.array(["
            for elemento in listaVariables:
                indiceIn = elemento.find("=")
                cadena += f"{elemento[(indiceIn + 1):]},"
            cadena = cadena[:(len(cadena) - 1)]
            cadena += "]"
            cadena += ", dtype = 'f')\n"
            fout.write(cadena)
        # Agrega las sentencias que se deben modificar
        elif linea.startswith("SENTENCIAS1"):
            cadena = "    print('-' * (15 * vectSol.shape[0]))\n"
            for elemento in listaVariables:
                cadena += f"    print((' ' * 5) + '"
                cadena += f"{elemento[0]}"
                cadena += "' + (' ' * 4), sep = '', end = '')\n"
            cadena += "    print((' ' * 6) + 'error')\n"
            fout.write(cadena)
        # Agrega la segunda fila que se debe modificar
        elif linea.startswith("SEGUNDA2"):
            contAux = 0
            cadena = "            vectSol[cont] = vectFun[cont, 0].subs("
            for elemento in listaVariables:
                cadena += f"{elemento[0]} = "
                cadena += f"vectSol[{contAux}], "
                cadena = cadena[:(len(cadena) - 1)]
                contAux += 1
            cadena += ")\n"
            fout.write(cadena)
        else:
            fout.write(linea)

    # Cierra los archivos de texto
    fin.close()
    fout.close()

if __name__ == "__main__":
    Llenar_Vector_Funciones()
    Escribir_Programa()
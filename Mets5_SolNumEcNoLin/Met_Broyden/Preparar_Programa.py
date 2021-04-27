"""Modulo que contiene las funciones necesarias para preparar el codigo para el modulo 'Met2_Newton.py'"""

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

    # Bucle que recorre el archivo para extraer lo que aparece despues del signo '=' en el archivo de texto
    for linea in archFun:
        indIn = linea.find("=")
        funciones = linea[(indIn + 1):]
    # Elimina las llaves que hay en la cadena
    indLlave1 = funciones.find("[")
    indLlave2 = funciones.find("]")
    funciones = funciones[(indLlave1 + 1):indLlave2]

    # Separa las funciones delimitadas por comas
    funciones = funciones.split(',')

    # Crea vector que contendra las expresiones que escriba el usuario en el archivo de texto
    matFun = np.empty((len(funciones), 1), dtype = type(SR()))

    contFun = 0
    # Recorre la lista de funciones, intenta convertir a formato de funciones de sagemath y las almacena en el vector de funciones
    for funcion in funciones:
        try:
            matFun[contFun, 0] = SR(funcion)
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

    # Bucle que recorre el archivo para extraer lo que aparece antes del signo '=' en el archivo de texto
    for linea in arch:
        indIn = linea.find("=")
        listaVar = linea[:(indIn)]

    # Elimina los parentesis de la cadena
    listaVar = listaVar.replace(" ", "")
    indParent1 = listaVar.find("(")
    indParent2 = listaVar.find(")")
    listaVar = listaVar[(indParent1 + 1):indParent2]

    # Separa las variables delimitadas por comas
    listaVar = listaVar.split(',')

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
        listaVar[cont] = listaVar[cont][0] + "=" + valIn
        cont += 1

    return listaVar

def Escribir_Programa(listaVariables):
    # Abre el archivo de texto con el codigo en modo lectura
    fin = open("Mets5_SolNumEcNoLin/Met_Broyden/Codigo.txt", "r")
    # Abre el archivo '.py' para escribir el codigo en modo escritura
    fout = open("Mets5_SolNumEcNoLin/Met3_Broyden.py", "w")

    contLinea = 0
    # Bucle que recorre todas las lineas del documento de texto
    for linea in fin:
        # Agrega la primera fila que se debe modificar
        if linea.startswith("PRIMERA1"):
            cadena = "    vectSol = np.array(["
            for elemento in listaVariables:
                indiceIn = elemento.find("=")
                cadena += f"{elemento[(indiceIn + 1):]},"
            cadena = cadena[:(len(cadena) - 1)] + "], dtype = 'f')\n"
            fout.write(cadena)
        # Agrega la segunda fila que se debe modificar
        elif linea.startswith("SEGUNDA2"):
            cadena = "    "
            for elemento in listaVariables:
                cadena += f"{elemento[0]},"
            cadena = cadena[:(len(cadena) - 1)]
            cadena += " = var("
            for elemento in listaVariables:
                cadena += f"'{elemento[0]}',"
            cadena = cadena[:(len(cadena) - 1)]
            cadena += ")\n"
            fout.write(cadena)
        # Agrega la tercera fila que se debe modificar
        elif linea.startswith("TERCERA3"):
            cadena = "        filaJac = jacobian(funcion[0], ("
            for elemento in listaVariables:
                cadena += f"{elemento[0]},"
            cadena = cadena[:(len(cadena) - 1)]
            cadena += "))\n"
            fout.write(cadena)
        # Agrega las sentencias que se deben modificar
        elif linea.startswith("SENTENCIAS1"):
            cadena = "    print('-' * (15 * vectSol.shape[0]))\n"
            for elemento in listaVariables:
                cadena += f"    print((' ' * 5) + '{elemento[0]}' + (' ' * 4), sep = '', end = '')\n"
            cadena += "    print((' ' * 6) + 'error')\n"
            fout.write(cadena)
        # Agrega la cuarta fila que se debe modificar
        elif linea.startswith("CUARTA4"):
            cadena = f"            mtrzA[cont1, cont2] = matJac[cont1, cont2].subs("
            cont = 0
            for elemento in listaVariables:
                cadena += f"{elemento[0]} = vectSol[{cont}, 0],"
                cont += 1
            cadena = cadena[:(len(cadena) - 1)]
            cadena += ")\n"
            fout.write(cadena)
        elif linea.startswith("QUINTA5") or linea.startswith("SEXTA6"):
            cadena = "            evalFun1X[contFun, 0] = vectFun[contFun][0].subs("
            cont = 0
            for elemento in listaVariables:
                cadena += f"{elemento[0]} = vectSol[{cont}, 0],"
                cont += 1
            cadena = cadena[:(len(cadena) - 1)]
            cadena += ")\n"
            fout.write(cadena)
        else:
            fout.write(linea)

    # Cierra los archivos de texto
    fin.close()
    fout.close()

if __name__ == "__main__":
    print(Llenar_Vector_Funciones("FunMul"))
    print(Identificar_Variables("FunMul"))  
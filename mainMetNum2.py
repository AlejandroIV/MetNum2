from Mets5_SolNumEcNoLin.Met1_PtoFijMain import Punto_Fijo
from Mets5_SolNumEcNoLin.Met2_NewMain import Newton
from Mets5_SolNumEcNoLin.Met3_BroyMain import Broyden
from Mets6_IntYAproxPol.Met1_PolInterLagMain import Lagrange
from Mets6_IntYAproxPol.Met2_DifDivMain import DiferenciasDivididas
from Mets6_IntYAproxPol.Met3_NewAdeYAtrMain import NewtonInterpolacion

print("\nMetodos Numericos II\n")
print("1.- Menu de los metodos para aproximar las soluciones en un sistema de ecuaciones no lineales")
print("2.- Menu de los metodos de interpolacion y aproximacion polinomial")

while True:
    try:
        opcion = int(input("\nElija una opcion: "))
        if opcion > 0 and opcion < 3:
            break
        print("Opcion invalida!!!")
    except:
        print("Opcion invalida!!!")

if opcion == 1:
    print("\nMetodos numericos para aproximar las soluciones de un sistema de ecuaciones no lineales\n")
    print("1.- Punto fijo para sistemas de ecuaciones no lineales")
    print("2.- Metodo de Newton para sistemas de ecuaciones no lineales")
    print("3.- Metodo de Broyden")

    while True:
        try:
            opcion = int(input("\nElija una opcion: "))
            if opcion > 0 and opcion < 4:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    if opcion == 1:
        print("\nCree un archivo de texto e ingrese las expresiones de la siguiente manera:")
        print("'variable despejada' = 'expresion'\n")
        Punto_Fijo()

    elif opcion == 2:
        print("\nCree un archivo de texto e ingrese las expresiones de la siguiente manera:")
        print("F(a, b, c, ...) = [f1, f2, f3, ...]")
        print("Donde '(a, b, c, ...)' son las variables y 'f1, f2, f3, ...' son las funciones\n")
        Newton()

    elif opcion == 3:
        print("\nCree un archivo de texto e ingrese las expresiones de la siguiente manera:")
        print("F(a, b, c, ...) = [f1, f2, f3, ...]")
        print("Donde '(a, b, c, ...)' son las variables y 'f1, f2, f3, ...' son las funciones\n")
        Broyden()

elif opcion == 2:
    print("\nMetodos numericos de interpolacion y aproximacion polinomial\n")
    print("Interpolacion polinomial")
    print("1.- Fomula de Lagrange")
    print("2.- Diferencias divididas")
    print("3.- Formula de Interpolacion de Newton: hacia adenlante y hacia atras")
    print("4.- Metodo de Hermite - NO DISPONIBLE")

    while True:
        try:
            opcion = int(input("\nElija una opcion: "))
            if opcion > 0 and opcion < 4:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    if opcion == 1:
        print("\nCree un archivo de texto e ingrese los datos ahi de la siguiente manera:")
        print("(x_0,y_0) (x_1,y_1) ...")
        print("Donde 'x_0, x_1, ...' son las abscisas y 'y_0, y_1, ...' son las imagenes de las funciones en los puntos\n")
        Lagrange()

    elif opcion == 2:
        print("\nCree un archivo de texto e ingrese los datos ahi de la siguiente manera:")
        print("(x_0,y_0) (x_1,y_1) ...")
        print("Donde 'x_0, x_1, ...' son las abscisas y 'y_0, y_1, ...' son las imagenes de las funciones en los puntos\n")
        DiferenciasDivididas()

    elif opcion == 3:
        print("\nCree un archivo de texto e ingrese los datos ahi de la siguiente manera:")
        print("(x_0,y_0) (x_1,y_1) ...")
        print("Donde 'x_0, x_1, ...' son las abscisas y 'y_0, y_1, ...' son las imagenes de las funciones en los puntos\n")
        NewtonInterpolacion()

    else:
        print("\n\nEN PROCESO")
        print("TERMINANDO PROGRAMA...\n\n")
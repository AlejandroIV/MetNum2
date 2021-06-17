import sys
import os

sys.path.append(os.getcwd() + "/Mets5_SolNumEcNoLin")
sys.path.append(os.getcwd() + "/Mets6_IntYAproxPol")
sys.path.append(os.getcwd() + "/Mets7_DiffEIntNum")

import Met1_PtoFijMain, Met2_NewMain, Met3_BroyMain
import Met1_PolInterLagMain, Met2_DifDivMain, Met3_NewAdeYAtrMain, Met4_PolInterHer, Met5_TrazCub, Met6_MinCuad
import Met1_DiffNum, Met2_IntNum, Met3_IntRom

print("\nMetodos Numericos II\n")
print("1.- Menu de los metodos para aproximar las soluciones en un sistema de ecuaciones no lineales")
print("2.- Menu de los metodos de interpolacion y aproximacion polinomial")
print("3.- Menu de los metodos de derivacion e integracion numerica")

while True:
    try:
        opcion = int(input("\nElija una opcion: "))
        if opcion > 0 and opcion < 4:
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
        Met1_PtoFijMain.Punto_Fijo()

    elif opcion == 2:
        Met2_NewMain.Newton()

    elif opcion == 3:
        Met3_BroyMain.Broyden()

elif opcion == 2:
    print("\nMetodos numericos de interpolacion y aproximacion polinomial\n")
    print("1.- Fomula de Lagrange")
    print("2.- Diferencias divididas")
    print("3.- Formula de Interpolacion de Newton: hacia adenlante y hacia atras")
    print("4.- Metodo de Hermite")
    print("5.- Trazadores Cubicos")
    print("6.- Minimos Cuadrados")

    while True:
        try:
            opcion = int(input("\nElija una opcion: "))
            if opcion > 0 and opcion < 7:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    if opcion == 1:
        Met1_PolInterLagMain.Lagrange()

    elif opcion == 2:
        Met2_DifDivMain.DiferenciasDivididas()

    elif opcion == 3:
        Met3_NewAdeYAtrMain.NewtonInterpolacion()

    elif opcion == 4:
        Met4_PolInterHer.Hermite()

    elif opcion == 5:
        Met5_TrazCub.SplinesCubicos()

    elif opcion == 6:
        Met6_MinCuad.MinimosCuadrados()

elif opcion == 3:
    print("\nMetodos de derivacion e integracion numerica\n")
    print("1.- Derivacion Numerica")
    print("2.- Newton Cotes")
    print("3.- Integracion de Romberg")

    while True:
        try:
            opcion = int(input("\nElija una opcion: "))
            if opcion > 0 and opcion < 4:
                break
            print("Opcion invalida!!!")
        except:
            print("Opcion invalida!!!")

    if opcion == 1:
        Met1_DiffNum.DerivacionNumerica()

    elif opcion == 2:
        Met2_IntNum.IntegracionNumerica()

    elif opcion == 3:
        Met3_IntRom.IntegracionRomberg()
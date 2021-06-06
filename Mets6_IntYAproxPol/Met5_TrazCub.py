"""Modulo que contiene el codigo para construir los Trazadores Cubicos Naturales o Sujetos"""

from sage.all import SR, sage, round
import sys
import numpy as np
from Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, AlgoritmoTraz

def Interpolacion_Splines_Cubicos(nombre):
    """Funcion que construira la tabla de los coeficientes para construir los Splines Cubicos"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    vectH = np.empty(((matDatos.shape[0] - 1), 1), dtype = 'f')
    # Bucle que calcula la diferencia entre cada par de x en el intervalo y los almacena en 'vectH'
    for i in range(vectH.shape[0]):
        vectH[i] = matDatos[(i + 1), 0] - matDatos[i, 0]

    # Manda a llamar a la funcion para pedir al usuario que elija una opcion para aplicar el algoritmo
    listaDts = AlgoritmoTraz()

    # Si el usuario elije usar el algoritmo de trazador cubico natural
    if listaDts[0] == 1:
        vectAlpha = np.zeros(vectH.shape, dtype = 'f')
    # Si el usuario elije usar el algoritmo de trazador cubico sujeto
    else:
        vectAlpha = np.zeros((matDatos.shape[0], 1), dtype = 'f')
        # Calcula el primer y el ultimo valor de alpha [Burden p. 148]
        vectAlpha[0] = ((3 * (matDatos[1, 1] - matDatos[0, 1])) / vectH[0]) - (3 * listaDts[1][0])
        vectAlpha[vectAlpha.shape[0] - 1] = ((3 * listaDts[1][1]) - \
        ((3 * (matDatos[(vectAlpha.shape[0] - 1), 1] - matDatos[(vectAlpha.shape[0] - 2), 1])) / vectH[vectAlpha.shape[0] - 2]))

    # Bucle que calcula los alphas
    for j in range(1, vectH.shape[0]):
        vectAlpha[j] = ((3 / vectH[j]) * (matDatos[(j + 1), 1] - matDatos[(j), 1])) - ((3 / vectH[j - 1]) * (matDatos[(j), 1] - matDatos[(j - 1), 1]))

    # Despues resuelve un sistema lineal tridiagonal [Burden p. 146]
    vectL = np.ones((matDatos.shape[0], 1), dtype = 'f')
    vectZ = np.zeros(vectL.shape, dtype = 'f')
    vectMu = np.zeros(((matDatos.shape[0] - 1), 1), dtype = 'f')

    # Si el usuario elije usar el algoritmo de trazador cubico sujeto [Burden p.146]
    if listaDts[0] == 2:
        vectL[0] = 2 * vectH[0]
        vectMu[0] = 0.5
        vectZ[0] = vectAlpha[0] / vectL[0]

    for k in range(1, vectMu.shape[0]):
        vectL[k] = (2 * (matDatos[(k + 1), 0] - matDatos[k - 1, 0])) - (vectH[k - 1] * vectMu[k - 1])
        vectMu[k] = vectH[k] / vectL[k]
        vectZ[k] = (vectAlpha[k] - (vectH[k - 1] * vectZ[k - 1])) / vectL[k]

    vectC = np.zeros(vectL.shape, dtype = 'f')
    vectB = np.copy(vectC)
    vectD = np.copy(vectB)

    # Si el usuario elije usar el algoritmo de trazador cubico sujeto [Burden p.146]
    if listaDts[0] == 2:
        vectL[vectL.shape[0] - 1] = (vectH[vectL.shape[0] - 2] * (2 - vectMu[vectL.shape[0] - 2]))
        vectZ[vectL.shape[0] - 1] = (vectAlpha[vectL.shape[0] - 1] - (vectH[vectL.shape[0] - 2] * vectZ[vectL.shape[0] - 2])) / vectL[vectL.shape[0] - 1]
        vectC[vectL.shape[0] - 1] = vectZ[vectL.shape[0] - 1]

    for l in range((vectC.shape[0] - 2), -1, -1):
        vectC[l] = vectZ[l] - (vectMu[l] * vectC[l + 1])
        vectB[l] = ((matDatos[(l + 1), 1] - matDatos[(l), 1]) / vectH[l]) - (vectH[l] * ((vectC[l + 1] + (2 * vectC[l])) / 3))
        vectD[l] = (vectC[l + 1] - vectC[l]) / (3 * vectH[l])

    # Almacena los valores obtenidos de las iteraciones anteriores en la matriz 'matDatos'
    matDatos = np.append(matDatos, vectB, axis = 1)
    matDatos = np.append(matDatos, vectC, axis = 1)
    matDatos = np.append(matDatos, vectD, axis = 1)

    np.set_printoptions(precision = 6, suppress = True)

    print(f"\n{matDatos}\n")

    x = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa

    # Si 'x' no se encuentra en el intervalo
    if np.size(np.where(matDatos[:matDatos.shape[0], 0] > x)) == 0:
        print(f"\n\nEl valor {x} no se encuentra en el intervalo")
        print("Pruebe con otro valor\n\n")
        sys.exit(1)

    # Bucle que recorrera los elementos de la primera columna de la matriz 'matDatos'
    for fila in range(matDatos.shape[0] - 2, -1, -1):  # No se considera el elemento de la ultima fila
        if matDatos[fila, 0] < x:
            # La variable 'fila' se usara para indexar la fila de la matrz 'matDatos' que se usara para construir el spline
            break

    # Crea la variable que contendra el polinomio en formato'str'
    polinomio = ''
    # Variable auxiliar que se usara para indicar el grado
    expAux = 0
    # Bucle que contruye el polinomio usando como coeficientes los elementos de la fila 'fila' de la matriz 'matDatos'
    for coeficiente in matDatos[fila, 1:]:
        polinomio += f"({coeficiente} * (x - {matDatos[fila, 0]}) ** {expAux})+"
        expAux += 1

    # Elimina el ultimo signo '+' que esta en la cadena que contiene el polinomio
    polinomio = polinomio[:(len(polinomio) - 1)]

    print(f"\nEl Polinomio Interpolante es: {polinomio}")

    # Sustituye el punto que se quiere calcular por las 'x' que aparecen en la cadena de caracteres que contiene el polinomio
    polinomio = polinomio.replace('x', str(x))
    polinomio = SR(polinomio)

    # Simplifica el resultado y lo imprime redondeandolo a 8 decimales
    print(f"\n\nEl valor de la funcion en el punto {x} es aproximadamente: {round(polinomio.simplify_full(), 8)}\n")

def SplinesCubicos():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Interpolacion_Splines_Cubicos(fNombre)

if __name__ == "__main__":
    Interpolacion_Splines_Cubicos("prueba")
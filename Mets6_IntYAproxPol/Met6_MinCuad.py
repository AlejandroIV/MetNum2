"""Modulo que contiene el codigo para construir el Polinomio Discreto de Minimos Cuadrados"""

from sage.all import SR, sage, round, ln, var, e
import sys
import numpy as np
from Mods_Preparar_Metodos.Preparar_Programa import LLenar_Matriz_Datos, RelacionMinCuad

def Interpolacion_Minimos_Cuadrados(nombre):
    """Funcion que construira el Polinomio Interpolante usando Minimos Cuadrados"""
    # Primero llena una matriz con los datos contenidos en el documento de texto
    matDatos = LLenar_Matriz_Datos(nombre)

    # Pide al usuario que indique si la relacion de los datos es exponencial
    relacionExp = RelacionMinCuad()

    # Si la relacion de los datos es exponencial
    if relacionExp:
        # Calcula los valores de las columnas (ln y, x^2, x * ln y) que se agregaran a la matriz 'matDatos' [Burden p. 492]
        vetcAux = np.copy(ln(matDatos[:, 1]))
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)
        vetcAux = np.copy(matDatos[:, 0] * matDatos[:, 0])
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)
        vetcAux = np.copy(matDatos[:, 0] * matDatos[:, 2])
        matDatos = np.append(matDatos, np.reshape(vetcAux, (vetcAux.shape[0], 1)), axis = 1)

        # Crea una matriz con las sumatorias necesarias para calcular el polinomio de la forma bx^a
        matBXA = np.array([[np.sum(ln(matDatos[:, 0]) * ln(matDatos[:, 0])), np.sum(ln(matDatos[:, 0])), np.sum(ln(matDatos[:, 0]) * ln(matDatos[:, 1]))], \
        [np.sum(ln(matDatos[:, 0])), matDatos.shape[0], np.sum(matDatos[:, 2])]])

        # Calculamos las inversas de las matrices para calcular el polinomio de orden 2
        matBXA = np.matmul(np.linalg.inv(matBXA[:, :2]), matBXA[:, 2])

    # Si la relacion de los datos no es exponencial
    else:
        # Bucle que calcula los valores de 'x' elevados a un exponente y los agrega a la matriz 'matDatos'
        for exponente in range(2, 7):
            vetcAux = np.copy(matDatos[:, 0]**exponente)
            matDatos = np.append(matDatos, np.reshape(vetcAux, (matDatos.shape[0], 1)), axis = 1)

        # Bucle que calcula los valores 'y' por 'x' elevados a un exponente y los agrega a la matriz 'matDatos'
        for columna in range(0, 4):  # Recorrera las columnas con los valores calculados en el bucle anterior
            # Se salta la columna con los valores de la 'y'
            if columna == 1:  
                continue
            vetcAux = np.copy(matDatos[:, columna]*matDatos[:, 1])
            matDatos = np.append(matDatos, np.reshape(vetcAux, (matDatos.shape[0], 1)), axis = 1)

        # Crea una matriz con las sumatorias necesarias para calcular el polinomio de orden 2
        matPolOrd2 = np.array([[matDatos.shape[0], np.sum(matDatos[:, 0]), np.sum(matDatos[:, 2]), np.sum(matDatos[:, 1])], \
        [np.sum(matDatos[:, 0]), np.sum(matDatos[:, 2]), np.sum(matDatos[:, 3]), np.sum(matDatos[:, 7])], \
        [np.sum(matDatos[:, 2]), np.sum(matDatos[:, 3]), np.sum(matDatos[:, 4]), np.sum(matDatos[:, 8])]])

        # Crea una matriz con las sumatorias necesarias para calcular el polinomio de orden 3
        matPolOrd3 = np.array([[matDatos.shape[0], np.sum(matDatos[:, 0]), np.sum(matDatos[:, 2]), np.sum(matDatos[:, 3]), np.sum(matDatos[:, 1])], \
        [np.sum(matDatos[:, 0]), np.sum(matDatos[:, 2]), np.sum(matDatos[:, 3]), np.sum(matDatos[:, 4]), np.sum(matDatos[:, 7])], \
        [np.sum(matDatos[:, 2]), np.sum(matDatos[:, 3]), np.sum(matDatos[:, 4]), np.sum(matDatos[:, 5]), np.sum(matDatos[:, 8])], \
        [np.sum(matDatos[:, 3]), np.sum(matDatos[:, 4]), np.sum(matDatos[:, 5]), np.sum(matDatos[:, 6]), np.sum(matDatos[:, 9])]])

        # Calculamos las inversas de las matrices para calcular el polinomio de orden 2
        matPolOrd2 = np.matmul(np.linalg.inv(matPolOrd2[:, :3]), matPolOrd2[:, 3])

        # Calculamos las inversas de las matrices para calcular el polinomio de orden 3
        matPolOrd3 = np.matmul(np.linalg.inv(matPolOrd3[:, :4]), matPolOrd3[:, 4])

    # Imprime la matriz 'matDatos'
    print("\n" + "\n".join([''.join(['{:12}'.format(round(val, 6)) for val in fila]) for fila in matDatos]) + "\n")

    # Crea la variable que contendra el polinomio en formato'str'
    polinomio = ''
    # Constuiye el polinomio usando como coeficientes las sumatorias  tomando en [Burden pp. 487, 492]
    # Si la relacion de los datos es exponencial
    if relacionExp:
        # Crea las variable que contendran los polinomios en formato'str'
        polinomio2 = ''

        valor1 = ((matDatos.shape[0] * np.sum(matDatos[:, 4])) - (np.sum(matDatos[:, 0]) * np.sum(matDatos[:, 2])))
        valor1 /= ((matDatos.shape[0] * np.sum(matDatos[:, 3])) - (np.sum(matDatos[:, 0]) ** 2))
        valor2 = ((np.sum(matDatos[:, 3]) * np.sum(matDatos[:, 2])) - (np.sum(matDatos[:, 4]) * np.sum(matDatos[:, 0])))
        valor2 /=((matDatos.shape[0] * np.sum(matDatos[:, 3])) - (np.sum(matDatos[:, 0]) ** 2))
        polinomio = f"(e ** {valor2}) * (e ** ({valor1} * x))"

        polinomio2 = f"({e ** matBXA[1]}) * x ** {matBXA[0]}"
    # Si la relacion de los datos no es exponencial
    else:
        # Crea las variable que contendran los polinomios en formato'str'
        polinomio2 = ''
        polinomio3 = ''

        valor1 = ((np.sum(matDatos[:, 2]) * np.sum(matDatos[:, 1])) - (np.sum(matDatos[:, 0]) * np.sum(matDatos[:, 7])))
        valor1 /= ((matDatos.shape[0] * np.sum(matDatos[:, 2])) - (np.sum(matDatos[:, 0]) ** 2))
        valor2 = ((matDatos.shape[0] * np.sum(matDatos[:, 7])) - (np.sum(matDatos[:, 0]) * np.sum(matDatos[:, 1])))
        valor2 /= ((matDatos.shape[0] * np.sum(matDatos[:, 2])) - (np.sum(matDatos[:, 0]) ** 2))
        polinomio = f"({valor2} * x) + {valor1}"

        polinomio2 = f"({matPolOrd2[2]} * x**2) + ({matPolOrd2[1]} * x) + {matPolOrd2[0]}"
        polinomio3 = f"({matPolOrd3[3]} * x**3) + ({matPolOrd3[2]} * x**2) + ({matPolOrd3[1]} * x) + {matPolOrd3[0]}"

    polinomio = SR(polinomio)
    polinomio2 = SR(polinomio2)
    # Si la relacion de los datos es exponencial
    if relacionExp:
        print(f"\nEl Polinomio Interpolante de la forma be^(ax) es: {polinomio}")
        print(f"\nEl Polinomio Interpolante de la forma bx^a es: {polinomio2}")

        # Matriz que contendra los valores de error
        matErr = np.empty((matDatos.shape[0], 2), dtype = 'f')
        cont = 0
        # Bucle para almacenar las evaluaciones de los polinomios
        for valorX in matDatos[:, 0]:
            matErr[cont, 0] = polinomio.subs(x = valorX)
            matErr[cont, 1] = polinomio2.subs(x = valorX)
            cont += 1

        # Calcula los errores
        matErr[:, 0] = abs(np.copy(matErr[:, 0] - matDatos[:, 1]))**2
        matErr[:, 1] = abs(np.copy(matErr[:, 1] - matDatos[:, 1]))**2

        print(f"\nLos errores totales de los polinomios respectivamente son:\n {np.sum(matErr[:, 0])} y \n {np.sum(matErr[:, 1])}")

    # Si la relacion de los datos no es exponencial
    else:
        polinomio3 = SR(polinomio3)

        print(f"\nEl Polinomio Interpolante de grado 1 es: {polinomio}")
        print(f"El Polinomio Interpolante de grado 2 es: {polinomio2}")
        print(f"El Polinomio Interpolante de grado 3 es: {polinomio3}")
        # Matriz que contendra los valores de error
        matErr = np.empty((matDatos.shape[0], 3), dtype = 'f')
        cont = 0
        # Bucle para almacenar las evaluaciones de los polinomios
        for valorX in matDatos[:, 0]:
            matErr[cont, 0] = polinomio.subs(x = valorX)
            matErr[cont, 1] = polinomio2.subs(x = valorX)
            matErr[cont, 2] = polinomio3.subs(x = valorX)
            cont += 1

        # Calcula los errores
        matErr[:, 0] = abs(np.copy(matErr[:, 0] - matDatos[:, 1]))**2
        matErr[:, 1] = abs(np.copy(matErr[:, 1] - matDatos[:, 1]))**2
        matErr[:, 2] = abs(np.copy(matErr[:, 2] - matDatos[:, 1]))**2

        print(f"\nLos errores totales de los polinomios respectivamente son:\n {np.sum(matErr[:, 0])}, \n {np.sum(matErr[:, 1])} y \n {np.sum(matErr[:, 2])}")

    a = float(input("\nIngresa una abscisa: "))  # Pide al usuario una abscisa

    # Declara la variable simbolica
    x = var('x')

    # Si la relacion de los datos es exponencial
    if relacionExp:
        print(f"\n\nEl valor de la funcion en el punto {a} (usando be^(ax)) es aproximadamente: {round(polinomio.subs(x = a).simplify_full(), 8)}")
        print(f"\n\nEl valor de la funcion en el punto {a} (usando bx^a) es aproximadamente: {round(polinomio2.subs(x = a).simplify_full(), 8)}")

    # Si la relacion de los datos no es exponencial
    else:
        # Simplifica el resultado y lo imprime redondeandolo a 8 decimales
        print(f"\n\nEl valor de la funcion en el punto {a} (usando el polinomio lineal) es aproximadamente: {round(polinomio.subs(x = a).simplify_full(), 8)}")
        print(f"El valor de la funcion en el punto {a} (usando el polinomio cuadratico) es aproximadamente: {round(polinomio2.subs(x = a).simplify_full(), 8)}")
        print(f"El valor de la funcion en el punto {a} (usando el polinomio cubico) es aproximadamente: {round(polinomio3.subs(x = a).simplify_full(), 8)}\n")

def MinimosCuadrados():
    fNombre = input("Escribe el nombre del archivo sin escribir la extension '.txt': ")
    Interpolacion_Minimos_Cuadrados(fNombre)

if __name__ == "__main__":
    Interpolacion_Minimos_Cuadrados("prueba")
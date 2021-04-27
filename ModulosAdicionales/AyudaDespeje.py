"""Modulo que aplica una operaciones a ambos miembros de una igualdad"""

from sage.all import *
import numpy as np
import sys

def despeje():
    # Pide al usuario que ingrese las expresiones que conformaran los miembros de la igualdad
    expr1 = input("Ingresa el primer miembro de la igualdad: ")
    expr2 = input("Ingresa el segundo miembro de la igualdad: ")
    try:
        SR(expr1)
        SR(expr2)
    except:
        print("\nAlguna de las expresiones no son validas y no es posible continuar")
        sys.exit(1)

    # Imprime las opciones disponibles al usuario
    print("\n1 - Suma")
    print("2 - Resta")
    print("3 - Multiplicacion")
    print("4 - Division")
    print("5 - Elevar a un exponente")
    print("6 - Aplicar una expresion")
    print("0 - Salir\n")

    while True:
        op = int(input("Introduce la operacion que quieras aplicar a ambos miembros de la igualdad: "))

        # Continua con otra iteracion nueva si el usuario no ingresa una opcion valida
        if op > 6 or op < 0:
            print("\nIngresa una opcion valida\n")
            continue

        # Condicional para parar en caso de que el usuario digite el cero
        if op == 0:
            break

        # Condicional que concatenara expr1 y expr2 con un signo de mas seguido de un numero o letra (variable) que indique el usuario
        elif op == 1:
            num = input("Ingresa lo que quieras sumar a ambos miembros de la igualdad: ")
            expr1 += ("+" + num)
            expr2 += ("+" + num)

        # Condicional que concatenara expr1 y expr2 con un signo de menos seguido de un numero o letra (variable) que indique el usuario
        elif op == 2:
            num = input("Ingresa lo que quieras sumar a ambos miembos de la igualdad: ")
            expr1 += ("-(" + num + ")")
            expr2 += ("-(" + num + ")")

        # Condicional que concatenara expr1 y expr2 con un signo de multiplicacion seguido de un numero o letra (variable) que indique el usuario
        elif op == 3:
            num = input("Ingresa lo que quieras multiplicar a ambos miebros de la igualdad: ")
            expr1 = "(" + expr1 + ")" + "*" + num
            expr2 = "(" + expr2 + ")" + "*" + num

        # Condicional que concatenara expr1 y expr2 con un signo de multiplicacion seguido del reciproco de un numero o letra (variable) que indique el usuario
        elif op == 4:
            num = input("Ingresa lo que quieras dividir a ambos miembros de la igualdad: ")
            expr1 = "(" + expr1 + ")" + "*" + f"1/{num}"
            expr2 = "(" + expr2 + ")" + "*" + f"1/{num}"

        # Condicional que concatenara expr1 y expr2 con un signo de exponenciacion seguido de un numero o letra (variable) que indique el usuario
        elif op == 5:
            num = input("Ingresa a lo que quieras elevar ambos miembros de la igualdad: ")
            expr1 = "(" + expr1 + ")" + "^" + num
            expr2 = "(" + expr2 + ")" + "^" + num
            expr1 = SR(expr1).canonicalize_radical()
            expr2 = SR(expr2).canonicalize_radical()

        # Condicional que concatenara la expresion dada por el usuario con la expr1 y expr2 entre parentesis
        elif op == 6:
            num = input("Ingresa que expresion quieres aplicar a ambos miemrbos de la igualdad: ")
            expr1 = num + "(" + expr1 + ")"
            expr2 = num + "(" + expr2 + ")"

        # Sentencias para imprimir las expresiones de ambos miembros de la igualdad
        expr1 = SR(expr1)
        expr2 = SR(expr2)
        print("\nExpresion resultante:", expr1, "=", expr2, "\n")
        expr1 = str(expr1)
        expr2 = str(expr2)

    # Si se decide terminar con el bucle se imprime la expresion resultante de aplicar las tranformaciones a ambos miembros de la igualdad
    expr1 = SR(expr1)
    expr2 = SR(expr2)
    print("\n\nExpresion resultante final:", expr1.canonicalize_radical(), "=", expr2, "\n\n")

if __name__ == "__main__":
    despeje()
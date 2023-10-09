import math
import numpy as np

def pedirFuncion():
    funcion = input("Ingresa la función a calcular: ")
    return funcion

def pedirValX():
    valX = float(input("Ingrese valor de X: "))
    return valX

def pedirIntervalo():
    x0 = int(input("Ingrese valor x0 del intervalo: "))
    x1 = int(input("Ingrese valor x1 del intervalo: "))
    return x0, x1

def usarFuncion(funcion, x):
    return eval(funcion)

def pedir_matriz():
    A = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    B = [0, 0, 0]
    print("""
          La matriz A tiene la siguiente forma:
          [A0, A1, A2]
          [A3, A4, A5]
          [A6, A7, A8]
          """)
    A[0][0] = int(input("Ingrese A0: "))
    A[0][1] = int(input("Ingrese A1: "))
    A[0][2] = int(input("Ingrese A2: "))
    A[1][0] = int(input("Ingrese A3: "))
    A[1][1] = int(input("Ingrese A4: "))
    A[1][2] = int(input("Ingrese A5: "))
    A[2][0] = int(input("Ingrese A6: "))
    A[2][1] = int(input("Ingrese A7: "))
    A[2][2] = int(input("Ingrese A8: "))

    print("""
          La matriz B tiene la siguiente forma:
          [B0, B1, B2]
          """)

    B[0] = int(input("Ingrese B0: "))
    B[1] = int(input("Ingrese B1: "))
    B[2] = int(input("Ingrese B2: "))

    return A, B
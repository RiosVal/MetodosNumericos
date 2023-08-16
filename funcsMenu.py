import math

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
import numpy as np

def x_cuadrado(x):
    return x**2

def extremosIzquierdos(funcion, a, b, n):
    deltaX = (b - a) / n
    suma = 0
    for i in range(n):
        suma += deltaX * funcion(a + i*deltaX)
    return suma

def puntosMedios(funcion, a, b, n):
    listax = np.linspace(a, b, n+1)
    deltaX = (b - a) / n
    suma = 0
    for k in range(1, n+1):
        suma += deltaX * funcion((listax[k] + listax[k-1])/2)
    return suma

print(extremosIzquierdos(x_cuadrado, 0, 3, 5))
print(puntosMedios(x_cuadrado, 0, 3, 5))
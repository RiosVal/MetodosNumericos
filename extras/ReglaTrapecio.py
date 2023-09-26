import numpy as np

def x_cuadrado(x):
    return x**2

def trapecio(funcion, a, b, n):
    listax = np.linspace(a, b, n+1)
    ancho = (b-a)
    suma = 0
    for i in range(1, n):
        suma += funcion(listax[i])

    numerador = funcion(listax[a]) + (2*suma) + funcion(listax[n])
    return ancho * (numerador / (2*n))



print(trapecio(x_cuadrado, 0, 3, 10))
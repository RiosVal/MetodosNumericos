import numpy as np

def x_cuadrado(x):
    return x**2

def simpson_un_tercio(funcion, a, b):
    listax = np.linspace(a, b, 3)
    numerador = funcion(listax[0]) + (4*funcion(listax[1])) + funcion(listax[2])
    return (b - a) * (numerador / 6)

def simpson_intervalos(funcion, a, b, n):
    listax = np.linspace(a, b, n+1)
    suma_impares = 0
    suma_pares = 0

    for i in range(1, n):
        if i % 2 == 0:
            suma_pares += funcion(listax[i])
        else:
            suma_impares += funcion(listax[i])
    
    numerador = funcion(listax[0]) + (4*suma_impares) + (2*suma_pares) + funcion(listax[n])

    return (b-a) * (numerador / (3*n))

def simpson_3_8_intervalos(funcion, a, b, n):
    listax = np.linspace(a, b, n + 1)
    suma = 0

    h = (b - a) / n

    for i in range(1, n):
        if i % 3 == 0:
            suma += 2 * funcion(listax[i])
        else:
            suma += 3 * funcion(listax[i])

    resultado = (3 * h / 8) * (funcion(listax[0]) + funcion(listax[n]) + suma)

    return resultado

#simpson 3/8

#print(simpson_un_tercio(x_cuadrado, 0, 3))
print(simpson_intervalos(x_cuadrado, 0, 3, 2))
print(simpson_3_8_intervalos(x_cuadrado, 0, 3, 6))
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

def romberg(funcion, a, b, n):
    matriz = np.zeros((n, n), float)
    intervalos = 1
    for j in range(len(matriz)):
        for k in range(len(matriz[j])):
            if k == 0 and intervalos <= n:
                matriz[j,k] = trapecio(funcion, a, b, intervalos)
        intervalos += 1
    
    contador = 1
    for j in range(1, len(matriz) -1):
        for k in range(contador, len(matriz[j])):
            print(f'{j}, {k}')
            numerador = ((4**(k-1))*matriz[j+1,k-1])-matriz[j,k-1]
            matriz[j, k] = numerador / (4**(k-1))-1
        contador += 1
    
    print(matriz)

def romberg_chat(funcion, a, b, n):
    tol = 1e-6  # Tolerancia para la convergencia
    I = np.zeros((n, n))
    h = b - a

    # Inicialización con el método del trapecio
    I[0, 0] = 0.5 * h * (funcion(a) + funcion(b))
    
    for k in range(1, n):
        h = h / 2
        suma = 0

        for i in range(1, 2**k, 2):
            suma += funcion(a + i * h)

        I[k, 0] = 0.5 * I[k-1, 0] + suma * h

        for j in range(1, k + 1):
            I[k, j] = (4**j * I[k, j-1] - I[k-1, j-1]) / (4**j - 1)

        if abs(I[k, k] - I[k-1, k-1]) < tol:
            break

    return I[k, k]


print(romberg_chat(x_cuadrado, 0, 3, 4))
#numerador = ((4**(k-1))*matriz[j+1,k-1])-matriz[j,k-1]
#denominador = (4**(k-1))-1
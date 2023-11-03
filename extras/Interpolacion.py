import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import math

def f(x):
    return math.log(x)


def Newton(a, b, n, f, x):
    A = np.zeros((n, n))
    xi = np.linspace(a, b, n)

    prod = np.zeros(n)
    prod[0] = 1
    prod[1] = x - xi[1]
    for i in range(1, n):
        prod[i] = prod[i-1]*(x-xi[i-1])

    fila = 0
    inicial = 0

    for k in range(n):
        if k == 0:
            for i in range(n):
                A[i][k] = f(xi[i])
        else:
            for i in range(fila, n):
                A[i][k] = (A[i][k-1] - A[i-1][k-1]) / (xi[i] - xi[inicial])
                inicial += 1
            inicial = 0
        print(A[k])
        fila += 1

    diag = np.diag(A)

    newInter = f(xi[0])

    for i in range(n):
        newInter += diag[i]*prod[i]
    return newInter

# x=2
# InterpNew = Newton(1, 5, 5, f, x)
# error = abs(InterpNew - f(2))/(f(2))
# print('{:<20} {:<20} {:<20}'.format('f(x)', 'Newton', '%Error'))
# print('{:<20} {:<20} {:<20}'.format(f(x), InterpNew, error*100))


def lagrange():
    # Interpolacion de Lagrange
    # divisoresL solo para mostrar valores


    # INGRESO , Datos de prueba
    xi = np.array([0, 0.2, 0.3, 0.4])
    fi = np.array([1, 1.6, 1.7, 2.0])

    # PROCEDIMIENTO
    # Polinomio de Lagrange
    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype = float)
    for i in range(0,n,1):
        
        # Termino de Lagrange
        numerador = 1
        denominador = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    # simplifica el polinomio
    polisimple = polinomio.expand()

    # para evaluación numérica
    px = sym.lambdify(x,polisimple)

    # Puntos para la gráfica
    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)

    # SALIDA
    print('    valores de fi: ',fi)
    print('divisores en L(i): ',divisorL)
    print()
    print('Polinomio de Lagrange, expresiones')
    print(polinomio)
    print()
    print('Polinomio de Lagrange: ')
    print(polisimple)

    # Gráfica
    plt.plot(xi,fi,'o', label = 'Puntos')
    plt.plot(pxi,pfi, label = 'Polinomio')
    plt.legend()
    plt.xlabel('xi')
    plt.ylabel('fi')
    plt.title('Interpolación Lagrange')
    plt.show()

lagrange()

def hola():
    a = 1
    b = 2
    c = a + b
    return c
import numpy as np
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

x=2
InterpNew = Newton(1, 5, 5, f, x)
error = abs(InterpNew - f(2))/(f(2))
print('{:<20} {:<20} {:<20}'.format('f(x)', 'Newton', '%Error'))
print('{:<20} {:<20} {:<20}'.format(f(x), InterpNew, error*100))


def Lagrange(a, b, n, f, x):
    xi = np.linspace(a, b, n +1)
    sum = 0

    for i in range(n+1):
        prod = 1
        for j in range(n + 1):
            if j != i:
                prod = (x - xi[j])/(xi[i] - xi[j])
            else:
                continue
        sum += prod*f(xi[i])
    return sum

x=2
InterpLag = Lagrange(1, 5, 5, f, x)
error = abs(InterpLag - f(x))/(f(x))
print('{:<20} {:<20} {:<20}'.format('f(x)', 'Lagrange', '%Error'))
print('{:<20} {:<20} {:<20}'.format(f(x), InterpLag, error*100)) 
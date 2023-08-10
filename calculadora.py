import math
import sympy as sp

def funcionLn(x):       #prueba de derivadas
    return math.log(x)

def funcionExp(x):      #prueba de biseccion
    return math.exp(-x) - x

def g(x):               #prueba de punto fijo
    return math.exp(-x)

def calcularError(aprox, teor):   #error de derivada
    return abs(aprox - teor)

def derivadaCentral(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def derivadaAtras(f, x, h):
    return (f(x) - f(x-h)) / h

def derivadaAdelante(f, x, h):
    return (f(x + h) - f(x)) / h

def metodoPuntoFijo(g, x0, tol):
    xold = x0
    for i in range(50):
        xnew = g(xold)
        error = abs((xnew - xold) / xnew)
        if error <= tol:
            break
        else:
            xold = xnew
    print('{:<3} {:<20} {:<25}'.format(i, xold, error))

def metodoBiseccion(f, x0, x1, tol):
    anterior = x0
    for i in range(50):
        if f(x0) * f(x1) < 0:
            medio = (x0 + x1)/2
        else:
            print('La función no tiene cero en ese intervalo')

        error = abs((medio - anterior) / medio)

        if error <= tol:
            break

        if f(x0) * f(medio) < 0:
            x1 = medio
            anterior = x1
        else:
            x0 = medio
            anterior = x0
    print('{:<6} {:<22} {:<20}'.format(i, medio, error))    

def metodoFalsaPosicion(f, x0, x1, tol):
    anterior = x0

    for i in range(50):
        if f(x0) * f(x1) < 0:
            pos = x0 - (x0 - x1)*f(x0)/(f(x0) - f(x1))
        error = abs((pos - anterior) / pos)

        if error <= tol:
            break

        if f(x0) * f(pos) < 0:
            x1 = pos
            anterior = x1
        else:
            x0 = pos
            anterior = x0
    print('{:<3} {:<22} {:<25}'.format(i, pos, error))    

def metodoNewtonRaphson(f, x0, tol):
    for i in range(50):
        x1 = x0 - ((f(x0))/(derivadaAdelante(f, x0, 0.001)))
        error = abs((x1 - x0) / x1)
        if error < tol:
            break
        else:
            x0 = x1
    print('{:<22} {:<25}'.format(x1, error))    

def verificacionDerivadas():
    x = 1.05
    h = 0.00001
    derivCentral = derivadaCentral(funcionLn, x, h)
    derivAdelante = derivadaAdelante(funcionLn, x, h)
    derivAtras = derivadaAdelante(funcionLn, x, h)
    derivTeorica = 1/x
    print(derivCentral, "           ", calcularError(derivCentral, derivTeorica))
    print(derivAdelante, "           ", calcularError(derivAdelante, derivTeorica))
    print(derivAtras, "           ", calcularError(derivAtras, derivTeorica))
    print(derivTeorica, "           ", calcularError(derivTeorica, derivTeorica))

def verificacionPuntoFijo():
    tol = 0.000001
    x0 = 1
    metodoPuntoFijo(g, x0, tol)

def verificacionBiseccion():
    tol = 0.000001
    metodoBiseccion(funcionExp, 0, 1, tol)

def verificacionFalsaPosicion():
    tol = 0.000001
    metodoFalsaPosicion(funcionExp, 0, 1, tol)

def verificacionNewtonRaphson():
    tol = 0.000001
    metodoNewtonRaphson(funcionExp, 1, tol)

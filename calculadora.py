import math
from funcsMenu import usarFuncion
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
    return (usarFuncion(f, (x + h)) - usarFuncion(f, (x - h))) / (2 * h)

def derivadaAtras(f, x, h):
    return (usarFuncion(f, x) - usarFuncion(f, (x-h))) / h

def derivadaAdelante(f, x, h):
    return (usarFuncion(f, (x + h)) - usarFuncion(f, x)) / h

def metodoPuntoFijo(g, x0, tol):
    xold = x0
    for i in range(50):
        xnew = usarFuncion(g, xold)
        error = abs((xnew - xold) / xnew)
        if error <= tol:
            break
        else:
            xold = xnew
    return (i, xold, error)
    #print('{:<3} {:<20} {:<25}'.format(i, xold, error))

def metodoBiseccion(f, x0, x1, tol):
    anterior = x0
    for i in range(50):
        if usarFuncion(f, x0) * usarFuncion(f, x1) < 0:
            medio = (x0 + x1)/2
        else:
            return

        error = abs((medio - anterior) / medio)

        if error <= tol:
            break

        if usarFuncion(f, x0) * usarFuncion(f, medio) < 0:
            x1 = medio
            anterior = x1
        else:
            x0 = medio
            anterior = x0
    return (i, medio, error)
    #print('{:<6} {:<22} {:<20}'.format(i, medio, error))    

def metodoFalsaPosicion(f, x0, x1, tol):
    anterior = x0

    for i in range(50):
        if usarFuncion(f, x0) * usarFuncion(f, x1) < 0:
            pos = x0 - (x0 - x1)*usarFuncion(f, x0)/(usarFuncion(f, x0) - usarFuncion(f, x1))
        error = abs((pos - anterior) / pos)

        if error <= tol:
            break

        if usarFuncion(f, x0) * usarFuncion(f, pos) < 0:
            x1 = pos
            anterior = x1
        else:
            x0 = pos
            anterior = x0
    return (i, pos, error)
    #print('{:<3} {:<22} {:<25}'.format(i, pos, error))    

def metodoNewtonRaphson(f, x0, tol):
    for i in range(50):
        x1 = x0 - ((usarFuncion(f, x0))/(derivadaAdelante(f, x0, 0.001)))
        error = abs((x1 - x0) / x1)
        if error < tol:
            break
        else:
            x0 = x1
    return x1, error
    #print('{:<22} {:<25}'.format(x1, error))    

def MetodoSecante(funcion, x0, x1, tol=0.00000001):
    def der():
        return (usarFuncion(funcion, x0) - usarFuncion(funcion, x1)) / (x0 -x1)

    for i in range(50):
        derivate = der()
        pos = x0 - usarFuncion(funcion, x0)/derivate
        error = abs((pos - x0) / pos)

        if error <= tol:
            break
        else:
            x0 = x1
            x1 = pos
    return (i, pos, error)
    #print("{:<6} {:<22} {:<20}".format(i, pos, error))

def calcularIntervalos(metodo, funcion, inicio, fin):
    raices = []
    limite = fin
    inferior = 0
    superior = 0

    while superior < limite:
        
        superior = inferior + 0.2
        try:
            raiz = metodo(funcion, inferior, superior, 0.0000001)
        except:
            raiz = None
        if raiz != None:
            raices.append([inferior, superior])
        inferior = superior
    
    for intervalo in raices:
        print(intervalo)
    return raices

def calcularIntervalos2(metodo, funcion):
    deltaX = float(input("Ingrese valor Δ del intervalo: "))
    limite = int(input("Ingrese valor x1 del intervalo: "))
    raices = []
    inferior = 0
    superior = 0

    while superior < limite:
        superior = inferior + deltaX
        evaluacion = usarFuncion(funcion, inferior)*usarFuncion(funcion, superior) 

        if evaluacion < 0:
            raices.append([inferior, superior])

        inferior = superior
    print("Los intervalos y las raices son: ")
    for intervalo in raices:
        print(intervalo)

    for intervalo in raices:
        a, b = intervalo
        print(metodo(funcion, a, b, 0.0000001))







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

import math
import numpy as np
from funcsMenu import *
import matplotlib.pyplot as plt


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
    return i, xold, error
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
    return i, medio, error
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
    return i, pos, error
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
    return i, pos, error
    #print("{:<6} {:<22} {:<20}".format(i, pos, error))

def calcularIntervalos(metodo, funcion):
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


def sumas_riemman_izquierda(funcion, a, b, tol):
    numero_rectangulos = int(input("Ingrese el numero de rectangulos: "))
    deltaX= (b-a)/numero_rectangulos
    valoresX = np.linspace(a, b-deltaX, numero_rectangulos)
    suma = 0

    for i in valoresX:
        suma = (usarFuncion(funcion, i)*deltaX)+ suma
        
    return suma


def sumas_riemman_punto_medio(funcion, a, b, tol):
    numero_rectangulos = int(input("Ingrese el número de rectangulos: "))
    deltaX= (b-a)/numero_rectangulos
    valoresX = np.linspace(a, b-deltaX, numero_rectangulos)
    suma = 0
    
    for i in valoresX:
        suma = (usarFuncion(funcion, i+(deltaX/2))*deltaX)+ suma
        
    return suma

def trapecio(funcion, a, b, tol):
    a = int(a)
    b = int(b)
    n = int(input("Ingrese el número de trapecios: "))
    listax = np.linspace(a, b, n+1)
    ancho = (b-a)
    suma = 0
    for i in range(1, n):
        suma += usarFuncion(funcion, listax[i])

    numerador = usarFuncion(funcion, listax[a])+(2*suma)+usarFuncion(funcion, listax[n])
    return ancho * (numerador / (2*n))

def simpson_un_tercio(funcion, a, b, tol):
    listax = np.linspace(a, b, 3)
    numerador = usarFuncion(funcion, listax[0]) + (4*usarFuncion(funcion, listax[1])) + usarFuncion(funcion, listax[2])
    return (b - a) * (numerador / 6)

def simpson_intervalos(funcion, a, b, tol):
    n = int(input("Defina el número de intervalos: "))
    listax = np.linspace(a, b, n+1)
    suma_impares = 0
    suma_pares = 0

    for i in range(1, n):
        if i % 2 == 0:
            suma_pares += usarFuncion(funcion, listax[i])
        else:
            suma_impares += usarFuncion(funcion, listax[i])
    
    numerador = usarFuncion(funcion, listax[0]) + (4*suma_impares) + (2*suma_pares) + usarFuncion(funcion, listax[n])

    return (b-a) * (numerador / (3*n))

def simpson_3_8_intervalos(funcion, a, b, tol):
    n = int(input("Defina el número de intervalos: "))
    listax = np.linspace(a, b, n + 1)
    suma = 0

    h = (b - a) / n

    for i in range(1, n):
        if i % 3 == 0:
            suma += 2 * usarFuncion(funcion, listax[i])
        else:
            suma += 3 * usarFuncion(funcion, listax[i])

    resultado = (3 * h / 8) * (usarFuncion(funcion, listax[0]) + usarFuncion(funcion, listax[n]) + suma)

    return resultado

def romberg_integration(funcion, a, b, tol):
    n = int(input("Ingrese el número de iteraciones que desea hacer: "))
    R = np.zeros((n, n), dtype=float)

    h = b - a
    R[0, 0] = 0.5 * h * (usarFuncion(funcion, a) + usarFuncion(funcion, b))

    for i in range(1, n):
        h /= 2
        sum_term = 0
        for k in range(1, 2**i, 2):
            sum_term += usarFuncion(funcion, a + k * h)
        R[i, 0] = 0.5 * R[i-1, 0] + sum_term * h

        for j in range(1, i+1):
            R[i, j] = (4**j * R[i, j-1] - R[i-1, j-1]) / (4**j - 1)

    return R[n-1, n-1]

def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        x_new = [0.0] * n
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            break
        x = x_new.copy()
    return x

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(b)
    x = x0.copy()
    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]
        if all(abs(x[i] - x0[i]) < tol for i in range(n)):
            break
        x0 = x.copy()
    return x

def regresion_lineal():
    x_dato = []
    y_dato = []
    dato = 0.0
    cantidad_datos = int(input("Ingrese cantidad de datos: "))
    
    print("Ingrese valores de X")
    for i in range(cantidad_datos):
        dato = float(input("Siguiente: "))
        x_dato.append(dato)
    
    print("Ingrese valores de y")
    for i in range(cantidad_datos):
        dato = float(input("Siguiente: "))
        y_dato.append(dato)

    suma1 = 0
    suma2 = 0
    suma3 = 0
    suma4 = 0
    n = len(x_dato)

    for i in range(0, n):
        suma1 += x_dato[i]*y_dato[i]
        suma2 += x_dato[i]
        suma3 += y_dato[i]
        suma4 += x_dato[i]**2

    a1 = ((n*suma1)-(suma2*suma3))/((n*suma4)-(suma2**2))
    a0 = (suma3/n)-(a1*(suma2/n))
    print(f"Coeficiente: {a0}")

    resol = 20
    xx = np.linspace(-1,12, resol)
    yy = a0 + a1*xx

    fig, ax = plt.subplots()
    ax.plot(xx, yy, "b")
    ax.plot(x_dato, y_dato, "o")
    plt.grid()
    plt.show()


def Gauss(SumXY, SumXX, SumXXX, SumXXXX, SumXXY, SumX, SumY, n):
    A=np.array([[n, SumX, SumXX],
                [SumX, SumXX, SumXXX],
                [SumXX, SumXXX, SumXXXX]])
    
    b = np.array([SumY, SumXY, SumXXY])

    VVI = np.dot(np.linalg.inv(A), b)

    return VVI

def minCuad(x, y, m, n):
    SumXY=0; SumXX=0; SumX=0; SumY=0; SumXXX=0; SumXXXX=0; SumXXY=0

    for i in range(len(x)):
        SumXY += x[i]*y[i]
        SumXX += x[i]**2
        SumXXX += x[i]**3
        SumXXXX += x[i]**4
        SumXXY += x[i]**2*y[i]
        SumX += x[i]
        SumY += y[i]
    a0, a1, a2 = Gauss(SumXY, SumXX, SumXXX, SumXXXX, SumXXY, SumX, SumY, n)

    return a0, a1, a2

def regresion_polinomial():
    x_dato = []
    y_dato = []
    dato = 0.0
    cantidad_datos = int(input("Ingrese cantidad de datos: "))
    
    print("Ingrese valores de X")
    for i in range(cantidad_datos):
        dato = float(input("Siguiente: "))
        x_dato.append(dato)
    
    print("Ingrese valores de y")
    for i in range(cantidad_datos):
        dato = float(input("Siguiente: "))
        y_dato.append(dato)
    
    m = 2; n = len(x_dato)

    if n < m+1:
        print('Pocos datos (n > m+1)')
    else:
        a0,a1,a2 = minCuad(x_dato, y_dato, m, n)

        resol = 100
        xx = np.linspace(-2, 12, resol)
        yy = a0 + a1*xx + a2*xx**2

        fig, ax = plt.subplots()
        ax.plot(xx,yy,'r')
        ax.plot(x_dato,y_dato,'o')
        plt.grid()
        plt.show()

def lagrange_interpolation(funcion, x):
    x_values = []

    dato = 0.0
    cantidad_datos = int(input("Ingrese cantidad de datos: "))
    
    print("Ingrese valores de X")
    for i in range(cantidad_datos):
        dato = float(input("Siguiente: "))
        x_values.append(dato)

    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = usarFuncion(funcion, x_values[i])
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


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
import numpy as np
import matplotlib.pyplot as plt

def polinomial(arrayX, arrayY):  #regresion de grado 2
    n = len(arrayX)
    sumX = 0; sumX2 = 0; sumX3 = 0
    sumX4 = 0; sumY = 0; sumXY = 0
    sumXXY = 0

    for i in range(0, n):
        sumX += arrayX[i]
        sumX2 += arrayX[i]**2
        sumX3 += arrayX[i]**3
        sumX4 += arrayX[i]**4
        sumY += arrayY[i]
        sumXY += arrayX[i]*arrayY[i]
        sumXXY += (arrayX[i]**2)*arrayY[i]

    A = np.array([
        [n, sumX, sumX2],
        [sumX, sumX2, sumX3],
        [sumX2, sumX3, sumX4]
    ])
    b = np.array([sumY, sumXY, sumXXY])

    VV1 = np.dot(np.linalg.inv(A), b)
    return VV1     #coeficientes de la regresión polinómica de grado 2


def Gauss(sumXY, sumXX, sumXXX, sumXXXX, sumXXY, sumX, sumY, n):
    A = np.array([
        [n, sumX, sumXX],
        [sumX, sumXX, sumXXX],
        [sumXX, sumXXX, sumXXXX]
    ])
    b = np.array([sumY, sumXY, sumXXY])

    VV1 = np.dot(np.linalg.inv(A), b)
    return VV1           #coeficientes

def minCuad(arrayX, arrayY, m, n):    #regresion de grado 2
    n = len(arrayX)
    sumXY = 0; sumX2 = 0; sumX = 0; sumY = 0
    sumX3 = 0; sumX4 = 0; sumXXY = 0

    for i in range(0, n):
        sumX += arrayX[i]
        sumX2 += arrayX[i]**2
        sumX3 += arrayX[i]**3
        sumX4 += arrayX[i]**4
        sumY += arrayY[i]
        sumXY += arrayX[i]*arrayY[i]
        sumXXY += (arrayX[i]**2)*arrayY[i]
    
    a0, a1, a2 = Gauss(sumXY, sumX2, sumX3, sumX4, sumXXY, sumX, sumY, n)
    return a0, a1, a2

def graficar(arrayX, arrayY):
    m = 2; n = len(arrayX)
    if n < m + 1:
        print('pocos datos (n > m + 1)')
    else:
        a0, a1, a2 = minCuad(arrayX, arrayY, m, n)

        resol = 100
        xx = np.linspace(-2, 12, resol)
        yy = a0 + a1*xx + a2*xx**2

        fig, ax = plt.subplots()
        ax.plot(xx, yy, 'r')
        ax.plot(arrayX, arrayY, 'o')
        plt.grid()
        plt.show()
    

x_dato = np.array([1.1, 2, 3.01, 4, 4.98, 6, 7.02, 8])
y_dato = np.array([2.5, 5.1, 8, 9.6, 10.8, 14, 15.1, 18])

#x_dato = np.array([1.1, 2.1, 3.01, 4, 4.98, 6.1, 7.02, 8, 9, 10])
#y_dato = np.array([4.1, 5.2, 12.2, 19, 31, 43, 52, 71, 84.6, 104])

graficar(x_dato, y_dato)
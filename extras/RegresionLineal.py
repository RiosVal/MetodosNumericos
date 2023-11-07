import numpy as np
import matplotlib.pyplot as plt

#----------------------ECUACIONES NORMALES----------------------


def ecuacion1(arrayX, arrayY):
    n = len(arrayX)
    sumatoriaXY = 0
    sumatoriaX = 0
    sumatoriaY = 0
    sumatoriaX2 = 0

    for i in range(0,n):
        sumatoriaXY += arrayX[i]*arrayY[i]
        sumatoriaX += arrayX[i]
        sumatoriaY += arrayY[i]
        sumatoriaX2 += arrayX[i]**2
    a1 = ((n*sumatoriaXY) - (sumatoriaX*sumatoriaY)) / ((n*sumatoriaX2) - ((sumatoriaX)**2)) 
    a0 = (sumatoriaY/n) - a1*(sumatoriaX/n)
    return (a0, a1)                      #coeficientes de la regresión lineal, a1 es la pendiente y a0 es el intercepto

def grafica(arrayX, arrayY):
    a0, a1 = ecuacion1(arrayX, arrayY)
    resol = 20
    xx = np.linspace(-1, 12, resol)
    yy = a0 + a1*xx             #ecueacion de regresión lineal simple

    fig, ax = plt.subplots()
    ax.plot(xx, yy, "b")
    ax.plot(arrayX, arrayY, "o")
    plt.grid()
    plt.show()

x_dato = np.array([1.1, 2, 3.01, 4, 4.98, 6, 7.02, 8])
y_dato = np.array([2.5, 5.1, 8, 9.6, 10.8, 14, 15.1, 18])


print(ecuacion1(x_dato, y_dato))
grafica(x_dato, y_dato)
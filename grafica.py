import numpy as np
import matplotlib.pyplot as plt
from funcsMenu import *


def grafica(funcion):
    rangoDerecho = float(input("Ingrese limite derecho del eje X: "))
    rangoIzquierdo = float(input("Ingrese limite izquierdo del eje X: "))
    rangoSuperior = float(input("Ingrese limite superior del eje Y: "))
    rangoInferior = float(input("Ingrese limite inferior del eje Y: "))
    x = np.linspace(rangoIzquierdo, rangoDerecho, 400)
    # Calcular los valores de y correspondientes a los valores de x
    y = usarFuncion(funcion, x)

    # Crear el gráfico
    plt.plot(x, y, label=funcion)
    plt.axhline(0, color='black', linewidth=0.5)  # Línea del eje x
    plt.axvline(0, color='black', linewidth=0.5)  # Línea del eje y
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Gráfico de la función {funcion} y Plano Cartesiano")
    plt.legend()
    plt.grid()
    plt.ylim(ymin = rangoInferior, ymax = rangoSuperior)
    plt.show()
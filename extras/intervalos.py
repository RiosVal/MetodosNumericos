import math

def f(x):
    funcion = math.exp(-x)-x 
    return funcion

def intervalos(distancia, repeticiones):
    x = distancia
    intervalosValidos = []
    x0 = x-distancia
    for i in range (0, repeticiones):
        if( (f(x0)*f(x)) < 0 ):
            intervaloAnadir =x0, x 
            intervalosValidos.append(intervaloAnadir)
        x += distancia
        x0 = x-distancia
        
    print(f"El o los intervalos donde hay una raiz: {intervalosValidos}")

intervalos(2, 5)

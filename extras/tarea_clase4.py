import math

def metodoFalsaPosicion(f, x0, x1, tol):
    anterior = x0

    for i in range(50):
        if f(x0) * f(x1) < 0:
            pos = x0 - (x0 - x1)*f(x0)/(f(x0) - f(x1))
        
        try:
            error = abs((pos - anterior) / pos)
            if error <= tol:
                break
        except:
            return None


        if f(x0) * f(pos) < 0:
            x1 = pos
            anterior = x1
        else:
            x0 = pos
            anterior = x0
    return (i, pos, error)


def metodoBiseccion(f, x0, x1, tol):
    anterior = x0
    for i in range(50):
        if f(x0) * f(x1) < 0:
            medio = (x0 + x1)/2
        else:
            return None
            #print('La función no tiene cero en ese intervalo')

        error = abs((medio - anterior) / medio)

        if error <= tol:
            break

        if f(x0) * f(medio) < 0:
            x1 = medio
            anterior = x1
        else:
            x0 = medio
            anterior = x0

    return (i, medio, error)
    #print('{:<6} {:<22} {:<20}'.format(i, medio, error))   

def cos(x, n=50):
    suma = 0
    for i in range(n):
        suma += ((-1) ** i) * ((x ** (2*i))/(math.factorial(2*i)))
    return suma

raices = []
intervalo = [0, 3*math.pi]
limite = intervalo[1]
inferior = 0
superior = 0

while superior < limite:
    superior = inferior + 0.2
    raiz = metodoBiseccion(cos, inferior, superior, 0.0000001)
    if raiz != None:
        raices.append([inferior, superior])
    inferior = superior
print(raices)
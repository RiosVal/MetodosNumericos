from calculadora import *
from funcsMenu import *
from grafica import *

def menu():
    bandera = True
    #math.exp(-x)-x
    while (bandera):
        bandera = False 
        print("-----------------------------------------------------------------")
        print("                           Calculadora                           ")
        print("-----------------------------------------------------------------")
        print("1. Calcular la derivada central de una funcion")
        print("2. Calcular la derivada hacia adelante de una funcion")
        print("3. Calcular la derivada hacia atras de una funcion")
        print("4. Calcular la raiz de una función con el método del punto fijo")
        print("5. Calcular la raiz de una función con el método de biseccion")
        print("6. Calcular la raiz de una función con el método de falsa posición")
        print("7. Calcular la raiz de una función con el método de newton raphson")
        print("8. Calcular la raiz de una función con el método de la secante")
        print("9. Calcular los intervalos en donde SI hay raices de una función")
        print("10. Graficar una función")
        opcion = int(input("Escoge la opcion de tu preferencia: "))
        if opcion < 0 or opcion > 9:
            print("Ingrese un número válido")
            bandera = True
    funcion = pedirFuncion()
    if opcion== 1:
        valorX = pedirValX()
        print(derivadaCentral(funcion, valorX, 0.0000001))
    elif opcion== 2:
        valorX = pedirValX()
        print(derivadaAdelante(funcion, valorX, 0.0000001))
    elif opcion== 3:
        valorX = pedirValX()
        print(derivadaAtras(funcion, valorX, 0.0000001))
    elif opcion== 4:
        valorX = pedirValX()
        i, xold, error = metodoPuntoFijo(funcion, valorX, 0.0000001)
        print('{:<3} {:<20} {:<25}'.format(i, xold, error))
    elif opcion== 5:
        x0, x1 = pedirIntervalo()
        i, medio, error = metodoBiseccion(funcion, x0, x1, 0.0000001)
        print('{:<6} {:<22} {:<20}'.format(i, medio, error))
    elif opcion== 6:
        x0, x1 = pedirIntervalo()
        i, pos, error = metodoFalsaPosicion(funcion, x0, x1, 0.0000001)
        print('{:<3} {:<22} {:<25}'.format(i, pos, error))
    elif opcion== 7:
        valorX = pedirValX()
        x1, error = metodoNewtonRaphson(funcion, valorX, 0.0000001)
        print('{:<22} {:<25}'.format(x1, error))
    elif opcion== 8:
        x0, x1 = pedirIntervalo()
        i, pos, error = MetodoSecante(funcion, x0, x1)
        print("{:<6} {:<22} {:<20}".format(i, pos, error))
    elif opcion == 9:
        inicio, fin = pedirIntervalo()
        
        menu =  """"
                Con qué metodo quieres econtrar las raices:
                1. Biseccion
                2. Falsa posición
                3. Secante
            """
        opciones2 = {
            1: metodoBiseccion,
            2: metodoFalsaPosicion,
            3: MetodoSecante
        }

        while True:
            print(menu)

            try:
                opcion2 = int(input("Escoge la opción de tu preferencia: "))
            except BaseException:
                print("Tienes que ingresar un valor correcto") 
                continue

            if opcion2 not in opciones2.values():
                break

        resultadoSeleccionado = opciones2.get(opcion2)

        if resultadoSeleccionado is None: 
            print("Opción no valida")
            return
        
        intervalos = calcularIntervalos(resultadoSeleccionado, funcion, inicio, fin)
        print("Las raices son: ")
        for intervalo in intervalos:
            a, b = intervalo
            print(resultadoSeleccionado(funcion, a, b, 0.0000001))
        #calcularIntervalos(metodoFalsaPosicion, funcion, inicio, fin)

    
        
    








#------------------------------------------------------------------------------------------------------------------------
def menu2(funcion):
    menu2 =  """"
                Con qué metodo quieres econtrar las raices:
                1. Biseccion
                2. Falsa posición
                3. Secante
            """
    opciones2 = {
        1: metodoBiseccion,
        2: metodoFalsaPosicion,
        3: MetodoSecante
        }

    while True:
        print(menu2)

        try:
            opcion2 = int(input("Escoge la opción de tu preferencia: "))
        except BaseException:
            print("Tienes que ingresar un valor correcto") 
            continue

        if opcion2 not in opciones2.values():
            break

        resultadoSeleccionado = opciones2.get(opcion2)

    if resultadoSeleccionado is None: 
        print("Opción no valida")
        return
    print("Los intervalos y las raices son: ")
    calcularIntervalos(resultadoSeleccionado, funcion)


def menu3():
    bandera = True
    #math.exp(-x)-x
    menu1 = """
        -----------------------------------------------------------------
                                   Calculadora                           
        -----------------------------------------------------------------
        1. Calcular la derivada central de una funcion
        2. Calcular la derivada hacia adelante de una funcion
        3. Calcular la derivada hacia atras de una funcion
        4. Calcular la raiz de una función con el método del punto fijo
        5. Calcular la raiz de una función con el método de biseccion
        6. Calcular la raiz de una función con el método de falsa posición
        7. Calcular la raiz de una función con el método de newton raphson
        8. Calcular la raiz de una función con el método de la secante
        9. Calcular los intervalos en donde SI hay raices de una función
        10. Graficar una función
        """
    opciones1 = {
        1:derivadaCentral,
        2:derivadaAdelante,
        3:derivadaAtras,
        4:metodoPuntoFijo,
        5:metodoBiseccion,
        6:metodoFalsaPosicion,
        7:metodoNewtonRaphson,
        8:MetodoSecante,
        9:menu2,
        10:grafica
        }
    while True:
        print(menu1)

        try:
            opcion1 = int(input("Escoge la opción de tu preferencia: "))
        except BaseException:
            print("Tienes que ingresar un valor correcto") 
            continue

        if opcion1 not in opciones1.values():
            break

    resultadoSeleccionado = opciones1.get(opcion1)

    if resultadoSeleccionado is None: 
        print("Opción no valida")
        return
    
    funcion = pedirFuncion()

    if opcion1 == 1 or opcion1 ==2 or opcion1 ==3 or opcion1 ==4 or opcion1 ==7:
        valX = pedirValX()
        print(resultadoSeleccionado(funcion, valX, 0.0000001))
    elif opcion1 == 10:
        resultadoSeleccionado(funcion)
    else:
        x0, x1 = pedirIntervalo()
        print(resultadoSeleccionado(funcion, x0, x1, 0.0000001))

menu3()


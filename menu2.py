from calculadora import *
from funcsMenu import *
from grafica import *

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
    
    calcularIntervalos2(resultadoSeleccionado, funcion)


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
    elif opcion1 == 10 or opcion1 == 9:
        resultadoSeleccionado(funcion)
    else:
        x0, x1 = pedirIntervalo()
        print(resultadoSeleccionado(funcion, x0, x1, 0.0000001))

menu3()
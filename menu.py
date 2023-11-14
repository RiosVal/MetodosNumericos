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
    
    calcularIntervalos(resultadoSeleccionado, funcion)


def menu():
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
        11. Calcular el área por sumas de riemman izquierda
        12. Calcular el área por sumas de riemman punto medio
        13. Calcular el área por trapecios 
        14. Calcular el área por simpson 1/3
        15. Calcular el área por simpson intervalos 
        16. Calcular el área por simpson 3/8
        17. Calcular el área por Romberg
        18. Calcular sistema de ecuaciones por Jacobi
        19. Calcular sistema de ecuaciones por Gauss Seidel
        20. Realizar regresión lineal
        21. Realizar regresión polinomial
        22. Realizar interpolación por metodo de lagrange 
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
        10:grafica,
        11: sumas_riemman_izquierda,
        12: sumas_riemman_punto_medio, 
        13: trapecio,
        14: simpson_un_tercio,
        15: simpson_intervalos,
        16: simpson_3_8_intervalos,
        17: romberg_integration,
        18: jacobi,
        19: gauss_seidel,
        20: regresion_lineal,
        21: regresion_polinomial,
        22: lagrange_interpolation
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
    
    if opcion1 < 18 or opcion1 == 22:
        funcion = pedirFuncion()

    if opcion1 == 1 or opcion1 ==2 or opcion1 ==3 or opcion1 ==4 or opcion1 ==7:
        valX = pedirValX()
        print(resultadoSeleccionado(funcion, valX, 0.0000001))
    elif opcion1 == 10 or opcion1 == 9:
        resultadoSeleccionado(funcion)
    elif opcion1 == 18 or opcion1 == 19:
        A, B = pedir_matriz()
        C = [0, 0, 0]
        print(resultadoSeleccionado(A, B, C))
    elif opcion1 == 20 or opcion1 == 21:
        resultadoSeleccionado()
    elif opcion1 == 22:
        val_X = pedirValX()
        print(lagrange_interpolation(funcion, val_X))
    else:
        x0, x1 = pedirIntervalo()
        print(resultadoSeleccionado(funcion, x0, x1, 0.0000001))

menu()
import math

def pedirFuncion():
    funcion = input("Ingresa la función a calcular: ")
    return funcion

def pedirValX():
    valX = int(input("Ingrese valor de X: "))
    return valX

def pedirIntervalo():
    x0 = int(input("Ingrese valor x0 del intervalo: "))
    x1 = int(input("Ingrese valor x1 del intervalo: "))
    return x0, x1

def usarFuncion(funcion, x):
    return eval(funcion)

def der (funcion, x, h = 0.001):
    retorno = (usarFuncion(funcion, x+h)-usarFuncion(funcion, x))/h
    return retorno

def biseccion(funcion, intervalo = 0, err = 1e-20, control = 0.1):
    if intervalo == 0:
        a, b = pedirIntervalo()
    else:
        a, b = intervalo 


    while control > err:
        fa, fb = usarFuncion(funcion, a), usarFuncion(funcion, b)
        Xtiempo = (a+b)/2
        fc = usarFuncion(funcion, Xtiempo)

        if (fc * fb) < 0:
            a = Xtiempo

        else:
            b = Xtiempo

        control = abs(fa-fb)

    print(f"La raiz es: {Xtiempo} ")

def newtonRaphson(funcion, err = 1e-20, control = 0.1):
    xi = pedirValX()
    
    while control > err :
        xi1 = xi -(usarFuncion(funcion, xi))/der(funcion, xi)  
        control = abs(xi-xi1)
        xi = xi1 
        
    print(xi)

def intervalos(funcion):
    distancia = int(input("Ingrese la distancia entre los intervalos: "))
    repeticiones = int(input("Ingrese cuantos intervalos quiere revisar: "))
    x = distancia
    intervalosValidos = []
    ingreso = []
    x0 = x-distancia
    
    for i in range (0, repeticiones):
        if( (usarFuncion(funcion, x0)*usarFuncion(funcion, x)) < 0 ):
            intervaloAnadir = x0, x 
            intervalosValidos.append(intervaloAnadir)
            
        x += distancia
        x0 = x-distancia
    

    menu2_string= f"""
        El o los intervalos donde hay una raiz: {intervalosValidos}
          
        Indique con qué función desea evaluar el o los intervalos: 
        1. Bisección
        2. Falsa posición 
        3. Secante
    """
    options2 = {
        1: biseccion,
        #Falsa posicion
        #Metodo secante
    }

    while True:
        print(menu2_string)

        try:
            opcion = int(input("Escoge la opcion de tu preferencia: "))

        except BaseException:
            print("Tienes que ingresar un valor correcto")
            continue

        if opcion not in options2.values():
            break
            
       
    selection_result = options2.get(opcion)

    if selection_result is None:
        print("Opcion no valida")
        return 
    
    for intervalo in intervalosValidos:
        selection_result(funcion, intervalo)

def menu():
    menu_string = """

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
        8. Calcular los intervalos donde hay una raiz y evaluarlos
"""

    options = {
        7: newtonRaphson,
        8: intervalos,
        5: biseccion,
    }

    while True:
        print(menu_string)

        try:
            opcion = int(input("Escoge la opcion de tu preferencia: "))

        except BaseException:
            print("Tienes que ingresar un valor correcto")
            continue

        if opcion not in options.values():
            break
            
       
    selection_result = options.get(opcion)

    if selection_result is None:
        print("Opcion no valida")
        return 
    
    fun = pedirFuncion()
    selection_result(fun)

menu()

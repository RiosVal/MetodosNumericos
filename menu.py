from calculadora import *

def pedirFuncion():
    funcion = input("Ingresa la función a calcular: ")
    return funcion

def menu():
    bandera = True
    
    while (bandera):
        bandera =False 
        print("-----------------------------------------------------------------")
        print("                           Calculadora                           ")
        print("-----------------------------------------------------------------")
        print("1. Calcular la derivada central de una funcion")
        print("2. Calcular la derivada hacia adelante de una funcion")
        print("3. Calcular la derivada hacia atras de una funcion")
        print("4. Calcular la raiz de una función con el método del punto fijo")
        print("5. Calcular la raiz de una función con el método de biseccion")
        print("6. Calcular la raiz de una función con el método de falsa posición")
        print("7. Calcular la raiz de una función con el método de nexton raphson")
        opcion = int(input("Escoge la opcion de tu preferencia"))
        if opcion < 0 or opcion > 7:
            print("Ingrese un número válido")
            bandera =True
        
    fun = pedirFuncion()
    if opcion== 1:
    elif opcion== 2:
    elif opcion== 3:
    elif opcion== 4:
    elif opcion== 5:
    elif opcion== 6:
    elif opcion== 7:
    
        
    



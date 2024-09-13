import time

numero = 1
palabra = "x"

while True:
    #Contar números
    print(f"Número: {numero}")
    numero = +1  #Sumar 1 al número
    time.sleep(3)  #Esperar 3 segundos

    #Cambiar la palabra
    palabra = input("Ingrese una palabra: ")
    print(f"La palabra ingresada es: {palabra}")
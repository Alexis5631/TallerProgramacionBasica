#Este programa funciona para adivinar un numero
import random

numero_aleatorio = random.randint(1,10)
print("¡Bienvenid@ al juego de adivinanza!")

while True:
    #Solicitar al usuario digitar un numero
    numero_adivinar = int(input("Introduce tu numero: "))
    if numero_adivinar < numero_aleatorio:
        print("El numero es mayor.")
    elif numero_adivinar > numero_aleatorio:
        print("El numero es menor.")
    else:
        print(f'¡Correcto! El numero era {numero_aleatorio}.')
        exit()#Salir del programa cuando se adivina el numero

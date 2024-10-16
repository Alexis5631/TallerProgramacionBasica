#Este programa funciona para que el usuario adivine una letra secreta
import random

letra_secreta = random.choice('AEIOU')

while True:   
    #solictar al usuario digite una letra
    adivinar = input("Adivina la letra secreta: ").upper()
    if adivinar not in 'AEOIU':
        print("Entrada no valida, solo puedes ingresar A, E, I, O, U")
        continue #continua el programa si se ingresa otra letra
    match adivinar:
        case adivinar if adivinar == letra_secreta:
            print("Felicidades, Adivinaste la letra secreta.")
            break #sale del bucle cuando se adivina la letra
        case _:
            print("Lo siento, esa no es la letra secreta")
        
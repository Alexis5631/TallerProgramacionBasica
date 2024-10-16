#Este programa funciona para clasificar un usuario segun su edad
edad = int(input("Digite su edad: "))

#clasificamos las edades
if edad <= 12:
    print("Eres un niño.")
elif edad <= 17:
    print("Eres un adolescente.")
elif edad <= 64:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")
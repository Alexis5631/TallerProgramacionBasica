#Este programa funciona para clasficar un triangulo segun los angulos
angulo1 = float(input("Introduce el primer angulo del triangulo: "))
angulo2 = float(input("Introduce el segundo angulo del triangulo: "))
angulo3 = float(input("Introduce el tercer angulo del triangulo: "))

#verificar si los angulos suman 180 grados
if angulo1 + angulo2 + angulo3 == 180:
    print("Los angulos no forman un triangulo valido.")
else: 
    #clasificamos el triangulo segun sus angulos
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        print("El triangulo es agudo.")
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        print("El triangulo es rectangulo.")
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("El triangulo es obtuso.")

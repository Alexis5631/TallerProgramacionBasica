#Este programa funciona para identificar un dia de la semana dado un numero
numero = int(input("Introduce un numero del 1 al 7: "))

#Mostrar el dia de la semana usando match
match numero:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Numero no valido, Digite un numero del 1 al 7.")
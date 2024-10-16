#Este programa funciona para determinar si un año es bisiesto
año = int(input("Introduce un año: "))

#Determinar si el año es bisiesto
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
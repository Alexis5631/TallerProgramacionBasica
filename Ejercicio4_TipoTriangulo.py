#Este programa define el tipo de triangulo en funcion de sus lados 
lado1 = int(input("Ingrese el valor del lado numero 1: "))
lado2 = int(input("Ingrese el valor del lado numero 2: "))
lado3 = int(input("Ingrese el valor del lado numero 3: "))

#Realizar la operacion 
if lado1 == lado2 == lado3:
    print("El triangulo es Equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isosceles.")
else:
    print("El triangulo es Escaleno.")

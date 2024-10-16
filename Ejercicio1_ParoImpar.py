#Este programa funciona para identificar si un numero es par o impar

numero = int(input('Ingrese un numero: '))

#Verficiar si el numero es par o impar 
if (numero % 2 == 0):
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")
    
#Este programa funciona para comparar entre 3 numeros cual es el mayor
#solicitamos al usuario ingresar 3 numeros
num1 = float(input("Ingrese el primer numero : "))
num2 = float(input("Ingrese el segundo numero : "))
num3 = float(input("Ingrese el tercer numero : "))

#determinamos el numero usando if
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

#mostrar resultado
print(f"El numero mayor es {mayor}.")
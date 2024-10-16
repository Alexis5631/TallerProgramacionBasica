#Este programa es una calculadora basica 
#Le pedimos al usuario que ingrese la operacion a realizar y los numeros 
operacion = input("Introduce la operación (+, -, *, /): ")
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

#Realizar la operacion con match
match operacion:
    case '+':
        resultado = numero1 + numero2        
    case '-':
        resultado = numero1 - numero2        
    case '*':
        resultado = numero1 * numero2       
    case '/':
        if numero2 == 0:
            print("Error en la division")
            exit() #Salir del programa en caso de error 
        resultado = numero1 / numero2

print(f"El resultado de {numero1} {operacion} {numero2} es {resultado}")
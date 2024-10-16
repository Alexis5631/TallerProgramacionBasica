#Este programa funciona para convertir calificaiones numericas a letras
calificacion = float(input("Ingrese tu calificacion (0-100): "))

#Convertimos los numeros a letras 
match calificacion:
    case calificacion if  calificacion < 0 or calificacion > 100:
        letra = 'calificacion fuera de rango'
        print("Recuerda ingresar una calificacion entre (0-100).")      
    case calificacion if calificacion >= 0 and calificacion <=  59:
        letra = 'F'
    case calificacion if calificacion >= 60 and calificacion <= 69:
        letra = 'D'
    case calificacion if calificacion >= 70 and calificacion <= 79:
        letra = 'C'
    case calificacion if calificacion >= 80 and calificacion <= 89:
        letra = 'B'
    case calificacion if calificacion >= 90 and calificacion <= 100:
        letra = 'A'

#Resultado
print(f'Tu calificacion en letra es: {letra}') 
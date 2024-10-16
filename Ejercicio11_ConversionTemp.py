#Este programa funciona para convertir grados Celsius a Fahrenheit o Fahrenheit a Celsius
temp = float(input("Ingrese la temperatura: "))
escala = (input("Ingrese una letra (C: (Celsius) o F: (Fahrenheit)): "))

#convertimos la temperatura a la escala opuesta 
match escala:
    case 'C':
        #CONVERTIR CELSIUS A FAHRENHEIT
        temperatura_convertida = (temp * 9/5) + 32
        print(f'{temp}°C es igual a {temperatura_convertida}°F.')
    case 'F':
        #CONVERTIR FAHRENHEIT A CELSIUS
        temperatura_convertida = (temp - 32) * 5/9
        print(f'{temp}°F es igual a {temperatura_convertida}°C.')
    case _:
        print("Escala no reconocida por favor ingresa C para celsius o F para fahtenheit.") 
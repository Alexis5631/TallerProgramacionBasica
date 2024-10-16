#Este programa funciona para calcular el indice de masa corporal 
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))


#calcular el IMC
imc = float((peso / (altura ** 2)))

#clasificar tu peso segun el IMC 
print(f'Tu IMC es: {imc:.2f}')

if imc < 18.5:
    print("Tienes bajo peso.")
elif imc <= 24.9:
    print("Tienes un peso normal")
elif imc <= 29.9:
    print("Tienes sobrepeso.")
else:
    print("Sufres de obesidad.")

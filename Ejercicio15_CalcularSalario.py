# Este programa calcula el salario neto despues de aplicar los impuestos

# Solicitamos al usuario ingresar su salario bruto y el país de residencia
salario_bruto = float(input("Ingresa tu salario bruto: "))
pais_residencia = input("Ingresa tu país de residencia \nPais A \nPais B \nPais C \nOtro \n: ").strip().upper()

# Calculamos el porcentaje de impuestos segun el pais
if pais_residencia == 'Pais A':
    impuesto = 0.20
elif pais_residencia == 'Pais B':
    impuesto = 0.15
elif pais_residencia == 'Pais C':
    impuesto = 0.10
else:
    impuesto = 0.25 

salario_neto = salario_bruto * (1 - impuesto)

# Resultado del salario neto
print(f'Tu salario neto despues de aplicar los impuestos es de: ${salario_neto: .0f}')
#Este programa calcula los creditos totales de un estudiante segun las materias cursadas
materias_cursadas = int(input("Ingrese el numero de materias cursadas: "))

#ponemos el contador de creditos en 0
total_creditos = 0

#Evaluar cada materia 
for i in range (materias_cursadas):
    porcentaje = float(input("Introduce el porcentaje obtenido en la materia: "))

    if porcentaje >= 60:
        total_creditos += 3 

print(f'El numero total de creditos es: {total_creditos}')
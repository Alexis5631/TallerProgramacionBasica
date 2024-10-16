#Este programa funciona para cuanto tiempo tarda en llegar un vehiculo a su destino
distancia = float(input("Ingrese la distancia a recorrer en (Km): "))
velocidad = float(input("Ingrese la velocidad promedio en la que va el vehiculo en (Km/h): "))

#advertencia si el vehiculo va a una velocidad de 120 Km/h
if velocidad >= 120:
    print("Advertencia vas a +120 Km/h, conduce con mas precaucion.")

#calcular el tiempo de viaje en horas 
tiempo_total_horas = distancia / velocidad

#calcular el tiempo en horas y minutos
horas = int(tiempo_total_horas)
minutos = int((tiempo_total_horas - horas) * 60 )

#mostrar el resultado
print(f'El tiempo estimado de viaje es de {horas} horas y {minutos} minutos.')
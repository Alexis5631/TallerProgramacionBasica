#Este programa funciona para mostrar la nota de un estudiante y darle puntos si hizo tareas extras
calificaion = float(input("Ingrese la calificaion: "))
bonificacion = input("Hizo tareas adicionales (si o no): ").lower()

#verficar si el estudiante hizo tareas adicionales
if bonificacion == 'si':
    calificaion += calificaion * 0.05

#si la calificacion pasa de 100, ajustarla a 100
if calificaion > 100:
    calificaion = 100

#resultado
print(f'La calificacion final del estudiante es de: {calificaion}')
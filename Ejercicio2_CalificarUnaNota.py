#Este programa funciona para saber mediante una nota si un estudiante es reprobado o aprobado 
nota = int(input('Ingrese la nota odtenida: '))

#Verficar si el estudiante reprueba o aprueba la materia 
if (nota >= 60):
    print("El estudiante fue Aprobado")
else:
    print("El estudiante fue Reprobado")
#Este programa funciona para asignar una clasificacion segun una nota numerica
nota = float(input("Ingrese su nota: "))

#Clasificamos las notas
if nota < 0 or nota >100:
    print("La nota debe estar entre 0 y 100.")
elif nota >= 90:
    print("Tu clasificacion es A.")
elif nota >= 80:
    print("Tu clasificacion es B.")
elif nota >= 70:
    print("Tu clasificaiomn es C")
elif nota >= 60:
    print("Tu clasificaion es D.")
else:
    print("Tu clasficacion es F.")
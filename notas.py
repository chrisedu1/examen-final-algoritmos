# Solicitar al usuario el nombre del estudiante y sus notas
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
notas = []
for i in range(4):
    nota = float(input(f"Ingrese la nota {i + 1}: "))  # Convertir la entrada a un número flotante
    notas.append(nota)

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Guardar los datos en el archivo "notas.txt"
with open("notas.txt", "a") as archivo:
    archivo.write(f"Nombre del estudiante: {nombre_estudiante}\n")
    archivo.write("Notas: " + ", ".join(map(str, notas)) + "\n")
    archivo.write(f"Promedio: {promedio}\n\n")

print("Datos guardados en el archivo 'notas.txt'.")
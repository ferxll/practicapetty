# Calcular el promedio de edades de 6 estudiantes

# Solicitar las edades de los 6 estudiantes
edades = []
for i in range(6):
    edad = int(input(f"Ingresa la edad del estudiante {i+1}: "))
    edades.append(edad)

# Calcular el promedio
promedio = sum(edades) / len(edades)

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Edades: {edades}")
print(f"Promedio de edades: {promedio:.2f} años")

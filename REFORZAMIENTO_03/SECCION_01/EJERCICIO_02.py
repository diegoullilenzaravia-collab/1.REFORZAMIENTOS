# Diccionario con los nombres de los estudiantes y sus notas
notas = {
    "Ana": 16,
    "Luis": 10,
    "María": 18,
    "Pedro": 8,
    "Rosa": 14
}

# Mostrar todos los estudiantes registrados
print("ESTUDIANTES REGISTRADOS:")
for nombre, nota in notas.items():
    print(f"{nombre}: {nota}")

# Mostrar estudiantes aprobados (nota >= 11)
aprobados = []

for nombre, nota in notas.items():
    if nota >= 11:
        aprobados.append(nombre)

print("\nEstudiantes aprobados:", ", ".join(aprobados))

# Calcular el promedio general
suma = sum(notas.values())
cantidad = len(notas)
promedio = suma / cantidad

print(f"Promedio general: {promedio:.2f}")

# Identificar al estudiante con mayor nota
mejor_estudiante = max(notas, key=notas.get)
nota_mayor = notas[mejor_estudiante]

print(f"Nota más alta: {nota_mayor} ({mejor_estudiante})")

# Contar estudiantes desaprobados (nota < 11)
desaprobados = 0

for nota in notas.values():
    if nota < 11:
        desaprobados += 1

print("Estudiantes desaprobados:", desaprobados)

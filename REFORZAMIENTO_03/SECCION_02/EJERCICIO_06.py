
# EJERCICIO 06: ANALISIS DE VENTAS SEMANALES

# Datos iniciales: ventas de los 7 dias
ventas = [150, 220, 180, 300, 175, 260, 190]

# 1. Funcion para calcular el total vendido
def calcular_total(ventas):
    return sum(ventas)


# 2. Funcion para calcular el promedio diario
def calcular_promedio(ventas):
    return sum(ventas) / len(ventas)


# 3. Funcion para identificar la venta maxima
def venta_maxima(ventas):
    return max(ventas)


# 4. Funcion para contar los dias que superaron el promedio
def dias_superiores_promedio(ventas, promedio):
    contador = 0

    for venta in ventas:
        if venta > promedio:
            contador += 1

    return contador


# LLAMADA A LAS FUNCIONES
total = calcular_total(ventas)
promedio = calcular_promedio(ventas)
maxima = venta_maxima(ventas)
dias = dias_superiores_promedio(ventas, promedio)


# MOSTRAR RESULTADOS
print("===== ANALISIS DE VENTAS SEMANALES =====")
print("Ventas registradas:", ventas)
print("Total vendido en la semana: S/.", total)
print("Promedio diario de ventas: S/.", round(promedio, 2))
print("Venta maxima registrada: S/.", maxima)
print("Dias que superaron el promedio:", dias)
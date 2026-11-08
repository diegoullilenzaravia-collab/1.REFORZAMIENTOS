
# EJERCICIO 01: CONTROL DE STOCK DE PRODUCTOS

# 1. Crear las listas de productos y cantidades
productos = ["Arroz", "Azúcar", "Aceite", "Leche", "Fideos"]
cantidades = [8, 3, 12, 2, 6]

# 2. Mostrar cada producto con su cantidad
print("PRODUCTOS REGISTRADOS:")

for i in range(len(productos)):
    print(f"{productos[i]}: {cantidades[i]} unidades")

# 3. Calcular el total de unidades disponibles
total = 0

for cantidad in cantidades:
    total = total + cantidad

print("\nTotal de unidades disponibles:", total)

# Identificar productos con menos de 5 unidades
print("\nPRODUCTOS CON MENOS DE 5 UNIDADES:")

stock_bajo = 0

for i in range(len(productos)):
    if cantidades[i] < 5:
        print(f"- {productos[i]}: {cantidades[i]} unidades")
        stock_bajo += 1

# 4. Mostrar mensaje si ningún producto tiene stock bajo
if stock_bajo == 0:
    print("Ningún producto tiene stock bajo.")

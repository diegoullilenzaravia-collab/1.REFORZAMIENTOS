
# ==========================================
# SISTEMA DE COMPRAS DE UNA TIENDA
# ==========================================

# 1. Diccionario con los productos y sus precios
precios = {
    "Teclado": 75,
    "Mouse": 45,
    "Audífonos": 120,
    "USB": 35
}

# Lista de productos seleccionados
carrito = ["Teclado", "Audífonos", "USB"]

# Variables para los cálculos
subtotal = 0
descuento = 0

print("===== PRODUCTOS SELECCIONADOS =====")

# 2. Recorrer la lista de compras
for producto in carrito:

    # 4. Verificar si el producto existe
    if producto in precios:
        precio = precios[producto]

        print(f"{producto}: S/ {precio:.2f}")

        # Acumular el importe
        subtotal += precio

    else:
        print(f"Producto no registrado: {producto}")

# 3. Aplicar descuento del 10 % si supera S/ 200
if subtotal > 200:
    descuento = subtotal * 0.10

# Calcular total a pagar
total = subtotal - descuento

# Mostrar resultados finales
print("\n===== RESUMEN DE COMPRA =====")
print(f"Subtotal: S/ {subtotal:.2f}")
print(f"Descuento (10 %): S/ {descuento:.2f}")
print(f"Total a pagar: S/ {total:.2f}")

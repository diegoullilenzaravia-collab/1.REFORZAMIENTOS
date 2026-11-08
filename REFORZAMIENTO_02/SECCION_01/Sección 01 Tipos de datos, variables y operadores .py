
# EJERCICIO 10: CONVERSION NUMERICA Y MULTIPLOS

# 1. Crear dos variables de tipo float
numero1 = 20.8
numero2 = 5.2

# 2. Convertir los valores a enteros
entero1 = int(numero1)
entero2 = int(numero2)

# 3. Mostrar valores originales y convertidos
print("===== CONVERSION DE NUMEROS =====")
print("Primer numero original:", numero1)
print("Segundo numero original:", numero2)

print("Primer numero entero:", entero1)
print("Segundo numero entero:", entero2)

# 4. Comprobar si el primer numero es multiplo del segundo
residuo = entero1 % entero2

if residuo == 0:
    print("Los numeros SI son multiplos.")
else:
    print("Los numeros NO son multiplos.")

# 5. Calcular el cociente
cociente = entero1 / entero2

# 6. Mostrar residuo y cociente con dos decimales
print("Residuo:", residuo)
print("Cociente:", format(cociente, ".2f"))


# EJERCICIO 04: SUMA DE DIGITOS Y COMPARACION

# 1. Funcion que recibe un numero y suma sus digitos
def sumar_digitos(numero):
    suma = 0

    while numero > 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10

    return suma


# 2. Numeros predefinidos
numero_1 = 583
numero_2 = 241

# 3. Calcular la suma de los digitos
suma_1 = sumar_digitos(numero_1)
suma_2 = sumar_digitos(numero_2)

# 4. Mostrar los resultados
print("NUMERO 1:", numero_1)
print("SUMA DE SUS DIGITOS:", suma_1)

print("NUMERO 2:", numero_2)
print("SUMA DE SUS DIGITOS:", suma_2)

# 5. Comparar las sumas de los digitos
print("\nCOMPARACION DE RESULTADOS")

if suma_1 > suma_2:
    print("El numero", numero_1, "tiene mayor suma de digitos")

elif suma_2 > suma_1:
    print("El numero", numero_2, "tiene mayor suma de digitos")

else:
    print("Existe un empate en la suma de digitos")

# 6. Identificar numeros cuya suma sea menor que 10
print("\nNUMEROS CON SUMA MENOR QUE 10")

if suma_1 < 10:
    print("El numero", numero_1, "tiene una suma menor que 10")

if suma_2 < 10:
    print("El numero", numero_2, "tiene una suma menor que 10")

if suma_1 >= 10 and suma_2 >= 10:
    print("Ninguno tiene una suma menor que 10")

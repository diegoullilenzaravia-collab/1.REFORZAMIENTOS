
# Funcion para eliminar la primera aparicion de un valor
def eliminar_valor(lista, valor):
    nueva_lista = lista.copy()

    if valor in nueva_lista:
        nueva_lista.remove(valor)

    return nueva_lista


# Datos iniciales
numeros = [10, 20, 30, 20, 40]

# Prueba 1: eliminar un valor existente
eliminar = 20

resultado = eliminar_valor(numeros, eliminar)

print("PRUEBA 1: VALOR EXISTENTE")
print("Lista original:", numeros)
print("Valor buscado:", eliminar)
print("Lista resultante:", resultado)


# Prueba 2: eliminar un valor inexistente
eliminar = 50

resultado = eliminar_valor(numeros, eliminar)

print("\nPRUEBA 2: VALOR INEXISTENTE")
print("Lista original:", numeros)
print("Valor buscado:", eliminar)
print("Lista resultante:", resultado)

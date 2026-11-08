
class CuentaBancaria:
    # Constructor de la clase
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    # Método para depositar dinero
    def depositar(self, monto):
        if monto <= 0:
            print("Error: El depósito debe ser mayor a cero.")
        else:
            self.saldo += monto
            print(f"Depósito exitoso: S/ {monto:.2f}")

    # Método para retirar dinero
    def retirar(self, monto):
        if monto <= 0:
            print("Error: El retiro debe ser mayor a cero.")
        elif monto > self.saldo:
            print("Error: Saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso: S/ {monto:.2f}")

    # Método para mostrar el saldo
    def mostrar_saldo(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: S/ {self.saldo:.2f}")


# Crear una cuenta bancaria
cuenta = CuentaBancaria("María López", 500)

print("===== CUENTA BANCARIA =====")
cuenta.mostrar_saldo()

# Realizar tres depósitos
print("\n===== DEPÓSITOS =====")
cuenta.depositar(200)
cuenta.depositar(150)
cuenta.depositar(100)

# Realizar tres intentos de retiro
print("\n===== RETIROS =====")
cuenta.retirar(100)
cuenta.retirar(300)
cuenta.retirar(1000)

# Mostrar saldo final
print("\n===== SALDO FINAL =====")
cuenta.mostrar_saldo()

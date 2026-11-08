
class Agenda:
    # Constructor de la clase
    def __init__(self):
        self.contactos = []

    # Método para agregar contactos
    def agregar_contacto(self, nombre, telefono, email, dni):

        # Verificar si el DNI ya existe
        if self.buscar_por_dni(dni) is not None:
            print(f"ERROR: El DNI {dni} ya está registrado.")
            return False

        # Crear diccionario del contacto
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "dni": dni
        }

        self.contactos.append(contacto)
        print(f"Contacto {nombre} agregado correctamente.")
        return True

    # Método para mostrar todos los contactos
    def mostrar_contactos(self):

        print("\n===== LISTA DE CONTACTOS =====")

        if len(self.contactos) == 0:
            print("La agenda está vacía.")
            return

        for contacto in self.contactos:
            print("----------------------------")
            print("Nombre:", contacto["nombre"])
            print("Teléfono:", contacto["telefono"])
            print("Email:", contacto["email"])
            print("DNI:", contacto["dni"])

    # Método para buscar un contacto por DNI
    def buscar_por_dni(self, dni):

        for contacto in self.contactos:
            if contacto["dni"] == dni:
                return contacto

        return None


# ==================================
# PROGRAMA PRINCIPAL
# ==================================

# Crear objeto de la clase Agenda
mi_agenda = Agenda()

# Agregar tres contactos
mi_agenda.agregar_contacto(
    "Diego Ullilen", "987654321",
    "diego@gmail.com", "12345678"
)

mi_agenda.agregar_contacto(
    "Carlos Perez", "956789123",
    "carlos@gmail.com", "87654321"
)

mi_agenda.agregar_contacto(
    "Maria Lopez", "945678123",
    "maria@gmail.com", "45678912"
)

# Intentar registrar un DNI repetido
mi_agenda.agregar_contacto(
    "Pedro Torres", "912345678",
    "pedro@gmail.com", "12345678"
)

# Mostrar todos los contactos
mi_agenda.mostrar_contactos()

# Primera búsqueda: DNI existente
print("\n===== PRIMERA BUSQUEDA =====")

resultado = mi_agenda.buscar_por_dni("12345678")

if resultado is not None:
    print("Contacto encontrado:")
    print(resultado)
else:
    print("No se encontraron coincidencias.")

# Segunda búsqueda: DNI inexistente
print("\n===== SEGUNDA BUSQUEDA =====")

resultado = mi_agenda.buscar_por_dni("11111111")

if resultado is not None:
    print("Contacto encontrado:")
    print(resultado)
else:
    print("No se encontraron coincidencias.")

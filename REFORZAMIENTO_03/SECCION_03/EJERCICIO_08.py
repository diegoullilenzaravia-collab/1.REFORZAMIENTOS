
# Crear la clase Alumno
class Alumno:

    # Constructor
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    # Metodo para mostrar los datos del alumno
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Nota final:", self.nota_final)
        print("Condicion academica:", self.obtener_condicion())
        print("-----------------------------")

    # Metodo para retornar la condicion academica
    def obtener_condicion(self):
        if self.nota_final >= 11:
            return "Aprobado"
        else:
            return "Desaprobado"


# Crear tres objetos de la clase Alumno
alumno1 = Alumno("Ana", 18, 16)
alumno2 = Alumno("Luis", 20, 9)
alumno3 = Alumno("Rosa", 19, 13)

# Almacenar los objetos en una lista
lista_alumnos = [alumno1, alumno2, alumno3]

# Recorrer la lista y mostrar la informacion
print("===== REGISTRO DE ALUMNOS =====")

for alumno in lista_alumnos:
    alumno.mostrar_datos()

# Mostrar cantidad de alumnos
print("Total de alumnos registrados:", len(lista_alumnos))
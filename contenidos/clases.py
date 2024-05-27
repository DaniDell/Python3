# Definición de la clase
class Persona:
    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de la clase
    def saludo(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Creación de un objeto de la clase Persona
juan = Persona("Juan", 30)

# Uso de los atributos del objeto
print(juan.nombre)  # Imprime: Juan
print(juan.edad)  # Imprime: 30

# Uso de los métodos del objeto
juan.saludo()  # Imprime: Hola, mi nombre es Juan y tengo 30 años.
class Animal():
    # Constructor de la clase Animal
    # Atributos de la clase Animal (características compartidas por  todos los objetos de la clase)
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    # Métodos de la clase Animal (comportamientos)
    def correr(self):
        print(f"{self.nombre} está corriendo")

    def dormir(self):
        print(f"{self.nombre} está durmiendo")

# Creando un objeto de la clase Animal
gatito = Animal("Tom", "Gato", 4)
perrito = Animal("Pluto", "Perro", 2)
conejito = Animal("Bugs Bunny", "Conejo", 3)

# Impresión de los atributos de los objetos
print(f"El nombre del animal {gatito.especie} es: {gatito.nombre}")
print(f"El nombre del animal {perrito.especie} es: {perrito.nombre}")
print(f"El nombre del animal {conejito.especie} es: {conejito.nombre}")
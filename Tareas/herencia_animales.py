class Animal:
    # Creación de la Superclase Animal y mejorar el __init__
    def __init__(self, nombre, edad, peso, género):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.género = género

    # Métodos Generales
    def comer(self):
        print(f"- {self.nombre} está comiendo")

    def dormir(self):
        print(f"- {self.nombre} está durmiendo")

    # Método de Ficha
    def mostrar_ficha(self):
        print(f"- Nombre: {self.nombre}")
        print(f"- Edad: {self.edad} años")
        print(f"- Peso: {self.peso} kg")
        print(f"- Género: {self.género}")

# Subclase de Perro
class Perro(Animal):
    def __init__(self, nombre, edad, peso, género, raza):
        # Llamar al constructor de la clase base Animal
        super().__init__(nombre, edad, peso, género)
        self.raza = raza
    
    # Método Específico
    def ladrar(self):
        print(f"- {self.nombre} está ladrando")
    
    # Método de Ficha
    def mostrar_ficha(self):
        # Llamar al método de mostrar_ficha() de la clase base
        super().mostrar_ficha()
        print(f"- Raza: {self.raza}")

# Subclase de Gato
class Gato(Animal):
    def __init__(self, nombre, edad, peso, género, color_pelaje):
        # Llamar al constructor de la clase base Animal
        super().__init__(nombre, edad, peso, género)
        self.color_pelaje = color_pelaje
    
    # Método Específico
    def maullar(self):
        print(f"- {self.nombre} está maullando")
    
    # Método de Ficha
    def mostrar_ficha(self):
        # Llamar al método de mostrar_ficha() de la clase base
        super().mostrar_ficha()
        print(f"- Color de pelaje: {self.color_pelaje}")

# Subclase de Pajaro
class Pajaro(Animal):
    def __init__(self, nombre, edad, peso, género, color_plumaje):
        # Llamar al constructor de la clase base Animal
        super().__init__(nombre, edad, peso, género)
        self.color_plumaje = color_plumaje
    
    # Método Específico
    def volar(self):
        print(f"- {self.nombre} está volando alto")
    
    # Método de Ficha
    def mostrar_ficha(self):
        # Llamar al método de mostrar_ficha() de la clase base
        super().mostrar_ficha()
        print(f"- Color de plumaje: {self.color_plumaje}")

# Creación de Instancias
print(f"\n################################\n")
# Probando la clase Perro
print("DESCRIPCIÓN DEL PERRO:")
perro = Perro("Martha", 4, 25, "Hembra", "Labrador")
perro.mostrar_ficha()
print("ACCIONES:")
perro.ladrar()
perro.comer()
perro.dormir()

print(f"\n################################\n")
# Probando la clase Gato
print("DESCRIPCIÓN DEL GATO:")
gato = Gato("Stuart", 2, 7, "Macho", "Gris")
gato.mostrar_ficha()
print("ACCIONES")
gato.maullar()
gato.comer()
gato.dormir()

print(f"\n################################\n")
# Probando la clase Pajaro
print("DESCRIPCIÓN DEL PAJARO:")
pajaro = Pajaro("Gerardo", 3, 10, "Macho", "Verde")
pajaro.mostrar_ficha()
print("ACCIONES:")
pajaro.volar()
pajaro.comer()
pajaro.dormir()

print(f"\n################################\n")
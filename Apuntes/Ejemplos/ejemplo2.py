class Camión():
    # Constructor de la clase Camión
    # Atributos de la clase Camión (características compartidas por todos los objetos de la clase)
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
    
    # Métodos de la clase Camión (comportamientos)
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando")
    
    def frenar(self):
        print(f"El {self.marca} {self.modelo} está frenando")

    def acelerar(self):
        print(f"El {self.marca} {self.modelo} está acelerando")

# Creando un objeto de la clase Camión
camión_1 = Camión("Chevrolet", "Cisterna", 2019, "Negro")
camión_2 = Camión("Hyundai", "Portacoches", 2022, "Blanco")
camión_3 = Camión("Ford", "Carretera", 2020, "Gris")

# Impresión de los atributos de los objetos
print(f"El año del primer camión de color {camión_1.color} es del {camión_1.año}")
print(f"El año del segundo camión de color {camión_2.color} es del {camión_2.año}")
print(f"El año del tercer camión de color {camión_3.color} es del {camión_3.año}")

camión_1.arrancar()
camión_2.frenar()
camión_3.acelerar()
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
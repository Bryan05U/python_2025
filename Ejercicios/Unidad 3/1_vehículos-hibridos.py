# Clase base de Vehículo con el método moverse()
class Vehículo:
    def moverse(self):
        pass

# Vehículo Terrestre
class Terrestre(Vehículo):
    def rodar(self):
        print(f"El vehículo terrestre {self.__class__.__name__} está rodando sobre la carretera")

class Coche(Terrestre):
    def moverse(self):
        self.rodar()


# Clase de Vehículo Acuático
class Acuático(Vehículo):
    def navegar(self):
        print(f"El vehículo acuático {self.nombre} está navegando sobre el mar")

class Moto_Acuática():
    def moverse(self):
        self.navegar()

# Clase de Vehículo Aéreo
class Aéreo(Vehículo):
    def volar(self):
        print(f"El vehículo aéreo {self.nombre} está volando en el aire")

# Clase de Vehículo Híbrido
class Híbrido(Vehículo):
    def moverse(self):
        self.rodar()
        self.navegar()
    
    def rodar(self):
        print(f"El vehículo híbrido {self.nombre} está rodando sobre la tierra")
    
    def navegar(self):
        print(f"El vehículo híbrido {self.nombre} está navegando sobre el mar")

# Creación de vehículos
carrera_de_vehículos = [
    
]
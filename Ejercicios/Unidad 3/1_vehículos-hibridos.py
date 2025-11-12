import time, random

#################################################
# Clase base de Vehículo con el método moverse()
class Vehículo:
    def moverse(self, nombre):
        self.nombre = nombre
#################################################
    

# Clase de Vehículo Terrestre
class Terrestre(Vehículo):
    def moverse(self):
        # Llamando la función self.rodar() 
        self.rodar()

    def rodar(self):
        print(f"El vehículo terrestre {self.nombre} está rodando sobre la carretera")

# Clase de Vehículo Acuático
class Acuático(Vehículo):
    def moverse(self):
        # Llamando la función self.navegar()
        self.navegar()
    
    def navegar(self):
        print(f"El vehículo acuático {self.nombre} está navegando sobre el mar")

# Clase de Vehículo Aéreo
class Aéreo(Vehículo):
    def moverse(self):
        # Llamando la función self.volar()
        self.volar()
    
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

# Función de simulación de carrera
def simular_carrera(vehículos):
    print()

# Creación de vehículos
vehículo1 = Terrestre("Auto")
class Vehículo:
    # Constructor de la clase Coche
    # Atributos privados de la clase Coche
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__disponible = True
    
    # Método para marcar estado del vehículo a "No Disponible"
    def marcar_venta(self):
        self.__disponible = False
    
    # Método que muestra los detalles del vehículo
    def __str__(self):
        if self.__disponible:
            estado = "Disponible"
        else:
            estado = "No disponible"
        return f"Marca: {self.__marca} | Modelo: {self.__modelo} | Año: {self.__año} | Estado: {estado}"

class Concesionaria:
    # Constructor de la clase Concesionaria
    def __init__(self):
        self.vehículos = [] # Lista pública de vehículos

    # Método para añadir vehículos nuevos a la concesionaria
    def agregar_vehículo(self, vehículo):
        self.vehículos.append(vehículo)

    # Método para listar todos los vehículos que están disponibles en la concesionaria
    def mostrar_vehículos(self):
        print("##### Vehículos disponibles en la concesionaria #####")
        for vehículo in self.vehículos:
            if vehículo._Vehículo__disponible:
                print(Vehículo)
    
    # Método para cambiar el estado de disponibilidad del vehículo
    def vender_vehículo(self, vehículo):
        if vehículo in self.vehículos:
            if vehículo._Vehículo__disponible:
                vehículo.marcar_venta()
                print(f"El vehículo {vehículo} ha sido vendido")
            else:
                print(f"No se encuentra disponible el vehículo {vehículo}")
        else:
            print(f"El vehículo {vehículo} no está en la concesionaria")

concesionaria = Concesionaria()

# Creación de objetos de la clase Vehículo
vehículo_1 = Vehículo("Toyota", "GR Yaris", 2020)
vehículo_2 = Vehículo("Volkswagen", "Sedan", 2022)
vehículo_3 = Vehículo("Hyundai", "HB20 HB", 2017)

# Agregando vehículos a la concesionaria
concesionaria.agregar_vehículo(vehículo_1)
concesionaria.agregar_vehículo(vehículo_2)
concesionaria.agregar_vehículo(vehículo_3)

# Mostrar la lista de vehículos
concesionaria.mostrar_vehículos()

# Vender un vehículo
concesionaria.vender_vehículo(vehículo_3)

# Mostrar la lista actualizada
concesionaria.mostrar_vehículos()
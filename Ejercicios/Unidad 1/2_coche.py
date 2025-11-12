import math
class Coche():
    # Constructor de la clase Coche
    # Atributos de la clase Coche (características compartidas por  todos los objetos de la clase)
    def __init__(self, marca, gasolina):
        self.marca = marca
        self.gasolina = float(gasolina)
        self.km_recorridos = 0.0
    
    # Métodos (comportamientos)
    def conducir(self, km):
        gasolina_necesaria = km / 10

        # Averiguar si hay gasolina necesaria
        if gasolina_necesaria <= self.gasolina:
            self.actualizar_estado(km, gasolina_necesaria)
            print(f"Recorriste {km} km/h\n - Te quedan {self.gasolina:.2f} litros de gasolina")
        else:
            km_posibles = self.gasolina * 10
            self.actualizar_estado(km_posibles, self.gasolina)
            print(f"Recorriste {km} km/h\n - Se acabó la gasolina")

    def cargar_gasolina(self, litros):
        self.gasolina += litros
        print(f"Llenaste {litros} litros\n - Ahora tienes {self.gasolina:.2f} litros de gasolina")

    def actualizar_estado(self, km, gasolina_usada):
        self.km_recorridos += km
        self.gasolina = gasolina_usada

# Creando un objeto de la clase Coche
coche = Coche("Chevrolet", 30)

# Acceso a los atributos y métodos del objeto
print(f"Tu marca de coche: {coche.marca}")

# Llamando a los métodos de la clase Coche
coche.conducir(30)
coche.conducir(60)
coche.cargar_gasolina(20)
coche.conducir(30)
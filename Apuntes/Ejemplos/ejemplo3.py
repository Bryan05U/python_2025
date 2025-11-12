class Animal:
    def caminar(self):
        print("El animal está caminando")

class AnimalPesoLigero(Animal):
    def saltar(self):
        print("El animal está saltando")

class Gato(AnimalPesoLigero):
    pass

class Elefante(Animal):
    pass
    
def saltar_agujero(animal: AnimalPesoLigero):
    animal.caminar()
    animal.saltar()
    animal.saltar_agujero()
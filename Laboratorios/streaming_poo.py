# Clase Base Principal
class Contenido:
    def __init__(self, título, año):
        self.título = título
        self.año = año
    
    def mostrar_detalle(self):
        print(f"Título: {self.título}, Año: {self.año}")

# Estructuras de Clases
class Reproducible:
    def reproducir(self):
        pass

class Calificable:
    def __init__(self):
        self.rating = 0.0

    def calificar(self, puntuación):
        if puntuación >= 0.0 and puntuación <= 10:
            print(f"Rating: {self.rating}")
        else:
            print("La puntuación ingresada no es válida") # No me funcionó

# Subclases
class Película(Contenido, Reproducible):
    def __init__(self, título, año, duración_minutos):
        super().__init__(título, año)
        self.duración_minutos = duración_minutos
    
    def reproducir(self):
        print(f"Reproduciendo película... {self.título}")

class Documental(Contenido):
    def __init__(self, título, año, tema):
        super().__init__(título, año)
        self.tema = tema

# LSP que solo permite reproducir clases que corresponden
def lista_de_reproducción(medio: Reproducible):
    medio.reproducir()

class Miniserie(Contenido, Reproducible, Calificable):
    def __init__(self, título, año, num_episodios):
        super().__init__(título, año)
        self.num_episodios = num_episodios
    
    def reproducir(self):
        print(f"Reproduciendo miniserie... {self.título}")
    
# Instancias
película = Película("ICINF - La Película", 2025, 120)
documental = Documental("Un Documental sobre ICINF", 2025, "Drama")
miniserie = Miniserie("ICINF - La Serie", 2025, 50)

print("Película")
película.mostrar_detalle()
print()
print("Documental")
documental.mostrar_detalle()
print()
print("Miniserie")
miniserie.mostrar_detalle()
print()

lista_reproducible = [película, miniserie]
for item in lista_reproducible:
    lista_de_reproducción(item)

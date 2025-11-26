# Superclase
class ArchivoMultimedia:
    def __init__(self, nombre, tamaño_mb):
        self.nombre = nombre
        self.tamaño_mb = tamaño_mb
    
    def obtener_peso(self):
        return self.tamaño_mb

# Clase intermedia para cosas que sí se reproducen
class Reproducible(ArchivoMultimedia):
    def reproducir(self):
        pass

# Las subclases ahora heredan de donde corresponde
class Audio(Reproducible):
    def reproducir(self):
        print(f"Reproduciendo audio: {self.nombre}")
    
class Video(Reproducible):
    def reproducir(self):
        print(f"Reproduciendo video: {self.nombre}")
    
class Imagen(ArchivoMultimedia):
    def mostrar(self):
        print(f"Mostrando imagen en pantalla: {self.nombre}")
    
# Función corregida: Solo acepta tipos "reproducible"
def reproductor_seguro(medio: Reproducible):
    medio.reproducir()

# Prueba
audio = Audio("canción.flac", 20)
video = Video("video.mp4", 500)
imagen = Imagen("imagen.png", 5)

lista_reproducible = [audio, video]

for item in lista_reproducible:
    reproductor_seguro(item)

imagen.mostrar()
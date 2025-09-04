class Canción:
    # Constructor de la clase Canción
    def __init__(self, título, artista, duración_segundos):
        self.título = título
        self.artista = artista
        self.duración_segundos = int(duración_segundos)
    
    # Métodos de clase
    # Convertir la duración a formato mm:ss 
    def milisegundos(self):
        # Corroborar el paso de milisegundos a minutos
        m, s = divmod(max(self.duración_segundos(), 0), 60)
        return f"{m}:{s}"
    
    def __str__(self):
        return f"{self.título} - {self.artista} - {self.duración_segundos}"

class Playlist:
    # Constructor de la clase Playlist
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = [] # Lista del número de canciones de la playlist
    
    # Métodos de clase
    # Añadir cancion a la playlist
    def agregar(self, canción):
        self.canciones.append(canción)

    # Duración total de la playlist
    def duración_total(self):
        # Iterador for en una línea
        return sum(c.duración_segundos for c in self.canciones)

    # Mostrar la duración total en mm:ss
    def milisegundos_total(self):
        total = self.duración_total() 
        m, s = divmod(max(total, 0), 60)
        return f"{m}:{s}"

    # Contar el número de canciones
    def __len__(self):
        return len(self.canciones)

    # Combinación de las dos playlists
    def __add__(self, other):
        # Crear una variable que fusiona ambas playlists en una nueva
        nueva = Playlist(f"{self.nombre} + {other.nombre}")

        # Guardando las canciones en las playlists combinadas
        nueva.canciones = self.canciones + other.canciones
        return nueva
    
    def __str__(self):
        # Encabezado a mostrar de la Playlist
        encabezado = f"Playlist: {self.nombre} | {len(self.canciones)} | Total: {self.milisegundos_total()}"

        # Lanzar mensaje si la lista está vacia
        if not self.canciones:
            return encabezado, f"Lista Vacía"
        
        # Para la creación del formato de impresión de la playlist
        líneas = [encabezado]
        # Creación de ciclo para mostrar el listado de canciones de la playlist combinada
        for i, c in enumerate(self.canciones):
            líneas.append(f"{i}: {c}")
            return "\n".join(líneas) # Combina el salto de línea

# Instanciar Clases (creación de objetos)

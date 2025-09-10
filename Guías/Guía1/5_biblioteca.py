class Libro:
    def __init__(self, título, autor, año_publicación, cantidad):
        self.título = título
        self.autor = autor
        self.año_publicación = año_publicación
        self.cantidad = cantidad
    

class Bibloteca:
    def __init__(self):
        self.libros = {}
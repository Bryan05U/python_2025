class Libreria:
    # Variable de Clase
    __descuento_frecuente = 0.05 # (descuento inicial: 5%)
    
    __descuento_min = 0.05 # 5% de descuento como mínimo
    __descuento_max = 0.10 # 10% de descuento como máximo

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__catálogo = {} # Título del libro como clave y su precio como valor
        self.__carrito = [] # Lista de títulos (strings)
    
    # Métodos de Clase
    @staticmethod
    
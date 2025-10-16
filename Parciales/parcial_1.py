# Implementar Clase Jugador
class Jugador:
    JUGADORES_CREADOS = 0
    POSICIONES_VALIDAS = {"DEL", "VOL", "DEF", "ARQ"}

    def __init__(self, nombre, edad, posicion, club: str, energia):
        # Atributos privados
        self.__nombre = nombre; assert nombre != ""
        self.__edad = edad; assert edad >= 15
        self.__posicion = posicion
        self.goles = 0
        # Atributos públicos
        self.club = club; assert club != ""
        self.energia = energia; assert 0 <= energia <= 100
    
    @classmethod
    def creados(cls):
        return cls.JUGADORES_CREADOS
    
    @staticmethod
    def posicion_valida(self):
        if self.posicion not in self.POSICIONES_VALIDAS:
            return False
        else:
            return True
    @property
    def nombre(self):
        if self.nombre == "":
            raise ValueError("El nombre no puede ser vacío")
        assert self.nombre

    @property
    def edad(self):
        if self.edad <= 15:
            raise ValueError("El jugador es muy jóven para ir a jugar")
        assert self.edad

    
    def entrenar(self, minutos):
        self.minutos = minutos > 0
        if self.minutos:
            self.energia -= 1
    
    # Métodos de Clase
    def anotar_gol(self):
        self.goles += 1
        assert self.goles >= 0

    def __str__(self):
        return f"Nombre: {self.__nombre} | Club: {self.club} | Posición: {self.__posicion} | Energía: {self.energia} | Goles: {self.goles}"

# Instancias de Clase
jugador_1 = Jugador("Bryan", 20, "DEF", "Club 1", 70)
jugador_2 = Jugador("Jorge", 21, "DEL", "Club 2", 90)
print("### Lista de Jugadores ###")
Jugador.creados()
print(jugador_1)
print(jugador_2)

print(" ")

jugador_2.entrenar(5)
print("### Entrenar ###")
print(jugador_2)

print(" ")

jugador_1.anotar_gol()
jugador_2.anotar_gol()
print("### Anotar gol ###")
print(jugador_1)
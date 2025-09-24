class Fracción():
    # Constructor de Clase
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("Error: El denominador no puede ser 0")
        self.numerador = numerador
        self.denominador = denominador

    # Método mágico que devuelva la fracción como una representación de cadena
    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    # Método mágico que permita sumar dos fracciones
    def __add__(self, other):
        nuevo_denominador = self.denominador * other.denominador
        nuevo_numerador = (self.numerador * other.denominador + other.numerador * self.denominador)
        return Fracción(nuevo_numerador, nuevo_denominador)
    
    # Método mágico que permita el producto entre dos fracciones
    def __mul__(self, other):
        nuevo_numerador = self.numerador * other.numerador
        nuevo_denominador = self.denominador * other.denominador
        return Fracción(nuevo_numerador, nuevo_denominador)
    
    # Método mágico que permita comparar dos fracciones. Dos fracciones se consideran iguales si sus valores numéricos son equivalentes
    def __eq__(self, other):
        return (self.numerador * other.denominador == self.denominador * other.numerador)

# Crear instancias para probar
fracción_1 = Fracción(1,5)
fracción_2 = Fracción(5,10)
fracción_3 = Fracción(4,8)

# Probar métodos
suma = fracción_1 + fracción_2
multiplicación = fracción_1 * fracción_2
igualdad_1 = fracción_1 == fracción_2
igualdad_2 = fracción_2 == fracción_1

print("Fracción 1:\n", "-", fracción_1)
print("Fracción 2:\n", "-", fracción_2)
print("Fracción 3:\n", "-", fracción_3)
print("Suma (1+2):\n", "-", suma)
print("Multiplicación (1*2):\n", "-", multiplicación)
print("¿La fracción 1 es igual a la fracción 3?\n", "-", igualdad_1)
print("¿La fracción 1 es igual a la fracción 2?\n", "-", igualdad_2)
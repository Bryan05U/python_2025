import math

class Círculo:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_área(self):
        return math.pi * self.radio ** 2

class Rectángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_área(self):
        return self.base * self.altura

class Triángulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_área(self):
        return (self.base * self.altura) / 2

class Cuadrado:
    def __init__(self, lado):
        
    
    def calcular_área(self):
        return self.lado ** 2

class Trapecio:


class Pentágono_Regular:

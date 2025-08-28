import math
class Persona():
    # Constructor de la clase Persona
    # Atributos de la clase Persona (características compartidas por  todos los objetos de la clase)
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = float(altura)
        self.peso = float(peso)
    
    # Métodos (Comportamientos)
    def hablar(self):
        print(f"{self.nombre} está hablando sobre su futuro")

    def estudiar(self):
        print(f"{self.nombre} está estudiando Programación Orientada a Objetos")

    def beber(self):
        print(f"{self.nombre} está bebiendo agua para hidratarse")

    # Método para calcular el IMC
    def calcularIMC(self):
        print(f"El IMC es de: ", (math.trunc(self.peso / self.altura **2)))
        if (self.peso / self.altura **2) < 18.5:
            print(f"Rango de IMC: por debajo")
        elif (self.peso / self.altura **2) >= 18.5 and (self.peso / self.altura **2) < 24.9:
            print(f"Rango de IMC: saludable")
        elif (self.peso / self.altura **2) >= 25 and (self.peso / self.altura **2) < 29.9:
            print(f"Rango de IMC: sobrepeso")
        elif (self.peso / self.altura **2) >= 30 and (self.peso / self.altura **2) < 34.9:
            print(f"Rango de IMC: obesidad 1")
        elif (self.peso / self.altura **2) >= 35 and (self.peso / self.altura **2) < 39.9:
            print(f"Rango de IMC: obesidad 2")
        else:
            print(f"Rango de IMC: obesidad 3")
    
    # Método para calcular el promedio de las 3 notas
    def promedio_asignatura(self, nota_1: float, nota_2: float, nota_3: float):
        promedio = (nota_1 + nota_2 + nota_3) / 3
        if promedio >= 4.0:
            print(f"{self.nombre} ha aprobado con un promedio de {promedio}, ¡buen trabajo!")
        else:
            print(f"{self.nombre} ha reprobado con un promedio de {promedio}, hace falta más estudio, ¿no?")

# Creando un objeto de la clase Persona
persona = Persona("Bryan", "Cárcamo", 19, 1.75, 90)

# Acceso a los atributos y métodos del objeto
print(f"Nombre: {persona.nombre}")
print(f"Apellido: {persona.apellido}")
print(f"Edad: {persona.edad} años")
print(f"Altura: {persona.altura}")
print(f"Peso: {persona.peso}")

# Llamando a los métodos de la clase Persona
persona.hablar()
persona.estudiar()
persona.beber()
persona.calcularIMC()
persona.promedio_asignatura(3.9, 4.3, 3.0)
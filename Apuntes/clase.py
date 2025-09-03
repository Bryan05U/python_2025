class Persona():
        # Atributos de la clase Persona (características compartidas por  todos los objetos de la clase)
        nombre = "Bryan"
        apellido = "Cárcamo"
        edad = 19

        # Métodos (Comportamientos)
        def hablar(self):
            print(f"{self.nombre} está hablando")

        def caminar(self):
            print(f"{self.nombre} está caminando")

# Creando un objeto de la clase Persona
persona_1 = Persona()

# Acceso a los atributos y métodos del objeto
print(f"Nombre: {persona_1.nombre}")
print(f"Apellido: {persona_1.apellido}")
print(f"Edad: {persona_1.edad} años")

# Llamando a los métodos de la clase Persona
persona_1.hablar()
persona_1.caminar()
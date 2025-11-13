class Pato:
    def graznar(self):
        print("Quack!")

class Persona:
    def granzar(self):
        print("Estoy imitando a un pato")

def graznido(ser):
    ser.graznar()

pato = Pato()
persona = Persona()

graznido(pato)
graznido(persona)
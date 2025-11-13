class Pato:
    def graznar(self):
        print("Pato: Quack!")

class Persona:
    def graznar(self):
        print("Persona: Estoy imitando a un pato")

def graznido(ser):
    ser.graznar()

pato = Pato()
persona = Persona()

graznido(pato)
graznido(persona)
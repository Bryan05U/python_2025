"1. Gestión de Gatos en el Café (50 Puntos)"
"Los gatos son los protagonistas del café y cada uno tiene características y necesidades únicas. Piensa encómo representarías a los gatos dentro del sistema."
"A. ¿Cómo representarías a los gatos dentro del sistema?"
"- I. ¿Qué atributos crees que serían importantes para describir a un gato? Piensa en atributos como el nombre, la edad, el nivel de energía y el nivel de hambre."
"- II. Crea un constructor que inicialice estos atributos al momento de instanciar un objeto."
"B. Métodos que necesita la clase Gato:"
"- I. ¿Cómo diseñarías un método que permita que los gatos jueguen y cómo impactaría esto en sus atributos como los niveles de energía y hambre?"
"- II. ¿Cómo diseñarías un método que permita alimentar a los gatos y restaurar sus niveles de energía y hambre?"
"C. Método Mágico:"
"- I. Implementa un método que te permita imprimir de forma clara el estado del gato. ¿Qué información incluirías en la representación del gato?"

"2. Espacios en el Café (30 Puntos)"
"El café tiene diferentes áreas donde los gatos pueden estar (por ejemplo: salon, terraza, etc). Imagina cómo organizarías estas áreas dentro del sistema."
"A. ¿Cómo representarías los espacios dentro del café?"
"- I. ¿Qué atributos serían importantes para describir un espacio del café? Piensa en atributos como el nombre del espacio, la capacidad máxima de gatos que puede albergar, y una lista de los nombres de los gatos presentes en ese espacio."
"- II. Crea un constructor que inicialice estos atributos al momento de instanciar un objeto."
"B. Métodos que necesita la clase Espacio:"
"- I. ¿Cómo diseñarías un método que permita agregar un gato a un espacio del café? Debes asegurarte de que no se exceda la capacidad máxima del área."
"- II. ¿Cómo diseñarías un método que permita mostrar la información básica de los gatos (nombre, edad) que se encuentran en cada espacio del café?"

"3. Finalizador (20 puntos)"
"A. Implementa un finalizador en la clase Gato que muestre un mensaje cuando un gato sea eliminado del sistema (por ejemplo, “El gato [nombre] ha salido del café”)."

# Constructor de clase Gato
class Gato():
    def __init__(self, nombre, edad, género, energía, hambre):
        self.nombre = nombre
        self.edad = edad
        self.género = género
        self.energía = energía
        self.hambre = hambre
    
    # Método que permite que los gatos jueguen, mientras juegan, se le reduce la energía y aumenta el hambre
    def jugar(self, estado):
        self.energía -= 5
        self.hambre += 5
        if self.energía <= 10 and self.hambre >= 40:
            estado = estado(["Hambriento"])
        else:
            estado = estado(["Normal"])
        print(f"El gato {self.nombre} está jugando")

    # Método que permite alimentar a los gatos
    def comer(self):
        self.energía += 5
        self.hambre -= 5
        print(f"El gato {self.nombre} está comiendo")
    
    # Método mágico que imprime el estado del gato
    def __str__(self):
        return f"Estado: {self.estado}"

    # Método mágico que elimina el gato del café y arroje un mensaje
    def __del__(self):
        print(f"El gato {self.nombre} ha salido del café")

# Constructor de clase Espacio
class Espacio():
    def __init__(self, nombre):
        self.nombre = nombre
        self.capacidad_máxima = 10
        self.lista_gatos = []

    def agregar_gato(self):
        if self.capacidad_máxima > 10:
            ValueError("No puede haber más de 10 gatos en un Café")

    def mostrar_info(self):
        lista_gatos = lista_gatos[f"Nombre: {self.nombre} | Edad: {self.edad} | Género: {self.género}"]

gato_1 = Gato("Eduardo", 3, "Macho", 50, 2)
gato_2 = Gato("Lucy", 2, "Hembra", 45, 0)
gato_3 = Gato("Jorge", 4, "Macho", 39, 3)

gato_1.jugar()
gato_1.comer()
gato_2.jugar()
gato_2.comer()

del gato_3
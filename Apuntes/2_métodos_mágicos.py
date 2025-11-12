class Triángulo:
    # Constructor de Clase
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    # Método mágico __str__ que devuelve una cadena del triángulo representada
    def __str__(self):
        return f"El triángulo tiene estos lados:\n- {self.lado1} cm\n- {self.lado2} cm\n- {self.lado3} cm"
    
    # Método mágico __eq__ que compara los dos triángulos y determinar si son iguales o no
    def __eq__(self, triángulo):
        return {self.lado1, self.lado2, self.lado3} == {triángulo.lado1, triángulo.lado2, triángulo.lado3}
    
    # Método mágico __add__ que suma ambos triángulos
    def __add__(self, triángulo):
        return Triángulo(
            self.lado1 + triángulo.lado1,
            self.lado2 + triángulo.lado2,
            self.lado3 + triángulo.lado3
        )

    # Método mágico __len__ que devuelve el perímetro de triángulo
    def __len__(self):
        return int(self.lado1 + self.lado2 + self.lado3)
    
    # Verificar si los lados ingresados forman un triángulo válido
    def verificar_validez(self):
        return (self.lado1 + self.lado2 > self.lado3 and self.lado1 + self.lado3 > self.lado2 and self.lado2 + self.lado3 > self.lado1)
    
# Crear 2 instancias de la clase triángulo
triángulo_1 = Triángulo(2, 4, 6)
triángulo_2 = Triángulo(2, 4, 6)

# Llamar método __str__ para representar el triángulo como cadena
print(triángulo_1,"\n")

# Usar método __eq__ para comparar si los dos triángulo son iguales
print(f"¿Los dos triángulos son iguales?", "\n", triángulo_1 == triángulo_2,"\n")

# Crear nuevo triángulo al sumar ambos triángulos
triángulo_3 = triángulo_1 + triángulo_2
print(triángulo_3,"\n")

# Usar método __len__ para obtener el perímetro del triángulo
print(f"Perímetro del triángulo:", len(triángulo_1),"\n")

# Verificar si los lados forman un triángulo válido
print(f"¿Los lados forman un triángulo válido?" ,"\n", triángulo_1.verificar_validez())
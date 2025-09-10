class Pedido():
    # Constructor de la clase Pedido
    def __init__(self, n_mesa):
        self.n_mesa = n_mesa
        self.platos = []
        self.total = 0

    # Método para añadir platos al pedido (cada plato tiene un nombre y un precio)
    def agregar_plato(self, nombre, precio):
        self.platos.append({"Nombre": nombre, "Precio": precio})
        self.total += precio

    # Método para calcular el total del precio
    def calcular_total(self):
        self.total = sum(plato["Precio"] for plato in self.platos)
        return self.total
    
    # Devuelve la cantidad de platos en el pedido
    def __len__(self):
        return len(self.platos)
    
    # Método mágico para combinar dos pedidos de la misma mesa (sumar platos y total)
    def __add__(self, other):
        if self.n_mesa != other.n_mesa:
            ValueError(f"Distintas mesas no pueden ser combinadas")
        pedido_nuevo = Pedido(self.n_mesa)
        pedido_nuevo.platos = self.platos + other.platos
        pedido_nuevo.precio = self.total + other.total
        return pedido_nuevo
    
    # Al eliminar un pedido, mostrar un mensaje indicando que el pedido ha sido completado
    def __del__(self):
        print(f"El pedido de la mesa {self.n_mesa} ha sido completado con éxito")

pedido_1 = Pedido(3)
pedido_1.agregar_plato("Curanto", 7900)
pedido_1.agregar_plato("Café", 800)
pedido_2 = Pedido(3)
pedido_2.agregar_plato("Ensalada", 3000)

print(f"Total del primer pedido: ", pedido_1.calcular_total())
print(f"Total del segundo pedido: ", pedido_2.calcular_total())

pedido_total = pedido_1 + pedido_2
print(f"Total de pedidos combinados: ", pedido_total.total)
print(f"Número total de platos: ", len(pedido_total))

del pedido_1, pedido_2, pedido_total
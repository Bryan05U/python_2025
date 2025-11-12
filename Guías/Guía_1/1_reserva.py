from datetime import datetime

class ReservaHostal():
    def __init__(self, nombre_cliente, fecha_entrada, fecha_salida, número_habitación):
        self.nombre_cliente = nombre_cliente
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.número_habitación = número_habitación
    
    def calcular_duración_estadia(self):
        fecha_entrada = datetime.strptime(self.fecha_entrada, "%Y-%m-%d")
        fecha_salida = datetime.strptime(self.fecha_salida, "%Y-%m-%d")
        duración = (fecha_salida - fecha_entrada)
        return duración
    

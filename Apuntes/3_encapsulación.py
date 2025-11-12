class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular # Atributo público
        self.__saldo = saldo # Atributo privado
    
    # Método público para mostrar la información de la cuenta
    def mostrar_info(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.__saldo} CLP")

    # Método público para depositar plata
    def depositar(self, monto):
        if monto < 0:
            print("Error: Depositar una cantidad negativa no es válida")
        else:
            self.__saldo += monto
            print(f"Has depositado ${monto} CLP en la cuenta")
        
    # Método privado para calcular intereses
    def __calcular_intereses(self):
        return self.__saldo * 0.05
    
    # Método público para agregar intereses al saldo
    def agregar_intereses(self):
        intereses = self.__calcular_intereses()
        self.__saldo += intereses
        print(f"Has agregado ${intereses} CLP en intereses")
    
# Crear una cuenta bancaria
cuenta = CuentaBancaria("Bryan Cárcamo", 500000)

# Acceder al atributo público
print(cuenta.titular)
print()

# Mostrar información de la cuenta
cuenta.mostrar_info()
print()

# Depositar plata en la cuenta
cuenta.depositar(150000)
cuenta.mostrar_info() # Actualizar información
print()

# Agregar intereses
cuenta.agregar_intereses()
cuenta.mostrar_info()
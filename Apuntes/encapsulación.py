class CuentaBancaria:
    def __init__(self, titular, saldo):
        # Atributo público
        self.titular = titular

        # Atributo privado
        self.__saldo = saldo
    
    # Método público para mostrar la información de la cuenta
    def mostrar_info(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo actual: ${self.__saldo} CLP")

    # Método público ñara depositar dinero
    def depositar(self, monto):
        if monto < 0:
            print("Error: Depositar una cantidad negativa no es válida")
        else:
            self.__saldo += monto
            print(f"Has depositado ${monto} CLP en la cuenta")
        
        # Método privado para calcular intereses
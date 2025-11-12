class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular # Atributo público
        self.__saldo = saldo # Atributo privado
        # Assert para asegurar el invariante en la inicialización
        assert self.__saldo >= 0, "Error: El saldo no puede tener un valor negativo"
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo_nuevo):
        if saldo_nuevo >= 0:
            self.__saldo == saldo_nuevo
        else:
            print("Error: El saldo no puede tener un valor negativo")
    
# Probar la Invariante de Clase
# Crear una cuenta que tenga saldo positivo para que funcione
cuenta_nueva = CuentaBancaria("Bryan Cárcamo", 650000)
print(f"Cuenta Bancaria:\n- Titular: {cuenta_nueva.titular}\n- Saldo: {cuenta_nueva.saldo}")

# Esto ocurre si se intenta establecer un saldo negativo en el setter
#cuenta_nueva.saldo = -650000
#print(f"Cuenta Bancaria:\n- Titular: {cuenta_nueva.titular}\n- Saldo: {cuenta_nueva.saldo}")

# Intentar crear una nueva cuenta con saldo negativo
#cuenta2 = CuentaBancaria("Bryan Cárcamo", -650000)
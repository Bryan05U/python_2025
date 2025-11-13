class Doctor:
    def __init__(self, nombre, especialidad, salario):
        # Atributos privados
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__sueldo = salario
    
    # Getter para el nombre
    def get_nombre(self):
        return self.__nombre
    
    # Setter para el nombre
    def set_nombre(self, nombre_nuevo):
        if len(nombre_nuevo) < 0:
            print("Error: El nombre ingresado no puede ser vacío")
        else:
            self.__nombre = nombre_nuevo

    # Getter para la especialidad
    def get_especialidad(self):
        return self.__especialidad

    # Setter para la especialidad
    def set_especialidad(self, especialidad_nueva):
        if len(especialidad_nueva) < 0:
            print("Error: La especialidad ingresada no puede ser vacía")
        else:
            self.__especialidad = especialidad_nueva

    # Getter para el sueldo
    def get_sueldo(self):
        return self.__sueldo
    
    # Setter para el sueldo
    def set_sueldo(self, salario_nuevo):
        if salario_nuevo <= 0:
            print("Error: El sueldo ingresado no puede ser negativo")
        else:
            self.__sueldo = salario_nuevo

    # Método que muestra información del doctor
    def mostrar_info(self):
        print(f"Doctor: {self.__nombre}\nEspecialidad: {self.__especialidad}\nSueldo: {self.__sueldo}")

# Crear instancias de clase
doctor_1 = Doctor("Dr. Bryan Cárcamo", "Cirugano", 3000000)
print(doctor_1.get_nombre())
doctor_1.set_nombre("Dr. Benjamín Concha")
print(doctor_1.get_nombre())
print()

# Mostrar información inicial
doctor_1.mostrar_info()
print()

# Cambiar nombre, especialidad y sueldo usando setters
doctor_1.set_nombre("Dr. Benjamín Concha")
doctor_1.set_especialidad("Dentista")
doctor_1.set_sueldo(6000000)
doctor_1.mostrar_info()
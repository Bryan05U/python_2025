class Doctor:
    def __init__(self, nombre, especialidad, sueldo):
        # Atributos privados
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__sueldo = sueldo
    
    # Getter y Setter para el nombre, especialidad y sueldo usando @property
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre_nuevo):
        if len(nombre_nuevo) < 0:
            print("Error: El nombre ingresado no puede ser vacío")
        else:
            self.__nombre = nombre_nuevo
    
    @property
    def especialidad(self):
        return self.__especialidad
    
    @especialidad.setter
    def especialidad(self, especialidad_nueva):
        if len(especialidad_nueva) < 0:
            print("Error: La especialidad ingresada no puede ser vacía")
        else:
            self.__especialidad = especialidad_nueva
    @property
    def sueldo(self):
        return self.__sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo_nuevo):
        if sueldo_nuevo <= 0:
            print("Error: El sueldo ingresado no puede ser negativo")
        else:
            self.__sueldo = sueldo_nuevo

    # Método que muestra información del doctor
    def mostrar_info(self):
        print(f"Doctor: {self.__nombre}\nEspecialidad: {self.__especialidad}\nSueldo: {self.__sueldo}")

# Instancias utilizando @property
doctor_1 = Doctor("Dr. Bryan Cárcamo", "Cirugano", 3000000)
doctor_1.mostrar_info()
print()

# Modificación de los atributos utilizando setters con el @property
doctor_1.nombre = "Dr. Benjamín Concha"
doctor_1.especialidad = "Dentista"
doctor_1.sueldo = 6000000
doctor_1.mostrar_info()
from Persona import Persona


class Empleado(Persona):

    def __init__(self,id, nombre, apellido, correo, contrasena, cargo, salario, tipo_contrato):
        super().__init__(id, nombre, apellido, correo, contrasena)
        self._cargo = cargo
        self._salario = salario
        self._tipo_contrato = tipo_contrato

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def tipo_contrato(self):
        return self._tipo_contrato

    @tipo_contrato.setter
    def tipo_contrato(self, tipo_contrato):
        self._tipo_contrato = tipo_contrato


    #Vamos a sobre escribir los metodos


    def registrar_usuario(self):
        self._id = input(f"Ingrese el id del usuario: ")
        self._nombre = input("Ingrese el nombre del usuario:")
        self._apellido = input("Ingrese el apellido del usuario:")
        self._correo = input("Ingrese el correo del usuario:")
        self._contrasena = input("Ingrese la contraseña del usuario: ")
        self._cargo= input("Ingrese el cargo del empleado")
        self._salario = float(input("Ingrese el salario del empleado"))
        self._tipo_contrato = input("Indique el tipo de contrato")

    def imprimir_registro(self):
        super().imprimir_registro()
        print(f"Cargo: {self._cargo} Salario: {self._salario} Tipo de contrato: {self._tipo_contrato} ")


    def iniciar_sesion(self):
        correo_emp = input("Ingrese el correo registrado: ")
        contras_emp = input("Ingrese la contraeña: ")

        if correo_emp == self._correo and contras_emp == self._contrasena:
            return True
        else:
            return False

    def appEmpleado(self, iniciar_sesion, imprimir_registro):
        iniciar_sesion()== True
        print("Has iniciado sesion")
        imprimir_registro()






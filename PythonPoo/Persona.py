
class Persona:

    def __init__(self, id,nombre, apellido, correo, contrasena):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
        self._contrasena = contrasena

    #Vamos a generar Getter and Setters
    #GET
    @property
    def id(self):
        return self._id

    #SET
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self,apellido):
        self._apellido = apellido

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self._contrasena = contrasena


    #Vamos a generar los metodos
    # para registrar los usuarios e imprimir el registro

    def registrar_usuario(self):
        id = input(f"Ingrese el id del usuario: ")
        nombre = input("INgrese el nombre del usuario:")
        apellido = input("Ingrese el apellido del usuario:")
        correo = input("Ingrese el correo del usuario:")
        contrasena = input("Ingrese la contraseña del usuario: ")


    def imprimir_registro(self):
        print(f"Id: {self._id} Nombre: {self._nombre} Apellido {self._apellido} Correo: {self._correo} Contraseña {self._contrasena}")






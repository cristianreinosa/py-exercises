#Para crear una clase en python, usamos la palabra "class"
class Persona:

    # Creamos un metodo constructor

    def __int__(self,id,nombre,apellido,correo,contrasena):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena
        #Este contiene la palabra reservada self,
        #similar a this en java, por ejemplo

        #Encapsulamiento con python

        #Se usa un underscore al principio de la variable
        #Para indicar que sera encapsulada

        #Ahora usaremos decoradores para crear los getter and setters


        #Esto es un getter
        @property
        def id(self):
            return  self._id

        #Esto es un setter
        @id.setter
        def id(self,id):
            self._id = id

        #@propety = > indica los getters
        #@variable = > indica los setters

        #Instancia

        @property
        def nombre(self):
            return  self._nombre

        @nombre.setter
        def nombre(self,nombre):
            self._nombre = nombre

        @property
        def apellido(self):
            return  self._apellido

        @nombre.setter
        def apellido(self,apellido):
            self._apellido = apellido

        @property
        def correo(self):
            return  self._correo

        @nombre.setter
        def correo(self,correo):
            self._correo = correo

        @property
        def contrasena(self):
            return  self._contrasena

        @nombre.setter
        def contrasena(self,contrasena):
            self._contrasena = contrasena


    def imprimir_persona(self):
        print(f"Id : {self._id} Nombre : {self._nombre} Apellido : {self._apellido}")



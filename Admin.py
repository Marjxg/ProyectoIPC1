class Admin:

    #constructor
    def __init__(self, nombre, apellido,usuario, contra):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contra = contra

    #Métodos get y set
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getUsuario(self):
        return self.usuario

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getContra(self):
        return self.contra

    def setContra(self, contra):
        self.contra = contra

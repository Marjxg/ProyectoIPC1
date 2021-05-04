class Doctor:
    
    #constructor
    def __init__(self, nombre, apellido, fecha, sexo, usuario, contra, specialty, tel):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.sexo = sexo
        self.usuario = usuario
        self.contra = contra
        self.specialty = specialty
        self.tel = tel

    #Métodos get y set
    
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getSexo(self):
        return self.sexo

    def setSexo(self, sexo):
        self.sexo = sexo

    def getUsuario(self):
        return self.usuario

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getContra(self):
        return self.contra

    def setContra(self, contra):
        self.contra = contra

    def getSpecialty(self):
        return self.specialty

    def setSpecialty(self, specialty):
        self.specialty = specialty

    def getTel(self):
        return self.tel

    def setTel(self, tel):
        self.tel = tel

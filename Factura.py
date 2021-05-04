class Factura:
    
    #constructor
    def __init__(self, fecha, nombre, doctor, precio, costoO, costoI, total):
        self.fecha = fecha
        self.nombre = nombre
        self.doctor = doctor
        self.precio = precio
        self.costoO = costoO
        self.costoI = costoI
        self.total = total

    #Métodos get y set
    
    def getFecha(self):
        return self.fecha

    def setfecha(self, fecha):
        self.fecha = fecha

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getDoctor(self):
        return self.doctor

    def setDoctor(self, doctor):
        self.doctor = doctor

    def getPrecoi(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getCostoO(self):
        return self.costoO

    def setCostoO(self, costoO):
        self.costoO = costoO

    def getCostoI(self):
        return self.costoI

    def setCostoI(self, costoI):
        self.costoI = costoI

    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total
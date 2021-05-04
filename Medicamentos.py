class Medicamento:

    #constructor
    def __init__(self, code, nombre, precio, descripcion, cantidad):
        self.code = code
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad

    #Métodos get y set
    
    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad
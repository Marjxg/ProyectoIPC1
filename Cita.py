class Cita:

    #constructor
    def __init__(self, id, fecha, hora, motivo, estado, doctor):
        self.id = id
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.motivo = motivo
        self.doctor = doctor

    #Métodos get y set
    
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getHora(self):
        return self.hora

    def setHora(self, hora):
        self.hora = hora

    def getMotivo(self):
        return self.motivo
    
    def setMotivo(self, motivo):
        self.motivo = motivo

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getDoctor(self):
        return self.doctor

    def setDoctor(self, doctor):
        self.doctor = doctor
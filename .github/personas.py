class Persona:
    def __init__(self,param_nombre,param_email):
        self.nombre=param_nombre
        self.email=param_email
        self.asistencia = 0
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def asistencia_clase(self):
        self.asistencia += 1
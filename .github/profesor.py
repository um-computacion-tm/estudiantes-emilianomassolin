from personas import Persona

class Profesor(Persona):
    def __init__(self, param_nombre, param_email,legajo):
        super().__init__(param_email,param_nombre)
        self.legajo=legajo
profesor_pepe = Profesor("Pepe", "jose@um.edu.ar",123)
print(id(profesor_pepe))
print("el nombre es: ")
print(profesor_pepe.nombre)
print("el email es: ")
print(profesor_pepe.email)
print("su asistencia es: ")
print(profesor_pepe.asistencia)

print("EL PROFESOR FUE A CLASE...")
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("su asistencia es: ")
print(profesor_pepe.asistencia)

# profesor_pepe.cambiar_nombre("JOSE!")

# print(profesor_pepe.nombre)


# profesor_walter = Profesor("Walter")
# profesor_daniel = Profesor("Daniel")

# print(id(profesor_daniel))
# print(profesor_daniel.nombre)
# print(profesor_daniel.nombre)

# print(id(profesor_walter))
# print(profesor_walter.nombre)


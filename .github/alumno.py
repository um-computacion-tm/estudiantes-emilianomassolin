from personas import Persona
class Alumno(Persona):
    def __init__(self,param_nombre,param_email,legajo):
        self.legajo=legajo
        self.materias_cursando=[]
        super().__init__(param_nombre,param_email)
    def agegrar_materia(self,materia):  
        self.materias_cursando.append(materia)    

alumnoEmiliano=Alumno("emiliano","emiliano@gmail.com",1)
alumnoPepe:Alumno = Alumno("Pepe", "jose@um.edu.ar",2)
print(id(alumnoEmiliano))
print("el nombre es: ")
print(alumnoEmiliano.nombre)
print("el email es: ")
print(alumnoEmiliano.email)
print("su asistencia es: ")
print(alumnoEmiliano.asistencia)
alumnoEmiliano.agegrar_materia("hola")
print(alumnoEmiliano.materias_cursando)

print("EL ALUMNO FUE A CLASE...")
alumnoEmiliano.asistencia_clase()
alumnoEmiliano.asistencia_clase()
alumnoEmiliano.asistencia_clase()
alumnoEmiliano.asistencia_clase()
alumnoEmiliano.asistencia_clase()
alumnoEmiliano.asistencia_clase()
alumnoEmiliano.asistencia_clase()

print("su asistencia es: ")
print(alumnoEmiliano.asistencia)

# profesor_pepe.cambiar_nombre("JOSE!")

# print(profesor_pepe.nombre)


# profesor_walter = Profesor("Walter")
# profesor_daniel = Profesor("Daniel")

# print(id(profesor_daniel))
# print(profesor_daniel.nombre)
# print(profesor_daniel.nombre)

# print(id(profesor_walter))
# print(profesor_walter.nombre)


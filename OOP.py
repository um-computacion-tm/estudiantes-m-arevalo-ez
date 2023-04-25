#CLASES
class Persona:
    def __init__(self, param_nombre, param_apellido, param_email):
        self.nombre = param_nombre
        self.apellido = param_apellido
        self.email = param_email
        self.asistencia = 0

class Profesor(Persona): 
    def __init__(self, param_nombre, param_apellido, param_email, param_legajo):
        self.legajo = param_legajo
        super().__init__(param_nombre, param_apellido, param_email)

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1

class Alumno(Persona):
    def __init__(self, param_nombre, param_apellido, param_email, param_legajo):
        self.legajo = param_legajo
        self.materias_cursando = []
        super().__init__(param_nombre, param_apellido, param_email)

    def asistencia_clase(self):
        self.asistencia += 1

    def cursando(self, materia):
        self.materias_cursando.append(materia)

class Materia:
    def __init__(self, param_codigo, param_nombre, param_profesor):
        self.codigo = param_codigo
        self.nombre = param_nombre
        self.profesor = param_profesor

#OBJETOS
profesor_gabriel = Profesor("Gabriel", "Flores", "Jose@um.edu.ar", "1034") #INSTANCIA DE LA CLASE PROFESOR
profesor_gabriel.asistencia_clase()
profesor_gabriel.cambiar_nombre("Jose")

materia_computacion = Materia("2022", "Computacion", "Gabriel Flores")
materia_bdi = Materia("2023", "Diseño de base de datos I", "Fernando Zapata")
materia_asii = Materia("2024", "Analisis de sistemas II", "Maria Reina")

alumno_marcos = Alumno("Marcos", "Arevalo", "m.arevalo@um.edu.ar", "62189")
alumno_marcos.asistencia_clase()
alumno_marcos.cursando(materia_computacion.nombre)
alumno_marcos.cursando(materia_bdi.nombre)
alumno_marcos.cursando(materia_asii.nombre)
print(alumno_marcos.materias_cursando)





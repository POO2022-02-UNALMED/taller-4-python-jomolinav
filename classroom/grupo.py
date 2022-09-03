

from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = None

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes= None):


        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.asignarNombre("Grado 12")

    def __str__(self):
        cadena = "Grupo de estudiantes: " + self._grupo 
        return str(cadena)
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 12"):
        cls.grado = nombre


    def listadoAsignaturas(self, **kwargs):
        self._asignaturas = []
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    #def __str__(self):
     #   total = str(self._asignaturas)
      #  return total 
 

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
            lista.append(alumno)
            self.listadoAlumnos =   [alumno]
        else:
            lista.append(alumno)
            self.listadoAlumnos = lista

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre


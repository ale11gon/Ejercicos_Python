class Alumno():
    nombre = None
    nota = None

    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print('Nombre del alumno:',self.nombre,'y su nota es:',self.nota)
        if(self.nota >= 5.0):
            print('Esta aprobado')
        else:
            print('No esta aprobado')


c = Alumno('Carlos',4)
d = Alumno('Anna',9.4)

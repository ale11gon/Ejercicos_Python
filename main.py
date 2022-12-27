import sqlite3

def main():
    insertarAlumno(1, "Carlos", "Perez")
    insertarAlumno(2, "Anna", "Gomez")
    insertarAlumno(3, "Rosa", "Ruiz")
    insertarAlumno(4, "Alex", "Gonzalez")
    insertarAlumno(5, "Ruben", "Martin")
    insertarAlumno(6, "Antonio", "Santiago")
    insertarAlumno(7, "Pepe", "Gil")
    insertarAlumno(8, "Paula", "Lopez")

    buscarAlumno("Pepe","Gil")


def insertarAlumno(identificador, nombre, apellido):
    conn = sqlite3.connect('Alumnos.db')
    cursor = conn.cursor()

    query = '''INSERT INTO Alumnos(id,nombre,apellido) VALUES (?,?,?)'''
    cursor.execute(query,(identificador,nombre,apellido))

    print(identificador,nombre,apellido,"añadido")

    conn.commit()
    cursor.close()
    conn.close()

def buscarAlumno(nombre,apellido):
    conn = sqlite3.connect('Alumnos.db')
    cursor = conn.cursor()

    query = f'SELECT id FROM Alumnos WHERE nombre="{nombre}" AND apellido="{apellido}"'
    rows = cursor.execute(query)
    data = rows.fetchone()

    print("El id del alumno",nombre,apellido,"es",data[0])

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
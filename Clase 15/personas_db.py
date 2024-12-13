import sqlite3

def crear_tabla_personas():
    conexion = sqlite3.connect("Clase 15/base_datos.db")
    
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Personas (
        nombre TEXT, edad INTEGER, ciudad TEXT) ''')

    conexion.commit()
    conexion.close()

def registrar_persona():
    conexion = sqlite3.connect("base_datos.db")

    cursor = conexion.cursor()

    nombre = input("Nombre: ")
    edad   = int(input("Edad: "))
    ciudad = input("Ciudad: ")

    cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES (?, ?, ?)", (nombre, edad, ciudad))

    conexion.commit()
    conexion.close()

def mostrar_personas():
    conexion = sqlite3.connect("base_datos.db")

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Personas")

    resultados = cursor.fetchall()

    for registro in resultados:
        print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:", registro[2])

    conexion.close()

def actualizar_persona():
    conexion = sqlite3.connect("base_datos.db")

    cursor = conexion.cursor()

    nombre     = input("Nombre de la persona: ")
    nueva_edad = int(input("Nueva edad: "))

    cursor.execute("UPDATE Personas SET edad = ? WHERE nombre = ?", (nueva_edad, nombre))

    conexion.commit()
    conexion.close()

def eliminar_persona():
    conexion = sqlite3.connect("base_datos.db")

    cursor = conexion.cursor()

    nombre = input("Nombre de la persona a eliminar: ")

    cursor.execute("DELETE FROM Personas WHERE nombre = ?", (nombre,))

    conexion.commit()
    conexion.close()

def buscar_persona():
    conexion = sqlite3.connect("base_datos.db")

    cursor = conexion.cursor()

    nombre = input("Nombre de la persona: ")

    cursor.execute("SELECT * FROM Personas WHERE nombre = ?", (nombre,))

    resultado = cursor.fetchone()

    print("Nombre:", resultado[0], "Edad:", resultado[1], "Ciudad:", resultado[2])

    conexion.close()

def reporte_menores_edad():
    conexion = sqlite3.connect("base_datos.db")

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM Personas WHERE edad < 18")

    resultados = cursor.fetchall()

    for registro in resultados:
        print("Nombre:", registro[0], "Edad:", registro[1], "Ciudad:", registro[2])

    conexion.close()

def mostrar_menu():
    print("\nMenú:")
    print("1. Registrar persona")
    print("2. Mostrar personas")

    # Continúa con las demás opciones

crear_tabla_personas()

# Iniciar el programa llamando al menú principal
mostrar_menu()

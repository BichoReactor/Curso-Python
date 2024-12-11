import sqlite3

conexion = sqlite3.connect("Clase 14/base_de_datos.db")

cursor = conexion.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        ciudad TEXT NOT NULL
    )
    """
)
"""
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Bebito', 1, 'CABA')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Manuel', 47, 'CABA')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Sofía', 32, 'San Juán')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Arnaldito Jr.', 1, 'Tucumán')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Arnaldo', 2, 'Tierra del Fuego')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Tití', 3, 'Córdoba')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Monito', 2, 'La Pampa')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Tita', 3, 'Mendoza')")
cursor.execute("INSERT INTO Personas (nombre, edad, ciudad) VALUES ('Lilita', 3, 'Misiones')")
"""

#cursor.execute("UPDATE Personas SET edad = 24 WHERE nombre = 'Lilita'")

#cursor.execute("DELETE FROM Personas WHERE nombre = 'Manuel'")

#conexion.commit()

#cursor.execute("SELECT * FROM Personas")

#cursor.execute("SELECT * FROM Personas WHERE edad = 3")

#cursor.execute("SELECT nombre, edad FROM Personas")

cursor.execute("SELECT * FROM Personas ORDER BY nombre ASC;")

resultados = cursor.fetchall()

for registro in resultados:
    print("Nombre:", registro[1], "Edad:", registro[2], "Ciudad:", registro[3])

conexion.close()
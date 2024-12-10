import sqlite3

conexion = sqlite3.connect("Clase 14/inventario.db")

cursor = conexion.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        categoria TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )
    """
)

cursor.execute("SELECT * FROM productos")

resultados = cursor.fetchall()

print(resultados)

cursor.execute("")

conexion.commit()

conexion.close()

conexion.row_factory = sqlite3.Row

for registro_obj in resultados:
    registro = dict(registro_obj)
    
    for key, value in registro.items():
        print(f"{key} : {value}")
# Importar modulo sqlite
import sqlite3

# Conexión
conexion = sqlite3.connect('tests.db')

# Crear cursor (para hacer consultas SQL)
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
	id INTEGER PRIMARY KEY AUTOINCREMENT, 
	titulo VARCHAR(255), 
	descripcion TEXT, 
	precio INT(255)
);
""")

# Guardar cambios
conexion.commit()

# Insertar datos
#cursor.execute("INSERT INTO productos VALUES(NULL, 'M&Ms', 'Chocolate confitado de colores', 15)")
#conexion.commit()

# Borrar registros
# cursor.execute("DELETE FROM productos")
# conexion.commit()

# Insertar muchos registros de golpe
productos = [
	("Odenador Portatil", "Buen PC", 700),
	("Telefono Movil", "Buen Telefono", 140),
	("Placa Base", "Buena Placa", 80),
	("Tablet 15", "Buena Tablet", 300),
]
# cursor.executemany("INSERT INTO productos VALUES(NULL, ?, ?, ?)", productos)
# conexion.commit()


# Actualizar registro (UPDATE)
cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 80")

# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 100")
productos = cursor.fetchall()

for producto in productos:
	print(f"ID: {producto[0]}")
	print(f"Titulo: {producto[1]}")
	print(f"Descripción: {producto[2]}")
	print(f"Precio: {producto[3]}")
	print("\n")

# Imprimir el primer registro de una tabla
cursor.execute("SELECT * FROM productos")
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()
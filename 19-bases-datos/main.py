import mysql.connector

# Conexión
database = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "master_python",
)

# ¿La conexión ha sido correcta?

# Cursor para hacer consultas
cursor = database.cursor(buffered = True)

# Crear la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

"""
# Mostrar todas las bases de datos
cursor.execute("SHOW DATABASES;")

for db in cursor:
	print(db)
"""
# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
	id INT(10) AUTO_INCREMENT NOT NULL,
	marca VARCHAR(40) NOT NULL,
	modelo VARCHAR(40) NOT NULL,
	precio FLOAT(10, 2) NOT NULL,
	CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES;")
for table in cursor:
	print(table)

# Insertar un solo registros en una tabla
#cursor.execute("INSERT INTO vehiculos VALUES(NULL, 'Dodge', 'Challenger', 812000.50)")
#database.commit()

# Insertar una lista de registros en una tabla
cars = [
	('Ford', 'Mustang GTX', 1550000),
	('Seat', 'Ibiza', 5000),
	('Renault', 'Clio', 15000),
	('Citroen', 'Saxo', 2000),
	('Mercedes', 'Clase C', 35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES(NULL, %s, %s, %s)", cars)
#database.commit()

# Listar todos los registros de una tabla
print("\n\t\t ######### Todos los vehiculos #########")
#cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat';")
cursor.execute("SELECT * FROM vehiculos;")
cars = cursor.fetchall()

for car in cars:
	print(car)

# Listar el primer registro de la tabla
print("\n\t\t ########## Primer  vehiculo ###########")

cursor.execute("SELECT * FROM vehiculos;")
car = cursor.fetchone()
print(car)

# Borrar registros de la tabla
print("\n\t\t ######### Borrar un vehiculo ##########")
cursor.execute("DELETE FROM vehiculos WHERE id = 12")
database.commit()
print(f"{cursor.rowcount} registros borrados !!")

# Actualizar registros de la tabla
print("\n\t\t ####### Actualizar un vehiculo ########")
cursor.execute("UPDATE vehiculos SET modelo = 'León' WHERE marca = 'Seat'")
database.commit()
print(f"{cursor.rowcount} registros actualizados !!")
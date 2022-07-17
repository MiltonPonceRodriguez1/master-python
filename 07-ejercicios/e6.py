"""

Ejercicio No.6

Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las 
multiplicaciones

"""

for table in range(1, 11):
	print(f"\n\t\t\tTabla de Multiplicar del número {table}")
	for i in range(1, 11):
		print(f"{table}x{i} = {table*i}")
"""
# FOR

for var in elems_iterable (lista, rango, etc)
	BLOQUE DE INSTRUCCIONES

"""
contador = 0
resultado = 0

for contador in range(0, 10):
	print(f"Voy por el {str(contador)}!")
	resultado += contador

print(f"El resultado es: {resultado}")

# Ejemplo tablas de multiplicar
print("\n\t\t\t########## EJEMPLO ##########")

user_number = int(input("¿De que número quieres la tabla?: "))

if user_number < 1:
	user_number = 1

print(f"\n\t\t#### Tabla de multiplicar del número {user_number} ####")

for x in range(0,10):
	
	if user_number > 10:
		print("\nNo se pueden mostrar números prohibidos !!")
		break

	print(f"\t{user_number}x{x+1} = {(x+1)*user_number}")
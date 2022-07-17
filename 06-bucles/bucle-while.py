"""

# BUCLE WHILE

Estructura de control que itera o repite la ejecución
de una serie de instrucciones tantas veces como sea
necesario, hasta que deje de cumploirse la condición

while  condicion:
	bloque de instrucciones
	actualizamos el contador
"""

contador = 1

while contador <= 100:
	print(f"{contador}")
	contador += 1

print("\n\t\t----------------------------------------------\n")
contador = 1
text = str()

while contador <= 100:
	if contador < 100:
		text += str(contador) + ", "
	else:
		text += str(contador)
	contador += 1

print(text)

# Ejemplo tablas de multiplicar
print("\n\t\t\t########## EJEMPLO ##########")

user_number = int(input("¿De que número quieres la tabla?: "))

if user_number < 1:
	user_number = 1

print(f"\n\t\t#### Tabla de multiplicar del número {user_number} ####")

contador = 1

while contador <= 10:
	print(f"{user_number} x {contador} = {user_number*contador}")
	contador += 1
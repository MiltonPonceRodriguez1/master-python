"""

Ejercicio No.2 

Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego 
mostrar la lista.

PLUS: Usar while y for
"""

def getPrintList(lista):
	text = ""
	for elemento in lista:
		text += f"{lista.index(elemento)}-. {elemento} \n"

	return text

coleccion = []
i = 0

while i < 120:
	#var = input(f"Introduzca el elemento {i+1}: ")
	coleccion.append(f"Elemento #{i+1}")
	i += 1

print("\n\t\t ##### Elementos de la Lista While #####")
print(getPrintList(coleccion))

coleccion = []

for i in range(120):
	#var = input(f"Introduzca el elemento {i+1}: ")
	coleccion.append(f"Elemento #{i+1}")

print("\n\t\t ###### Elementos de la Lista For ######")
print(getPrintList(coleccion))

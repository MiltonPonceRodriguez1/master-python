"""
Ejercicio No.1
	
Hacer un programa que tenga una lista de 8 números
enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra listas de numeros y devuelva el resultado
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar un elemento que el usuario introduce por teclado

"""

def printList(numbers):
	string = ""
	for number in numbers:
		string += f"{number}, "
		
	return string

numbers = [9, 12, 56, 6, 7, 3, 1,85]
print("\n\t\t ########### Recorrer Lista ###########")
print(printList(numbers))

print("\n\t\t ########### Ordenar  Lista ###########")
numbers.sort()
print(printList(numbers))

print("\n\t\t ########### Longitud Lista ###########")
print(f"Longitud: {len(numbers)}")
try:
	print("\n\t\t ########### Buscar Element ###########")
	search = int(input("¿Que número deseas buscar?: "))

	comprobar = isinstance(search, int)

	while not comprobar or search <= 0:
		search = int(input("¿Que número deseas buscar?: "))
		comprobar = isinstance(search, int)

	print("\n\t\t--------------------------------------------")
	print(f"\t\t\tHas introducido el número {search}")
	print("\t\t--------------------------------------------\n")

	validate = numbers.index(search)
except:
	print(f"El número NO esta en la lista")
else:
	print(f"El número {search}, se encuentra en el indice {validate} de la lista !!")
finally:
	None
	#print("\tFin de la iteración")
"""
if(numbers.find(search)):
	print(f"El número {search} si esta en la lista !")
else:
	print(f"El número NO esta en la lista !")
"""
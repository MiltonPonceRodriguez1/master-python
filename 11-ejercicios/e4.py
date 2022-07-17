"""

Ejercicio No.4

Crear un script que tenga 4 variables, una lista,
un string, un entero y un booleano y que imprima
un mensaje segun el tipo de dato de cada variable.
Usar funciones

"""
def translateType(tipo):
	if tipo == list:
		return "Lista"
	elif tipo == int:
		return "Entero"
	elif tipo == str:
		return "Cadena de Texto"
	elif tipo == bool:
		return "Booleano"


def checkType(dato, tipo):
	if isinstance(dato, tipo):
		return f"La variable '{dato}' si es del tipo '{translateType(tipo)}'\n"
	else:
		return f"La variable '{dato}' NO es del tipo '{translateType(tipo)}'\n"

mi_lista = ["Dokken", "Lee"]
titulo = "Master en Python"
numero = 256
flag = True

print(checkType(mi_lista, list))
print(checkType(titulo, str))
print(checkType(numero, int))
print(checkType(flag, bool))
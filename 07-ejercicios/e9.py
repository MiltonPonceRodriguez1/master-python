"""

Ejercicio No.9

Hacer un programa que pida números al usuario
indefinidamente hasta meter el número 111

"""

number = int(input("Introduzca un número: "))

while number != 111:
	number = int(input("Introduzca un número: "))
	print(f"\tIngresasste el número: {number}\n")
"""

Ejercicio No.5

Hacer un programa que muestre todos los numeros entre
dos números que diga el usuario.

"""

number_init = int(input("\tIntroduzca el número inicial: "))
number_end = int(input("\tIntroduzca el número final: "))

for cont in range(number_init, number_end+1):
	print(f"{cont}")
"""

Ejercicio No.7

Hacer un programa que muestre todos los números
impares entre dos números que decida el usuario.

"""

first_number = int(input("Introduzca el primer número: "))
second_number = int(input("Introduzca el segundo número: "))

print(f"\n\t\t ####### Números Impares entre {first_number}-{second_number} #######\n")
if first_number < second_number:
	for i in range(first_number, second_number+1):
		if(i % 2 != 0):
			print(f"{i} es número impar!")
else:
	print("El primer número debe ser menor que el segundo !!")
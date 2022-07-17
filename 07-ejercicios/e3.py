"""

Ejercicio No.3

Escribir un programa que imprima los cuadrados de los
primeros 60 numeros naturales
-Usar bucle For 
-Usar bucle While

"""

# While
print("\n\t\t############# WHILE #############")

number = 1

while number <= 60:
	print(f"{number}^2 = {number*number}")
	number += 1

# For
print("\n\t\t############## FOR ##############")
for i in range(0, 60):
	print(f"{i+1}^2 = {(i+1)*(i+1)}")
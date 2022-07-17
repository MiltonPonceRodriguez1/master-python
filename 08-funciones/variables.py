"""

Variables locales: Se definen dentro de la funcion y
no se puede usar fuera de ella, solo están disponibles
dentro. A no ser que hagamos un return

Variables globales: Son las que se declaran fuera de
una funcion y estan disponibles dentro y fuera de ellas

"""
print("")
# Variables globales
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print(frase)

def holaMundo():
	frase = "Hola Mundo!!"
	print(frase)

	year = 2021
	print(f"{year}")

	global website
	website = "dokkenlee.com"
	print(f"\tDentro: {website}")

	return f"Dato devuelto: {year}"

print(holaMundo())
print(frase)
print(f"\tFuera: {website}")
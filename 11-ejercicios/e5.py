"""

Ejercicio No.5

Crear una lista con el contenido de esta tabla:

ACCION	AVENTURA			DEPORTES
GTA		ASSASSINS			FIFA 21
COD 	CRASH				PRO 21
PUGB	PRINCE OF PERSIA	MOTO GP 21

Mostrar esta informacion ordenada

"""

videogames = [
	{
		'accion': 'GTA',
		'aventura': 'Assassins Creed',
		'deportes': 'FIFA 21'
	},
	{
		'accion': 'COD',
		'aventura': 'Crash Bandicot  ',
		'deportes': 'PRO 21'
	},
	{
		'accion': 'PUGB',
		'aventura': 'Prince of Persia',
		'deportes': 'MOTO GP21'
	}
]
print("\n\t\t ############ Primer Versión ############")

print("\n-------------------------------------------")
print("ACCIÓN \t|AVENTURA \t\t|DEPORTES")
print("-------------------------------------------")
for videogame in videogames:
	print(f"{videogame['accion']} \t|{videogame['aventura']} \t|{videogame['deportes']}")
print("-------------------------------------------")

tabla = [
	{
		'categoria': 'ACCION',
		'juegos': ["GTA", "COD", "PUGB"]
	},
	{
		'categoria': 'AVENTURA',
		'juegos': ["Assassins Creed", "Crash Bandicot", "Prince of Persia"]
	},
	{
		'categoria': 'DEPORTES',
		'juegos': ["FIFA 21", "PRO 21", "MOTO GP21"]
	},
]

print("\n\t\t ############ Segunda Versión ###########\n")
for elemento in tabla:
	print(f" CATEGORIA {elemento['categoria']}")

	for juego in elemento['juegos']:
		print(f"{elemento['juegos'].index(juego)+1}-. {juego}")
	print("---------------------------")
"""

LISTAS (arrays)

Son colecciones o conjuntos de datos/valores,
bajo un unico nombre.

Para acceder a esos valores podemos usar un 
indice númerico

"""

movie = "Batman"

# Definir lista
movies = ["Batman", "Spiderman", "El señor de los anillos"]
singers = list(("Freddie Mercury", "Axl Rose", "Jim Morrison"))
years = list(range(2020, 2030))
mixed = ["Milton", 264, 64.8, True, "Texto"]

# Indices
movies[1] = "Gran Torino"
movies[2] = "El Hobbit"

print(movies[1]) # Aceso al valor del inidice 1 de la lista
print(movies[-2]) # Aceso al valor del inidice -2 de la lista empieza del final al inicio
print(singers[1:3]) # Aceso a los valores del inidice n al m-1 de la lista
print(movies[1:]) # Aceso a los valores apartir del indice dado

print("\n\t\t------------------------------------------------\n")
# Añadir elemento a lista
singers.append("Mick Jagger")
singers.append("John Lennon")

print(singers)

print("\n\t\t ###### Agregar Nuevas Peliculas ######")

new_movie = "fin"
while new_movie != "fin":
	new_movie = input("Enter a new Movie: ")
	if new_movie != "fin":
		movies.append(new_movie)

print("\n\t\t ######## Listado de Peliculas ########")

for movie in movies:
	print(f"{(movies.index(movie))+1}-.{movie}")

# Listas multidimensionales
print("\n\t\t ######## Listado de Contactos ########")

contactos = [
	[
		'Milton',
		'miltonponceipn@gmail.com'
	],
	[
		'Hector',
		'hectorponce@gmail.com'
	],
	[
		'Dokken',
		'dokken@gmail.com'
	]
]

for contacto in contactos:
	for dato in contacto:
		if contacto.index(dato) == 0:
			print(f"Nombre: {dato}")
		else:
			print(f"Email: {dato}")
	print()
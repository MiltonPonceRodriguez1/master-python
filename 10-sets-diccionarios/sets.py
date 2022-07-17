"""
SET es un tipo de dato, para tener colecion de valores,
pero no tiene ni indice ni orden
"""

personas = {
	"Milton",
	"Hector",
	"Dokken"
}

print(type(personas))
print(personas)

# Agregar Elementos a un SET
print("\n\t\t ########## Agregar Elementos ##########")
personas.add("DokkenLee")
print(personas)

# Eliminar Elementos a un SET
print("\n\t\t ########## Eliminar Elementos #########")
personas.remove("Dokken")
print(personas)
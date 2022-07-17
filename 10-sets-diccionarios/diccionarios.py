"""

DICCIONARIO:
Es un tipo de dato que almacena un conjunto de datos.
En formato clave > valor.
Es parecido a un array asociativo o un objeto JSON

"""

person = {
	"name": "Milton",
	"surname": "Ponce",
	"web": "dokkenlee.com"
}

print("\n\t\t ############ Tipo De Dato ############")
print(type(person))
print("\n\t\t ############ Elementos Dic ###########")
print(person)
print("\n\t\t ########### Elemento Clave ###########")
print(person['name'])

# Lista con diccionarios
print("\n\t\t ######## Listado de Contactos ########")
contactos = [
	{
		'name': 'Milton',
		'email': 'miltonponceipn@gmail.com'
	},
	{
		'name': 'Hector',
		'email': 'hectorponce@gmail.com'
	},
	{
		'name': 'Dokken',
		'email': 'dokken@gmail.com'
	}
]

for contacto in contactos:
	print(f"Nombre: {contacto['name']}")
	print(f"Email: {contacto['email']}")
	print()
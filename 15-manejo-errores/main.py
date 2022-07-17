# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores
print("\n\t\t ######### Excepciones Simples #########")
try:
	#name = input("¿Cuál es tu nombre?: ")
	name = "Milton"

	if len(name) > 1:
		user_name = f"El nombre es: {name}"

	print(user_name)
except:
	print("Ha ocurrido un error, mete bien el nombre !!")
else:
	print("Todo ha funcionado correctamente !!")
finally:
	print("\tFin de la iteración")

# Multiples excepciones
print("\n\t\t ######## Excepciones Multiples ########")
try:
	# number = int(input("¿Que número deseas elevar al cuadrado?: "))
	number = 3
	print(f"\n\tEl cuadrado es: {number*number}")
except TypeError:
	print(f"\n\tDebes convertir tus cadenas a enteros en el código!!")
except ValueError:
	print(f"\n\tIntroduce un número correcto !!")
except Exception as e:
	print(f"\n\tHa ocurrido un error: {type(e).__name__}")

# Excepciones Personalizadas o lanzar excepcion
print("\n\t\t ###### Excepciones Personalizadas #####")

try:
	name = input("Introduce el nombre: ")
	age = int(input("Introduce la edad: "))

	if age < 5 or age > 110:
		raise ValueError("\n\tLa edad introducida no es real !!")
	elif len(name) <= 1:
		raise ValueError("\n\tEl nombre no está completo !!")
	else:
		print(f"\n\tBienvenido al Master en Python {name}")
except ValueError:
	print("\n\tIntroduce los datos correctamente !!")
except Exception as e:
	print(f"\n\tExiste un error {e}")
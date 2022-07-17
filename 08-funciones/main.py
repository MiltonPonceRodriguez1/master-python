"""
FUNCIONES:

Una funcion es un conjunto de instrucciones agrupadas
bajo un nombre concreto que pueden reutilizarse
invocando a la funcion tantas veces como sea 
necesario

def nombreDeMiFuncion(parametros):
	#Bloque / Conjunto de instrucciones

nombreDeMiFuncion(mis_parametros)

"""

# Ejemplo No.1
print('\n\t\t\t########) Ejemplo 1 (########')

# Definir funcion
def muestraNombre():
	print("Milton")
	print("Hector")
	print("Dokken")
	print("\n")

# Invocar la función
muestraNombre()
muestraNombre()

# Ejemplo No.2: parametros
print('\n\t\t\t########) Ejemplo 2 (########\n')

def mostrarTuNombre(nombre, edad):
	print(f"\nTu nombre es: {nombre}")

	if edad >= 18:
		print("Y eres mayor de edad!")

#name = input("Introduce tu nombre: ")
name = "Dokken"
#edad = int(input("Introduce tu edad: "))
edad = 19
mostrarTuNombre(name, edad)

# Ejemplo No.3
print('\n\t\t\t########) Ejemplo 3 (########\n')

def table(number):
	print(f"\t\t\tTabla de multiplicar del número {number}")
	for i in range(1, 11):
		print(f"{number} x {i} = {number*i}")
	print("\n")

table(5)

# Ejemplo No.3.1
print('\n\t\t\t########) Ejemplo 3.1 (########\n')

for i in range(1, 11):
	table(i)

# Ejemplo No.4
print('\n\t\t\t########) Ejemplo 4 (########\n')

# Parametros opcionales

def getEmpleado(name, dni = None):
	print("\t\t\t--------- Empleado ---------")
	print(f"Nombre: {name}")

	if dni != None:
		print(f"DNI: {dni}")

getEmpleado("Dokken", 1324)

# Ejemplo No.5 return y devolver datos
print('\n\t\t\t########) Ejemplo 5 (########\n')

def saludame(name):
	return f"\nHola, saludos {name}."

print(saludame("Milton Ponce Rodriguez"))

# Ejemplo No.6
print('\n\t\t\t########) Ejemplo 6 (########\n')

def calculadora(a, b, basic = False):
	if basic != False:
		cadena = f"\nSuma: {a+b} \nResta: {a-b}"
	else:
		cadena = f"\nMultiplicación: {a*b} \nDivisión: {a/b}"
	return cadena

print(calculadora(2, 3, True))

# Ejemplo No.7
print('\n\t\t\t########) Ejemplo 7 (########\n')

def getName(name):
	return f"El nombre es: {name}"

def getSurname(surname):
	return f"Los apellidos son: {surname}"

def getAll(name, surname):
	return f"{getName(name)}\n{getSurname(surname)}"

print(getAll("Milton", "Ponce"))

# Ejemplo No.8: Funciones Lambda (Anonimas)
print('\n\t\t\t########) Ejemplo 8 (########\n')

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))

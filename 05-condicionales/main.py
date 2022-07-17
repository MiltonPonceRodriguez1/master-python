"""
# Condicional IF

SI se_cumple_esta_condicion
	Ejecutar grupo de instrucciones
SI NO:
	Se ejecutan otro grupo de instrucciones

if condicion:
	instrucciones
else:
	otras instrucciones

# Operadores de comparación
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos
and Y
or 	O
! 	NEGACION
not	NO


"""

# Ejemplo 1
print("\n\t\t############ EJEMPLO 1 ############")
color = "rojo"
#color = input("Adivina cuál es mi color favorito: ")

if color == "rojo":
	print("Enhorabuena!!")
	print("El color es Rojo!")
else:
	print("Color incorrecto!")

# Ejemplo 2
print("\n\t\t############ EJEMPLO 2 ############")

year = 2020
#year = int(input("¿En que año estamos?: "))

if year >= 2021:
	print("Estamos de 2021 en adelante!")
else:
	print("Es un año anterior a 2021!")

# Ejemplo 3 IF's anidados
print("\n\t\t############ EJEMPLO 3 ############")

nombre = "Milton Ponce"
ciudad = "Barcelona"
continente = "Europa"
edad = 18

if edad >= 18:
	print(f"{nombre} es mayor de edad !!")
	if continente != "Europa":
		print("\tEl usuario NO es Europeo!")
	else:
		print(f"\tEs Europeo y de {ciudad}")
else:
	print(f"{nombre} NO es mayor de edad!")

# Ejemplo 4 ELIF
print("\n\t\t############ EJEMPLO 4 ############")

dia = 2
#dia = int(input("Introduzca el número del dia de la semana: "))

if dia == 1:
	print("Es Lunes")
elif dia == 2:
	print("Es Martes")
elif dia == 3:
	print("Es Miercoles")
elif dia == 4:
	print("Es Jueves")
elif dia == 5:
	print("Es Viernes")
else:
	print("Es fin de semana")

# Ejemplo 5 OP Logicos
print("\n\t\t############ EJEMPLO 5 ############")

edad_minima = 18
edad_maxima = 65
edad_oficial = 17
#edad_oficial = int(input("¿Tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
	print("Esta en edad de trabajar !!")
else:
	print("No está en edad de trabajar")

# Ejemplo 6
print("\n\t\t############ EJEMPLO 6 ############")

pais = "Alemania"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
	print(f"{pais} es un pais de habla hispana !!")
else:
	print(f"{pais} NO es un pais de habla hispana :(")

# Ejemplo 7
print("\n\t\t############ EJEMPLO 7 ############")

pais = "Mexico"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
	print(f"{pais} NO es un pais de habla hispana :(")
else:
	print(f"{pais} SI es un pais de habla hispana :)")

# Ejemplo 8
print("\n\t\t############ EJEMPLO 8 ############")

pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
	print(f"{pais} NO es un pais de habla hispana :(")
else:
	print(f"{pais} SI es un pais de habla hispana :)")
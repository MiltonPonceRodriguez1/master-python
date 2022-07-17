"""
Una variable es un contenedor de información 
que dentro guarda un dato, se pueden crear 
muchas variables y que cada una tenga un 
dato distinto.
"""
# Crear variables y asignarles un valor
texto = "\nMaster en Python"
texto2 = ", con Milton Ponce"
numero = 14
decimal = 12.54

# Mostrar el valor de cada variable
print(texto+texto2)
print(numero)
print(decimal)
print("\t\t\t<--------------------------->")
# Sobreescribir el valor de variables
numero = 889
decimal = 215.41

# Mostrar el valor de cada variable
print(numero)
print(decimal)
print("\t\t\t<--------------------------->")

# Concatenación
nombre = "Milton"
apellido = "Ponce"
web = "DokkenLee.com"

print(nombre, apellido, web)
print(nombre + " " + apellido + " - " + web)
print(f"{nombre} {apellido} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))
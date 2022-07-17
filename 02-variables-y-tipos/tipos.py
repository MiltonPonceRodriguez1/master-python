nada = None
cadena = "Hola soy Milton Ponce!"
cadena += ", Desarrollador Web"
entero = 256
flotante = 64.128
boolean = False
lista = [10, 20, 30, 100, 200]
listaMixed = [44, "treinta", 30, "cuarenta"]
tupla = ("master", "en", "python") # NOTA: Las tuplas no cambian
diccionario = {
	"nombre": "Milton",
	"apellido": "Ponce",
	"curso": "Master en Python"
}
rango = range(9)
byte = b"Byte"

# Imprimir variable
print(nada)
print(cadena)
print(entero)
print(flotante)
print(boolean)
print(lista)
print(listaMixed)
print(tupla)
print(diccionario)
print(rango)
print(byte)
print("\n")

# Mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(boolean))
print(type(lista))
print(type(listaMixed))
print(type(tupla))
print(type(diccionario))
print(type(rango))
print(type(byte))

# Convertir tipo de dato a otro
texto = "\nHola soy un texto!"
strnumber = "256"
numero = 256
print(texto + " " + str(numero)) 		# Convertir int to string
print(numero+int(strnumber))			# Convertir string to int
print(float(numero)+float(strnumber))	# Convertir string e int to float
nombre = "Milton Ponce"

# FUNCIONES GENERALES

# Imprimir por pantalla
print('\n\t\t########) Imprimir consola (########\n')
print(f"{type(nombre)}")

# Detectar el tipado
print('\n\t\t########)  Detectar tipado (########\n')
check = isinstance(nombre, str)
if check:
	print("Esa variable es un string")
else:
	print("No es un string")

if not isinstance(nombre, float):
	print("La variable NO es un número con decimales")

# Limpiar espacios
print('\n\t\t########)  Limpar espacios (########\n')
frase = "       mi contenido      "
print(f"{frase}")
print(frase.strip())

# Comprobar variable vacia
print('\n\t    ########) Comprovacion variables vacias (########\n')
text = "  ff   "

if len(text) <= 0:
	print("La variable está vacia")
else:
	print(f"La variable tiene contenido: {len(text)}")

# Encontrar caracteres
print('\n\t\t########) Encontrar caracteres (########\n')

frase = "La vida es bella"
print(frase.find("vida"))

# Remplazar palabras en un string
print('\n\t\t########)  Remplazar palabras  (########\n')
nueva_frase = frase.replace("vida", "moto")
print(nueva_frase)

# Mayusculas y Minusculas 
print('\n\t\t########) Mayusculas/Minusculas (########\n')
print(nombre)
print(nombre.lower())
print(nombre.upper())
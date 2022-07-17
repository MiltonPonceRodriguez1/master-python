from io import open
import pathlib
import shutil
import os
import os.path

# Abrir archivo (Escritura)
route = f"{str(pathlib.Path().absolute())}/fichero_texto.txt"
file = open(route, "a+")

# Escribir en un archivo
file.write("****** Soy un texto metido desde python ******\n")

# Cerrar un archivo
file.close()

# Abrir archivo (Lectura)
print("\n\t\t ############ Abrir Archivo ############")
route = f"{str(pathlib.Path().absolute())}/fichero_texto.txt"
file_read = open(route, "r")

# Leer contenido
#content = file_read.read()
#print(content)

# Leer una sola linea del fichero
# print(file_read.readline())

# Leer caracter por caracter del fichero
"""
for char in content:
	print(char)
"""

# Leer contenido y guardar en lista
print("\n\t\t ######### Leer y Guardar-Lista ########")
lista = file_read.readlines()

# Cerrar archivo
file_read.close()

for frase in lista:
	# Separa la frase por espacios en una lista
	# lista_frase = frase.split()
	
	# Imprimir frase en minusculas
	# print(frase.lower())

	# Imprimir frase en mayusculas
	# print(frase.upper())
	print(f"- {frase.center(72)}")

# Copiar archivos a otros directorios
print("\n\t\t ######## Copiar != Directorios #########")
ruta_origen = f"{str(pathlib.Path().absolute())}/fichero_texto.txt"
ruta_destino = f"{str(pathlib.Path().absolute())}/fichero_copy.txt"
ruta_alternativa = f"{str(pathlib.Path().absolute())}/copy-files/file1.txt"
shutil.copyfile(ruta_origen, ruta_destino)

# Mover/Renombrar un archivo
print("\n\t\t ####### Mover/Renombrar Archivo ########")
ruta_origen = f"{str(pathlib.Path().absolute())}/fichero_copy.txt"
ruta_nueva = f"{str(pathlib.Path().absolute())}/fichero_copy_NEW.txt"

shutil.move(ruta_origen, ruta_nueva)

# Eliminar un archivo
ruta_nueva = f"{str(pathlib.Path().absolute())}/fichero_copy_NEW.txt"
os.remove(ruta_nueva)

# Comprobar si existe un archivo
print("\n\t\t ######### Comprobar Existencia #########")
print(os.path.abspath(""))
# Ruta absoluta
ruta_comprobar = f"{os.path.abspath('./')}/fichero_texto.txt"
# Ruta relativa
ruta_comprobar = "fichero_texto.txt"

if os.path.isfile(ruta_comprobar):
	print("El archivo existe !!")
else:
	print("El archivo NO existe !!")
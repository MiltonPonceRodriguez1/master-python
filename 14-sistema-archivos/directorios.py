import os, shutil

# Crear Carpeta
print("\n\t\t ############ Crear Carpeta ############")
#absolute_route = f"{os.path.abspath('./')}/dir"
absolute_route = f"{os.path.abspath('./')}/mi_carpeta"

if not os.path.isdir(absolute_route):
	os.mkdir(absolute_route)
	print("La carpeta se creo correctamente !")
else:
	print("Ya existe el directorio !!")

# Copiar carpetas a otros directorios
print("\n\t\t ######## Copiar != Directorios ########")
ruta_origen = f"{os.path.abspath('./')}/mi_carpeta"
ruta_destino = f"{os.path.abspath('./')}/mi_carpeta_copy"
if not os.path.isdir(ruta_destino):
	shutil.copytree(ruta_origen, ruta_destino)
	print("Directorio copiado correctamente !!")
else:
	print("El direcctorio copiado ya existe !!")

# Eliminar el directorio
print("\n\t\t ########### Eliminar Carpeta ##########")
flag = False
if os.path.isdir(ruta_destino) and flag:
	shutil.rmtree(ruta_destino)
	print("La carpeta se Elimino correctamente !")
else:
	print("La carpeta NO se pudo eliminar !!")

print("\n\t\t ####### Contenido De La Carpeta #######")
content = os.listdir(f"{os.path.abspath('./')}/mi_carpeta_copy")

for script in content:
	print(f"{content.index(script)+1}-. {script}")
print("\n\t\t ########## Probando Paquetes ##########")

# Importar ALGUNOS modulos de un paquete
# from package import pruebas
# from package import herramientas

# Importar TODOS los modulos de un paquete
from package import pruebas, herramientas

pruebas.testing()
herramientas.completeName("Milton", "Ponce")
"""
MODULOS: 

Son funcionalidades ya hechas para reutilizar
se pueden consultar aqui: 
https://docs.python.org/3/py-modindex.html

Podemos ocnseguir modulos que ya vieron en el
lenguaje, modulos de internet y tambien crear
nuestros propios modulos
"""

# Importar TODO el modulo propio
#import module

#print(module.holaMundo("Dokken"))
#print(module.calculadora(3, 5, True))

#importar solo ALGUNAS funciones del modulo propio
#from module import holaMundo
#print(holaMundo("Dokken"))

# Importar TODO el modulo propio pero sin usar modulo.funcion
from module import *
print(holaMundo("Dokken"))
print(calculadora(3, 5, True))

# Modulo fechas
import datetime

print(f"\n{datetime.date.today()}")

print("\n\t\t ########### Fecha Completa ############")
fecha_completa = datetime.datetime.now()
print(f"{fecha_completa}")

print("\n\t\t ########### Fecha Parciales ###########")
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

print("\n\t\t ######### Fecha Personalizada #########")
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)

print("\n\t\t ########### Timestamp y Time ###########")
print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

# Modulo matematicas
import math
print("\n\t\t ---------- Modulo Mátematicas ---------")
print(f"Raiz cuadrada de 10: {math.sqrt(10)}")
print(f"Número pi: {math.pi}")
print(f"Redondear hacia arriba: {math.ceil(6.56798)}")
print(f"Redondear hacia abajo: {math.floor(6.56798)}")

# Modulo Random
import random
print("\n\t\t ----------- Modulo  Random ------------")
print(f"Número aleatorio entre [15, 67]: {random.randint(15, 67)}")
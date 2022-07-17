from coche import Coche

carro = Coche("Azul", "Ford", "Mustang-GTX", 450, 780, 4)
carro1 = Coche("Amarillo", "Lamborghini", "Veneno", 650, 910, 2)
carro2 = Coche("Rojo", "Dodge", "Challenger", 420, 725, 2)
carro3 = Coche("Verde", "Chevrolet", "Camaro", 650, 850, 4)

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

# Detectar el tipado de los objetos
print("\n\t\t ####### Detectar Tipado Objetos #######")

if type(carro3) == Coche:
	print("Es un objeto correcto !!")
else:
	print("El objeto NO es un Coche()")

# Visibilidad de los atributos
print("\n\t\t ######## Visibilidad Atributos ########")
print(carro.soy_public)
print(carro.getPrivate())

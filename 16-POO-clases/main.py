# Programación orientada a objetos (POO o OOP)

# Definir una clase (molde para crear más objetos de
# de este tipo (coche) con caracteristicas similares)

class Coche:

	# Atributos o propiedades
	# Caracteristicas del coche
	color = "rojo"
	marca = "Ferrari"
	modelo = "Aventador"
	velocidad = 300
	caballaje = 500
	plazas = 2

	# Metodos: acciones que hace el objeto (coche)
	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def setModelo(self, modelo):
		self.modelo = modelo

	def getModelo(self):
		return self.modelo

	def acelerar(self):
		self.velocidad += 1

	def frenar(self):
		self.velocidad -= 1

	def getVelocidad(self):
		return self.velocidad

# Fin definición clase

# Instanciar objeto
print("\n\t\t ######### Instancia 1er Coche #########")
coche = Coche()

coche.setColor("Azul")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad nueva: ", coche.getVelocidad())		

# Objetos multiples
print("\n\t\t ######### Instancia 2do Coche #########")
coche2 = Coche()
coche2.setColor("Verde")
coche2.setModelo("Gallardo")
print(coche2.marca, coche2.getModelo(), coche2.getColor())
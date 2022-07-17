class Coche:

	# Atributos o propiedades
	# Caracteristicas del coche
	color = "rojo"
	marca = "Ferrari"
	modelo = "Aventador"
	velocidad = 300
	caballaje = 500
	plazas = 2

	#Visibilidad de los atributos (public, private)
	soy_public = "Hola, soy un atributo publico !!"
	__soy_private = "Hola, soy un atributo privado !!"

	# COnstructor de la clase
	def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
		self.color = color
		self.marca = marca
		self.modelo = modelo
		self.velocidad = velocidad
		self.caballaje = caballaje
		self.plazas = plazas


	# Metodos: acciones que hace el objeto (coche)
	def getPrivate(self):
		return self.__soy_private
		
	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def setModelo(self, modelo):
		self.modelo = modelo

	def getModelo(self):
		return self.modelo

	def setMarca(self, marca):
		self.marca = marca

	def getMarca(self):
		return self.marca

	def setVelocidad(self, velocidad):
		self.velocidad = velocidad

	def getVelocidad(self):
		return self.velocidad

	def setCaballaje(sekf, caballaje):
		self.caballaje = caballaje

	def getCaballaje(self):
		return self.caballaje

	def setPlazas(self, plazas):
		self.plazas = plazas

	def getPlazas(self):
		return self.plazas

	def acelerar(self):
		self.velocidad += 1

	def frenar(self):
		self.velocidad -= 1

	def getInfo(self):
		info = "\n\t\t ######## Información del Carro ########\n"
		info += f"\n\tColor: {self.getColor()}"
		info += f"\n\tMarca: {self.getMarca()}"
		info += f"\n\tModelo: {self.getModelo()}"
		info += f"\n\tVelocidad: {self.getVelocidad()}"

		return info

# Fin definición clase
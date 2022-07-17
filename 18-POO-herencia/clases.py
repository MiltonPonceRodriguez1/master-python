class Person:
	"""
	Name
	Surname
	Height
	Age
	"""

	def getName(self):
		return self.__name

	def getSurname(self):
		return self.__surname

	def getHeight(self):
		return self.__height

	def getAge(self):
		return self.__age

	def setName(self, name):
		self.__name = name 

	def setSurname(self, surname):
		self.__surname = surname

	def setHeight(self, height):
		self.__height = height

	def setAge(self, age):
		self.__age = age

	def talk(self):
		return "\nEstoy hablando !!"

	def walk(self):
		return "\tEstoy caminando !!"

	def sleep(self):
		return "\tEstoy Durmiendo !!"

class Informatic(Person):
	"""
	Languages
	Experience
	"""

	def __init__(self, name, surname, height, age, languages, experience):
		self.__name = name
		self.__surname = surname
		self.__height = height
		self.__age = age
		self.__languages = languages
		self.__experience = experience

	def getInfo(self):
		return f"Soy {self.__name} {self.__surname}, mido {self.__height}mts y tengo {self.__age} años; Domino los siguientes lenguajes: {self.__languages} con {self.__experience} de experiencia"

	def aprender(Self, language):
		self.__languages += language

	def program(self):
		return "\tEstoy programando !!"

	def repairPC(self):
		return "\tHe reparado un ordenador !!"

class TecnicoRedes(Informatic):
	def __init__(self):
		# Invocar el constructor de la clase Padre
		super().__init__("Milton", "Ponce", 180, 21, "C, C++", 4)
		self.auditarRedes = 'Experto'
		self.experienciaRedes = 15

	def auditoria(self):
		return "Estoy auditando una red !!"
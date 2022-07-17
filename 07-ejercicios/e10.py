"""

Ejercicio No.10

El programa tiene que pedir la nota de 15 alumnos y
sacar por pantalla cuantos han aprobado y cuantos han
suspendido

"""
alumnos = int(input("\nIntroduzca el número total de alumnos: "))
aprobados = 0
suspendidos = 0

for i in range(alumnos):
	nota = int(input(f'¿Que nota obtuvo el "alumno {(i+1)}"?: '))
	if nota >= 6:
		aprobados += 1
	else:
		suspendidos += 1

print(f"\n\tAlumnos aprobados: {aprobados} !!")
print(f"\tAlumnos suspendidos: {suspendidos} !!")
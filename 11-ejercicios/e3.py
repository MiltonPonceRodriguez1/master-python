"""

Ejercicio No.3

Programa que compruebe si una variables está vacia
y si esta vacia, rellenarla con texto en minusculas
y mostrarlo con mayusculas.

"""

texto = " "

if len(texto.strip()) <= 0:
	texto = f"este es un texto que rellena la variable"
	print(f"\n{texto}\n")

print(texto.upper())
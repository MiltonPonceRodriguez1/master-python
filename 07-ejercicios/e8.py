"""

Ejercicio 8
Calcular el x porciento de X número

"""

number = int(input("\nIntroduce el número al cuál desea calcular el porcentaje: "))
percent = int(input("¿Que porcentaje desea calcular del número?: "))

print(f"\n\tEl {percent}% de {number} es: {(number * percent) / 100} !!")
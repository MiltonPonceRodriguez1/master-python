def holaMundo(nombre):
	return f"Hola que tal estas, {nombre}"

def calculadora(a, b, basic = False):
	if basic != False:
		cadena = f"\nSuma: {a+b} \nResta: {a-b}"
	else:
		cadena = f"\nMultiplicación: {a*b} \nDivisión: {a/b}"
	return cadena
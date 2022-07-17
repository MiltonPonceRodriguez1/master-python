# No.1 Las funciones se deben declarar al principio
def mi_funcion(nombre): # No.3 Pasarle parametros a las funciones
	# No.2 Regresar siempe un valor
	return f"Hola que tal {nombre}!"

def mi_segunda_funcion(apellidos):
	# No.2 Regresar siempe un valor
	return f"Hola que tal 2 {apellidos}!"

nombre = "Milton"
apellidos = "Ponce"

print("\n"+mi_funcion(nombre))
print(mi_segunda_funcion(nombre+" "+apellidos))
"""
PROYECTO Python-MySQL

- Abrir asistente
- Login o registro
- Si elegimos registro, creará un nuevo usuario en la DB
- Si elegimos login, identifica al usuario y nos preguntará
- Crear nota, mostrar nota, borrarlas

"""
from users import Actions

print("""
        Acciones disponibles:
            - [1] Registrate
            - [2] Identificate
""")

doThe = Actions.Actions()
accion = int(input("¿Que quieres hacer?: "))

if accion == 1:
   doThe.register() 
elif accion == 2:
    doThe.login()
    
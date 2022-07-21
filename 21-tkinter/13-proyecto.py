"""
Crear un programa que tenga:
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, Añadir, Info, Salir)
- Diferentes pantallas
- Formulario de añadir producto
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
- Opción de salir
"""

from tkinter import *

# DEFINIR VENTANA
ws = Tk()
ws.geometry("500x500")
ws.title("Proyecto Tkinter - Master Python")
ws.resizable(0, 0)

# INICIO CREACION PANTALLAS
def home():
    home_label = Label(ws, text="Inicio")
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)

def add():
    add_label = Label(ws, text="Añadir Producto")
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)

    return True

def info():
    info_label = Label(ws, text="Información")
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)

    return True
# FIN CREACION PANTALLAS

# CARGAR HOME PAGE
home()

# INICIO DEL MENU DE NAVEGACIÓN
nav = Menu(ws)
ws.config(menu=nav)

nav.add_command(label="Inicio", command=home)
nav.add_command(label="Añadir", command=add)
nav.add_command(label="Información", command=info)
nav.add_command(label="Salir", command=ws.quit)
# FIN DEL MENU DE NAVEGACIÓN

# CARGAR VENTANA
ws.mainloop()
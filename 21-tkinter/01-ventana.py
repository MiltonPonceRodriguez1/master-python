"""
Tkinter
Modulo para crear interfaces graficas de usuario
"""
from tkinter import *
import os.path

class GUI:

    def __init__(self):
        self.title = "Master en Python"
        self.icon = './images/logo_1.ico'
        self.icon_alt = './21-tkinter/images/logo_1.ico'
        self.size = "770x470"
        self.resizable = False

    def load(self):
        # Crear la ventana raiz
        window = Tk()
        self.window = window

        # Titulo de la ventana
        window.title(self.title)

        # Comprobar si existe un archivo
        ruta_icon = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icon):
            ruta_icon = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        window.iconbitmap(ruta_icon)

        # Mostrar texto en la ventana
        texto = Label(window, text = ruta_icon)
        texto.pack()

        # Redimensionar la ventana
        window.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            window.resizable(1, 1)
        else:
            window.resizable(0,0)

    def add_text(self, text_to_add: str = "Texto desde un método !!"):
        text = Label(self.window, text = text_to_add)
        text.pack()

    def show(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.window.mainloop()

# Instancia GUI
gui = GUI()
gui.load()
gui.add_text()
gui.add_text("DokkenLee !!")
gui.show()
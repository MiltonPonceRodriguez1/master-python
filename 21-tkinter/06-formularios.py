from tkinter import *
from turtle import width

window = Tk()
window.geometry("700x500")

window.title("Formularios en Tkinter | DokkenLee")

# Texto Encabezado
header = Label(window, text="Formularios con Tkinter - Milton Ponce")
header.config(
    fg = "white",
    bg = "darkgray",
    font = ("Open Sans", 18),
    padx = 10,
    pady = 10
)
header.grid(row=0, column=0, columnspan=12, sticky=W)

# Label para el campo de texto Nombre
label = Label(window, text="Nombre: ")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de Texto Nombre
text_field = Entry(window)
text_field.grid(row=1, column=1, sticky=W, padx=5, pady=5)
text_field.config(
    justify="center",
    state="normal"
)

# Label para el campo de texto Apellidos
label = Label(window, text="Apellidos: ")
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de Texto Apellidos
text_field = Entry(window)
text_field.grid(row=2, column=1, sticky=W, padx=5, pady=5)
text_field.config(
    justify="center",
    state="normal" #(normal | disabled)
)

# Label para el campo de textarea Descripción
label = Label(window, text="Descripción: ")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Campo de texto grande
textarea = Text(window)
textarea.grid(row=3, column=1, padx=5, pady=5)
textarea.config(
    width=30,
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

# Label separador
Label(window).grid(row=4, column=1)

# Boton
button = Button(window, text="Enviar")
button.grid(row=5, column=1, sticky=W)
button.config(
    padx=10,
    pady=10,
    bg="green",
    fg="white"
)

window.mainloop()
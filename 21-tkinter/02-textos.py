from tkinter import *

window = Tk()

window.geometry("700x500")

text = Label(window, text = "Bienvenido a mi aplicación !!")

# Configuración textos
text.config(
    fg= "white",
    bg="#000000",
    padx= 20,
    pady= 20,
    font=("Vivaldi", 30)
)
text.pack()

text = Label(window, text = "Soy Milton Ponce.")
text.config(
    height= 2,
    bg= "yellow",
    font= ("Consolas", 18),
    padx= 10,
    pady= 20,
    cursor= "circle"
)
text.pack(anchor=SE)

def keyword_arguments(name, surname, country):
    return f"Hola {name} {surname}, veo que eres de {country}"

text = Label(window, text = keyword_arguments(country = 'Mexico', surname = 'Ponce', name = 'Milton'))
text.config(
    height= 2,
    bg= "green",
    font= ("Consolas", 18),
    padx= 10,
    pady= 20,
    cursor= "circle"
)
text.pack(anchor=NW)

window.mainloop()
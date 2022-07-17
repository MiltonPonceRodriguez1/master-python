from tkinter import *

window = Tk()

#window.geometry("700x500")

text = Label(window, text = "Bienvenido a mi aplicación !!")

# Configuración textos
text.config(
    fg= "white",
    bg="#000000",
    padx= 20,
    pady= 20,
    font=("Vivaldi", 30)
)
text.pack(side=TOP, fill=X, expand=YES)

text = Label(window, text = "Soy Milton Ponce.")
text.config(
    height= 2,
    fg= 'white',
    bg= "#0080ff",
    font= ("Consolas", 18),
    padx= 10,
    pady= 20,
    cursor= "circle"
)
text.pack(side=TOP, fill=BOTH, expand=YES)

text = Label(window, text = 'Basico 1')
text.config(
    height= 2,
    bg= "green",
    font= ("Consolas", 18),
    padx= 10,
    pady= 20,
    cursor= "circle"
)
text.pack(side=LEFT, fill=X, expand=YES)

text = Label(window, text = 'Basico 2')
text.config(
    height= 2,
    bg= "red",
    font= ("Consolas", 18),
    padx= 10,
    pady= 20,
    cursor= "circle"
)
text.pack(side=LEFT, fill=X, expand=YES)

text = Label(window, text = 'Basico 3')
text.config(
    height= 2,
    bg= "orange",
    font= ("Consolas", 18),
    padx= 10,
    pady= 20,
    cursor= "circle"
)
text.pack(side=LEFT, fill=X, expand=YES)

window.mainloop()
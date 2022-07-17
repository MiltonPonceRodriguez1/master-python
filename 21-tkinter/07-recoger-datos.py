from tkinter import *

window = Tk()
window.geometry("700x700")
window.config(
    bd=50
)

def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >= 1:
        text.config(
            bg="green",
            fg="white"
        )
    else:
        text.config(
            bg=window.cget("bg")
        )


dato = StringVar()
resultado = StringVar()

Label(window, text="Introduce un texto: ").pack(anchor=NW)
Entry(window, textvariable=dato).pack(anchor=NW)

Label(window, text="Dato recogido: ").pack(anchor=NW)
text = Label(window, textvariable=resultado)
text.pack(anchor=NW)

Button(window, text="Mostrat Dato", command=getDato).pack(anchor=NW)

window.mainloop()
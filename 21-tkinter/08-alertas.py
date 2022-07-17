from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(bd=70)

def showAlert():
    messagebox.showinfo("Alerta", "Hola soy Milton Ponce")

Button(window, text="Mostrar Alerta!!", command=showAlert).pack()

def exit(name):
    resultado = messagebox.askquestion("Salir", "Continuar ejecutando la aplicación")

    if resultado != "yes":
        messagebox.showinfo("Chao!!", f"Adios {name}")
        window.destroy()


Button(window, text="Salir", command=lambda: exit("Milton Ponce")).pack()

window.mainloop()
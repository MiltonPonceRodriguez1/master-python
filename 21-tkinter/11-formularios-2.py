from tkinter import *

def showProfesion():
    text = ""
    if web.get():
        text += "Desarrollador Web"

    if mobile.get():
        if web.get():
            text += " y Movil"
        else:
            text += "Desarrollador Movil"

    show.config(text=text, bg="green", fg="white")

def mark():
    marked.config(text=option.get(), bg="yellow")

ws = Tk()
ws.title("Formularios II")
ws.geometry("800x500")

header = Label(ws, text="Formularios II")
header.config(
    padx=15,
    pady=15,
    bg="green",
    fg="white",
    font=("Consolas", 20)
)
header.grid(row=0, column=0, columnspan=5, sticky=W)

# Checkbox
web = BooleanVar()
mobile = BooleanVar()

Label(ws, text="¿A que te dedicas?").grid(row=1, column=0)

Checkbutton(
    ws,
    text="Desarrollo Web",
    variable=web,
    onvalue=True,
    offvalue=False,
    command=showProfesion
).grid(row=2, column=0)

Checkbutton(
    ws,
    text="Desarrollo Movil",
    variable=mobile,
    onvalue=True,
    offvalue=False,
    command=showProfesion
).grid(row=3, column=0)

show = Label(ws)
show.grid(row=4, column=0)

# Radio buttons
option = StringVar()
option.set(None)

Label(ws, text="").grid(row=5)

Label(ws, text="¿Cuál es tu género?").grid(row=6)

Radiobutton(
    ws,
    text="Masculino",
    value="Masculino",
    variable=option,
    command=mark
).grid(row=7)

Radiobutton(
    ws,
    text="Femenino",
    value="Femenino",
    variable=option,
    command=mark
).grid(row=8)

marked = Label(ws)
marked.grid(row=9)

Label(ws, text="").grid(row=5)

# Options Menu

ws.mainloop()
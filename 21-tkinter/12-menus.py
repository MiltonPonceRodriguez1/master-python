from tkinter import *

ws = Tk()
ws.title("Menus de Navegación")
ws.geometry("700x400")

nav = Menu(ws)
ws.config(menu=nav)

#Submenu de File
file = Menu(nav, tearoff=0)
file.add_command(label="New Text File")
file.add_command(label="New File")
file.add_command(label="New Window")

file.add_separator()

file.add_command(label="Open File")
file.add_command(label="Open Folder")
file.add_command(label="Open Recent")

file.add_separator()

file.add_command(label="Exit", command=ws.quit)

nav.add_cascade(label="File", menu=file)
nav.add_command(label="Edit")
nav.add_command(label="Selection")

ws.mainloop()
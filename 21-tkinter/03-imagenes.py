from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.geometry("700x500")

Label(window, text="Hola, soy Milton ponce").pack(anchor=W)

image = Image.open('./21-tkinter/images/morrison.jpg')
render = ImageTk.PhotoImage(image)

Label(window, image=render).pack(anchor=CENTER)

window.mainloop()
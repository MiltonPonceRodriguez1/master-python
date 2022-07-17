from struct import pack
from tkinter import *

window = Tk()

window.title("Marcos | Master en Python")
window.geometry("700x700")

frame_root = Frame(window, width=250, height=250)
frame_root.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

frame = Frame(frame_root, width=250, height=250)
frame.config(
    bg='red',
    bd=5,
    relief="raised"
)
frame.pack(side=LEFT)
frame.pack_propagate(False)

text = Label(frame, text="Primer Frame")
text.config(
    bg = "red",
    fg = "white" ,
    font = ("Consolas", 20)
)
text.pack(anchor=CENTER, fill=Y, expand=YES)

frame = Frame(frame_root, width=250, height=250)
frame.config(
    bg='green',
    bd=5,
    relief="raised"
)
frame.pack(side=RIGHT)

frame_root = Frame(window, width=250, height=250)
frame_root.pack(side=TOP, anchor=N, fill=X, expand=YES)

frame = Frame(frame_root, width=250, height=250)
frame.config(
    bg = 'blue',
    bd = 5,
    relief = RAISED
)
frame.pack(side=LEFT)

frame = Frame(frame_root, width=250, height=250)
frame.config(
    bg='orange',
    bd=5,
    relief="raised"
)
frame.pack(side=RIGHT)
window.mainloop()
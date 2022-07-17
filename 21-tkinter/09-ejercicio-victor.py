from tkinter import *
from tkinter import messagebox

def cFloat(number):
    res = 0

    try:
        res = float(number)
    except:
        messagebox.showerror("Error", "Introduce bien los datos")

    return res

def sumar():
    result.set(cFloat(number1.get()) + cFloat(number2.get()))
    showResult()

def restar():
    result.set(cFloat(number1.get()) - cFloat(number2.get()))
    showResult()

def multiplicar():
    result.set(cFloat(number1.get()) * cFloat(number2.get()))
    showResult()

def dividir():
    result.set(cFloat(number1.get()) / cFloat(number2.get()))
    showResult()


def showResult():
    messagebox.showinfo("Resultado", f"El resultado de la operación es: {result.get()}")
    number1.set("")
    number2.set("")

ws = Tk()
ws.geometry("400x400")
ws.title("Ejercicio Completo | Master Python")
ws.config(
    bd=25
)

number1 = StringVar()
number2 = StringVar()
result = StringVar()

frame = Frame(ws, width=340, height=200)
frame.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
frame.pack(side=TOP, anchor=CENTER)
frame.pack_propagate(False)

Label(frame, text="Primer número: ").pack()
Entry(frame, textvariable=number1, justify=CENTER).pack()

Label(frame, text="Segundo número: ").pack()
Entry(frame, textvariable=number2, justify=CENTER).pack()

Label(frame, text="").pack()

Button(frame, text="Sumar", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(frame, text="Restar", command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(frame, text="Multiplicar", command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(frame, text="Dividir", command=dividir).pack(side=LEFT, fill=X, expand=YES)


ws.mainloop()
from tkinter import *
from tkinter import messagebox

class Calculator:

    def __init__(self, alerts):
        self.number1 = StringVar()
        self.number2 = StringVar()
        self.result = StringVar()
        self.alerts = alerts

    def cFloat(self, number):
        res = 0

        try:
            res = float(number)
        except:
            self.alerts.showerror("Error", "Introduce bien los datos")

        return res

    def add(self):
        self.result.set(self.cFloat(self.number1.get()) + self.cFloat(self.number2.get()))
        self.showResult()

    def less(self):
        self.result.set(self.cFloat(self.number1.get()) - self.cFloat(self.number2.get()))
        self.showResult()

    def prod(self):
        self.result.set(self.cFloat(self.number1.get()) * self.cFloat(self.number2.get()))
        self.showResult()

    def div(self):
        self.result.set(self.cFloat(self.number1.get()) / self.cFloat(self.number2.get()))
        self.showResult()


    def showResult(self):
        self.alerts.showinfo("Resultado", f"El resultado de la operación es: {self.result.get()}")
        self.number1.set("")
        self.number2.set("")

ws = Tk()
ws.geometry("400x400")
ws.title("Ejercicio Completo | Master Python")
ws.config(
    bd=25
)

calculator = Calculator(messagebox)

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
Entry(frame, textvariable=calculator.number1, justify=CENTER).pack()

Label(frame, text="Segundo número: ").pack()
Entry(frame, textvariable=calculator.number2, justify=CENTER).pack()

Label(frame, text="").pack()

Button(frame, text="Sumar", command=calculator.add).pack(side=LEFT, fill=X, expand=YES)
Button(frame, text="Restar", command=calculator.less).pack(side=LEFT, fill=X, expand=YES)
Button(frame, text="Multiplicar", command=calculator.prod).pack(side=LEFT, fill=X, expand=YES)
Button(frame, text="Dividir", command=calculator.div).pack(side=LEFT, fill=X, expand=YES)


ws.mainloop()
"""
CALCULADORA:
- 2 Campos de texto
- 4 Botones para las operaciones
- Mostrar el resultado
"""

from tkinter import *
from tkinter import messagebox

def calculator(operation, a, b):

    if(operation == '+'):
        result.set(a+b)
        messagebox.showinfo("Resultado Suma", f"{a+b}")
        return a+b

    elif(operation == '-'):
        result.set(a-b)
        messagebox.showinfo("Resultado Resta", f"{a-b}")
        return a-b

    elif(operation == '*'):
        result.set(a*b)
        messagebox.showinfo("Resultado Producto", f"{a*b}")
        return a*b

    else:
        result.set(a/b)
        messagebox.showinfo("Resultado Division", f"{a/b}")
        return a/b

window = Tk()
window.geometry("500x250")
window.config(
    bd=25
)

op1 = StringVar()
op2 = StringVar()
result = StringVar()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

# Inicio Texto de Encabezado
header = Label(window, text="Calculadora con Python")
header.config(
    bg = "#ccc",
    fg = "white",
    font = ("Open Sans", 15)
)
header.grid(row=0, column=0, padx=5, pady=5, sticky=W, columnspan=12)
# Fin Texto de Encabezado

Label(window).grid(row=1, column=1) # Label separador

# Inicio Operando 1
Label(window, text="Operando 1:").grid(row=2, column=0, sticky=W)

tf_op1 = Entry(window, textvariable=op1)
tf_op1.config(
    justify="center",
    state="normal"
)
tf_op1.grid(row=2, column=1, padx=5, pady=5, sticky=W)

# Fin Operando 1

# Inicio Operando 2
Label(window, text="Operando 2:").grid(row=2, column=2, sticky=E)

tf_op2 = Entry(window, textvariable=op2)
tf_op2.config(
    justify="center",
    state="normal"
)
tf_op2.grid(row=2, column=3, padx=5, pady=5, sticky=W)
# Fin Operando 2


Label(window).grid(row=3, column=1) # Label separador

# Inicio Resultado
Label(window, text="Resultado:").grid(row=4, column=1, sticky=E)
tf_result = Entry(window, textvariable=result)
tf_result.config(
    justify="center",
    state="disabled"
)
tf_result.grid(row=4, column=2, padx=5, pady=5, sticky=W)
# Fin Resultado

Label(window).grid(row=5, column=1) # Label separador

# Inicio Botones
btn_add = Button(window, text="+", command=lambda: calculator("+", int(op1.get()), int(op2.get())))
btn_add.grid(row=6, column=0, padx=5, pady=5)
btn_add.config(
    font=("Arial", 15),
    bg="#0250c4",
    fg="#fafafa",
    width=5,
    anchor=CENTER
)

btn_sub = Button(window, text="-", command=lambda: calculator("-", int(op1.get()), int(op2.get())))
btn_sub.grid(row=6, column=1, padx=5, pady=5)
btn_sub.config(
    font=("Arial", 15),
    bg="#0250c4",
    fg="#fafafa",
    width=5,
    anchor=CENTER
)

btn_product = Button(window, text="*", command=lambda: calculator("*", int(op1.get()), int(op2.get())))
btn_product.grid(row=6, column=2, padx=5, pady=5)
btn_product.config(
    font=("Arial", 15),
    bg="#0250c4",
    fg="#fafafa",
    width=5,
    anchor=CENTER
)

btn_div = Button(window, text="/", command=lambda: calculator('/', int(op1.get()), int(op2.get())))
btn_div.grid(row=6, column=3, padx=5, pady=5)
btn_div.config(
    font=("Arial", 15),
    bg="#0250c4",
    fg="#fafafa",
    width=5,
    anchor=CENTER
)
# Fin Botones

window.mainloop()

# VERSION VICTOR ROBLES
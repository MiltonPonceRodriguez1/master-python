"""
Crear un programa que tenga:
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, Añadir, Info, Salir)
- Diferentes pantallas
- Formulario de añadir producto
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
- Opción de salir
"""

from tkinter import *
from tkinter import ttk

# DEFINIR VENTANA
ws = Tk()
# TAMAÑO CON DIMENSIONES PREDEFINIDAS
# ws.geometry("500x500")

# TAMAÑO CON DIMENSION MINIMA PREDEFINIDA PERO EXPANDIBLE
ws.minsize(500, 500)

ws.title("Proyecto Tkinter - Master Python")
ws.resizable(0, 0)

# INICIO CREACION PANTALLAS
def home():
    # MONTAR PANTALLA
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)

    # ENLISTAR PRODUCTOS
    """
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="-------------------").grid()
    """

    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert('', 0, text=product[0], values=(product[1]))

    # OCULTAR OTRAS PANTALLAS
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


def add():
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    add_frame.grid(row=1)

    # CAMPOS DEL FORMULARIO
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    # OCULTAR OTRAS PANTALLAS
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )

    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    # OCULTAR OTRAS PANTALLAS
    add_frame.grid_remove()
    home_label.grid_remove()
    products_box.grid_remove()
    add_label.grid_remove()

    return True
# FIN CREACION PANTALLAS

# INICIO PROCEDIMIENTO AGREGAR PRODUCTO
def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])

    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    home()
# FIN PROCEDIMIENTO AGREGAR PRODUCTO

# INICIO CREACIÓN VARIABLES
products = []
name_data = StringVar()
price_data = StringVar()
# FIN CREACIÓN VARIABLES

# INICIO DEFINICIÓN DE CAMPOS DE PANTALLAS
home_label = Label(ws, text="Inicio")
add_label = Label(ws, text="Añadir Producto")
info_label = Label(ws, text="Información")
data_label = Label(ws, text="Creado Por Dokken Lee - 2022")
# FIN DEFINICIÓN DE CAMPOS DE PANTALLAS

# INICIO DEFINICION FRAME DE PRODUCTOS
# products_box = Frame(ws, width=250)
Label(ws). grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)

products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)
# FIN DEFINICION FRAME DE PRODUCTOS

# INICIO DEFINICIÓN DE CAMPOS DEL FORMULARIO (ADD)
add_frame = Frame(ws)

add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame)
# FIN DEFINICIÓN DE CAMPOS DEL FORMULARIO (ADD)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)

# CARGAR HOME PAGE
home()

# INICIO DEL MENU DE NAVEGACIÓN
nav = Menu(ws)
ws.config(menu=nav)

nav.add_command(label="Inicio", command=home)
nav.add_command(label="Añadir", command=add)
nav.add_command(label="Info", command=info)
nav.add_command(label="Salir", command=ws.quit)
# FIN DEL MENU DE NAVEGACIÓN

# CARGAR VENTANA
ws.mainloop()
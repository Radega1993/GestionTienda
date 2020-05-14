from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from classes.inventario import Inventario


class AddProducto:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Añadir Producto")
        width_value = self.master.winfo_screenwidth()
        height_value = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.master)
        self.frame.pack()

        product = self.add_frame_product()


    def add_frame_product(self):
        ################# VAR FORM #############################################
        self.nombre = StringVar()
        self.categoria = StringVar()
        self.precio = DoubleVar()
        self.cantidad = DoubleVar()


        self.LabelTitle = Label(self.frame, text = "Añadir Producto",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.AddFrame1 = Frame(self.frame, width=1010, height=300, bd = 20,
                                relief='ridge')
        self.AddFrame1.grid(row=1, column=0)
        self.AddFrame2 = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.AddFrame2.grid(row=3, column=0)

        ######################## TEXT LOGIN ####################################

        self.LblNombre = Label(self.AddFrame1, text = "Nombre",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblNombre.grid(row = 0, column = 0)
        self.TxtNombre = Entry(self.AddFrame1,
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.nombre)
        self.TxtNombre.grid(row = 0, column = 1)


        self.LblCategoria = Label(self.AddFrame1, text = "Categoria",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblCategoria.grid(row = 3, column = 0)
        self.comboCategoria = ttk.Combobox(self.AddFrame1, font = ('arial', 20, 'bold'),
            textvariable=self.categoria, state = "readonly")

        all_categories = Inventario().find_category()
        list_categories = [category['nombre'] for category in all_categories]
        self.comboCategoria['values']= list_categories
        self.comboCategoria.set("Selecciona categoria")
        self.comboCategoria.grid(row = 3, column = 1)


        self.btnCrear = Button(self.AddFrame1, text = "Crear categoría", width = 17,
                        font =('arial', 20, 'bold'), command = self.add_category)
        self.btnCrear.grid(row = 3, column = 2)


        self.LblPrecio = Label(self.AddFrame1, text = "Precio",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblPrecio.grid(row = 4, column = 0)
        self.TxtPrecio = Entry(self.AddFrame1,
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.precio)
        self.TxtPrecio.grid(row = 4, column = 1)


        self.LblCantidad = Label(self.AddFrame1,  text = "Cantidad",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblCantidad.grid(row = 5, column = 0)
        self.TxtCantidad = Entry(self.AddFrame1,
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.cantidad)
        self.TxtCantidad.grid(row = 5, column = 1, padx = 65)


        ######################### BOTONES ######################################

        self.btnCrear = Button(self.AddFrame2, text = "Añadir", width = 17,
                        font =('arial', 20, 'bold'), command = self.add_producto)
        self.btnCrear.grid(row = 0, column = 0)

        self.btnReset = Button(self.AddFrame2, text = "Reset", width = 17,
                        font =('arial', 20, 'bold'), command = self.reset)
        self.btnReset.grid(row = 0, column = 1)

        self.btnAtras = Button(self.AddFrame2, text = "Atras", width = 17,
                        font =('arial', 20, 'bold'), command = self.back_system)
        self.btnAtras.grid(row = 0, column = 2)

        ######################## LOGIN ########################################

    def add_producto(self):

        name = (self.nombre.get())
        categoria = (self.categoria.get())
        precio = (self.precio.get())
        cantidad = (self.cantidad.get())


        name_find = Inventario().find_product_by_name(name)

        if (name_find == None):
            if (
                self.comboCategoria.get() != "Selecciona categoria" and len(self.nombre.get()) != 0
                ):

                insert = Inventario().add_product(name, categoria, precio, cantidad)
                tkinter.messagebox.showinfo("Terranova gestión de productos",
                    "El producto " + name + " añadido correctamente!")
                self.reset()
            else:
                tkinter.messagebox.showinfo("Terranova gestión de productos",
                    "Selecciona una categoria o no dejes campos en blanco!")
        else:
            tkinter.messagebox.showinfo("Terranova gestión de productos",
                "El producto " + name + " ya existe")

            self.reset()

    def add_category(self):

        self.nombrecat = StringVar()

        self.CategoryFrame3 = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.CategoryFrame3.grid(row=2, column=0)

        self.LblNombre = Label(self.CategoryFrame3, text = "Nombre",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblNombre.grid(row = 0, column = 0)
        self.TxtNombre = Entry(self.CategoryFrame3,
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.nombrecat)
        self.TxtNombre.grid(row = 0, column = 1)

        self.btnCrear = Button(self.CategoryFrame3, text = "Crear categoría", width = 17,
                        font =('arial', 20, 'bold'), command = self.save_category)
        self.btnCrear.grid(row = 0, column = 2)

    def save_category(self):

        nombre = (self.nombrecat.get())

        name_find = Inventario().find_category_by_name(nombre)

        if (name_find == None):
            if len(nombre) != 0:
                insert = Inventario().add_category(nombre)
                tkinter.messagebox.showinfo("Terranova gestión de productos",
                    "La categoría " + nombre + " añadida correctamente!")

                #refresh page
                self.add_frame_product()

            else:
                tkinter.messagebox.showinfo("Terranova gestión de productos",
                    "No dejes campos en blanco!")
        else:
            tkinter.messagebox.showinfo("Terranova gestión de productos",
                "La categoría " + nombre + " ya existe")

            self.reset()

    def reset(self):
        self.nombre.set("")
        self.categoria.set("Selecciona categoria")
        self.precio.set(0.0)
        self.cantidad.set(0.0)
        self.TxtNombre.focus()

    def back_system(self):
        from interfaces.principal import Principal
        frame = Principal(self.master)
        self.frame.destroy()

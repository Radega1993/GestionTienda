from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from classes.inventario import Inventario


class UpdateProducto:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Añadir Usuario")
        width_value = self.master.winfo_screenwidth()
        height_value = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.master)
        self.frame.pack()

        ################# VAR FORM #############################################
        all_products = Inventario().find_all()
        list_products = [product['nombre'] for product in all_products]

        self.nombre = StringVar()
        self.categoria = StringVar()
        self.precio = DoubleVar()
        self.cantidad = DoubleVar()

        self.LabelTitle = Label(self.frame, text = "Modificar Producto",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.FormFrame1 = Frame(self.frame, width=1010, height=300, bd = 20,
                                relief='ridge')
        self.FormFrame1.grid(row=1, column=0)
        self.FormFrame2 = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.FormFrame2.grid(row=2, column=0)

        ######################## TEXT LOGIN ####################################

        self.LblRole = Label(self.FormFrame1, text = "Producto",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblRole.grid(row = 0, column = 0)
        self.comboProduct = ttk.Combobox(self.FormFrame1, font = ('arial', 20, 'bold'),
            textvariable=self.nombre, state = "readonly")
        self.comboProduct['values'] = list_products
        self.comboProduct.set("Seleciona producto")
        self.comboProduct.grid(row = 0, column = 1)

        self.btnGetData = ttk.Button(self.FormFrame1,
                text="Ver datos", command = self.fill_data)
        self.btnGetData.grid(row = 0, column = 2)


        ######################### BOTONES ######################################

        self.btnCrear = Button(self.FormFrame2, text = "Modificar", width = 17,
                        font =('arial', 20, 'bold'), command = self.modificar_producto)
        self.btnCrear.grid(row = 0, column = 0)

        self.btnReset = Button(self.FormFrame2, text = "Reset", width = 17,
                        font =('arial', 20, 'bold'), command = self.reset)
        self.btnReset.grid(row = 0, column = 1)

        self.btnAtras = Button(self.FormFrame2, text = "Atras", width = 17,
                        font =('arial', 20, 'bold'), command = self.back_system)
        self.btnAtras.grid(row = 0, column = 2)

        ######################## LOGIN ########################################
    def fill_data(self):

        if self.comboProduct.get() != "Seleciona producto":
            self.categoria.set("")
            self.precio.set("")
            self.cantidad.set("")
            self.current = self.comboProduct.get()

            product_data = Inventario().find_product_by_name(self.comboProduct.get())


            self.LblRole = Label(self.FormFrame1, text = "categoría",
                font = ('arial', 20, 'bold'), bd=5)
            self.LblRole.grid(row = 3, column = 0)
            self.comboCategoria = ttk.Combobox(self.FormFrame1, font = ('arial', 20, 'bold'),
            textvariable=self.categoria, state = "readonly")
            all_categories = Inventario().find_category()
            list_categories = [category['nombre'] for category in all_categories]
            self.comboCategoria['values']= list_categories
            self.comboCategoria.set(product_data.get("categoria"))
            self.comboCategoria.grid(row = 3, column = 1)


            self.LblApellido = Label(self.FormFrame1, text = "precio",
                                    font = ('arial', 20, 'bold'), bd=5)
            self.LblApellido.grid(row = 2, column = 0)
            self.TxtApellido = Entry(self.FormFrame1,
                        font = ('arial', 20, 'bold'), bd=5, textvariable=self.precio)
            self.TxtApellido.insert(END, product_data.get("precio"))
            self.TxtApellido.grid(row = 2, column = 1)


            self.LblCargo = Label(self.FormFrame1, text = "Cantidad",
                                    font = ('arial', 20, 'bold'), bd=5)
            self.LblCargo.grid(row = 4, column = 0)
            self.TxtCargo = Entry(self.FormFrame1, text = "Cargo",
                        font = ('arial', 20, 'bold'), bd=5, textvariable=self.cantidad)
            self.TxtCargo.insert(END, product_data.get("cantidad"))
            self.TxtCargo.grid(row = 4, column = 1)


    def modificar_producto(self):

        name = (self.nombre.get())
        categoria = (self.categoria.get())
        precio = (self.precio.get())
        cantidad = (self.cantidad.get())


        if name == self.current:
            if (
                name != "Seleciona producto" and precio != "" and cantidad != ""
            ):
                insert = Inventario().update_product(name, categoria, precio, cantidad)
                tkinter.messagebox.showinfo("Terranova gestión de productos",
                    "El Producto " + name + " modificado correctamente!")

                from interfaces.principal import Principal
                frame = Principal(self.master)
                self.frame.destroy()
            else:
                tkinter.messagebox.showinfo("Terranova gestión de productos",
                    "Los campos no pueden estar vacios")
        else:
            tkinter.messagebox.showinfo("Terranova gestión de productos",
                "El producto " + name + " no es del que esta modificando datos!")

    def reset(self):
        self.nombre.set("Seleciona producto")
        self.categoria.set("")
        self.precio.set(0.0)
        self.cantidad.set(0.0)
        self.TxtNombre.focus()

    def back_system(self):
        from interfaces.principal import Principal
        frame = Principal(self.master)
        self.frame.destroy()

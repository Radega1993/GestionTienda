from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from classes.inventario import Inventario


class DelProducto:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Añadir Usuario")
        width_value = self.master.winfo_screenwidth()
        height_value = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.master)
        self.frame.pack()

        frame_producto = self.eliminar_producto_frame()


    def eliminar_producto_frame(self):

        self.nombre = StringVar()

        self.LabelTitle = Label(self.frame, text = "Eliminar Producto",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.LoginFrame1 = Frame(self.frame, width=1010, height=300, bd = 20,
                                relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)

        ######################## Delete User ###################################

        self.LblRole = Label(self.LoginFrame1, text = "Producto",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblRole.grid(row = 0, column = 0)
        self.comboRole = ttk.Combobox(self.LoginFrame1, font = ('arial', 20, 'bold'),
            textvariable=self.nombre, state = "readonly")
        my_list = Inventario().find_all()
        self.comboRole['values'] = [product['nombre'] for product in my_list]
        self.comboRole.grid(row = 0, column = 1)

        ######################### BOTONES ######################################

        self.btnCrear = Button(self.LoginFrame2, text = "Eliminar", width = 17,
                        font =('arial', 20, 'bold'), command = self.eliminar_categoria)
        self.btnCrear.grid(row = 0, column = 0)

        self.btnAtras = Button(self.LoginFrame2, text = "Atras", width = 17,
                        font =('arial', 20, 'bold'), command = self.back_system)
        self.btnAtras.grid(row = 0, column = 1)

        ######################## LOGIN ########################################

    def eliminar_categoria(self):

        nombre = (self.nombre.get())

        self.eliminar_categoria = tkinter.messagebox.askyesno("Terranova sistema de gestión",
            "De verdad quieres eliminar el producto " + nombre)

        if self.eliminar_categoria > 0:
            Inventario().delete_product(nombre)
            tkinter.messagebox.showinfo("Terranova eliminación de productos",
                "El producto " + nombre + " eliminado correctamente!")

            from interfaces.principal import Principal
            frame = Principal(self.master)
            self.frame.destroy()

        else:
            pass

    def back_system(self):
        from interfaces.principal import Principal
        frame = Principal(self.master)
        self.frame.destroy()

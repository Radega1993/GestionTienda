from tkinter import *
import tkinter.messagebox
from tkinter import ttk




class Principal:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Gestion")
        width_value = self.master.winfo_screenwidth()
        height_value = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LabelTitle = Label(self.frame, text = "Terranova Principal",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        bar = self.bar()
        inventario = self.inventario()
        logout = self.footer()

    def bar(self):


        self.barFrame = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.barFrame.grid(row=2, column=0)

        #######################################################################

        self.LblUsuario = Label(self.barFrame, text = "Bar",
                                font = ('arial', 30, 'bold'), bd=22)
        self.LblUsuario.grid(row = 0, column = 0)

        self.btnAddUsers = Button(self.barFrame, text = "Cobro",
                width = 17, font =('arial', 20, 'bold'), command = self.cobro_window)
        self.btnAddUsers.grid(row = 0, column = 1, padx = 10)


    def inventario(self):
        self.inventarioFrame = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.inventarioFrame.grid(row=3, column=0)

        #######################################################################

        self.LblUsuario = Label(self.inventarioFrame, text = "Inventario",
                                font = ('arial', 30, 'bold'), bd=22)
        self.LblUsuario.grid(row = 0, column = 0)

        self.btnAddProduct = Button(self.inventarioFrame, text = "Añadir producto",
                width = 17, font =('arial', 20, 'bold'), command = self.add_product_window)
        self.btnAddProduct.grid(row = 0, column = 1, padx = 10)

        self.btnupdateProduct = Button(self.inventarioFrame, text = "Actualizar producto",
                width = 17, font =('arial', 20, 'bold'), command = self.update_product_window)
        self.btnupdateProduct.grid(row = 0, column = 2, padx = 10)

        self.btndeleteProduct = Button(self.inventarioFrame, text = "Eliminar producto",
                width = 17, font =('arial', 20, 'bold'), command = self.del_product_window)
        self.btndeleteProduct.grid(row = 0, column = 3, padx = 10)

        self.btndDeleteCategory = Button(self.inventarioFrame, text = "Eliminar categoría",
                width = 17, font =('arial', 20, 'bold'), command = self.delete_category_window)
        self.btndDeleteCategory.grid(row = 0, column = 4, padx = 10)



    def footer(self):
        self.LogoutFrame = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.LogoutFrame.grid(row=8, column=0)


        self.btnAddUsers = Button(self.LogoutFrame, text = "Logout",
                width = 17, font =('arial', 20, 'bold'), command = self.logout_system)
        self.btnAddUsers.grid(row = 0, column = 0, padx = 10)

    def cobro_window(self):
        from interfaces.cobroInterface import CobroInterface
        frame = CobroInterface(self.master)
        self.frame.destroy()

    def add_product_window(self):
        from  interfaces.addProducto import AddProducto
        frame = AddProducto(self.master)
        self.frame.destroy()

    def update_product_window(self):
        from  interfaces.updateProducto import UpdateProducto
        frame = UpdateProducto(self.master)
        self.frame.destroy()

    def del_product_window(self):
        from  interfaces.delProducto import DelProducto
        frame = DelProducto(self.master)
        self.frame.destroy()

    def delete_category_window(self):
        from  interfaces.deleteCategory import DeleteCategory
        frame = DeleteCategory(self.master)
        self.frame.destroy()


    def logout_system(self):
        self.logout_system = tkinter.messagebox.askyesno("Terranova sistema de gestión",
            "De verdad quieres cerrar la session?")

        if self.logout_system > 0:
            from interfaces.mainapplication import MainApplication
            frame = MainApplication(self.master)
            self.frame.destroy()
        else:
            pass

from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from classes.usuario import Usuario


class CobroInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Cobro")
        width_value = self.master.winfo_screenwidth()
        height_value = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LabelTitle = Label(self.frame, text = "Terranova Cobro",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        form = self.form()
        productos = self.productos()

        footer = self.footer()


    def form(self):

        self.id_socio = StringVar()
        self.codigo = StringVar()
        self.recibido = StringVar()
        self.deudas = StringVar()
        self.total = StringVar()
        self.nombre = StringVar()
        self.cambio = StringVar()

        self.formFrame = Frame(self.frame, width=500, height=100, bd = 20,
                                relief='ridge')
        self.formFrame.grid(row=2, column=0)

        self.lbl_id_socio = Label(self.formFrame, text = "Nº Socio: ",
                                font = ('arial', 15, 'bold'), bd=5)
        self.lbl_id_socio.grid(row = 0, column = 0)
        self.txt_id_socio = Entry(self.formFrame,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.id_socio)
        self.txt_id_socio.grid(row = 0, column = 1)

        self.deudas.set("Libre de Deudas")
        self.txt_deudas = Label(self.formFrame,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.deudas)
        self.txt_deudas.grid(row = 0, column = 3)

        self.lbl_total = Label(self.formFrame, text = "Total €",
                                font = ('arial', 15, 'bold'), bd=5)
        self.lbl_total.grid(row = 1, column = 2)
        self.total.set("0")
        self.txt_total = Entry(self.formFrame, state = "readonly" ,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.total)
        self.txt_total.grid(row = 1, column = 3)


        self.lbl_codigo = Label(self.formFrame, text = "Codigo",
                                font = ('arial', 15, 'bold'), bd=5)
        self.lbl_codigo.grid(row = 1, column = 0)
        self.txt_codigo = Entry(self.formFrame,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.codigo)
        self.txt_codigo.grid(row = 1, column = 1)


        self.lbl_recibido = Label(self.formFrame, text = "recibido",
                                font = ('arial', 15, 'bold'), bd=5)
        self.lbl_recibido.grid(row = 2, column = 0)
        self.txt_recibido = Entry(self.formFrame,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.recibido)
        self.txt_recibido.grid(row = 2, column = 1)

        self.lbl_nombre = Label(self.formFrame, text = "Nombre",
                                font = ('arial', 15, 'bold'), bd=5)
        self.lbl_nombre.grid(row = 2, column = 2)
        self.txt_nombre = Entry(self.formFrame,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.nombre)
        self.txt_nombre.grid(row = 2, column = 3)


        self.btn_pago = Button(self.formFrame, text = "Pago", width = 17,
                        font =('arial', 20, 'bold'), command = self.pago)
        self.btn_pago.grid(row = 3, column = 1, padx=10)

        self.btn_deuda = Button(self.formFrame, text = "Deuda", width = 17,
                        font =('arial', 20, 'bold'), command = self.deuda)
        self.btn_deuda.grid(row = 3, column = 2)

        self.lbl_cambio = Label(self.formFrame, text = "Cambio: ",
                                font = ('arial', 15, 'bold'), bd=5)
        self.lbl_cambio.grid(row = 4, column = 0)
        self.cambio.set("0")
        self.txt_cambio = Entry(self.formFrame, state = "readonly" ,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.cambio)
        self.txt_cambio.grid(row = 4, column = 1)

    def productos(self):
        self.buscar = StringVar()

        self.productFrame = Frame(self.frame, width=500, height=100, bd = 20,
                                relief='ridge')
        self.productFrame.grid(row=2, column=1)

        self.lbl_buscar = Label(self.productFrame, text = "Buscar: ",
                                font = ('arial', 15, 'bold'), bd=5)
        self.lbl_buscar.grid(row = 0, column = 0)
        self.txt_buscar = Entry(self.productFrame,
                    font = ('arial', 15, 'bold'), bd=5, textvariable=self.buscar)
        self.txt_buscar.grid(row = 0, column = 1)

        ############################ TABLA #####################################

        # create Treeview with 3 columns
        cols = ('categoria', 'Nombre', 'Precio')
        self.listBox = ttk.Treeview(self.productFrame, columns=cols, show='headings')
        # set column headings
        for col in cols:
            self.listBox.heading(col, text=col)
        self.listBox.grid(row=2, column=0, columnspan= 2)


    def cuenta(self):
        pass

    def footer(self):
        self.footerFrame = Frame(self.frame, width=500, height=100, bd = 20,
                                relief='ridge')
        self.footerFrame.grid(row=4, column=0)

        self.btnAtras = Button(self.footerFrame, text = "Atras", width = 17,
                        font =('arial', 20, 'bold'), command = self.back_system)
        self.btnAtras.grid(row = 0, column = 2)

        self.btnloguot = Button(self.footerFrame, text = "Logout", width = 17,
                        font =('arial', 20, 'bold'), command = self.logout_system)
        self.btnloguot.grid(row = 0, column = 3)


    def pago(self):
        pass

    def deuda(self):
        pass

    def fill_table(self):
        for i, (name, score) in enumerate(tempList):
            listBox.insert("", "end", values=(i, name, score))

    ############################ FOOTER ########################################
    def back_system(self):
        from interfaces.principal import Principal
        frame = Principal(self.master)
        self.frame.destroy()

    def logout_system(self):
        self.logout_system = tkinter.messagebox.askyesno("Terranova logout",
            "De verdad quieres cerrar la session?")

        if self.logout_system > 0:
            from interfaces.mainapplication import MainApplication
            frame = MainApplication(self.master)
            self.frame.destroy()
        else:
            pass

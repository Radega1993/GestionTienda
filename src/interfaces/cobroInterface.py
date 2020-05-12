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


    def form(self):

        self.id_socio = StringVar()
        self.codigo = StringVar()
        self.recibido = StringVar()

        self.formFrame = Frame(self.frame, width=500, height=100, bd = 20,
                                relief='ridge')
        self.formFrame.grid(row=2, column=0)

        self.lbl_id_socio = Label(self.formFrame, text = "Nº Socio",
                                font = ('arial', 20, 'bold'), bd=5)
        self.lbl_id_socio.grid(row = 0, column = 0)
        self.txt_id_socio = Entry(self.formFrame, text = "Socio",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.id_socio)
        self.txt_id_socio.grid(row = 0, column = 1)


        self.lbl_codigo = Label(self.formFrame, text = "Codigo",
                                font = ('arial', 20, 'bold'), bd=5)
        self.lbl_codigo.grid(row = 1, column = 0)
        self.txt_codigo = Entry(self.formFrame, text = "Codigo",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.codigo)
        self.txt_codigo.grid(row = 1, column = 1)


        self.lbl_recibido = Label(self.formFrame, text = "recibido",
                                font = ('arial', 20, 'bold'), bd=5)
        self.lbl_recibido.grid(row = 2, column = 0)
        self.txt_recibido = Entry(self.formFrame, text = "recibido",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.recibido)
        self.txt_recibido.grid(row = 2, column = 1)


    def productos(self):
        self.productFrame = Frame(self.frame, width=500, height=100, bd = 20,
                                relief='ridge')
        self.productFrame.grid(row=2, column=1)

    def cuenta(self):
        pass

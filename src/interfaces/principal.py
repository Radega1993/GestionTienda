from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from  interfaces.inventario import Invetario


class Principal:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Gestion")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        #######################################################################

        self.btnInventario = Button(self.frame, text = "Inventario",
                                    command = self.inventory_window)
        self.btnInventario.grid(row = 0, column = 0)

    def inventory_window(self):
        self.new_window = Toplevel(self.master)
        self.app = Invetario(self.new_window)
        #######################################################################

from tkinter import *
import tkinter.messagebox
from tkinter import ttk


class Invetario:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Inventario")
        width_value = self.master.winfo_screenwidth()
        height_value = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.master)
        self.frame.pack()

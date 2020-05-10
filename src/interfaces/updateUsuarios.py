from tkinter import *
import tkinter.messagebox
from tkinter import ttk


class UpdateUsuarios:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Añadir Usuario")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

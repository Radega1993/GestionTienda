from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from interfaces.usuario.addUsuarios import AddUsuarios
from interfaces.usuario.updateUsuarios import UpdateUsuarios
from interfaces.usuario.deleteUsuarios import DeleteUsuarios


class PrincipalAdmin:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Administrador")
        width_value = self.master.winfo_screenwidth()
        height_value = self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (width_value, height_value))
        self.frame = Frame(self.master)
        self.frame.pack()

        self.LabelTitle = Label(self.frame, text = "Terranova Administración",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.GestionUsauriosFrame = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.GestionUsauriosFrame.grid(row=2, column=0)

        self.LogoutFrame = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.LogoutFrame.grid(row=3, column=0)
        #######################################################################

        self.LblUsuario = Label(self.GestionUsauriosFrame, text = "Gestion usuarios",
                                font = ('arial', 30, 'bold'), bd=22)
        self.LblUsuario.grid(row = 0, column = 0)

        self.btnAddUsers = Button(self.GestionUsauriosFrame, text = "Añadir usuarios",
                width = 17, font =('arial', 20, 'bold'), command = self.addUsers_window)
        self.btnAddUsers.grid(row = 0, column = 1, padx = 10)

        self.btnUpdateUsers = Button(self.GestionUsauriosFrame, text = "Modificar usuarios",
                width = 17, font =('arial', 20, 'bold'), command = self.updateUsers_window)
        self.btnUpdateUsers.grid(row = 0, column = 2, padx = 10)

        self.btnDeleteUsers = Button(self.GestionUsauriosFrame, text = "Eliminar usuarios",
                width = 17, font =('arial', 20, 'bold'), command = self.deleteUsers_window)
        self.btnDeleteUsers.grid(row = 0, column = 3, padx = 10)

        self.btnAddUsers = Button(self.LogoutFrame, text = "Logout",
                width = 17, font =('arial', 20, 'bold'), command = self.logout_system)
        self.btnAddUsers.grid(row = 0, column = 0, padx = 10)

    def addUsers_window(self):
        frame = AddUsuarios(self.master)
        self.frame.destroy()

    def updateUsers_window(self):
        frame = UpdateUsuarios(self.master)
        self.frame.destroy()

    def deleteUsers_window(self):
        frame = DeleteUsuarios(self.master)
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

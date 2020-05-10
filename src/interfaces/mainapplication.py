from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from classes.login import Login
from interfaces.principal import Principal
from interfaces.principalAdmin import *


class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | LOGIN")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.username = StringVar()
        self.password = StringVar()


        self.LabelTitle = Label(self.frame, text = "Terranova Gestión",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.LoginFrame1 = Frame(self.frame, width=1010, height=300, bd = 20,
                                relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)

        ######################## TEXT LOGIN #################################

        self.LblUsername = Label(self.LoginFrame1, text = "Username",
                                font = ('arial', 30, 'bold'), bd=22)
        self.LblUsername.grid(row = 0, column = 0)
        self.TxtUsername = Entry(self.LoginFrame1, text = "Username",
                    font = ('arial', 30, 'bold'), bd=22, textvariable=self.username)
        self.TxtUsername.grid(row = 0, column = 1)


        self.LblPassword = Label(self.LoginFrame1, text = "Password",
                                font = ('arial', 30, 'bold'), bd=22)
        self.LblPassword.grid(row = 1, column = 0)
        self.TxtPassword = Entry(self.LoginFrame1, text = "Password", show="*",
                    font = ('arial', 30, 'bold'), bd=22, textvariable=self.password)
        self.TxtPassword.grid(row = 1, column = 1, padx = 85)

        ######################## BOTONES LOGIN #################################

        self.btnLogin = Button(self.LoginFrame2, text = "Login", width = 17,
                        font =('arial', 20, 'bold'), command = self.login_system)
        self.btnLogin.grid(row = 0, column = 0)

        self.btnReset = Button(self.LoginFrame2, text = "Reset", width = 17,
                        font =('arial', 20, 'bold'), command = self.reset)
        self.btnReset.grid(row = 0, column = 1)

        self.btnExit = Button(self.LoginFrame2, text = "Exit", width = 17,
                        font =('arial', 20, 'bold'), command = self.exit_system)
        self.btnExit.grid(row = 0, column = 2)


        ######################## LOGIN ########################################

    def login_system(self):
        user = (self.username.get())
        passwd = (self.password.get())

        user_find = Login().get_user(user)
        passw_find = Login().get_password(passwd)

        if (user ==  user_find) and (passwd == passw_find):
            if (user == 'admin'):
                self.new_window = Toplevel(self.master)
                self.app = PrincipalAdmin(self.new_window)
            else:
                self.new_window = Toplevel(self.master)
                self.app = Principal(self.new_window)
        else:
            tkinter.messagebox.showinfo("Terranova sistema de gestión",
                "Usuario/contraseña incorrecta")
            self.username.set("")
            self.password.set("")
            self.TxtUsername.focus()

    def reset():
        self.username.set("")
        self.password.set("")
        self.TxtUsername.focus()

    def exit_system(self):
        self.exit_system = tkinter.messagebox.askyesno("Terranova sistema de gestión",
            "De verdad quieres cerrar el programa")

        if self.exit_system > 0:
            self.master.destroy()
            return
        else:
            pass

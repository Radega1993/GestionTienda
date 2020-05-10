from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from interfaces.principalAdmin import *


class AddUsuarios:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Añadir Usuario")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        ################# VAR FORM #############################################
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.usuario = StringVar()
        self.role = StringVar()
        self.cargo = StringVar()
        self.password = StringVar()


        self.LabelTitle = Label(self.frame, text = "Crear Usuario",
                                font = ('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.LoginFrame1 = Frame(self.frame, width=1010, height=300, bd = 20,
                                relief='ridge')
        self.LoginFrame1.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=1000, height=100, bd = 20,
                                relief='ridge')
        self.LoginFrame2.grid(row=2, column=0)

        ######################## TEXT LOGIN ####################################

        self.LblNombre = Label(self.LoginFrame1, text = "Nombre",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblNombre.grid(row = 0, column = 0)
        self.TxtNombre = Entry(self.LoginFrame1, text = "Nombre",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.nombre)
        self.TxtNombre.grid(row = 0, column = 1)


        self.LblApellido = Label(self.LoginFrame1, text = "Apellido",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblApellido.grid(row = 1, column = 0)
        self.TxtApellido = Entry(self.LoginFrame1, text = "Apellido",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.apellido)
        self.TxtApellido.grid(row = 1, column = 1)


        self.LblUsername = Label(self.LoginFrame1, text = "Usuario",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblUsername.grid(row = 2, column = 0)
        self.TxtUsername = Entry(self.LoginFrame1, text = "Username",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.usuario)
        self.TxtUsername.grid(row = 2, column = 1)


        self.LblRole = Label(self.LoginFrame1, text = "Role",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblRole.grid(row = 3, column = 0)
        self.comboRole = ttk.Combobox(self.LoginFrame1, font = ('arial', 20, 'bold'),
            textvariable=self.role, state = "readonly")
        self.comboRole['values']= ("USER_ROLE", "ADMIN_ROLE")
        self.comboRole.current(0)
        self.comboRole.grid(row = 3, column = 1)


        self.LblCargo = Label(self.LoginFrame1, text = "Cargo",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblCargo.grid(row = 4, column = 0)
        self.TxtCargo = Entry(self.LoginFrame1, text = "Cargo",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.cargo)
        self.TxtCargo.grid(row = 4, column = 1)


        self.LblPassword = Label(self.LoginFrame1, text = "Password",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblPassword.grid(row = 5, column = 0)
        self.TxtPassword = Entry(self.LoginFrame1, text = "Password", show="*",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.password)
        self.TxtPassword.grid(row = 5, column = 1, padx = 65)


        ######################### BOTONES ######################################

        self.btnCrear = Button(self.LoginFrame2, text = "Crear", width = 17,
                        font =('arial', 20, 'bold'), command = self.crear_usuario)
        self.btnCrear.grid(row = 0, column = 0)

        self.btnReset = Button(self.LoginFrame2, text = "Reset", width = 17,
                        font =('arial', 20, 'bold'), command = self.reset)
        self.btnReset.grid(row = 0, column = 1)

        self.btnAtras = Button(self.LoginFrame2, text = "Atras", width = 17,
                        font =('arial', 20, 'bold'), command = self.back_system)
        self.btnAtras.grid(row = 0, column = 2)

        ######################## LOGIN ########################################

    def crear_usuario(self):
        pass
        '''
        user = (self.username.get())
        passwd = (self.password.get())

        user_find = Login().get_user(user)
        passw_find = Login().get_password(passwd)

        if (user ==  user_find) and (passwd == passw_find):
            if (user == 'admin'):
                self.new_window = Toplevel(self.master)
                self.app = principalAdmin(self.new_window)
            else:
                self.new_window = Toplevel(self.master)
                self.app = principal(self.new_window)
        else:
            tkinter.messagebox.showinfo("Terranova sistema de gestión",
                "Usuario/contraseña incorrecta")
            self.username.set("")
            self.password.set("")
            self.TxtUsername.focus()
        '''
    def reset():
        self.nombre.set("")
        self.apellido.set("")
        self.usuario.set("")
        self.role.set("USER_ROLE")
        self.cargo.set("")
        self.password.set("")
        self.TxtNombre.focus()

    def back_system(self):
        self.new_window = Toplevel(self.master)
        self.app = PrincipalAdmin(self.new_window)

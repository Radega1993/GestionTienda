from tkinter import *
import tkinter.messagebox
from tkinter import ttk

from classes.usuario import Usuario


class UpdateUsuarios:
    def __init__(self, master):
        self.master = master
        self.master.title("Terranova | Añadir Usuario")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        ################# VAR FORM #############################################
        all_users = Usuario().find_all()
        list_users = [user['usuario'] for user in all_users]

        self.usuario = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.role = StringVar()
        self.cargo = StringVar()

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

        self.LblRole = Label(self.LoginFrame1, text = "Usuario",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblRole.grid(row = 0, column = 0)
        self.comboRole = ttk.Combobox(self.LoginFrame1, font = ('arial', 20, 'bold'),
            textvariable=self.usuario, state = "readonly")
        self.comboRole['values'] = list_users
        self.comboRole.current(0)
        self.comboRole.grid(row = 0, column = 1)

        self.LblNombre = Label(self.LoginFrame1, text = "Nombre",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblNombre.grid(row = 1, column = 0)
        self.TxtNombre = Entry(self.LoginFrame1, text = "Nombre",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.nombre)
        self.TxtNombre.grid(row = 1, column = 1)


        self.LblApellido = Label(self.LoginFrame1, text = "Apellido",
                                font = ('arial', 20, 'bold'), bd=5)
        self.LblApellido.grid(row = 2, column = 0)
        self.TxtApellido = Entry(self.LoginFrame1, text = "Apellido",
                    font = ('arial', 20, 'bold'), bd=5, textvariable=self.apellido)
        self.TxtApellido.grid(row = 2, column = 1)


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


        ######################### BOTONES ######################################

        self.btnCrear = Button(self.LoginFrame2, text = "Modificar", width = 17,
                        font =('arial', 20, 'bold'), command = self.modificar_usuario)
        self.btnCrear.grid(row = 0, column = 0)

        self.btnReset = Button(self.LoginFrame2, text = "Reset", width = 17,
                        font =('arial', 20, 'bold'), command = self.reset)
        self.btnReset.grid(row = 0, column = 1)

        self.btnAtras = Button(self.LoginFrame2, text = "Atras", width = 17,
                        font =('arial', 20, 'bold'), command = self.back_system)
        self.btnAtras.grid(row = 0, column = 2)

        ######################## LOGIN ########################################

    def modificar_usuario(self):


        name = (self.nombre.get())
        surname = (self.apellido.get())
        user = (self.usuario.get())
        role = (self.role.get())
        cargo = (self.cargo.get())

        user_find = Usuario().find_by_username(user)


        insert = Usuario().update_user(name, surname, user, role, cargo)
        tkinter.messagebox.showinfo("Terranova gestión de usuarios",
            "El usuario " + user + " modificado correctamente!")

        from interfaces.principalAdmin import PrincipalAdmin
        frame = PrincipalAdmin(self.master)
        self.frame.destroy()

    def reset():
        self.nombre.set("")
        self.apellido.set("")
        self.usuario.set("")
        self.role.set("USER_ROLE")
        self.cargo.set("")
        self.password.set("")
        self.TxtNombre.focus()

    def back_system(self):
        from interfaces.principalAdmin import PrincipalAdmin
        frame = PrincipalAdmin(self.master)
        self.frame.destroy()

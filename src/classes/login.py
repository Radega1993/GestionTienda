from  config.database import MongoDB
from pprint import pprint

class Login(object):
    """docstring for Login."""

    def __init__(self):
        super(Login, self).__init__()
        self.client = MongoDB()._db.usuarios


    def _init_usuario_db(self):
        admin_user = {
        "nombre": "admin",
        "apellido": "admin",
        "usuario": "admin",
        "role": "ADMIN_ROLE",
        "cargo": "Root",
        "password": "admin"
        }

        if self.client.find({}).count() == 0:
            insert = self.client.insert_one(admin_user)

    def get_user(self, usuario):
        myfind = self.client.find_one({"usuario": usuario})

        if self.client.find({"usuario": usuario}).count() == 0:
            self._init_usuario_db()

        if self.client.find({"usuario": usuario}).count() > 0:
            return myfind["usuario"]
        else:
            return print("El usuario es incorrecto")

    def get_password(self, password):
        myfind = self.client.find_one({"password": password})

        if self.client.find({"password": password}).count() > 0:
            return myfind["password"]
        else:
            return print("La contraseña es incorrecta")

from  config.database import MongoDB
from pprint import pprint

class Usuario(object):
    """docstring for Usuario."""

    def __init__(self):
        super(Usuario, self).__init__()
        self.client = MongoDB()._db.usuarios


    def add_usuario(self, nombre, apellido, usuario, role, cargo, password):

        new_user = {
            "nombre": nombre,
            "apellido": apellido,
            "usuario": usuario,
            "role": role,
            "cargo": cargo,
            "password": password
        }

        if self.client.find({"usuario": usuario}).count() == 0:
            insert = self.client.insert_one(new_user)
            print("El usuario " + new_user["usuario"]+ " añadido correctamente!")
            return new_user
        else:
            print("El usuario " + new_user["usuario"]+ " ya esta registrado!")


    def find_by_username(self, usuario):

        myfind = self.client.find_one({"usuario": usuario})

        if self.client.find({"usuario": usuario}).count() > 0:
            return myfind
        else:
            return None


    def find_all(self):

        list_users = []
        for usuarios in self.client.find():
            if usuarios['usuario'] != 'admin':
                list_users.append(usuarios)

        return list_users


    def update_user(self, nombre, apellido, usuario, role, cargo):

        update_user = {
            "nombre": nombre,
            "apellido": apellido,
            "usuario": usuario,
            "role": role,
            "cargo": cargo
        }

        update = self.client.find_one_and_update(
            {"usuario" : usuario },
            {"$set": update_user},upsert=True
        )

    def update_user_password(self, usuario, password):

        update = self.client.find_one_and_update(
            {"usuario" : usuario },
            {"$set": {"password": password}},upsert=True
        )

    def delete_user(self, usuario):

        remove = self.client.delete_one({"usuario": usuario})

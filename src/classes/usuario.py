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
            print("producto " + new_user["usuario"]+ " añadido correctamente!")
            return new_user
        else:
            print("El usuario " + new_user["usuario"]+ " ya esta registrado!")


    def find_product_by_username(self, usuario):

        myfind = self.client.find_one({"usuario": usuario})

        if self.client.find({"usuario": usuario}).count() > 0:
            return pprint(myfind)
        else:
            return print("No existe el usuario " + usuario)


    def find_all(self):

        for usuarios in self.client.find():
            pprint(usuarios)


    def update_user(self, nombre, apellido, usuario, role, cargo, password):

        update_user = {
            "nombre": nombre,
            "apellido": apellido,
            "role": role,
            "cargo": cargo,
            "password": password
        }

        update = self.client.find_one_and_update(
            {"usuario" : usuario },
            {"$set": update_user},upsert=True
        )


    def delete_product(self, usuario):

        remove = self.client.delete_one({"usuario": usuario})

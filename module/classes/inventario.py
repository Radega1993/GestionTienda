import json
from  config.database import MongoDB

class Inventario(object):

    categorias = []


    """docstring for Inventario."""
    def __init__(self):
        super(Inventario, self).__init__()

    def add_product(self, nombre, categoria, subcategoria, precio, cantidad):

        new_product = {
            "nombre": nombre,
            "categoria": categoria,
            "subcategoria": subcategoria,
            "precio": precio,
            "cantidad": cantidad
        }

        client = MongoDB()._db.productos

        insert = client.insert_one(new_product)
        print("producto " + new_product["nombre"]+ " añadido correctamente!")
        return new_product

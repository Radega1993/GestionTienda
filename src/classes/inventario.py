from  config.database import MongoDB
from pprint import pprint

class Inventario(object):

    categorias = []


    """docstring for Inventario."""
    def __init__(self):
        super(Inventario, self).__init__()
        self.client = MongoDB()._db.productos
        self.client2 = MongoDB()._db.category


    def add_product(self, nombre, categoria, precio, cantidad):

        new_product = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        }

        if self.client.find({"nombre": nombre}).count() == 0:
            insert = self.client.insert_one(new_product)
            print("producto " + new_product["nombre"]+ " añadido correctamente!")
            return new_product
        else:
            print("producto " + new_product["nombre"]+ " ya esta registrado!")



    def find_product_by_name(self, nombre):

        myfind = self.client.find_one({"nombre": nombre})

        if self.client.find({"nombre": nombre}).count() > 0:
            return myfind
        else:
            return print("No existe el producto " + nombre)


    def find_all(self):

        all_products = []
        for product in self.client.find():
            all_products.append(product)
        return all_products

    def update_product(self, nombre, categoria, precio, cantidad):

        update_product = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio,
            "cantidad": cantidad
        }

        update = self.client.find_one_and_update(
            {"nombre" : nombre },
            {"$set": update_product},upsert=True
        )


    def delete_product(self, nombre):

        remove = self.client.delete_one({"nombre": nombre})


    def add_category(self, nombre):

        new_category = {
        "nombre": nombre
        }

        if self.client2.find({"nombre": nombre}).count() == 0:
            insert = self.client2.insert_one(new_category)
            print("Categoria " + new_category["nombre"]+ " añadido correctamente!")
            return new_category
        else:
            print("producto " + new_category["nombre"]+ " ya esta registrado!")


    def find_category(self):

        all_category = []
        for cartegory in self.client2.find():
            all_category.append(cartegory)
        return all_category

    def find_category_by_name(self, nombre):

        myfind = self.client2.find_one({"nombre": nombre})

        if self.client2.find({"nombre": nombre}).count() > 0:
            return myfind
        else:
            return print("No existe el producto " + nombre)

    def delete_category(self, nombre):

        remove = self.client2.delete_one({"nombre": nombre})

import unittest

from config.database import MongoDB
from classes.inventario import Inventario

class TestSum(unittest.TestCase):

    def test_add_product():
        testprod = myinventario.add_product("cocacola", "Bebida", "Refresco", 10, 1)
        self.assertIs("cocacola", testprod)

    def test_add_product_alredy_db():
        testprod = myinventario.add_product("cocacola", "Bebida", "Refresco", 10, 1)
        assert testprod == "producto Cocacola ya esta registrado!", "ya en bd"

if __name__ == "__main__":
    # you want to initialize the class
    database   = MongoDB()
    collection = database.createCollection("test")
    myinventario = Inventario()

    unittest.main()

'''
if __name__ == '__main__':
    # you want to initialize the class
    database   = MongoDB()
    collection = database.createCollection("productos")
    myinventario = Inventario()

    print("------ añadir producto ------")
    articulo1 = myinventario.add_product("cocacola", "Bebida", "Refresco", 10, 1)

    print("------ buscar producto ------")
    buscar = myinventario.find_product_by_name("Cocacola")

    print("------ buscar todos los producto ------")
    buscar_todo = myinventario.find_all()


    mod_articulo1 = myinventario.update_product("Cocacola", "Bebida", "Refresco", 10, 50)

    print("------ buscar producto modificado ------")
    buscar = myinventario.find_product_by_name("Cocacola")

    print("------ eliminiar producto ------")
    buscar = myinventario.delete_product("cocacola")

    print("------ buscar producto eliminado ------")
    buscar = myinventario.find_product_by_name("cocacola")
'''

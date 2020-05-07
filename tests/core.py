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

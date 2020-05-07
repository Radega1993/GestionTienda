from config.database import MongoDB
from classes.inventario import Inventario

if __name__ == '__main__':
    # you want to initialize the class
    database   = MongoDB()
    collection = database.createCollection("productos")
    myinventario = Inventario()

    articulo1 = myinventario.add_product('cocacola', "Bebida", "Refresco", 10, 1)

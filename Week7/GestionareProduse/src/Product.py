class Product:
    def __init__(self, product_id, name, price, quantity=1):   #parametru optional cu valoare by default

        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


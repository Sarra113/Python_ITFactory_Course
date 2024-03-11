from AbstractClass import IRepository
from Product import Product


class ProductsRepository(IRepository):
    def __init__(self):
        self.products = []

    def create(self, data: dict):
        product_id = len(self.products) + 1
        product = Product(product_id, **data)  # dispatching
        self.products.append(product)

    def read(self, entry_id):
        for product in self.products:  # product e obiectul produs
            if product.product_id == entry_id:
                print(f'Product_id: {product.product_id}, name: {product.name}, price: {product.price}, quantity: {product.quantity}')
                return   # pentru a iesi din functie pentru ca am gasit produsul cautat si ca sa nu se mai execute si scenariul negativ
        print(f"The product with id {entry_id} is not available")

    def update(self, entry_id, new_data):
        for product in self.products:
            if product.product_id == entry_id:
                product.name = new_data.get('name', product.name)   # daca cheia name nu e furnizata in new_data, atunci numele produsului nu se va modifica
                product.price = new_data.get('price', product.price)
                product.quantity = new_data.get('quantity', product.quantity)
                print(f'The product with id {entry_id} has been updated')
                return
        print(f'The product with id {entry_id} was not found')

# search cum sa afiseze mesajul de la else doar o data

    def delete(self, entry_id):
        for product in self.products:
            if product.product_id == entry_id:
                self.products.remove(product)
                print(f'The product with id {entry_id} was deleted')
                return
        print(f'The product with id {entry_id} was not found')


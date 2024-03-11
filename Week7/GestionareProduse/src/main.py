from AbstractClass import IRepository
from ProductsRepository import ProductsRepository
from Product import Product
from User import User
from UserRepository import UserRepository


# products_repo = ProductsRepository()
# products_repo.create({'name': 'Laptop', 'price': 5000, 'quantity': 10})
# products_repo.create({'name': 'Telefon', 'price': 3000, 'quantity': 15})
# print(products_repo.products)
#
# products_repo.read(1)
# products_repo.read(2)
# products_repo.read(3)
#
# products_repo.update(1, {'name': 'TV', 'price': 7000, 'quantity': 3})
# products_repo.read(1)
#
# products_repo.update(2, {'name': 'Telefon2', 'quantity': 7})
# products_repo.read(2)
#
# products_repo.update(3, {'name': 'Mouse', 'price': 100})
#
# products_repo.delete(2)
# print(products_repo.products)

user_repo = UserRepository()
user_repo.create({'name': 'Sarra', 'email': 'creta.sarra@gmail.com', 'password': 'Parola11'})
user_repo.create({'name': 'Alin', 'email': 'bbbb@gmail.com', 'password': 'parolaL8888'})
print(user_repo.users)

user_repo.read(1)
user_repo.read(3)

user_repo.update(1, {'email': 'sarra_creta@yhaoo.com'})
user_repo.read(1)
user_repo.update(3, {'name': 'Mihai'})

user_repo.delete(2)
user_repo.delete(3)




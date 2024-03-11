# class Product:
#     def __init__(self, name: str, price: float, stock: int):
#         self.name = name
#         self.price = price
#         self.stock = stock
#
#     def check_product(self):
#         if self.stock == 0:
#             return f'Ne pare rau dar prod nu este in stock'
#
#         return f'Produsul se afla in stock'
#
#
# cafea = Product('cafea', 50.00, 5)
# ceai = Product('ceai', 10, 0)
#
# print(cafea.name, cafea.price, cafea.stock, sep=', ')
# print(cafea.check_product())



class Dog:
    rasa = 'chihuahua'

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


    def description(self):
        return f'Numele cainelui este {self.name}, are varsta de {self.age} si este de rasa {self.rasa}'

    def speak(self, sound: str):
        return f'{self.name} latra {sound}'

rex = Dog('Rex', 5)
max = Dog('Max', 9)

print(f'Numele cainelui este {rex.name} si are varsta de {rex.age}')
print(f'Numele cainelui este {max.name} si are varsta de {max.age}')

rex.name = 'Azorel'
print(rex.name)
print(rex.description())
print(rex.speak('ham'))

descriere_rex = rex.description()
print(descriere_rex)
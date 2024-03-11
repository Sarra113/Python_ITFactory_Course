# class Strabunic:
#     pass
#
# class Bunic(Strabunic):
#     pass
#
# class Parinte(Bunic):
#     pass
#
# class Copil(Parinte):
#     pass
#
#
# # MRO = Method Resolution Order
# # print(Copil.mro())
#
#
# class Car:
#     def __init__(self, brand):
#         self.__brand = brand
#
#     def run(self):
#         print(f"Please run {self.__brand}")
#
#
# car = Car("Dacia")
# car.run()


class Language:
    def language(self):
        return "language"


class English(Language):
    def language(self):
        parent_value = super().language()
        return parent_value + " English"


english = English()
print(english.language())

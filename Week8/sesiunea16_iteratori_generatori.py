# nums = list(range(1, 10))
#
#
# squared_list = [x**2 for x in nums]
# squared_gen = (x**2 for x in nums)  # gen expression
#
# print(squared_gen)
# print(next(squared_gen))
# print(next(squared_gen))
#
# for num in squared_gen:
#     print(num)

# nums = [1, 2, 3]
#
# i_nums = iter(nums)
# print(i_nums)
# print(iter(i_nums))
# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

"""
EX1: Implementeaza o clasa care sa fie atat iterabila cat si un iterator
si sa aiba acelasi comportament ca si functia range din Python.
"""


# class Iterator:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 10:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# ???
#
# numbers = Iterator()
# print(iter(numbers))
# print(next(numbers))
# print(next(numbers))

# def my_gen():
#     n = 1
#     while n < 10:
#         yield n
#         n += 1
#
# iterator_obj = my_gen()
# print(iterator_obj)
# print(next(iterator_obj))

"""
EX3: Implementeaza un generator de numere pare care ne va da acces la toate
numerele pare pana la un numar maxim luat ca si parametru.
"""


# def my_gen():
#     n = 2
#     while n % 2 == 0 and n <= 10:
#         yield n
#         n += 2
#     else:
#         raise StopIteration

# even_nr = my_gen()
# print(next(even_nr))
# print(next(even_nr))
# print(next(even_nr))
# print(next(even_nr))
# print(next(even_nr))
# print(next(even_nr))

# def my_gen(max_nr):
#     n = 0
#     while n <= max_nr:
#         if n % 2 == 0:
#             yield n
#         n += 2
#
#
# for i in my_gen(4):  # functia returneaza un obiect iterator
#     print(i)

"""
EX4: Implementeaza un generator de puteri ale unui numar.
Va lua doi parametri: numarul ce va fi ridicat la putere, si
un numar care va reprezenta puterea maxima pana la care primul
parametru va fi ridicat.
"""


# def my_gen(nr, puterea_maxima):
#     x = 1
#     while x <= puterea_maxima:
#         yield nr ** x
#         x += 1
#
#
# puteri = my_gen(2, 6)
#
# for i in puteri:
#     print(i)


"""
EX5: Implementeaza un context manager care va masura si va afisa
durata de executie a codului executat.
"""
import time


class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish = time.time()
        self.range = self.finish - self.start
        print(f"Durata de executie: {self.range} secunde")


with Timer():
    for i in range(1_000_000_000):
        pass







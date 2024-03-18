import time


"""
Sesiunea 17 - Exercitii cu Trainer
"""


"""
ITERATORS

1. Implementati un iterator numit ReverseIterator, care parcurge o colectie in sens opus. Exemplu de folosire:

note = [3, 7, 5, 8, 10] 
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d
"""

# class ReverseIterator:
#     def __init__(self, collection):
#         self.collection = collection
#         self.index = len(collection)
#
#     def __iter__(self): # permite obiectului sa fie iterabil si sa poata fi utilizat in bucle for
#         return self
#
#     def __next__(self):   # returneaza urm element la fiecare apelare a functiei next pe iterator
#         if self.index > 0:  # verificam daca mai sunt elemente care nu au fost iterate
#             self.index -= 1
#             rezultat = self.collection[self.index]
#             return rezultat
#         else:                  # daca nu mai sunt elemente de iterat:
#             raise StopIteration()
#
#
# note = [3, 7, 5, 8, 10]
# rev_it = ReverseIterator(note)
# print(next(rev_it))


"""
GENERATORS

2. Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""

# import random
# import time
#
#
# def loto_gen():
#     for _ in range(6):
#         yield random.randint(1, 49)
#     yield random.randint(1000000, 9999999)
#
#
# for numar in loto_gen():  # necesar pt a itera prin elem generate
#     print(numar)
#     time.sleep(1)



"""
DECORATORS

3. Implementați o clasă User, cu următoarele cerințe:
– constructorul va primi ca parametri nume, email, parola, și data nasterii 
- atribute in constructor: nume, email, parola, data_nasterii, este_logat (valoare default False)
– o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
– o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat,
folosind un decorator `@login_required` 
– o metoda logout, fara params, care delogheaza userul.

Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.
"""


# def login_required(func):
#     def wrapper(user_instance, *args, **kwargs):  # user_instance inlocuieste self
#         if not user_instance.este_logat:
#             return 'Utilizatorul nu este logat.'
#         return func(user_instance, *args, **kwargs)
#     return wrapper
#
# class User:
#     def __init__(self, nume, email, parola, data_nasterii):
#         self.nume = nume
#         self.email = email
#         self.parola = parola
#         self.data_nasterii = data_nasterii
#         self.este_logat = False
#
#     def login(self, email, parola):
#         if email == self.email and parola == self.parola:
#             self.este_logat = True
#             print('Login reusit')
#         else:
#             print('Email sau parola incorecte')
#
#     def log_out(self):
#         self.este_logat = False
#         print(f'Logout reusit')
#
#     @login_required
#     def get_info(self):
#         return f'{self.nume}, {self.email}, {self.data_nasterii}'


# user = User('Sarra', 'creta.sarra@gmail.com', 1234, '13.11.1997')
#
# print(user.get_info())
# user.login('creta.sarra@gmail.com', 1234)
# print(user.get_info())
# user.log_out()
# print(user.get_info())
# user.login('creta.sarra@gmail.com', 3333)




"""
DECORATORS

4. Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții 
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
"""

# class Timer:
#     def __enter__(self):
#         self.start = time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.finish = time.time()
#         self.range = self.finish - self.start
#         print(f"Durata de executie: {self.range} secunde")



# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         finish = time.time()
#         print(f'Functia {func.__name__} a durat {finish - start} secunde')
#         return result
#     return wrapper
#
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'Functia {func.__name__} a fost apelata cu argumentele {args or kwargs or None} si a returnat {result}')
#         return result
#     return wrapper
#
#
# @timeit
# @logger
# def multiply(x, y):
#     time.sleep(1)
#     return x * y
#
#
# print(multiply(2, 3))





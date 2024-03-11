"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 16)
"""


"""
1. Creeaza urmatoarele variabile: o lista, o tupla, un string.
Itereaza prin fiecare dintre ele, prima data folosind o bucla for,
iar apoi folosind un iterator (ne vom folosi de metodele iter si next):

my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(f'Primul element: {next(my_iterator)}')
print(f'Al doilea element: {next(my_iterator)}')
print(f'Al treilea element: {next(my_iterator)}')
print(f'Aici va da eroare: {next(my_iterator)}')
"""
# my_list = [2, 4, 6]
# for x in my_list:
#     print(x)
# my_iter1 = iter(my_list)
# print(next(my_iter1))
# print(next(my_iter1))
# print(next(my_iter1))
# print(next(my_iter1))

# my_tuple = (1, 3, 5, 7)
# for i in my_tuple:
#     print(i)
# my_iter2 = iter(my_tuple)
# print(next(my_iter2))

# my_string = 'alabala'
# for i in my_string:
#     print(i)
# my_iter3 = iter(my_string)
# print(next(my_iter3))

"""
2. Atunci cand nu mai contine elemente, un iterator va arunca o exceptie
de tipul StopIteration.
Foloseste un bloc try-except pe codul de mai sus pentru a gestiona aceasta exceptie
si pentru a te asigura ca programul tau ajunge la final cu un exit code de succes (adica 0).
"""
# my_list = [1, 2, 3, 4, 5]
# my_iterator = iter(my_list)
#
# while True:
#     try:
#         print(next(my_iterator))
#     except StopIteration:
#         break

# daca e o eroare in blocul try se executa exceptul


"""
3. Declara un string care contine toate literele alfabetului.
Folosind functia enumerate, care primeste ca si parametru o colectie
(lista, tupla, string) si returneaza un iterator,
 afiseaza pentru fiecare litera in parte:
`Pe mine ma cheama X si sunt a n-a litera din alfabet`
Nu uite sa gestionezi cazurile speciale (prima litera, etc)

Useful resource: https://www.geeksforgeeks.org/enumerate-in-python/
"""
# x = 'abcdefghijklmnoprstuvwxyz'

# print(list(enumerate(x, 1)))
#
# for index, letter in enumerate(x, 1):
#     if index == 1:
#         print(f'Pe mine ma cheama {letter.upper()} si sunt prima litera din alfabet')
#     elif index == 25:
#         print(f'Pe mine ma cheama {letter.upper()} si sunt ultima litera din alfabet')
#     else:
#         print(f'Pe mine ma cheama {letter.upper()} si sunt a {index} - a litera din alfabet')


"""
4. Declara trei liste: una cu oameni, una cu salarii, si una cu meserii
(important: trebuie sa aiba acelasi numar de elemente).
Apoi foloseste functia zip, care primeste ca si parametru un numar de colectii
si returneaza un iterator pentru a afisa:
`Pe mine ma cheama X, sunt de profesie Y, si castig Z ron pe luna`

Useful resource: https://www.w3schools.com/python/ref_func_zip.asp
"""
oameni = ['Ana', 'Andrei', 'Mihai']
meserii = ['florist', 'qa', 'medic']
salarii = [2000, 3000, 5000]

perechi = zip(oameni, meserii, salarii)
print(perechi)

for pereche in perechi:
    print(f'Pe mine ma cheama {pereche[0]}, sunt de profesie {pereche[1]}, si castig {pereche[2]} ron pe luna')
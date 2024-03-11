"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 14)
"""


"""
1. Creaza un fisier text, numit "hello.txt" si adauga urmatoarele linii in el:
Python                                                                                              
Java
Javascript                                                                                              
C/C++/C#
PHP
Node.js

Citeste continutul din fisier si afiseaza-l.
"""


# def create_text_file(path, lines):
#     with open(path, 'w') as my_file:
#         return my_file.writelines(lines)
#
#
# create_text_file('hello.txt', ['Python\n', 'Java\n', 'Javascript\n', 'C/C++/C#\n', 'PHP\n', 'Node.js\n'])
#
# def read_text_file(path):
#     with open(path, 'r') as my_file:
#         return my_file.read()
#
#
# print(read_text_file('hello.txt'))

"""
2.
Adauga urmatoarele linii in fisierul "hello.txt" generat la exercitiul 1:

Go                                                                                              
Kotlin
Swift

HINT: Foloseste o lista cu string-uri si un for loop. 

Afiseaza continutul noului fisier.
"""

# my_list = ['Go', 'Kotlin', 'Swift']
# def add_to_file(path, my_list):
#     with open(path, 'a') as file:
#         for line in my_list:
#             file.writelines(line + '\n')   # return opreste functia dupa o iteratie
#
# add_to_file('hello.txt', my_list)
#
# def read_file(path):
#     with open(path, 'r') as file:
#         return file.read()
#
# print(read_file('hello.txt'))


"""
4. Citeste continutul din fisierul "hello.txt" si afiseaza
doar liniile impare.
"""

# def read_file(path):
#     with open(path, 'r') as file:
#         line_number = 1
#         for line in file:
#             if line_number % 2 != 0:
#                 print(line)
#             line_number += 1
#
#
# read_file('hello.txt')

"""
5.
Genereaza 26 de fisiere txt, numite "A.txt", "B.txt", ... , "Z.txt".
Fiecare fisier va avea urmatorul continut:

My name is letter X.
I am the 24th letter of the alphabet.

Fii atent la folosirea terminatiei potrivite pentru fiecare litera in functie
de a cata litera este in alphabet (1st, 2nd, 3rd, 4th...)
"""
#
# def create_file(path, lines):
#     with open(path, 'w') as file:
#         for x in range(27):


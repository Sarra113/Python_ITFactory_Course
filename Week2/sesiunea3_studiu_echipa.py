"""
EXERCITII WORKSHOP (Sesiunea 3)
"""


"""
1.
a. Citeste un string de la tastatura (ex: alabala portocala).
b. Salveaza primul caracter intr-o variabila - indiferent care este el, incearca cu 2 string-uri diferite.
c. Capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter => alAbAlA portocAla.
"""
# my_string = input('Introdu text: ')
# first_letter = my_string[0]
# first_capitalized = first_letter.capitalize()
# count_mystring = my_string.count(first_letter)
# new = my_string.replace(first_letter, first_capitalized, count_mystring - 1)
# print(new.replace(first_capitalized, first_letter, 1))


# new_string = my_string[1:-1].replace(first_letter, first_letter.upper())
# print(new_string)
# cuvant_final = first_letter + new_string + first_letter
# print(cuvant_final)

propozitie = input('Introdu propozitie: ')
first = propozitie[0]
mijloc_prop = propozitie[1:-1].replace(first, first.upper())
final = first + mijloc_prop + propozitie[-1]
print(final)




"""
2.
a. Citeste un username de la tastatura.
b. Citeste o parola.
c. Afiseaza: 'Parola pentru user-ul x este ***** și are x caractere'.
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect.

Exemple:
- parola 'abc' => ***
- parola 'abcd' => ****
"""
# user = input('name: ')
# parola = input('parola: ')
# x = len(parola)
# inlocuire = '*' * x
# print(f'Parola pentru user-ul {user} este {inlocuire} si are {x} caractere')

"""
3. 
x, y, z - laturile unui triunghi.
Afișeaza daca triunghiul este isoscel, echilateral sau oarecare.
"""
# x = float(input('Introdu latura: '))
# y = float(input('Introdu latura: '))
# z = float(input('Introdu latura: '))
# if x * y == x * z:
#     print('Triunghi isoscel')
# elif x == y == z:
#     print('TRiunghi echilateral')
# elif x != y != z:
#     print('Triunghi oarecare')

"""
4.
a. Citeste un numar intreg, x, de la tastatura.
b. Verifica daca x are exact 6 cifre.
"""
# x = input('Introdu un nr intreg: ')
# if len(x) == 6:
#     print(True)
"""
5. 
a. Citeste trei numere intregi, x, y, z, de la tastatura.
b. Afiseaza care este cel mai mare dintre ele.
"""
# x = int(input('Nr intreg: '))
# y = int(input('Nr intreg: '))
# z = int(input('Nr intreg: '))
# if x > y and x > z:
#     print(x)
# elif y > x and y > z:
#     print(y)
# elif z > x and z > y:
#     print(z)

# SAU
# nr_cel_mai_mare = max(x, y, z)
# print(nr_cel_mai_mare)


"""
6. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock':
Declara un string nou care sa fie format din primele 5 caractere + ultimele 5.
"""
# my_string = 'Coral is either the stupidest animal or the smartest rock'
# new_string = my_string[:6] + my_string[-5:]
# print(new_string)

"""
7. Avand string-ul '0123456789':
- Afiseaza doar numerele pare. 
- Afiseaza doar numerele impare.

HINT: Foloseste slicing, controleaza din pas
"""
# numere = '0123456789'
# print(numere[::2])
# print(numere[1::2])

"""
EXERCITII RECOMANDATE - STUDIU INDIVIDUAL                                        .

1. Revizualizeaza sesiunile din aceasta saptamana si ia notite in caz ca ti-a scapat ceva.

2. Vizualizeaza din cursul ‘Primii pasi in Programare’ sectiunile:
- Variabile si Tipuri de date
- Operatori si Flow Control.
"""

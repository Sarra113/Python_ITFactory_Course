"""
EXERCITII WORKSHOP (Sesiunea 2)
"""


"""
NOTA: Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect vei exersa si operatorii in cadrul conditiilor ramurilor din if.

x poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte. 
X este un int.
"""


"""
1. Explica, cu cuvintele tale, in cadrul unui comentariu,
cum functioneaza un if else.
"""


"""
2. Verifica si afiseaza daca x este numar natural sau nu.
"""
x = 5.6
if x == int(x):
    print(True)
else:
    print(False)

"""
3. Verifica si afisează daca x este numar pozitiv, negativ sau neutru.
"""
# x = int(input('Introdu nr'))
# if x > 0:
#     print('Nr pozitiv')
# elif x == 0:
#     print('Nr neutru')
# elif x < 0:
#     print('Nr negativ')

"""
4. Verifica si afisează daca x este intre -2 si 13.
"""
# x = int(input('Numar'))
# if -2 < x < 13:
#     print('True')
# else:
#     print('False')

"""
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5.
"""
# x = int(input('Numar'))
# y = int(input('Numar'))
# if (x-y) < 5:
#     print(True)
# else:
#     print(False)
"""
6. Verifica daca x NU este intre 5 si 27  - a se folosi ‘not’.
"""
# x = int(input('Numar'))
# if not(5 < x < 27):
#     print(True)
# else:
#     print(False)

"""
7.
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu, afiseaza care din ele este mai mare.
"""

x = int(input('Numar'))
y = int(input('Numar'))
if x == y:
    print(True)
elif x > y:
    print('X mai mare decat Y')
elif y > x:
    print('Y mai mare decat Y')

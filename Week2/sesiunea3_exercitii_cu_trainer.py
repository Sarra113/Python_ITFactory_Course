"""
Sesiunea 3 - Exercitii cu Trainer
"""


"""
1. Citeste de la tastatura:
- lungimea unui dreptunghi
- latimea unui dreptungi

Calculeaza aria si afiseaz-o in consola astfel:
    'Aria dreptunghiului este x.'
"""
# lungimea = float(input('Introduceti lungimea'))
# latimea = float(input('Introduceti latimea'))
# aria = lungimea * latimea
# print(f'Aria dreptunghiului este {aria}')
"""
2. Avand string-ul:
'Coral is either the stupidest animal or the smartest rock':
- Afiseaza de cate ori apare cuvantul 'the'.
"""
my_string = 'Coral is either the stupidest animal or the smartest rock'
# print(my_string.count(' the'))
"""
3. Folosind string-ul de la exercitiul 2:
- Afiseaza in consola daca acest string contine doar numere.
"""
# number = '125'
# print(number.isnumeric()) # cifre 0-9 sau exponenti. Fara '-' '.'
# print(number.isdigit())  # doar cifre, fara virgule sau negative, asta sigur

"""
4. Citeste de la tastatura un string de dimensiune impara.
Afiseaza caracterul din mijloc.
"""
# string = input('Introduceti un sir de caractere impar: ')
# index_mijloc = len(string) // 2
# print(string[index_mijloc])

"""
5. Folosind o singura linie de cod, citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila.
- Afiseaza in consola ambele variabile pentru verificare.
"""
# cuv1, cuv2, *_ = input('Introduceti un text: ').split() # by default dupa spatiu
# print(cuv1)
# print(cuv2)
# print(*_) # print restul cuvintelor dupa primele doua. daca ar fi un singur cuvant am avea nevoie doar de _


"""
6. 
a. Citeste o litera de la tastatura.
b. Verifica si afiseaza daca este vocală sau nu.
"""
# litera = input('Introduceti o litera: ')
# # if litera == 'a' or 'e' or 'i' or 'o' or 'u':
# #     print(litera + ' este o vocala')
#
# if litera.lower() in 'aeiou':  # daca litera face parte din acel string
#     print('este vocala')
# else:
#     print('nu este vocala')

"""
7. Transforma si printeaza notele din sistem romanesc in:
 - Peste 9 => A
 - Peste 8 => B
 - Peste 7 => C
 - Peste 6 => D
 - Peste 4 => E
 - 4 sau sub => F
"""
# nota = float(input('Introdu nota: '))
# if nota >= 9:
#     print('A')
# elif nota >= 8:
#     print('B')
# elif nota >= 7:
#     print('C')
# elif nota >= 6:
#     print('D')
# elif nota >= 4:
#     print('E')
# elif nota <= 4:
#     print('F')


"""
8. 
a. Citeste un numar intreg, x, de la tastatura.
b. Verifica daca x are minim 4 cifre.

(Exemplu: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""
# x = input('Introdu un nr intreg: ')
# if len(x) >= 4:
#     print('Nr are 4 cifre')

"""
9.
a. Citeste un numar intreg, x, de la tastatura.
b. Verifica daca x este numar par sau impar.
"""
# x = int(input('Introdu nr: '))
# if x % 2 == 0:
#     print(f'{x} este numar par')
# else:
#     print(f'{x} este numar impar')

"""
10. 
a. Citeste trei numere intregi, x, y, z, de la tastatura,
care sa reprezinte unghiurile unui triunghi.
b. Verifica si afiseaza daca triunghiul este valid sau nu.
"""
# x = int(input('Introduceti unghiul x: '))
# y = int(input('Introduceti unghiul y: '))
# z = int(input('Introduceti unghiul z: '))
# # sau toate pe acelasi rand si apoi if int(x)....
# if x > 0 and y > 0 and z > 0 and (x + y + z) == 180:
#     print('Triunghiul este valid')

"""
11. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock':
a. Citește de la tastatura un numar intreg, x.
b. Afiseaza string-ul fara ultimele x caractere.

Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""
x = 'Coral is either the stupidest animal or the smartest rock'
# numar = int(input('Introdu un nr intreg: '))
# print(x[: - numar])
# de la inceput minus nr introdus! daca era [:numar] era de la inceput pana la idexul cu nr..

"""
12. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock': 
a. Salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o metoda ajutatoare care te ajuta sa faci asta)

b. Folosind variabila de la punctul a + slicing, afiseaza tot string-ul pana la acest cuvant
"""
# prop = 'Coral is either the stupidest animal or the smartest rock'
# index_rock = prop.rfind('r') # indexul de start al lui rock
                               # str.rfind() - cauta o anumita valoare in strig si da ultima pozitie
# print(index_rock)
# print(prop[:index_rock])

# sau
# index = prop.index('rock')
# print(index)
"""
13. Joc ghicit zarul
Cauta pe internet si vezi cum se genereaza un numar random.

Ne imaginam ca dai cu zarul si salvam acest numar in dice_roll.
Ia numarul ghicit de la utilizator.
Verifică si afiseaza daca utilizatorul a ghicit.
Vei avea 3 optiuni:
    - Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
    - Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
    - Ai ghicit. Felicitari! Ai ales x si zarul a fost y.
"""
import random # pachet random

dice_roll = random.randint(1, 6)
nr_ales = int(input('Alege un nr de la 1 la 6: '))
print(dice_roll)
if nr_ales < dice_roll:
    print(f'Ai pierdut. Ai ales un nr mai mic. Ai ales {nr_ales} dar a fost {dice_roll}')
elif nr_ales > dice_roll:
    print(f'Ai pierdut. Ai ales un nr mai mare. Ai ales {nr_ales} dar a fost {dice_roll}')
elif nr_ales == dice_roll:
    print(f'Ai ghicit. Ai ales {nr_ales} si zarul a fost {dice_roll}')

"""
14.  
a. Citeste de la tastatura un string.
b. Verifica daca primul si ultimul caracter sunt la fel, si afiseaza un mesaj
sugestiv pentru fiecare caz.

ATENTIE: se doreste ca programul sa fie case insensitive - 'apA' e acceptat
"""
# my_string = input('Introdu ceva: ')
# if my_string[0].casefold() == my_string[-1:].casefold():
#     print('Sunt ok')

# sau cu lower()
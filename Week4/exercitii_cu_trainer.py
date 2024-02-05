"""
1. GHICITOARE DE NUMAR
- numar_secret = Generati un numar random intre 1 si 30
- numar_ghicit = None
- Folosind un while:
   - Utilizatorul alege un numar
   - Programul îi spune (in functie de caz):
        - Nr secret e mai mare
        - Nr secret e mai mic
        - Felicitari! Ai ghicit!
"""

# import random
#
#
# secret_number = random.randint(1, 30)
# numar_ghicit = None
#
# while numar_ghicit != secret_number:
#     numar_ghicit = int(input('alege un numar intre 1 si 30\n>>> '))
#     if numar_ghicit > secret_number:
#         print('Nr secret e mai mic')
#     elif numar_ghicit < secret_number:
#         print('Nr secret e mai mare')
#     else:
#         print('Felicitari ai ghicit!')

"""
2. Alege un numar de la tastatura si genereaza in consola o piramida
de numere, ca in exemplele de mai jos: 

Exemplu: 7

1
22
333
4444
55555
666666
7777777

Exemplu: 3

1
22
333
"""

# numar = int(input('Introduceti un numar\n>>> '))
#
# for i in range(1, numar+1):
#     #print("-" * 40)
#     print(str(i) * i)

"""
3. Se da lista:
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

Itereaza prin lista 2D si printeaza ‘Cifra curenta este x.’
(HINT: nested for - adică for in for)
"""
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
#
# for rand in tastatura_telefon:
#     for cifra in rand:
#         print(f'Cifra curenta este {cifra}')

"""
4. Se da lista:
numere = [23, -45, 79, -236, 200, -13]

Creeaza o lista care contine doar numerele negative.
"""

numere = [23, -45, 79, -236, 200, -13]

# Syntactic Sugar for lists
# numere_negative = []

# for numar in numere:
#     if numar < 0:
#         numere_negative.append(numar)
#
# print(sorted(numere_negative))

# List Comprehension
# numere_negative = [numar for numar in numere if numar < 0]
# numere_negative.sort()
# print(numere_negative)

# lista1 = [3, 8, 2, 5, 1]
# lista2 = lista1[:] # sau lista1.copy()
# lista2.sort()
# print(lista1)
# print(lista2)
# mutabilitatea listelor. variabilele lista1 si lista2 se refera la aceeasi lista

# Syntactic sugar for dicts
# patrate_perfecte = {}
#
# for number in range(1, 6):
#     patrate_perfecte[number] = number ** 2
#
# print(patrate_perfecte)

# Dict Comprehension
# patrate_perfecte = {number: number ** 2 for number in range(1, 6)}
# print(patrate_perfecte)

"""
5. 
Se da dictionarul:
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}

a. Cere utilizatorului cheia si valoarea pe care doreste sa o
adauge in dictionar. Foloseste metoda update().
b. Printeaza, pe rand, toate cheile din dictionar.
c. Printeaza, pe rand, toate valorile din dictionar.
"""

# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
# #a
# cheie = input('Introduceti cheia: ')
# valoare = input('Introduceti valoarea: ')
# persoana.update({cheie: valoare})
# print(persoana)

#b
# for cheia in persoana.keys():
#     print(f'Cheia este {cheia}')
#
# #c
# for valoarea in persoana.values():
#     print(f'Valoarea este {valoarea}')

#d sa printeze toate cheile pe o linie


# print(f'Cheile din dictionar sunt {", ".join(persoana.keys())}')
# print(f'Valoarile din dictionar sunt {", ".join(str(value) for value in persoana.values())}')

"""
6. Cere utilizatorului sa introduca de la tastatura un numar intreg pozitiv.
Scrie un program care verifica daca numarul este prim.
Afiseaza un mesaj sugestiv in consola in fiecare caz.
"""

def este_prim(numar):
    if numar <= 1:
        return False
    for i in range(2, int(numar ** 0.5) + 1):
        if numar % i == 0:
            return False

    return True


numar = int(input('Introdu nr intreg pozitiv: '))

if este_prim(numar):
    print('Numarul ales este prim')
else:
    print('Numarul nu este prim')



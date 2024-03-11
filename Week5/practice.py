"""
2. Functie care returneaza True daca un caracter x se gaseste intr-un string dat
si False daca nu se gaseste.
"""


# def fin_char(x: str, prop: str) -> bool:
#     # if x in prop.lower():
#     #     return True
#     # else:
#     #     return False
#     return x.lower() in prop.lower()
#
#
# print(fin_char('c', 'Carmen'))

"""
4. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Printeaza ‘nu am adaugat numarul in set. Acesta există deja’ + returneaza False
"""


# def number_in_set(x: int, setul: set):
#     if x not in setul:
#         setul.add(x)
#         print('am adaugat numarul nou in set')
#         return True # se incheie conditia si functia e evaluata
#     print('nu am adaugat numarul in set. Acesta există deja')
#     return False
#
#
# number_in_set(4, {4, 6, 77})
# number_in_set(4, {9, 6, 77})

"""
5. Functie care primeste o luna din an si returneaza cate zile are acea luna.
"""


# def zile_luna(luna: str) -> int:
#     luni = {
#        "ianuarie": 31, "februarie": 29, "martie": 31,
#        "aprilie": 30, "mai": 31, "iunie": 30,
#        "iulie": 31, "august": 31, "septembrie": 30,
#        "octombrie": 31, "noiembrie": 30, "decembrie": 31
#     }
#     # return luni[luna]
#     return luni.get(luna, 'nu exista')
#
# print(zile_luna('caa'))

"""
6. Functie calculator care sa returneze 4 valori: Suma, diferenta, inmulțirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""


# def calculator(x: int, y: int):
#     suma = x + y
#     dif = x - y
#     inmultirea = x * y
#     impartirea = x / y if y != 0 else 'nu e permis'
#     return suma, dif, inmultirea, impartirea
#
# print(calculator(40, 5))
# suma, dif, inmultirea, impartirea = calculator(40, 5)
# print('Suma: ', suma, 'Diferenta: ', dif, 'Inmultirea :', inmultirea, 'Impartirea :', impartirea, sep=', ')

"""
7. Functie care primeste o lista de cifre (adica doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

# def numaratoare_cifra(lista: list[int]) -> dict:
#     # rezultat = {}
#     # for i in range(10):
#     #     rezultat[i] = lista.count(i)
#     # return rezultat
#     return {i: lista.count(i) for i in range(10)}
#
#
# print(numaratoare_cifra([3, 6, 6, 33, 4]))

"""
9. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: dacă dam numarul 3, suma va fi 6 (0+1+2+3)
"""


# def suma_nr(x: int):
#     return sum(range(x + 1))
#
#
# print(suma_nr(3))


# def suma_nr(x: int) -> int:
#     suma = 0
#     for i in range(x + 1):
#         suma += i
#     return suma
#
# print(suma_nr(3))


"""
10. Functie care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""
#
# def nr_comune(lista1: list, lista2: list):
#     return set(lista1).intersection(set(lista2))
#
# listaa = [5, 6, 7]
# listaaa = [5, 6, 77, 34]
# print(nr_comune(listaa, listaaa))

"""
11. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
"""

# def reducere(x: float, procent: int):
#     if procent < 0 or procent > 100:
#         print('Reducere invalida')
#         return None
#     else:
#         reducerea = x * procent / 100
#         pre_final = x - reducerea
#         return pre_final
#
#
# pret = 100
# reducerea = 40
# print(f'Pretul final este de {reducere(pret, reducerea)}')


"""
12. Funcție care sa afiseze data si ora curenta din Romania.
(bonus: afiseaza si data si ora curenta din China)
"""

import datetime

def data_ora_curenta(tara: str):
    from datetime

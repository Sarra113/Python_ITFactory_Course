"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 8)
"""

"""
! Pentru toate exercițiile: Apelati functia de cel putin 2 ori cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.
"""

"""
1. Scrieti o functie care primeste ca parametru lungimea laturii
unui patrat si returneaza aria sa.
"""
# def arie_patrat(number: float):
#     """
#     Calcul arie patrat
#
#     Parametrii
#     ----------
#     number : float
#         Latura patratului
#     """
#     return number ** 2
#
# print(arie_patrat(7))

"""
2. Scrieti un subprogram care primeste ca parametru lungimea laturii unui patrat
si returneaza atat lungimea diagonalei, cat si perimetrul patratului.
"""


# def operatiuni_patrat(latura: float):
#     """
#     Calcul lungime diagonala si perimetru patrat
#
#     Parametrii
#     ----------
#     number : float
#         Latura patratului
#     """
#     return latura * 4, latura ** 0.5
#
#
# print(operatiuni_patrat(2))


"""
3. Scrieti o functie care primeste ca parametri de intrare lungimile celor doua catete
ale unui triunghi dreptunghic si returneaza lungimea ipotenuzei.
"""

# import math
#
# def lungime_ipotenuza(latura1: int, latura2: int):
#     """
#     Calculam lungimea ipotenuzei
#
#     Parametrii
#     ----------
#     latura1 : int
#     latura2: int
#         Catetele
#     """
#     ipotenuza = math.sqrt(latura1 ** 2 + latura2 ** 2)
#     return ipotenuza
#
# cateta1 = 23
# cateta2 = 10
# print(lungime_ipotenuza(cateta1, cateta2))


"""
4. Scrieti o functie care primeste 3 parametri de tip real, cu semnificatia
de lungimi pentru 3 segmente. 
Functia va returna 1 daca cele trei segmente pot forma un triunghi si 0, in caz contrar.
"""
# def triunghi_valid(s1: int, s2: int, s3: int):
#     """
#     Determinam daca segmentele pot fi triunghi
#
#     Params
#     ------
#     s1 : int
#     s2 : int
#     s3 : int
#         Segmentele
#
#     Returns
#     -------
#     1 daca e triunghi
#     0 daca nu e
#     """
#     if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
#         return 1
#     else:
#         return 0
#
# print(triunghi_valid(7, 10, 5))
# print(triunghi_valid(3, 1, 5))



"""
# 5. Functie care returneaza aria cercului.
# """
# import math
#
# def aria_cercului(raza: int):
#     return math.pi * raza **2
#
# print(aria_cercului(5))


"""
6. Functie fara return, primeste un string si printeaza pe ecran:
Numarul de caractere lower case este x
Numarul de caractere upper case este y 
"""
# def numara_felul_caracterelor(cuvant: str):
#     lower = sum(1 for char in cuvant if char.islower())
#     upper = sum(1 for char in cuvant if char.isupper())    # rezulta o lista de 1, in fct de nr de carac cerut
#     print(f'Numarul de carac lower este {lower}')
#     print(f'Numarul de carac lower este {upper}')
#
# numara_felul_caracterelor('Ana Maria')

"""
7. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.
"""
# def numere_pozitive(lista: list):
#     """
#     Determinam numerele pozitive din lista
#
#     Parameters
#     ----------
#     lista : list
#
#     Return
#     ------
#     numere pozitive
#     """
#     nr_pozitive = [number for number in lista if number > 0]
#     return nr_pozitive
#
#
# lista_mea = [0, 9, -8, 77, -27]
# print(numere_pozitive(lista_mea))


def make_list(n: int, l=None) -> list:
    if l is None:
        l = []
    for i in range(0, n):
        l.append(i)
    return l


print(make_list(3))
print(make_list(12, [1, 2, 3]))
print(make_list(5))



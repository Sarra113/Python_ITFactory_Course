"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 9)
"""

"""
Pentru toate exercitiile - apelati functia de cel putin 2 ori cu valori diferite
pentru a testa.
Daca funcția are return, printeaza raspunsul.                        
"""

"""
1. Functie care sa calculeze si sa returneze suma a doua numere.
"""
# def suma_numere(a: int, b: int) -> int:
#     return a + b
#
#
# print(suma_numere(2, 4))


"""
2. Functie care sa returneze TRUE daca un numar este par, FALSE pentru impar
"""

# def fel_numar(x: int) -> bool:
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(fel_numar(4))


"""
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu)
"""


# def numar_caracter(nume: str, prenume: str, nume_mijloc: str) -> int:
#     nume = nume + prenume + nume_mijloc
#     return len(nume)
#
# print(numar_caracter('Creta', 'Sarra', 'Alexandrina'))



"""
4. Scrieti o functie care returneaza prima cifra a unui numar natural.
De exemplu, daca parametrul efectiv este 127,
functia va returna 1.
"""
# def prima_cifra(numar: int) -> str:
#     for i in str(numar):
#         return i[0]
#
#
# print(prima_cifra(234))



"""
5. Sa se tipareasca toate numerele prime aflate intre doi intregi cititi.
Programul va folosi o functie care testeaza daca un numar este prim sau nu.
"""

# def este_prim(numar):
#     if numar <= 1:
#         return False
#     for i in range(2, int(numar ** 0.5) + 1):
#         if numar % i == 0:
#             return False
#
#     return True
#
# def nr_prime_intre(a, b):
#     for c in range(a, b + 1):
#         if este_prim(c):
#             print(c)
#
# nr_prime_intre(2, 20)




"""
6. Scrieti un program care tipareste numerele intregi gasite intre doua valori citite,
numere care se divid cu suma cifrelor lor.
Programul va utiliza o functie care returneaza suma cifrelor unui numar intreg primit ca parametru.
"""


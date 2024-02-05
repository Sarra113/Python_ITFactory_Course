"""
EXERCITII WORKSHOP (Sesiunea 5)
"""


# --------- LISTE ---------
"""
1. Avand 2 liste: [3, 1, 0, 2] si [6, 5, 4],
gaseste 2 variante prin care sa le unesti intr-o singura lista.
"""
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# print(lista3)
# lista3 = lista1.extend(lista2)





"""
2. 
a. Sorteaza lista generata la exercitiul 1, folosind functia built-in sorted().
Afiseaza lista. Ce observi?
b. Sorteaza lista generata la exercitiul 1 folosind o metoda ajutatoare de pe liste.
Afiseaza lista. Ce observi?
"""
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# # lista3.sort()
# # print(lista3)
# print(sorted(lista3))

"""
3. Folosind un if, verifica daca lista generata la exercitiul 1 este goala,
si afiseaza un mesaj corespunzator in functie de caz:
- Lista este goala
- Lista nu este goala
"""
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# if len(lista3) == 0:
#     print('Lista goala')
# else:
#     print('Lista nu e goala')


"""
4. Foloseste o functie (metoda ajutatoare de pe lista) care sa stearga lista de la exercitiul 1.
"""
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# lista3.clear()
# print(lista3)

"""
5. Copy paste la exercitiul 3.
Verifica inca o data. Acum ar trebui sa se afiseze ca lista este goala.
"""
# lista1 = [3, 1, 0, 2]
# lista2 = [6, 5, 4]
# lista3 = lista1 + lista2
# lista3.clear()
#
# if len(lista3) == 0:
#     print('Lista goala')
# else:
#     print('Lista nu e goala')


# --------- DICTIONARE ---------
"""
6. Se da dictionarul:
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

Foloseste o functie (metoda ajutatoare dictionar) ca sa afisezi numele elevilor (cheile)
"""
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# print(dict1.keys())

"""
7. Printeaza cei 3 elevi si notele lor.
Exemplu: "Ana a luat nota 8".
Doar nota o vei lua folosindu-te de cheie.
"""
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# # print(f"Ana a luat nota {dict1['Ana']}")
#
# lista_elevi = list(dict1.keys())
# print(lista_elevi)
#
# lista_note = list(dict1.values())
# print(lista_note)
# si apoi 3 printuri
"""
8. Dorel a facut contestatie si a primit 6.
a. Modifica nota lui Dorel in 6.
b. Printeaza nota dupa modificare.
"""
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# dict1['Dorel'] = 6
# print(dict1)

"""
9. Gigel se transfera din clasa.
a. Cauta o functie care sa il stearga. Afiseaza dictionarul dupa stergere
b. Vine un coleg nou, Ionica. Adauga-l in dictionar si pune-i nota 9.
c. Printeaza noii elevi.
"""
# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# # del dict1['Gigel']
# # dict1.update({'Ionica': 9})
# # print(dict1)
# dict1.pop('Gigel')
# print(dict1)

# --------- SETURI ---------
"""
10. Se dau urmatoarele seturi:
zile_sapt = {"luni", "marti", "mercuri", "joi", "vineri", "sambata", "duminica"}
weekend = {"sambata", "duminica"}

a. Adauga in zile_sapt "luni".
b. Afiseaza zile_sapt. Ce observi?
"""
# zile_sapt = {"luni", "marti", "mercuri", "joi", "vineri", "sambata", "duminica"}
# weekend = {"sambata", "duminica"}
# zile_sapt.add("luni")
# print(zile_sapt)
# setul = {1, 2, 5, 4, 9, 8}
# print(setul)

"""
11. Folosind seturile de la exercitiul 10:
a. Foloseste un if si verifica:
 - daca weekend este un subset al zilelor din saptamana
 - daca weekend nu este un subset al zilelor din saptamana
Afiseaza un mesaj sugestiv in fiecare caz.
"""
# zile_sapt = {"luni", "marti", "mercuri", "joi", "vineri", "sambata", "duminica"}
# weekend = {"sambata", "duminica"}
# subset = weekend.issubset(zile_sapt)
# print(subset)   # returns true daca primul e un subset din al doilea

'''   SAU     '''
# if subset:
#     print(True)
# else:
#     print(False)

'''   SAU    '''
# if weekend <= zile_sapt:  # inseamna ca prima multime e inclusa in cea de-a doua; operator subset
#     print('Weekend este un subset al zile sapt')
# else:
#     print('Weekend nu este un subset')
#
# if zile_sapt >= weekend:
#     print('Zile sapt este un superset al weekend. Adica include weekend')
# else:
#     print(False)

"""
12. Folosind seturile de la exercitiul 10, afiseaza diferentele dintre cele 2 seturi.
"""
# zile_sapt = {"luni", "marti", "mercuri", "joi", "vineri", "sambata", "duminica"}
# weekend = {"sambata", "duminica"}
# difference = zile_sapt.difference(weekend)
# print(difference)

"""
13. Folosind seturile de la exercitiul 10, afiseaza intersectia elementelor dintre cele 2 seturi
"""
# zile_sapt = {"luni", "marti", "mercuri", "joi", "vineri", "sambata", "duminica"}
# weekend = {"sambata", "duminica"}
# intersectie = zile_sapt.intersection(weekend)
# print(intersectie)

# --------- EXERCITII RECOMANDATE - STUDIU INDIVIDUAL ---------

"""
1. Revizualizeaza sesiunile de pana acum si ia notite in caz ca ti-a scapat ceva.
"""


"""
2. Vizualizeaza din cursul PRIMII PASI IN PROGRAMARE sectiunile de mai jos:
- Structuri de date
- Flow Control
"""


"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 7)
"""


"""
1. Modernizează parcul de mașini:

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Crează o listă goală, masini_vechi.
Iterează prin mașini.
Când găsesti Lăstun sau Trabant:
Salvează aceste mașini în masini_vechi.
Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
Printează Modele vechi: x.
Modele noi: x.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# for masina in masini:
#     if masina == 'Lastun' or masina == 'Trabant':
#         masini_vechi.append(masina)
#         masini.remove(masina)
#
# masini.append('Tesla')
# print(masini_vechi)
# print(masini)

 #SAU
# for index, masina in enumerate(masini):
#     if masina == 'Lastun' or masina == 'Trabant':
#         masini_vechi.append(masina)
#         masini[index] = 'Tesla'
#
# print(masini_vechi)
# print(masini)





"""
2. Având dict:
pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}

Vine un client cu un buget de 15000 euro.

Prezintă doar mașinile care se încadrează în acest buget.
TIP: Cauta pe net ce e dict.items() si vezi cum poti sa il folosesti

Iterează prin dict.items() și accesează mașina și prețul.
Printează Pentru un buget de sub 15000 euro puteți alege mașină Lastun
"""
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# for masina, pret in pret_masini.items():
#     if pret < 15000:
#         print(f'Pentru un buget de sub 15000 euro puteți alege masina {masina}')

"""
3. Având lista:
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numar_aparitii = 0
#
# for numar in numere:
#     if numar == 3:
#         numar_aparitii += 1   # cand nr = 3 atunci nr aparitii creste cu 1
# print(f'Numarul 3 apare de {numar_aparitii} ori in lista')



"""
4. Aceeași listă:
Iterează prin ea
Calculează și afișează suma numerelor (nu ai voie să folosești sum).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
#
# for numar in numere:
#     suma += numar
# print(suma)



"""
5. Aceeași listă:
Iterează prin ea.
Afișază cel mai mare număr (nu ai voie să folosești max).
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# nr_mare = 0
#
# for numar in numere:
#     if numar > nr_mare:
#         nr_mare = numar
# print(nr_mare)

"""
6. Aceeași listă:
Iterează prin ea.
Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3
Afișază noua listă.
"""
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# neg = 0
# numere_negative = []
# for numar in numere:
#     if numar > 0:
#         neg = numar #???
#         numere_negative.append(-numar)
# print(numere_negative)

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# for numar in range(len(numere)):
#     if numere[numar] > 0:
#         numere[numar] = -numere[numar]
#
# print("Noua lista:", numere)

"""
7.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere 
Populează corect celelalte liste
Afișează cele 4 liste la final
"""
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     elif numar % 2 == 1:
#         numere_impare.append(numar)
#     elif numar > 0:
#         numere_pozitive.append(numar)
#     elif numar < 0:
#         numere_negative.append(numar)
#
# print(numere_pare)
# print(numere_impare)
# print(numere_negative)
# print(numere_pozitive)

# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     elif numar % 2 != 0:
#         numere_impare.append(numar)
# for numar in alte_numere:
#     if numar > 0:
#         numere_pozitive.append(numar)
#     elif numar < 0:
#         numere_negative.append(numar)
#
# print(numere_impare)
# print(numere_pare)
# print(numere_pozitive)
# print(numere_negative)


"""
Exerciții Recomandate - STUDIU INDIVIDUAL                                       .

1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.

2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
- Structuri de date
- Flow Control
"""

"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 6)
"""


"""
1. Avand lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Foloseste un for ca sa interezi prin toata lista si sa afisezi 'Masina mea preferata este x':

a. Fa acelasi lucru cu un for each.
b. Fa acelasi lucru cu un while.
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masina_pref = input('Introdu masina preferata: ')
#
# for masina in masini:
#     if masina.lower() == masina_pref:
#         print(f'Masina mea pref este {masina}')
#         break
# else:
#     print('Masina mea pref nu e in lista')

# a.
# for index in range(len(masini)):
#     print(f'Masina mea preferata este {masini[index]}')

# b.

# for masina in masini:
#     print(f'Masina mea preferata este {masina}')

# c.

# index = 0
# while index < len(masini): # daca as pune si egal si ajunge la index 9, nu imi va da nimic pentru ca ultimul e index 8
#     print(f'Masina mea preferata este {masini[index]}')
#     index += 1


"""
2. Folosind aceeasi lista ca la exercitiul 1:

- foloseste un for else:
    - in for: modifica elementele din lista astfel incat sa fie scrise cu majuscule,
    exceptand primul si ultimul.
    - in else: printeaza lista
"""
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# elementul din lista trebuie accesat prin index si actualizat ca upper

# for index, masina in enumerate(masini):
#     if index != 0 and index != len(masini) - 1:
#         masini[index] = masina.upper()
# else:
#     print(masini)
#Funcția enumerate() este utilă atunci când trebuie să iterăm printr-o secvență (cum ar fi o listă)
# și să obținem atât valoarea elementului, cât și indexul său în acea secvență.

# '''     Varianta 2     '''
#
for masina in masini[1:-1]:
    masini[masini.index(masina)] = masina.upper()   # medota index da indexul fiecarui element
else:
    print(masini)



"""
3. Folosind aceeasi lista ca la exercitiul 1:
Vine un cumparator care doreste sa cumpere Mercedes.
Itereaza prin lista cu masini prin modalitatea aleasa de tine.
Daca masina e 'Mercedes':
- printeaza 'Am gasit masina dorita de dvs'
- iesi din ciclu folosind un cuvant cheie care face acest lucru
altfel:
- printeaza 'Am gasit masina X. Mai cautam.'
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for masina in masini:
#     if masina == 'Mercedes':
#         print('Am gasit masina dorita de dvs')
#         break
#     else:
#         print(f'Am gasit masina {masina}. Mai cautam')



"""
4. Folosind aceeasi lista ca la exercitiul 1:
Vine un cumparator bogat dar indecis.
Ii vom prezenta toate masinile, cu exceptia Trabant si Lastun.
Daca masina e Trabant sau Lastun:
- Foloseste un cuvant cheie sa dea skip la ce urmeaza (nu trebuie else)
- Printeaza "S-ar putea sa va placa masina X".
"""
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     print(f'S-ar putea sa va placa masina {masina}')
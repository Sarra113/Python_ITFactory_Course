# lista_cumparaturi = ['rosii', 'paine', 'lapte']
# print(lista_cumparaturi)
#
# lista_cumparaturi.remove('rosii')
# print(lista_cumparaturi)
# lista_cumparaturi.pop()
# print(lista_cumparaturi)
#
# lista_cumparaturi.append('oua')  # adauga la final
# print(lista_cumparaturi)
#
# lista_cumparaturi.insert(1, 'ceapa')
# print(lista_cumparaturi)
#
# lista_cumparaturi[2] = 'peste'
# print(lista_cumparaturi)

# EX 1.
# lista1 = ['mere', 'pere', 'afine']
# print(lista1[1])
# print(len(lista1))

# EX 2.
# filme_pref = ['Eternal Sunshine', 'Harry Potter', 'The Truman Show']
# print(filme_pref[::-1])  # inversare lista!
#
# if len(filme_pref) == 0:
#     print('lista goala')
# else:
#     print('Lista nu e goala')

# EX 3.
# cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
# print(type(cifre))
# cifre.sort()
# print(cifre)   # de ce nu se poate sorta direct in print?
#
# if 9 in cifre:
#     print('9 este in lista')
# else:
#     print('9 nu este in cifre')
#
# print(cifre.count(7))
# cifre.reverse()
# print(cifre)

# DICTIONAR

# contacte = {
#     'Ana': '0722345678',
#     'Marius': '0721549888',
#     'Maria': '0765332967'}
#
# print(contacte['Ana'])
#
# print(contacte.get('Andrei', 'Contact inexistent'))
# print(contacte)
#
# contacte['Sarra'] = '0938373'
# print(contacte)
# contacte.update({'car': True})
# print(contacte)
#
# contacte['car'] = False
# contacte.update({'Sarra': 26})  # metoda update are ca param un nou dictionar
# print(contacte)
#
# del contacte['Sarra']
# contacte.pop('car')
# print(contacte)
#
# contacte.update({'orase': ['Bn', 'Cj']})
# print(contacte)
# oras = contacte['orase']
# print(oras)
# print(oras[1])
# # SAU
# print(contacte['orase'][1])

# EX 1
# student1 = {
#     'nume': 'Pop',
#     'prenume': 'Andrei',
#     'varsta': 21,
#     'an studiu': 2,
#     'facultate': 'drept',
#     'medie': 8.75
# }
#
# print(len(student1))
# print(student1['nume'])
# student1.update({'tara': 'Ro'})
# print(student1)
# print(student1.get('oras', 'nu stim'))

# nume = input('nume: ')
# ingrediente = input('ingrediente: ')
# timp = input('timp: ')
#
# reteta = {
#     'nume': nume,
#     'ingrediente': ingrediente,
#     'timp': timp
# }
# print(reteta)
# reteta['nume'] = nume.upper()
# print(reteta)

# contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
# contacte['Aurel'] = '0765166277'
# contacte.update({'Mihai': '0765388175'})
# contacte.pop('Maria')
# print(contacte)
# print(contacte.get('Mihaela', 'nu avem'))

# SETURI

# set = {'para', 'mar', 'afine'}
# print(set)
# # nu putem schimba elem pt ca nu are pozitie fixa
# set.add('mar')
# print(set)
# set.add('lamaie')
# print(set)
# set.pop()
# print(set)

'''  Exercitii  '''

# my_set = {1, 2, 3, 4}
# my_set.add(5)
# my_set.add(6)
# my_set.add(1)
# print(my_set)
# my_set.pop()
# print(my_set)
# my_set.remove(4)
# print(my_set)
# my_set.pop()   # daca sunt numere in set isi pastreaza ordinea?
# print(my_set)  # pop l-a sters mereu pe primul




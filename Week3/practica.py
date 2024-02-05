"""
Ex recap 1:
a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume,
ingrediente, timp preparare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""

# nume = input('Introdu nume: ')
# ingrediente = input('Introdu ingrediente: ')
# timp = input('Introdu timpul: ')
#
# dictionarul = {'numele': nume, 'ingredintele': ingrediente, 'timp': timp}
# print(dictionarul)
# dictionarul.update({'numele': nume.upper()})
# print(dictionarul)


# EX 1:
# x = -5
# while x < 0:
#     print(x)
#     x += 1
# else:
#     print('S-au afisat toate nr negative')

"""
EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""

# while True:               # solicitam utilizatorului continuu sa introduca note
#     x = float(input('Introdu nota: '))
#     y = float(input('Introdu nota: '))
#     z = float(input('Introdu nota: '))
#     media = (x + y + z) / 3
#     if x >= 0 and y >= 0 and z >= 0:
#         print(f'Media artmetica este: {media}')
#     elif x <= -1 or y <= -1 or z <= -1:
#         print('Numere incorecte')
#         break

x = float(input('Introdu nota: '))
y = float(input('Introdu nota: '))
z = float(input('Introdu nota: '))
media = (x + y + z) / 3

while x >= 0 and y >= 0 and z >= 0:
    print(f'Media artmetica este: {media}')
    x = float(input('Introdu nota: '))
    y = float(input('Introdu nota: '))
    z = float(input('Introdu nota: '))
    media = (x + y + z) / 3
else:
    print('Note incorecte')



# nr = 25
#
# while True:
#     x = int(input('Introdu nr: '))
#     if x != nr:
#         print('Mai incearca')
#     else:
#         print('Felicitari')
#         break

# Atâta timp cât condiția True este evaluată ca fiind adevărată,
# blocul de cod asociat cu instrucțiunea while va fi executat în mod repetat.
# while true va rula mereu pt ca conditia true e evaluata mereu ca adevarata
# deci nu exista nicio conditie explicita ca sa opresca - ruleaza pana la break

# username = input("Introduceti numele de utilizator: ")
# password = input("Introduceti parola: ")
#
# while len(username) < 6 and len(password) < 6:
#     print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
#     username = input("Introduceti numele de utilizator: ")
#     password = input("Introduceti parola: ")
# print("Autentificare reusita")     # am iesit din while cu indentarea

# variabilele sunt dublate, o data pt a incepe codul (pt a le putea defini in while) si apoi
# ca sa iti ceara din nou user si parola in interiorul lui while

'''   Varianta 2     '''

# while True:
#     username = input("Introduceti numele de utilizator: ")
#     password = input("Introduceti parola: ")
#     if len(username) < 6 and len(password) < 6:
#         print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
#     else:
#         print('Autentificare reusita')
#         break


'''   Joc de ghicit numarul      '''
# import random
#
# secret_number = random.randint(1, 10)
#
# guessed = False
# # while continua pana cand conditia este indeplinita. ruleaza cat este falsa
# while not guessed:
#     guess_number = int(input("Alege un numar de la 1 la 10: "))
#     if guess_number == secret_number:
#         print("Felicitari! Ai ghicit!")
#         guessed = True  # conditia de iesire
#     elif guess_number < secret_number:
#         print("Numarul este prea mic. Incercati din nou.")
#     else:
#         print("Numarul este prea mare. Incercati din nou.")

# Cautarea unui element intr-o lista

# numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
#
# search_value = int(input("Ce numar cautati? "))
#
# index = 0
# while index < len(numbers):
#     if numbers[index] == search_value:
#         print(f"Valoarea a fost gasita la indexul: {index}")
#         break
#     index += 1
# else:
#     print("Valoarea nu a fost gasita in lista!")

# daca nu se exec if nu se exec nici print, nici break si trece la incrementare
# else se executa cand epuizam while - nu mai indeplineste conditia si index >10  si nu dam de break

# data = list(range(1, 9, 2))
# print(data)

"""
EX3: Afiseaza toate numerele pare pana la 10.
"""

# for x in range(11):
#     print(x)
'''  
EX4: Se da lista:
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
Afiseaza toate elementele din lista accesandu-le dupa index.
'''
# legume = ['spanac', 'castraveti', 'conopida', 'ardei']
# for index in range(len(legume)):
#     print(legume[index])

# culori = ["rosu", "albastru", "galben", "mov"]
# culoare_pref = input('Culoarea mea pref este: ')
#
# for culoare in culori:
#     if culoare == culoare_pref:
#         print(f"Culoarea mea preferata este {culoare}")
#         break
# else:
#     print('Culoarea pref nu este in lista')

'''
EX5:
2. Se da lista:
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
Sa se afiseze toate produsele care au pretul mai mare de 5 lei.
'''
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
# for index in range(len(produse)):
#     if 'pret' in produse[index] and produse[index]['pret'] > 5:
#         print(produse[index]['nume produs'])

# Varianta 2

# for produs in produse:
#     if 'pret' in produs and produs['pret'] > 5:
#         print(produs['nume produs'])

"""
EX6: Sa se afiseze primul numar par din intervalul 1 - 10
(inclusiv capetele de interval).
"""
# for x in range(1, 11):
#     if x % 2 == 0:
#         print(f'Primul nr par este numarul {x}')
#     # if x == 2:
#         break

"""
EX7:
Se da lista:
participanti = ['Maria', 'Ionela', 'Marius', 'Paul']
Folosind un ciclu repetitiv, cauta daca 'Marius' se afla in lista de participanti.
Dupa ce l-ai gasit intrerupe ciclul repetitiv.
"""
# participanti = ['Maria', 'Ionela', 'Marius', 'Paul']
#
# for participant in participanti:
#     # if 'Marius' in participanti:
#     if participant == 'Marius':
#         print('Marius este in lista de participanti')
#         break
# else:
#     print('Marius nu este in lista de participanti')

"""
EX8: 1. Se da lista:
numere = [1, 2, 3, 4, 5, 6, 7]
Afiseaza toate elementele din lista numere,
cu exceptia numerelor 3 si 5
"""
# numere = [1, 2, 3, 4, 5, 6, 7]
# for nr in numere:
#     if nr == 3 or nr == 5:
#         continue
#     print(nr)



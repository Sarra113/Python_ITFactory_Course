"""
Sesiunea 5 - Exercitii cu Trainer
"""


"""
1. Lista de cumparaturi:

Se citeste de la tastatura o lista de cumparaturi. 
Utilizatorul introduce lista de cumparaturi ca un string,
cu alimentele separate prin virgula,
ATENTIE: fara spatii
Exemplu:rosii,castraveti,branza,oua

a. Sa se transforme string-ul citit de la tastatura intr-o lista. (vezi metode ajutatoare string).
b. Sorteaza lista de cumparaturi si printeaza lista sortata.
c. Adauga un aliment nou in lista de cumparaturi.
d. Sterge un aliment din lista de cumparaturi.
e. Modifica elementul de la pozitia 0 din lista.
f. Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
Daca nu, afiseaza mesajul "Iti recomandam rosiile de asemenea".
"""
# a. Transformarea sirului de caractere intr-o lista
# lista_cumparaturi = input('Introduceti alimente\n>>> ')  # new line
# lista_cumparaturi = lista_cumparaturi.split(',')
# print(lista_cumparaturi)
#
# # b. Sortarea si afisarea listei
# lista_cumparaturi.sort()
# print(f'Lista de cumparaturi sortata: {lista_cumparaturi}')
#
# # c. Adaugarea unui aliment nou la lista
# aliment_nou = input('Introduceti aliment nou: ')
# lista_cumparaturi.append(aliment_nou)
# print(f'Lista a fost actualizata: {lista_cumparaturi}')
#
# # d. Stergerea unui aliment din lista
# aliment_de_sters = input('Introduceti un aliment de sters: ')
# if aliment_de_sters in lista_cumparaturi:
#     lista_cumparaturi.remove(aliment_de_sters)
#     print('Alimentul a fost sters din lista')
# else:
#     print('Alimentul nu este in lista de cumparaturi')
#
# # e. Modificarea elementului de la pozitia 0
# lista_cumparaturi[0] = 'iaurt'
# print(lista_cumparaturi)
#
# # f. Verifica daca lista contine rosii
# if 'rosii' in lista_cumparaturi:
#     print('Aliment sanatos')
# else:
#     print("Iti recomandam rosiile de asemenea")



"""
2. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
Converteste lista la string si afiseaza string-ul.
A se vedea metoda join().
"""
# fructe = ['capsuni', 'mere', 'lamai']
# fructe_string = ', '.join(fructe)
# print(fructe_string)
"""
3. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
Afiseaza elementul cu valoarea maxima din string. (google- functia max())
"""
# lista_numere = [1, 2, 3, 4, 56, 22, 5]
# nr_max = max(lista_numere)
# print(nr_max)

"""
4. Se da lista preturi = [12.3, 34.5, 22].
Calculeaza suma elementelor din lista preturi. (google - functia sum())
"""
# preturi = [12.3, 34.5, 22]
# suma = sum(preturi)
# print(f'Suma preturilor este {suma}')

"""
5. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza valoarea cheii city.
b. Kelly a fost promovata. Salariul ei este acum de 10000 lei. Fa modificarea si in dictionar.
c. Sterge varsta din dictionar.
d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
"""
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # a. Afisam valoare cheii city
# print(sample_dict['city'])
#
# # b. Actualizarea salariului lui Kelly
# sample_dict['salary'] = 10000
# print(f"Salariul actualizat este {sample_dict['salary']}")
#
# # c. Stergem varsta din dictionar
# del sample_dict['age']
# print(f'Dictionarul dupa stergerea varstei: {sample_dict}')
#
# # d. Adaugarea unei noi perechi cheie valoare
# sample_dict['emplyment_date'] = '2023'
# print(sample_dict)
#
# # e. Cautarea unei chei in dict
# if 'country' not in sample_dict:
#     sample_dict['country'] = 'USA'
# print(f'Dictionar final: {sample_dict}')




"""
6. Concatenarea a doua dictionare

Se dau doua dictioanare:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

Sa se concateneze cele doua dictionare folosind metoda update().
Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
perechi cheie:valoare in dictionar.
"""
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)


"""
7. Se da urmatoarea lista cu dictionare:
lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
a. Adauga perechea {'c':'3'} in primul dictionar din lista.
b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
c. Aduaga un nou dictionar ca element in lista, la indexul 1.
d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
# """
# lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
#
# # a. Adaugare pereche in lista
# lista[0]['c'] = lista[1]['c']
# del lista[1]['c']
# print(lista)
#
# # b. Adaugare dict nou in lista
# nou_dict = {'g': 7, 'h': 8}
# lista.append(nou_dict)
# print(lista)
#
# # c. Adaugare nou dict la lista
# nou_dict2 = {'i': 9, 'j': 10}
# lista.insert(1, nou_dict2)
# print(lista)
#
# # d. Verificam dacac in al doilea dict
# if 'c' in lista[2]:
#     print('Cheia c se gaseste in al doilea dictionar')
# else:
#     print('Cheia c nu este prezenta in al doilea dictionar')


my_dict = {}
my_set = set{}
date_reteta = input("Introdu date")
"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 4)
"""


"""
1. 
a. Declara o lista, numita note_muzicale, in care sa pui: do re mi etc până la do.
b. Afiseaz-o.
c. Inverseaza ordinea folosind slicing si suprascrie aceasta lista.
d. Printeaza varianta actuala (inversata).
e. Pe lista de la punctul d aplica o metoda care banuiesti ca face acelasi lucru,
adica sa ii inverseze ordinea.
Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat.
f. Printeaza varianta actuala a listei. (Practic ai ajuns inapoi la varianta initiala.)

CONCLUZII:
- slicing e temporar. Daca vrei sa pastrezi noua varianta, va trebui sa suprascrii
lista sau sa o salvezi intr-o lista noua.
- Metoda gasita de tine face suprascrierea automat si permanentizeaza aceste modificări.
Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
"""
lista = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(lista)
lista = lista[::-1]
print(lista)
lista.reverse()
print(lista)   #cu metoda nu trebuie suprascriere


"""
2. Folosind lista de la exercitiul 1, afiseaza de cate ori apare ‘do’.
"""
print(lista.count('do'))

"""
3. Transforma lista de la exercitiul 1 intr-o tupla.
Incearca sa adaugi o nota noua.
"""
tuplu = ('do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do')


"""
4. Declara un dictionar cu notele muzicale de la exercitiul 1.
Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. 
Afiseaza-l.
"""
dictionar = {
    'do': 2,
    're': 1,
    'mi': 1,
    'fa': 1,
    'sol': 1,
    'la': 1,
    'si': 1
}

print(dictionar)
"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 15)
"""


"""
1. 
a. Creeaza un fisier txt, numit 'persons.txt' care contine pe fiecare linie,
un nume si o varsta.
b. Implementeaza o clasa Person care sa reprezinte o persoana
cu atributele nume si varsta.
c. Cititi datele din fisier si creati obiecte de tip Person
(pune toate obiectele create intr-o lista).
d. Afiseaza numele si varsta fiecarei persoane.
"""
with open('persons.txt', 'w') as file:
    file.write('Ana 23\n')
    file.write('Matei 27\n')
    file.write('Maria 30\n')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


persons = []
with open('persons.txt', 'r') as file:
    for line in file:
        name, age = line.strip().split()
        persons.append(Person(name, age))

for person in persons:
    print(f'Nume: {person.name}, Varsta: {person.age}')


"""
2. 
a. Creeaza un fisier JSON, cu informatii despre carti:
- practic va fi o lista, cu dictionare
- in fiecare dictionar vom avea informatiile despre o carte
- pentru fiecare carte vom avea urmatoarele informatii: titlu, autor, an

b. Implementeaza o clasa Book care sa reprezinte o carte (atribute: titlu, autor, an)
c. Citeste datele din fisierul JSON si creaza obiecte de tip Book
(pune toate obiectele create intr-o lista)
d. Afiseaza numele cartilor publicate dupa un anumit an.
"""






"""
3. 
a. Creati un fisier CSV cu informatii despre facturi (id, serie, numar, client, suma, status
(IMPORTANT: statusul poate sa fie "emisa" sau "incasata"
Asigura-te ca ai in fisierul tau CSV mai multe linii pentru acelasi client cu status diferit.
b. Implementeaza o clasa Factura care sa reprezinte o factura (atribute: id, serie, numar, client, suma, status)
c. Citeste datele din fisierul CSV si creeaza obiecte din clasa de tip Factura
(pune toate obiectele create intr-o lista)
d. Afiseaza informatiile despre facturile emise de un anumit client si doar cele cu statusul "incasata"
e. Avand in vedere facturile prelucrate la punctul d, afiseaza suma totala incasata de clientul respectiv.
"""


"""
4. 
a. Creati un fisier JSON care contine informatii despre produse (id, nume, cantitate, pret (per buc)), nume_furnizor
b. Creati o clasa care reprezinta un produs, numita Product (cu atributele: id, nume, cantitate, pret, nume_furnizor)
c. Citeste datele din fisierul JSON si creeaza obiecte din clasa de tip Product
(pune toate obiectele create intr-o lista)
d. Construieste o lista cu produsele care nu mai sunt in stoc.
e. Construieste o lista cu produsele care sunt in stoc si au un anumit furnizor.
"""

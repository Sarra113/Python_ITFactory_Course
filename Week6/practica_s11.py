"""
Defineste clasa TodoList.
Atribute in constructor:
- todo: dict, cheia e numele taskului, valoarea e descrierea
La început nu avem taskuri, dict e gol.

- Metode:
1. adauga_task(nume, descriere) - se va adauga in dict
2. finalizează_task(nume) - se va sterge din dict
3. afișează_todo_list() - doar cheile
4. afișează_detalii_suplimentare(nume_task)
- în funcție de numele taskului, printăm detalii suplimentare.
- Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l
adauge.
    Dacă acesta răspunde nu - la revedere
    Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii
în dict
"""

class TodoList:
    def __init__(self):
        self.dictionar = {}

    def adauda_task(self, nume: str, descriere: str):
        self.dictionar[nume] = 'descriere'

    def finalizeaza_task(self, nume:str):
        del self.dictionar[nume]

    def afiseaza_lista(self):
        print(self.dictionar.keys())

#     def detalii_suplimentare(self, nume:str):
#         if nume in self.dictionar:
#             print(f"Detalii task: {self.dictionar[nume]}")
#         else:
#             raspuns = input(f'Task-ul {nume} nu exista. Doriti sa il adaugati?')
#             if raspuns.lower() == 'da':
#                 detalii_task = input('Introduceti detalii task: ')
#                 self.adauda_task(nume, detalii_task)
#             elif raspuns.lower() == 'nu':
#                 print('La revedere')
#
#
# lista_mea = TodoList()
# lista_mea.afiseaza_lista()
# lista_mea.adauda_task('masa', 'curata masa')
# lista_mea.afiseaza_lista()
# lista_mea.detalii_suplimentare('masa')
# lista_mea.detalii_suplimentare('avion')


"""
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""

# class Persoana:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#
#     def descrie(self):
#         print(f'Persoana {self.nume} are {self.varsta} ani.')
#
#
#  # Pentru a adauga proprietati noi:
#     # 1. Extindem lista de parametrii pe care
#     # metoda __init__ ii poate lua.
#     # 2. Apelam __init__-ul din clasa parinte, folosindu-ne de
#     # super(), cu parametrii necesari pentru clasa parinte.
#
# class Angajat(Persoana):
#     def __init__(self, nume, varsta, salariu, post):
#         super().__init__(nume, varsta)
#         self.salariu = salariu
#         self.post = post
#
#     # Pentru a extinde metode din clasa parinte:
#     # Facem apel la metoda din clasa parinte folosind super()
#
#     def afiseaza_salariu(self):
#         return self.salariu
#
#     def descrie(self):
#         super().descrie()
#         print(f'Este angajata ca {self.post} si castiga {self.salariu}')
#
#
# om = Persoana('Sarra', 26)
# print(om.nume)
# print(om.varsta)
# om.descrie()
#
# angajatul = Angajat('Sarra', 26, 4000, 'QA')
# angajatul.descrie()
# print(angajatul.salariu)
# print(angajatul.afiseaza_salariu())
# angajatul.descrie()


"""
EX2: POLIMORFISM

a. Defineste o clasa Pasare care implementeaza metoda 
zboara.
In metoda zboara, afiseaza mesajul 'Majoritatea pasarilor
pot zbura.'

b. Defineste o clasa Strut, care mosteneste din clasa 
Pasare.
Defineste metoda zboara, si afiseaza mesajul 
'Strutii nu pot zbura."
(Nu extindem metoda din clasa de baza, 
ci o suprascriem -> OVERRIDING)

c. Defineste clasa Rata, care mosteneste din clasa Pasare.
Defineste metoda zboara, si afiseaza mesajul 
"Ratele pot zbura."

d. Instantiaza cele 3 clase si apeleaza metoda zboara
pe fiecare obiect.
POLIMORFISM => aceeasi metoda (acelasi nume) -> 
comportament diferit.
"""

# class Pasare:
#     def zboara(self):
#         print('Majoritatea pasarilor pot zbura')
#
#
# class Strut(Pasare):
#     def zboara(self):
#         print('Strutii nu pot zbura')
#
# class Rata(Pasare):
#     def zboara(self):
#         print('Ratele pot zbura')
#
#
# porumbel = Pasare()
# strutul = Strut()
# donald = Rata()
# porumbel.zboara()
# strutul.zboara()
# donald.zboara()

"""
EX3: ABSTRACTIZARE
a. Defineste interfata Car. Aceasta va avea o metoda
abstracta numita car_model.

b. Defineste clasele Tesla si BMW, care implementeaza
interfata Car.
Metoda car_model trebuie sa afiseze un mesaj legat
de modelul masinii.

Instantiaza clasele Tesla si BMW si invoca metoda 
car_model pe fiecare din acestea.
"""
#
# from abc import ABC, abstractmethod
#
# class Car(ABC):
#
#     @abstractmethod
#     def car_model(self):
#         pass
#
# class Tesla(Car):
#     def car_model(self):
#         print('Modelul masinii este Tesla')
#
# class BMW(Car):
#     def car_model(self):
#         print('Modelul masinii este BMW')
#
# m1 = Tesla()
# m2 = BMW()
# m1.car_model()
# m2.car_model()


# class CarPy:
#
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.getter
#     def color(self):
#         print(f"Getter: Culoarea este {self.__color}")
#         return self.__color
#
#     @color.setter
#     def color(self, culoare_noua):
#         print(f"Setter: Noua culoare este {culoare_noua}")
#         self.__color = culoare_noua
#
#     @color.deleter
#     def color(self):
#         print(f"Deleter: Am sters culoarea")
#         self.__color = None
#
#
# car2 = CarPy('gray')
# print(car2.color)
#
# car2.color = 'red'
# print(car2.color)
#
# del car2.color
# print(car2.color)

"""
EX5: Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""

from abc import abstractmethod


class AbstractVideo:

    @abstractmethod
    def show_details(self):
        pass

    def play(self):
        print('Video is playing')

"""
EX6: Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""


class Videoclip(AbstractVideo):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_details(self):
        print(f'{self.title} has a duration of {self.duration} minutes')

"""
EX7:
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""


class Movie(Videoclip):

    def __init__(self, title, duration, genre, director, actors: list):
        super().__init__(title, duration)
        self.genre = genre
        self.__director = director
        self.actors = actors

    def show_details(self):
        super().show_details()
        print(f'Is directed by {self.__director} and the actors are {self.actors}.')

    @property
    def director(self):
        return self.__director

    @director.getter
    def director(self):
        print(f'Directorul este {self.__director}')
        return self.__director

    @director.setter
    def director(self, new_director):
        print(f'Directorul nou este {new_director}')
        self.__director = new_director

    @director.deleter
    def director(self):
        self.__director = None

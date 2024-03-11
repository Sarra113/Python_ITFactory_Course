"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 10)
"""


"""
1.Implementeaza clasa Cerc:
- atribute: rază, culoare
- constructor pentru ambele atribute
- metode:
    - descrie_cerc() - va PRINTA culoarea și raza
    - aria() - va RETURNA aria 
    - diametru() 
    - circumferinta()
"""

# class Cerc:
#     def __init__(self, raza: int, culoare: str):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self):
#         print(f'Culoarea este {self.culoare} si raza este {self.raza}')
#
#     def aria(self):
#         pi = 3.14
#         aria_c = 3.14 * self.raza ** 2
#         return f"Aria este {aria_c}"
#
#     def diametru(self):
#         diamentrul = 2 * self.raza
#         return f'Diamentrul este {diamentrul}'
#
#     def circumferinta(self):
#         pi = 3.14
#         return 2 * 3.14 ** 2
#
#
# cercul = Cerc(6, 'rosu')
# print(cercul.descriere_cerc())
# print(cercul.aria())
# print(cercul.diametru())
# print(cercul.circumferinta())


"""
2. Implementeaza clasa Dreptunghi:
- atribute: lungime, lățime, culoare
- constructor pentru toate atributele
- metode:
    - descrie()
    - aria()
    - perimetrul()
    - schimbă_culoarea(noua_culoare):
        - această metodă nu returneaza nimic. 
        - Ea va lua ca parametru o noua culoare si va suprascrie atributul self.culoare.
        - Poti verifica schimbarea culorii prin apelarea metodei descrie().
"""

class Dreptunghi:
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        return f'Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}'

    def aria(self):
        return self.lungime * self.latime

    def perimetrul(self):
        return 2 * self.lungime + 2 * self.latime

    def schimba_culoarea(self, noua_culoare: str):
        self.culoare = noua_culoare


dreptunghiul_meu = Dreptunghi(12, 6, 'rosu')

print(dreptunghiul_meu.descriere())
dreptunghiul_meu.schimba_culoarea('alb')
print(dreptunghiul_meu.descriere())
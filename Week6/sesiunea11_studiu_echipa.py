"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 11)
"""


"""
1. Defineste o clasa abstracta FormaGeometrica:

- Conține un field PI=3.14 (atribut pe clasa)
- Conține o metodă abstractă aria
- Conține o metodă a clasei descrie() 
    - aceasta printează pe ecran ‘Cel mai probabil am colturi’
"""
from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(cls):   # metoda de clasa; nu opereaza pe o instanta specifica
        print('Cel mai probabil am colturi')


"""
2. Defineste o clasa Patrat, care mosteneste FormaGeometrica

- In constructor, defineste atributul latura
    - latura este proprietate privata
    - implementeaza getter, setter, deleter pentru latura
- Implementeaza metoda ceruta de interfața
"""

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    # @latura.getter
    # def latura(self):
    #     print(f'Getter: Latura este {self.__latura}')
    #     return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        self.__latura = latura_noua
        return latura_noua

    # @latura.deleter
    # def latura(self):
    #     print(f'Deletter: Am sters latura')
    #     self.__latura = None

    def aria(self):
        return self.latura * self.latura


pp = Patrat(30)
pp.descrie()
print(pp.aria())


"""
3. Defineste o clasa Cerc, care mosteneste FormaGeometrica

- In constructor, defineste atributul raza
    - raza este proprietate privata
    - implementează getter, setter, deleter pentru rază
- Implementeaza metoda ceruta de interfata - în calcul foloseste field PI
mostenit din clasa parinte
- Defineste metoda descrie() in clasa Cerc - printeaza ‘Eu nu am colturi’
"""

class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza_noua):
        self.__raza = raza_noua
        print(f'Raza nou este {raza_noua}')

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        return self.PI * self.raza() ** 2

    def descrie(self):
        print(f'Eu nu am colturi')


cc = Cerc(12)
print(cc.aria())



"""
4. Creeaza un obiect de tip Patrat si joaca-te cu metodele lui
Creeaza un obiect de tip Cerc si joaca-te cu metodele lui
"""

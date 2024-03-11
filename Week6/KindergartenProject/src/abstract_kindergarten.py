"""
1. Creaza o clasa abstracta numita Gradinita,
cu urmatoarele metode abstracte:
- activitate_practica()
- ora_de_somn()
"""

from abc import ABC, abstractmethod

class AbstractKindergarten(ABC):

    @abstractmethod
    def practical_activity(self):
        pass

    @abstractmethod
    def nap_time(self):
        pass
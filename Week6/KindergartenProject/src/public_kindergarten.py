from abstract_kindergarten import AbstractKindergarten

"""
2. Implementati doua clase, numite GradinitaPublica si
GradinitaPrivata care sa implementeze clasa abstracta Gradinita.

GradinitaPublica:
- activitate_practica() - printeaza "copiii invata sa deseneze"
- ora_de_somn() - printeaza "copiii trebuie sa doarma la ora 5"

GradinitaPrivata:
- activitate_practica() - printeaza "copiii invata sa modeleze cu plastilina"
"""


class PublicKindergarten(AbstractKindergarten):
    student_id = 1

    def __init__(self):    # nu punem in paranteza students pt ca nu primeste val din exterior
        self.student = {}

    def practical_activity(self):
        print('The kids are learning how to draw.')

    def nap_time(self):
        print('The kids must sleep at 5 o clock')

    def add_students(self, name, age, year):
        student = {'name': name, 'age': age, 'year': year}
        self.student[name] = student



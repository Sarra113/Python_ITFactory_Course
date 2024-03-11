from abstract_kindergarten import AbstractKindergarten


class PrivateKindergarten(AbstractKindergarten):
    student_id = 1

    def __init__(self):  # nu punem in paranteza students pt ca nu primeste val din exterior
        self.student = {}
        self.__valoare_taxa = 5000

    @property
    def valoare_taxa(self):
        return self.__valoare_taxa

    @valoare_taxa.getter
    def valoare_taxa(self):
        print(f"Valoarea taxei este de {self.__valoare_taxa} lei")
        return self.__valoare_taxa

    @valoare_taxa.setter
    def valoare_taxa(self, taxa_noua):
        if taxa_noua < 5000:
            print("Taxa e de 5000 lei. Trebuie achitata toata suma o data.")
        elif taxa_noua > 5000:
            rest = taxa_noua - 5000
            self.__valoare_taxa = 5000
            print(f'Taxa e de 5000 lei, a fost platita cu succes! Veti primi restul de {rest} inapoi')
        else:
            self.__valoare_taxa = taxa_noua

    def practical_activity(self):
        print('The kids are learning how to work with clay.')

    def nap_time(self):
        print('The kids must sleep at 4 o clock')

    def add_students(self, name, age, year, tax):
        student = {'name': name, 'age': age, 'year': year, 'tax': tax}
        self.student[self.student_id] = student



from public_kindergarten import PublicKindergarten
from private_kindergarted import PrivateKindergarten
from public_kindergarten25 import PublicKindergarten25


# public_kindergarten = PublicKindergarten()
# public_kindergarten.practical_activity()
# public_kindergarten.nap_time()
# public_kindergarten.add_students('Ionut', 4, 3)
# print(public_kindergarten.student)


private_kindergarten = PrivateKindergarten()
# private_kindergarten.practical_activity()
# private_kindergarten.nap_time()
# private_kindergarten.add_students('Alex', 5, 2, 1000)
# print(private_kindergarten.student)
print(private_kindergarten.valoare_taxa)
private_kindergarten.valoare_taxa = 6000
private_kindergarten.valoare_taxa = 2000
private_kindergarten.valoare_taxa = 5000
print(private_kindergarten.valoare_taxa)



# public_kindergarten25 = PublicKindergarten25()
# public_kindergarten25.nap_time()   # apeleaza metoda din clasa parinte
# public_kindergarten25.practical_activity()   # apeleaza metoda suprascrisa
# print(PublicKindergarten25.mro())






import json
import csv


# Interactiunea cu fisiere text

# Creare

fisier_nou = open(file='dummy.txt', mode='w')
# file e oblig si ii dai nume textului
# se creeaza in folderul de lucru
# daca faceam '../dummy.txt' - mergea cu un folder mai sus

fisier_nou.write('hello')

fisier_nou.write('hello\nworld\n')     # un singur sir

fisier_nou.writelines(['hello\n', 'again\n'])    # mai multe siruri
# hello e lipit de hello si apoi newline
# folosită pentru a scrie o listă de șiruri de caractere în fișierul deschis

fisier_nou.close()


# context manager - seteaza un context temporar cand se executa un bloc de cod

def scriere_in_fisier_txt(calea_fisier, informatii_as_list):
    with open(calea_fisier, mode="w") as file:  # file e variabila
        file.writelines(informatii_as_list)

# context temporar pt executia blocului de cod de scriere a informatiilor


def citire_din_fisier_txt(calea_catre_fisier_txt):
    with open(calea_catre_fisier_txt, 'r') as file:
        return file.readlines()

citire_din_fisier_txt("dummy.txt")
#citire_din_fisier_txt("fisiere_text/dogs.txt")


def adaugare_in_fisier_text(calea_fisier, informatii_as_list):
    with open(calea_fisier, 'a') as file:
        return file.writelines(informatii_as_list)


adaugare_in_fisier_text('dummy.txt', ['how are you'])



#Serializare
def scriere_in_fisier_json(path, lines):
    with open(path, 'w') as file:
        json.dump(lines, file)


scriere_in_fisier_json('hello.json', {"name": "John", "age": 30, "city": "New York"})


#Deserializare - Parsing
def citire_fisier_json(path):
    with open(path, 'r') as file:
        return json.load(file)

print(citire_fisier_json('hello.json'))


x = ['apple', 'banana']
y = json.dumps(x)
print(y)

'''
json.dump - ia doua argumente, datele si un fisier .json in care sa le stochezi
json.dumps - cand vrei sa obtii datele json serializate intr un sir de caractere
'''


with open('path_to_csv_file.csv', 'w') as file:
    writer = csv.writer(file)
# am creat un obiect writer

    writer.writerow(['id', 'nume'])  #header
    writer.writerow([1, 'Paula'])
    writer.writerow([2, 'Ana'])

with open('path_to_csv_file.csv', 'r') as file:
    reader = csv.reader(file)

    row = next(reader)  # citeste un rad pe rand
    print(row)

    for row in reader:
        print(row)

with open('path_to_csv_file.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


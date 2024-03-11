import csv
import json

with open('sursa.txt', 'w') as file1:
    file1.write('hello\nagain\nworld')

# Copiere din fisier text in alt fisier text

with open('sursa.txt', 'r') as file1:
    with open('destinatie.txt', 'w') as file2:
        for line in file1:
            file2.write(line)

with open('destinatie.txt', 'r') as file2:
    print(file2.read())


def word_count(word, file_path):
    count = 0

    with open('sursa.txt', 'r') as file:
        for line in file:
            words = line.split()
            # separam linia in cuvinte
            # imparte sirul in functie de spatii si genereaza o lista de cuvinte
            count += words.count(word)

    return count


print(word_count('hello', 'sursa.txt'))


with open('produse.csv', 'w') as file3:
    writer = csv.writer(file3)

    writer.writerow(['id', 'nume_produs', 'pret', 'cantitate'])
    writer.writerow([1, 'mere', 10, 8])
    writer.writerow([2, 'banane', 15, 4])
    writer.writerow([3, 'faina', 11, 2])
    writer.writerow([4, 'peste', 25, 1])

with open('produse.csv', 'r') as file3:
    reader = csv.DictReader(file3)
    for row in reader:
        print(row)



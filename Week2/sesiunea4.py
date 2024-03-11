""" LISTE """
# lista_cumparaturi = ['rosii', 'paine', 'lapte']
# print(lista_cumparaturi)
# print("-"*40)
#
# lista_cumparaturi.remove("rosii")
# # lista_cumparaturi.pop()
# print(lista_cumparaturi)
# print("-"*40)
#
# lista_cumparaturi.append("oua")
# lista_cumparaturi.insert(1, "cafea")
# print(lista_cumparaturi)
# print("-"*40)
#
# lista_cumparaturi[2] = "peste"
# print(lista_cumparaturi)
# print("-"*40)
#
# print(len(lista_cumparaturi))
# print("-"*40)
# print(type(lista_cumparaturi))
#
# contacte = ['0722345678', '0721549888', '0765332967']
# nr = int(contacte[0])
# print(nr)

# """ DICȚIONARE """
# contacte = {
#     'Ana': '0722345678',
#     'Marius': '0721549888',
#     'Maria': '0765332967'
# }
#
# print(contacte['Ana'])
# print("-"*40)
# print(contacte['Maria'])
# print("-"*40)
# # print(contacte['Andrei'])  # va da eroare
# print(contacte.get('Andrei', 'Contactul nu se află în listă.'))

# person = {
#     "name": "John",
#     "age": 30,
#     "cities": ["New York", "Los Angeles"],
#     "occupation": "teacher"
# }

# # ADAUGAREA unui element nou in dictionar
# # v1
# person['salary'] = 3000.00
# print(person)
# print("-"*40)
#
# # v2
# person.update({"has_car": True})
#
# # MODIFICAREA unui element in dictionar
# # v1
# person['age'] = 31
# print(person)
# print("-"*40)
#
# # v2
# person.update({"age": 32})
#
# # STERGEREA unui element din dictionar
# # v1
# del person['cities']
# # del person['city'], person['salary'] # stergem mai multe key:value deodata
# print(person)
# print("-"*40)
#
# # v2
# # stergerea unui perechi cheie:valoare dupa cheie
# person.pop('occupation')
# print(person)

# cities = person['cities']
# print(cities)
# city = cities[0]  # person['cities'][0]
# print(city)

# """ SETURI """
# set1 = {1, 2, 3, 4, 5}
# print(f"Set 1: {set1}")
# print("-"*40)
# set2 = {4, 5, 6, 7, 8}
# set1.remove(3)
# print(f"Set 1 after removal: {set1}")
# print("-"*40)
# intersection = set1.intersection(set2)
# print(f"Intersection between: {intersection}")
# print("-"*40)
# difference = set2.difference(set1)
# print(f"Elements in Set 2 but not in Set 1: {difference}")
# print("-"*40)
# union = set1.union(set2)
# print(f"Union between Set 1 and 2: {union}")

""" TUPLURILE """
# cos_de_cumparaturi = ("paine", "oua", "lapte", "peste", "cafea")
# cos_de_cumparaturi[3] = "carne"  # va da eroare
# print(cos_de_cumparaturi)

# students = {
#     ("grupa_A", "grupa_B"): ["Ana", "Maria", "Cornel", "Andrei", "Marius"]
# }
# print(students)

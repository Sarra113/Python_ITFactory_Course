# lista_cump = input('Introdu elem:')
# print(lista_cump)
# lista2 = list(lista_cump.split(','))
# print(lista2)
# print(type(lista2))
#
# lista2.sort()
# print(lista2)
# lista2.append('fructe')
# print(lista2)
# lista2.remove('fructe')
# print(lista2)
# lista2[0] = 'banane'
#
# if 'rosii' in lista2:
#     print('Aliment sanatos')
# else:
#     print('Iti recomandam rosiile')



# metoda join ia toate elem dintr-un iterabil si le aduna intr-un string
# trebuie sa numesti un string ca separator
# la dictionar, metoda join ia cheile
# fructe = ['capsuni', 'mere', 'lamai']
# string = ', '.join(fructe)
# print(string)

# numere = [1, 2, 3, 4, 56, 22, 5]
# print(max(numere))
#
# preturi = [12.3, 34.5, 22]
# print(sum(preturi))

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# print(sample_dict['city'])
# sample_dict["salary"] = 10000
# print(sample_dict)
# sample_dict.pop('age')
# sample_dict.update({'employment_date': 2023})
# print(sample_dict.get('country', 'USA'))
# sample_dict.update({'country': 'USA'})
# print(sample_dict)

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# # dict1.update({'c': 3, 'd': 4})
# print(dict1)

lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
lista[0].update({'c': '3'})
print(lista[0])
lista.append({'g': '7', 'h': '8'})
lista.insert(1, {'?': '0'})
print(lista)
if 'c' in lista[2]:
    print(True)
else:
    print(False)

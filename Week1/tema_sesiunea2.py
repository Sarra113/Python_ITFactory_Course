# EX1: Se da string-ul prop3 = 'Concertul va avea loc maine."
# a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
# b. Extrage primele 3 caractere din prop3.
# c. Afiseaza prop3 cu caracterele inversate.

# prop3 = 'Concertul va avea loc maine.'
# cuv1 = prop3[:9]
# print(cuv1)
# print(prop3[:3])
# print(prop3[::-1])

# '''
# EX2: Se da string-ul my_str = 'vacanta'.
# a. Foloseste metoda find() pentru a afla primul index la care se
# gaseste caracterul 'a'.
# b. Foloseste metoda count() pentru a afla de cate ori apare
# caracterul 'a' in my_str.
# c. Foloseste metoda capitalize() pentru a scrie cuvantul
# cu prima litera mare.
# d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
# '''
# my_str = 'vacanta'
# print(my_str.find('a'))
# print(my_str.count('a'))
# print(my_str.capitalize())
# print(my_str.casefold())
# print(my_str.upper())


# EX3: Exploreaza urmatoarele metode ajutatoare ale string-ului:
# a. endswith()
# b. index()
# c. lower()
# d. replace()
# e. strip()

# my_str = '    Vacanta    '
# print(my_str.endswith('a'))  # verifica daca se termina cu ceva anume
# print(my_str.endswith('n', 3, 5))
# print(my_str.endswith('t', 4))
# print(my_str.index('n'))
# print(my_str.lower())
# print(my_str.replace('v'.upper(), 'o'))  # case sensitive
# print(my_str.replace('a', 'o', 1))  # de cate ori sa fie inlocuit
# print(my_str.strip())  # scapa de spatiile de la final si inceput
# my_str = 'nnVacanta...'  # sau de caractere de la final/inceput
# print(my_str.strip('n.'))
#
# my_string2 = 'Vacanta mare'
# print(my_string2.split('m'))   # returneaza o lista cu substrings. cand e setat pe none imparte la spatiile albe
# # elimina ce ai pus in paranteza

"""
EX4: Se dau doua variabile, a = 10, b = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""
# a = 10
# b = 2
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a % b)
# print(a ** b)
# print(a // b)

'''
EX6: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
'''
# num = 12
# if num > 0:
#     print(True)
#
# if num > 5:
#     print(True)
#
# if num < 25:
#     print(True)
#
# if 0 < num < 20:
#     print(True)

# Verifica daca varsta introdusa de utilizator este mai mare decat 18 ani.
# v = 18
# varsta = int(input('Ce varsta ai?'))
# if varsta >= v:
#     print('Cont creat')
# else:
#     print(f'NU ai varsta necesara de {v} ani')

# Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.

# p = 100
# pret_introdus = int(input('Care este pretul?'))
# if pret_introdus <= p:
#     print(True)
# else:
#     print(False)

# EX9:
# a. Citeste un numar de la tastatura.
# b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv
# in fiecare situatie.
# x = int(input('Numar'))
# if x % 2 == 0:
#     print('Nr este par')
# else:
#     print('Nr este impar')

'''
EX10:
a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
'''
# v = int(input('Viteza medie de circulatie este'))
# if v <= 50:
#     print('Viteza normala')
# else:
#     print('Viteza depasita')

'''
EX11: Citeste de la tastatura varsta utilizatorului si afiseaza categoria
de varsta in care se incadreaza.
Tine cont de aceste categorii de varsta:
- intre 0-18 ani: minor
- intre 18-65 ani: adult
- peste 65 ani: senior
'''
# varsta_utilizator = int(input('Care este varsta ta?'))
# if varsta_utilizator < 18:
#     print('Minor')
# elif 18 <= varsta_utilizator <= 65:
#     print('Adult')
# elif varsta_utilizator > 65:
#     print('Senior')

'''
EX12: Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg
cosul de cumparaturi, in functie de totalul cosului de cumparaturi
Reducerea se aplica in felul urmator:
- Total este intre 100 si 200 lei -> reducere 10%
- Total intre 200 - 300 lei -> reducere 15%
- Total intre 300-400 -> reducere 20 %
- Total mai mare de 400 -> reducere 30 %.
a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi
dupa aplicarea reducerii.
'''
# cost_total = float(input('Costul total este de:'))
# if 100 <= cost_total <= 200:
#     print(cost_total - (cost_total * 0.10))
# elif 200 < cost_total <= 300:
#     print(cost_total - (cost_total * 0.15))
# elif 300 < cost_total <= 400:
#     print(cost_total - (cost_total * 0.20))
# elif cost_total > 400:
#     print(cost_total - (cost_total * 0.30))

'''
EX13:
a. Citeste de la tastatura nr de ore lucrate de un angajat intr-o
saptamana.
b. Tinand cont ca numarul de ore standard de munca dintr-o 
saptamana este 40, si se considera overtime, ce e peste 40 de ore,
afiseaza bonusul pe care angajatul il primeste si un mesaj sugestiv,
tinand cont de urmatoarele criterii:
- bonusul este de 50 lei daca angajatul a lucrat intre 40 si 50 ore.
- bonusul este de 100 lei daca angajatul a lucrat mai mult de 50 de ore.
- daca s-a lucrat nr de ore standard, angajatul nu e eligibil pentru bonus.
'''
# nr_ore_saptamana = int(input('Cate ore ati lucrat in aceasta saptamana?'))
# if 40 < nr_ore_saptamana <= 50:
#     print('Aveti un bonus de 50 lei.')
# elif nr_ore_saptamana > 50:
#     print('Aveti un bonus de 100 lei')
# else:
#     print('Nu sunteti eligibil pentru bonus')

'''
EX14:
a. Citeste de la tastatura varsta utilizatorului.
b. Spune-i utilizatorului daca are drept de vot in Romania.
Conditii drept de vot:
- utilizatorul are drept de vot daca este mai mare de 18 ani.
- utilizatorul are drept de vot daca locuieste in Romania.
'''
# varsta = int(input('Ce varsta aveti?'))
# locuinta = input('In ce tara locuiti?')
# tara = "Romania"
# if varsta >= 18 and locuinta.strip() == tara:   # cu metoda strip nu da rez negativ daca pun spatiu inainte de raspuns
#     print('Aveti drept de vot in Romania')                 # cu casefold nu da rez negativ daca scriu cu litera mica
# else:
#     print('Nu aveti drept de vot in Romania')

#V2
# varsta = int(input('Varsta dumneavoastra este: '))
# tara_1 = (input('Locuiti in tara: '))
# tara_2 = tara_1.lower()
# if varsta >= 18 and tara_2 == 'romania':
#     print('Aveti drept de vot')
# else:
#     print('Nu aveti drept de vot')



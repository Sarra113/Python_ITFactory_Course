"""
Sesiunea 9 - Exercitii cu Trainer
"""


"""
IMPORTANT! Pentru toate exercitiile: apelati functia de cel putin 2 ori
cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.                        
"""


"""
1. Functie care returneaza aria dreptunghiului.
"""
# def arie_dreptunghi(lungime: int, latime: int) -> int:
#     return lungime * latime
#
# lungimea = 12
# latimea = 6
# print(arie_dreptunghi(12, 6))


"""
2. Functie care returneaza True daca un caracter x se gaseste intr-un string dat
si False daca nu se gaseste.
"""
# def find_char_in_string(my_string: str, x: str) -> bool:
#     return x.lower() in my_string   # char in string face o validare de la sine. ceva in altceva intoarce True sau False de la sine
#     # if x.lower() in my_string:
#     #     return True
#     # else:
#     #     return False
#
# print(find_char_in_string('Ana are mere', 'M'))
# print(find_char_in_string('Ana are pere', 't'))

"""
3. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA:
Primul numar x este mai mare decat al doilea numar y
Al doilea numar y este mai mare decat primul numar x
Numerele sunt egale. 
"""

# def nr_comparison(x: int, y: int):
#     if x > y:
#         print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
#     elif y > x:
#         print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
#     else:
#         print('Numerele sunt egale. ')
#
# nr_comparison(5, 7)

"""
4. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Printeaza ‘nu am adaugat numarul in set. Acesta există deja’ + returneaza False
"""

# def add_to_set(numar: int, setul: set) -> bool:
#     # if numar in setul:
#     #     print('nu am adaugat numarul in set. Acesta există deja')
#     #     return False
#     # else:
#     #     setul.add(numar)
#     #     print('am adaugat numarul nou in set')
#     #     return True
#     if numar not in setul:
#         setul.add(numar)
#         print('am adaugat numarul nou in set')
#         return True
#     print('nu am adaugat numarul in set. Acesta există deja')
#     return False
#
#
# add_to_set(5, {5, 9, 10, 11})
# add_to_set(4, {5, 7, 8, 2})




"""
5. Functie care primeste o luna din an si returneaza cate zile are acea luna.
"""

# def days_in_month(month: str) -> int:
#     luni = {
#         "ianuarie": 31, "februarie": 29, "martie": 31,
#         "aprilie": 30, "mai": 31, "iunie": 30,
#         "iulie": 31, "august": 31, "septembrie": 30,
#         "octombrie": 31, "noiembrie": 30, "decembrie": 31
#     }
#     return luni.get(month.lower(), 'luna invalida')
#
# print(days_in_month('Aprilie'))
# print(days_in_month('Pacific'))




"""
6. Functie calculator care sa returneze 4 valori: Suma, diferenta, inmulțirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""


# def calculator(num_1: float, num_2: float) -> tuple:
#     suma = num_1 + num_2
#     diferenta = num_1 - num_2
#     inmultirea = num_1 * num_2
#     impartirea = num_1 / num_2 if num_2 != 0 else 'Impartirea la 0 nu este permisa'
#
#     return suma, diferenta, inmultirea, impartirea
#
#
# # print(calculator(3, 4.5))
# # dispatch ???
# suma, diferenta, inmultirea, impartirea = calculator(10, 4)
# print("Suma: ", suma)
# print("Diferenta: ", diferenta)
# print("Inmultirea: ", inmultirea)
# print("Impartirea: ", impartirea)





"""
7. Functie care primeste o lista de cifre (adica doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

# def contorizare_cifre(my_list: list[int]) -> dict:
#     return {i: my_list.count(i) for i in range(10)}
#
#   rezultat = {}
    # for i in range(10):
    #     rezultat[i] = my_list.count(i)
    # return rezultat
#
# print(contorizare_cifre([1, 3, 1, 5, 9, 7, 7, 5, 5]))



"""
8. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
"""


# def valoare_maxima(x: int, y: int, z: int) -> int:
#     # maxim = max(x, y, z)
#     # return maxim
#     return max(x, y, z)
#
# print(valoare_maxima(4, 78, 3))
# print(valoare_maxima(1, 11, 56))


"""
9. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: dacă dam numarul 3, suma va fi 6 (0+1+2+3)
"""


# def suma_numere(x: int) -> int:
#     return sum(range(x + 1))
#
#
# print(suma_numere(6))
# print(suma_numere(-3))
#
# print(list(range(-3)))



"""
10. Functie care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""

# def numere_comune(a: list, b: list) -> set:
#     return set(a).intersection(set(b))
#
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
#
# print(numere_comune(list1, list2))



"""
11. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
"""

# def reducere(pret_initial: float, procent_reducere: int):
#     if procent_reducere < 0 or procent_reducere > 100:
#         print('Reducere invalida')
#     else:
#         aplicare_reducere = pret_initial * procent_reducere / 100
#         pret_final = pret_initial - aplicare_reducere
#         print(f'Pretul final este {pre_final}')
#
#
# reducere(300, 120)


"""
12. Funcție care sa afiseze data si ora curenta din Romania.
(bonus: afiseaza si data si ora curenta din China)
"""

# import datetime
#
# now = datetime.datetime.now()
# print(f'Current date and time in Ro: {now}')
# china = datetime.timezone.fromutc()



"""
13. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun
daca nu vrei sa ne zici cand e ziua ta :)
"""

# nr zile pana la ziua mea si craciun

# import datetime
#
#
# def get_user_birthday():
#     year = int(input('When is your birthday? [YY] '))
#     month = int(input('When is your birthday? [MM] '))
#     day = int(input('When is your birthday? [DD] '))
#
#     birthday = datetime.datetime(year,month,day)
#     return birthday
#
#
# def calculate_dates(original_date, now):
#     date1 = now
#     date2 = datetime.datetime(now.year, original_date.month, original_date.day)
#     delta = date2 - date1
#     days = delta.total_seconds() / 60 /60 /24
#
#     return days
#
# def show_info(self):
#     pass
#
#
#
# bd = get_user_birthday()
# now = datetime.datetime.now()
# c = calculate_dates(bd,now)
# print(c)
"""
PROGRAM: Ghiceste numarul!

Se da variabila numar_magic = 25.
Citeste de la tastatura un numar introdus de utilizator
si verifica daca acesta este sau nu egal cu numar_magic.
Afiseaza un mesaj sugestiv in fiecare caz.
"""
# numar_magic = 25
#
# while True:
#     numar_utilizator = int(input("Introdu numărul\n>>> "))
#     if numar_utilizator != numar_magic:
#         print("Mai încearcă!")
#     else:
#         print("Felicitări, ai ghicit!")
#         break

# x = 8
# while x > 0:
#     print(f"Numarul {x} este pozitiv")
#     x -= 1
# print("S-a iesit din while")
# print(f"Dupa while, x are valoarea {x}")

# import random
#
# secret_number = random.randint(1, 10)

# guessed = False
#
# while not guessed:
#     guess_number = int(input("Alege un numar de la 1 la 10: "))
#     if guess_number == secret_number:
#         print("Felicitari! Ai ghicit!")
#         guessed = True  # conditia de iesire
#     elif guess_number < secret_number:
#         print("Numarul este prea mic. Incercati din nou.")
#     else:
#         print("Numarul este prea mare. Incercati din nou.")

# while True:
#     guess_number = int(input("Alege un numar de la 1 la 10: "))
#     if guess_number < secret_number:
#         print("Numarul este prea mic. Incercati din nou.")
#     elif guess_number > secret_number:
#         print("Numarul este prea mare. Incercati din nou.")
#     else:
#         print("Felicitari! Ai ghicit!")
#         break

# numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
#
# search_value = int(input("Ce numar cautati? "))
#
# index = 0
# while index < len(numbers):
#     if numbers[index] == search_value:
#         print(f"Valoarea a fost gasita la indexul: {index}")
#         break
#     index += 1
# else:
#     print("Valoarea nu a fost gasita in lista!")

# range(start, stop, step)
# data = list(range(1, 11, 2))
# print(data)

# for i in range(4):
#     print(i)
# else:
#     print("Am terminat.")

# culori = ["rosu", "albastru", "galben", "mov"]
# valoare_utilizator = input("Introdu culoarea ta preferată\n>>> ")
#
# for culoare in culori:
#     if culoare == valoare_utilizator:
#         print(f"{culoare} este culoarea preferată a utilizatorului")
#         break
# else:
#     print(f"Culoarea preferată a utilizatorului nu este în listă.")

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

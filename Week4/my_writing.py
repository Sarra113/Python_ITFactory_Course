
#Semnatura functiei
# def print_hello_message(name: str = None): # specificare tip de date
#     '''
#     [Scurta descriere a ce face functia]
#     Prints greeting message to the console
#
#     Parameters
#     ---------
#     name: str, Optional
#         The name of the person to greet
#
#     Returns
#     -------
#     None
#     '''
#     print(f'Hello {name}!')
#
# # Apelare
# print_hello_message('Felix')

# def add_numbers(a: int, b: int):
#     if not isinstance(a, int) or not isinstance(b, int):
#         return 'params are not integers'    # se opreste aici si nu mai face suma
#
#     return a + b
#
# added_numbers = add_numbers(4, 8)
# print(added_numbers)

# def este_natural(numar: int) -> str:   # ce tip de date intoarce functia
#     if numar < 0:
#         return 'Numarul nu este natural'
#
#     return 'Numarul este natural'
#
# print(este_natural(4))

# def get_square(num: int) -> int:
#     return num * num
#
# for i in [1, 2, 3]:
#     result = get_square(i)
#     print(f'Square of {i} is {result}.')

"""
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""

# def print_first_ten_numbers():
#     """
#     Print the first 10 numbers from 1 to 10.
#     """
#     for number in range(1, 11):
#         print(number)
#
#
# print_first_ten_numbers()

"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""

def print_even_odd_from_list(numbers: list):
    """
    Iterates through a list of numbers and prints odd or even

    Parameters
    ----------
    numbers : list
        The list of numbers to be checked
#     """
#     for number in numbers:
#         if not isinstance(number, int):
#             print(f'Elementul {number} nu este un numar intreg')
#         else:
#             if number % 2 == 0:
#                 print(f'Numarul {number} este par')
#             else:
#                 print(f'Numarul {number} este impar')
#
# numbers = [2, 4, 5, 9, 8.8, 'aaa']
# print_even_odd_from_list(numbers)

"""
EX3: Scrie o functie care calculeaza patratul unui numar.
Afiseaza rezultatul.
"""

# def square_number(number: int):
#     """
#     Returns the square of the given number
#
#     Parameters
#     ----------
#     number : integer
#     """
#     print(number ** 2)
#
# square_number(5)

"""
EX4: Scrie o functie care calculeaza inmultirea dintre doua numere.
Afiseaza rezultatul.
"""

# def number_addition(number1: float, number2: float):
#     """
#     Calculam inmultirea dintre 2 numere
#
#     Parameters
#     ----------
#     number1 : float
#     number2 : float
#         Cele doua numere care vor fi inmultite
#     """
#     print(number1 * number2)
#
#
# number_addition(3.0, 6.7)

"""
EX6: Rescrie functia de la exercitiul 3, 
astfel incat sa returneze rezultatul.
"""
# def square_number(number: int):
#     """
#     Returns the square of the given number
#
#     Parameters
#     ----------
#     number : integer
#     """
#     return print(number ** 2)
#
# square_number(3)

"""
EX8: Scrie o functie care ia ca parametru un numar intreg
si returneaza True daca numarul e par
si False daca numarul e impar.
"""

def numar_par_sau_impar(number: int):
    """
    Returneaza true la numar par si false la impar

    Parameters
    ----------
    number : integer
    """
    if number % 2 == 0:
        return True
    else:
        return False

print(numar_par_sau_impar(6))
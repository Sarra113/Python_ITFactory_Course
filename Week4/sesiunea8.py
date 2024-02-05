# print('Hello world')

# Semnătura funcției
# def print_hello_message(name: str = None):
#     """
#     [Scurtă descriere a ce face funcția]
#     Prints a greeting message to the console.
#
#     Parameters
#     ----------
#     name : str, Optional
#         The name of the person to greet.
#
#     Returns
#     -------
#     None
#     """
#     print(f"Hello {name}!")

# Apelarea funcției
# print_hello_message("Felix")
# print_hello_message("Irina")
# print_hello_message("Sergiu")


# def add_numbers(a: int, b: int):
#     # if not isinstance(a, int) or not isinstance(b, int):
#     #     return "params are not integers"
#
#     return a + b


# added_numbers = add_numbers(4, 3)
# print(added_numbers)
# add_numbers(1)  # => EROARE
# add_numbers(3, 4, 6)  # => EROARE

#
# def este_natural(numar: int) -> str:
#     if numar < 0:
#         return "Numărul nu este natural."
#
#     return "Numărul este natural."
#
#
# print(este_natural(4))
# print(este_natural(-4))


# def get_square(num: int) -> int:
#     return num ** 2

#
# for i in range(1, 11):
#     result = get_square(i)
#     print(f'Square of {i} is {result}.')


# x = 5 / 0  # ZeroDivisionError

# my_dict = {'pret': 25.00, 'nume': 'perna'}
# print(my_dict['culoare'])  # KeyError
# print(my_dict.get('culoare', 'alb'))


# try:
#     # execute/run this code
#     x = 5 / 0
# except ZeroDivisionError:
#     # execute this block when exception occured
#     print("Can not divide by zero!")
# else:
#     # execute this block if no exception occured
#     print("Yeah! Your answer is:", x)
# finally:
#     # always execute this block of code
#     print("This is always executed!")
#
#
# # Definirea tipului de date a parametrilor, respectiv a ce returnează, se intitulează TYPE HINTING
# def divide(a: int, b: int) -> float:
#     if b == 0:
#         raise ZeroDivisionError(
#             "Al doilea parametru trebuie să fie diferit de 0."
#         )
#     return a / b
#
#
# print(divide(5, 0))

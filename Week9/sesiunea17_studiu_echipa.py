"""
EXERCITII STUDIU IN ECHIPA (Sesiunea 17)
"""

"""
1. Implementeaza un generator care primeste ca parametru un string,
si genereaza cuvintele in acesta.
"""

# def generatorul_meu(stringul_meu):
#     cuvinte = stringul_meu.split()
#     for cuvant in cuvinte:
#         yield cuvant
#
#
# text ="Acesta este o propozitie pentru exemplu"
# generatorul_meu = generatorul_meu(text)
# for cuvant in generatorul_meu:
#     print(cuvant)


"""
2. Implementeaza un generator de numere prime pana la o limita,
luata ca parametru.
"""

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
#
# def my_gen(limit):
#     for num in range(2, limit):
#         if is_prime(num):
#             yield num
#
# limit = 25
#
# for prime_num in my_gen(limit):
#     print(prime_num)

"""
3. Defineste un decorator, enforce_return_type, care transforma
rezultatul functiei la un anumit tip specificat.
"""
# def enforce_return_type(return_type):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return return_type(result)
#         return wrapper
#     return decorator
#
# @enforce_return_type(float)
# def calculate_avg(numbers):
#     return sum(numbers) / len(numbers)
#
#
# print(calculate_avg([3, 5, 7, 10, 50]))


"""
4. Defineste un decorator, multiply, care multiplica rezultatul unei functii
cu n, n fiind un parametru luat de decorator.
"""

# def multiply(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result * n
#         return wrapper
#     return decorator
#
#
# @multiply(2)
# def divide(a,b):
#     return a/b
#
#
# print(divide(30, 5))

#db= pymysql.connect(host=”Demo”, user=”root” , passwd=”adm1n”, db=”test”)
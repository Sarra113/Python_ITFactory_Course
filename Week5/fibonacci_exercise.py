# Fibonacci series up to n
# 0, 1, 1, 2, 3, 5, ...
def fibonacci(n: int):
    a, b = 0, 1
    fib = []

    while len(fib) < n:
        fib.append(a)
        a, b = b, a+b

    print(fib)


fibonacci(12)

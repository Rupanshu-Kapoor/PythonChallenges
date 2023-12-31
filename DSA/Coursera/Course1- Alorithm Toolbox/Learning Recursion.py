from random import randint, randrange


def factorial(n: int):
    result = 1;

    for i in range(n, 0, -1):
        result *= i
    # print(result)
    return result


def factoriaRecursion(n: int):
    # result = 1
    if n - 1 > 0:
        return n * factoriaRecursion(n - 1)
    else:
        return 1
    # result



print(factoriaRecursion(-1))
print(factorial(-1))
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


# check if two approach has same results:

rand = randint(0, 1000)
for i in range(rand):
    if factorial(i) != factoriaRecursion(i):
        print("Error: Result Mismatched at {}".format(i))
        break
    else:
        print(f"factorial {i} is {factorial(i)} and factorial recursion is {factoriaRecursion(i)}")
print(rand)

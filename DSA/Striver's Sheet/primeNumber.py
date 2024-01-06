from math import sqrt


def isPrime(number: int) -> bool:
    if number == 1:
        return False
    sqr = int(sqrt(number))

    for i in range(2, sqr + 1):
        if number % i == 0 and number != i:
            return False

    return True


print(isPrime(1))
print(isPrime(2))
print(isPrime(6))
print(isPrime(5))
print(isPrime(322))
print(isPrime(73))
print(isPrime(97))

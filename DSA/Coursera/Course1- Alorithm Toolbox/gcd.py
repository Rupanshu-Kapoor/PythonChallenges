"""
    trying various ways to implement Greatest Common Divsior(GCD)
"""


def naiveGCD(a: int, b: int) -> int:
    """
    based on the simple approach that GCD is the number that divides both a and b
    :param a:
    :param b:
    :return: GCD of a and b
    time complexity: O(min a and b) = O(n)
    """
    best = 0
    small = min(a, b)
    for i in range(1, small + 1):
        if a % i == 0 and b % i == 0:
            best = i

    return best


def euclidGCD(a: int, b: int) -> int:
    """
    based on the Euclid theorem that stats that
    GCD(a,b) = GCD(a`,b)
    where a = bq + a`
    :param a:
    :param b:
    :return: CGD of a,b in a fast approach
    time complexity : O(log phi (min of a,b)) = O(log phi(n))
    """
    if b == 0:
        return a
    else:
        rem = a % b
        return euclidGCD(b, rem)


print(naiveGCD(3577, 2343))
print(euclidGCD(234, 3577))

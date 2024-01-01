from testing import stressTest as st


def exponent(num: int, exp: int) -> int:
    """
    Exponent using recursion[only computing for exponent >= 0]
    Uses linear search to calculate exponent
    :param num: base number
    :param exp: exponent power
    :return: Num ^ exp
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        return num * exponent(num, exp - 1)

def exponent2(num: int, exp: int) -> int:
    """
    Exponent using recursion[only computing for exponent >= 0]
    Uses binary search to calculate exponent
    :param num: base number
    :param exp: exponent power
    :return: Num ^ exp
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    elif exp % 2 == 0:
        temp = exponent2(num, exp/2)
        return temp * temp
    else:
        temp = exponent2(num, (exp-1)/2)
        return temp * temp * num


print(exponent2(2, 5))
expo = st.stressTest().randNumSmall()
for i in range(st.stressTest().randNumSmall()):

    if st.stressTest().testResult(exponent(i, expo), exponent2(i, expo)):
        print(f"Test Passed for number: {i} and exponent: {expo}")
    else:
        print(f"Test failed for number: {i} and exponent: {expo}")

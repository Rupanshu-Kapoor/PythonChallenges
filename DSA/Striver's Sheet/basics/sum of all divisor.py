"""
Sum of all divisors: https://www.codingninjas.com/studio/problems/sum-of-all-divisors_8360720
Easy
Problem statement
You are given an integer ‘n’.
Function ‘sumOfDivisors(n)’ is defined as the sum of all divisors of ‘n’.
Find the sum of ‘sumOfDivisors(i)’ for all ‘i’ from 1 to ‘n’.

Example:
Input: ‘n’  = 5

Output: 21

Explanation:
We need to find the sum of ‘sumOfDivisors(i)’ for all ‘i’ from 1 to 5.
‘sumOfDivisors(1)’ = 1
‘sumOfDivisors(2)’ = 2 + 1 = 3
‘sumOfDivisors(3)’ = 3 + 1 = 4
‘sumOfDivisors(4)’ = 4 + 2 +1 = 7
‘sumOfDivisors(5)’ = 5 + 1 = 6
Therefore our answer is sumOfDivisors(1) + sumOfDivisors(2) + sumOfDivisors(3) + sumOfDivisors(4) +
sumOfDivisors(5) = 1 + 3 + 4 + 7 + 6 = 21.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
3
Sample Output 1:
8
Explanation of sample output 1:
We need to find sumOfDivisors(1) + sumOfDivisors(2) +sumOfDivisors(3).
sumOfDivisors(1) = 1
sumOfDivisors(2) = 2 + 1 = 3
sumOfDivisors(3) = 3 + 1 = 4
Therefore, the answer is sumOfDivisors(1) + sumOfDivisors(2) + sumOfDivisors(3) = 1 + 3 + 4 = 8.

Sample Input 2:
10
Sample Output 2:
87
Expected Time Complexity:
Try to solve this in O(sqrt(‘n’)).

Constraints:
1 <= ‘n’ <= 3*10^4
Time Limit: 1 sec
"""
import math


def allDivisors(n: int) -> list[int]:
    factors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factors.append(i)
            if n / i != i:
                factors.append(int(n / i))
    return factors


def sumOfAllDivisors(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += sum(allDivisors(i))
    print(total)
    return total


def sumOfAllDivisors2(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                total += j
    print(total)
    return total


def sumOfAllDivisors3(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        factors = []
        for j in range(1, int(math.sqrt(i) + 1)):
            if i % j == 0:
                factors.append(j)
                if i / j != j:
                    factors.append(int(i / j))

        print(i, factors)
        total += sum(factors)
    return total


sumOfAllDivisors(5)
print(sumOfAllDivisors3(5))
# sumOfAllDivisors2(30000)

def generateFibonacci(n: int):
    fibonacci = [1, 1]
    for i in range(n - 2):
        total = sum(fibonacci[-2:])
        fibonacci.append(total)
    return fibonacci


number = int(input("Enter a number to generate Fibonacci:"))
print(generateFibonacci(number))

number = int(input("Enter Nth number:"))
print(generateFibonacci(number)[-1])
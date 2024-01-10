class Fibonacci:

    # using for loop
    def fabonacciGenerator(self, number: int) -> list[int]:
        fab = [0, 1]
        for i in range(number - 1):
            temp = fab[-1] + fab[-2]
            fab.append(temp)
        return fab

    # using recursion
    def fabonacci(self, n):
        if n <= 2:
            return 1
        return self.fabonacci(n - 1) + self.fabonacci(n - 2)

    # improved recursion fabonacci with stack
    def improvedFabonacci(self, stack: dict, n):
        if n in stack.keys():
            return stack[n]
        if n <= 2:
            return 1
        temp = self.improvedFabonacci(stack, n-1) + self.improvedFabonacci(stack, n-2)
        stack[n] = temp
        return temp


dic = {}
num = 1000
obj = Fibonacci()
print(obj.fabonacciGenerator(num)[-1])
# print(obj.fabonacci(4))
print(obj.improvedFabonacci(dic, num))
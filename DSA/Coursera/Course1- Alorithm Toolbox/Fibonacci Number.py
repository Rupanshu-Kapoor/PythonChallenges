
class Fibonacci:

    def FabonacciGenerator(self, number: int) -> list[int]:

        fab = [0,1]
        for i in range(number-2):
            temp = fab[-1] + fab[-2]
            fab.append(temp)
        return fab


obj = Fibonacci().FabonacciGenerator(5)
print(obj)
from random import randint
class stressTest():

    def randNumSmall(self):
        """
        Generate a random number between 1 and 1000
        :return: int: Return a random number generated
        """
        return randint(0, 1000)

    def randNumLarge(self) -> int:
        """
        Generate a random number between 1000, 10000
        :return: int : Return a random nuber generated
        """
        return randint(1000, 10000)

    def randArray(self, num: int, category = "small") -> list[int]:
        """
        Generate an array of size "num" consist of random numbers
        :param category:  "Small" or "Large"
        :param num: size of array
        :return: Array of size num containing random numbers
        """
        category = category.lower()
        array = []
        if category == "small":
            for i in range(num):
                array.append(self.randNumSmall())
        else:
            for i in range(num):
                array.append(self.randNumLarge())

        return array

    def testResult(self, res1, res2):
        """
        :param res1:
        :param res2:
        :return: True if both results are equal else False
        """
        return res1 == res2
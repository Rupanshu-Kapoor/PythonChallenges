from random import *

num = randint(0,20)
hash_table = [0] * (num+1)
arr = [randint(0, num) for x in range(randint(10,50))]

for i in arr:
    hash_table[i] += 1

print(arr)
print(hash_table)


string = "fhnsdjkfnasmasdasdndlksdfksd"

hash_arr = [0] * 256

for i in string:
    hash_arr[ord(i)-ord("a")] += 1

print(f"f appears {hash_arr[ord('f') - ord('a')]}")
print(f"c appears {hash_arr[ord('c') - ord('a')]}")
print(f"d appears {hash_arr[ord('d') - ord('a')]}")
print(f"k appears {hash_arr[ord('k') - ord('a')]}")


hash_dict = {}
i = 1

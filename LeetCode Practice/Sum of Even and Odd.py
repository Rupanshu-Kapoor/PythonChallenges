# string = "132456"
string = list(input())

even = sum([int(x) for x in string if int(x)%2==0])
odd = sum([int(x) for x in string if int(x)%2==1])
print(even, odd)


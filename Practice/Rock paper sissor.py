import random

l = ["R", "P", "S"]
x = input("Enter Choice: 'R', 'P', 'S': ")
y = random.choice(l)
print("Computer Choice:",y)
if x == y:
    print("It's a tie")
elif (x == "R" and y == "S") or (x == "P" and y == "R") or (x == "S" and y == "P"):
    print("You win")
else:
    print("Computer win")

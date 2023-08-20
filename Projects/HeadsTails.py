import random

print("Hello Player!")
print("--Press 0 or 1 to choose Heads or Tail respectively--")
choice = int(input())
result = random.randint(0,1)
var = str(result) + "  " + str(choice)
print(var)
if(choice == result):
    print("Hurray!,You got it right.")
else:
    print("Try again.")

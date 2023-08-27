import random 
str = input("Write the names of your friends who are going to pay the bill ->")
result = str.split(",")
# randomChoice = random.randint(0,len(result)-1)

# print(result[int(random.random()*len(result))]+" is going to pay the bill.")

# print(result[randomChoice] + " is going to pay the bill.")

print(random.choice(result))

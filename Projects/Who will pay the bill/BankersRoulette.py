import random 
str = input("Write the names of your friends who are going to pay the bill ->")
result = str.split(",")
print(result[int(random.random()*len(result))]+" is going to pay the bill.")

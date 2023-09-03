import string
import random
# Create a list containing all lowercase and uppercase alphabets
all_alphabets = [char for char in string.ascii_lowercase + string.ascii_uppercase]
symbols = ['!','@','#','$','%','&','*','(',')']
numbers = ['0','1','2','3','4','5','6','7','8','9']
a = int(input("Enter the numbers of alphabets->"))
b = int(input("Enter the numbers of symbols->"))
c = int(input("Enter the numbers of integers->"))
password_list = []
for i in range(0,a):
    password_list.append(random.choice(all_alphabets))
for i in range(0,b):
    password_list.append(random.choice(symbols))
for i in range(0,c):
    password_list.append(random.choice(numbers))
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password = ""
for i in password_list:
    password = password + i
print(f"Your Password is - {password}")

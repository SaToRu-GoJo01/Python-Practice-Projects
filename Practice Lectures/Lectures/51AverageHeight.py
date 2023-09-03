str = input("Enter the height of the students->")
heights = [int(x) for x in str.split()]
sum = 0
count = 0
for i in heights:
    sum = sum + i
    count = count + 1
print("The average height of the students =" , (sum/count))
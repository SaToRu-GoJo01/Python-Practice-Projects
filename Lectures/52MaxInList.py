int_min = float('-inf')
int_max = float('inf')
str = input("Enter the numbers->")
numbers = [int(x) for x in str.split( )]
for i in numbers:
    if(i > int_min):
        int_min = i
    else:
        int_max = i
print("The greatest and the smallest value in this list is " ,int_min ," and " , int_max ," respectively")
# 3. Write a program to read and find the largest of 3 numbers.

def largest(num1 , num2 , num3):
    if ( num1 >= num2 ) and ( num1 >= num3 ):
        largest = num1
    elif ( num2 >= num1 ) and ( num2 >= num3 ):
        largest = num2
    elif ( num3 >= num1 ) and ( num3 >= num2 ):
        largest = num3

    return largest

num1 = float(input("Enter first number: "))
num2 = float(input("enter second number: "))
num3 = float(input("enter third number: "))

print(f"largest number is {largest(num1,num2,num3)}")
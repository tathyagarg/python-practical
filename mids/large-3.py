# 3. Write a program to read and find the largest of 3 numbers.

def largest(num1 , num2 , num3):
    return max(num1, num2, num3) # Since the max func is written in C it's faster than using if statements

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

print(f"largest number is {largest(num1,num2,num3)}")

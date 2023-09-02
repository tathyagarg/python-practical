# 7. Write a program to display sum of all numbers from 1 to n

n = int(input("Enter the value of a number: "))

try:
    n = int(n)
    sum = 0
    
    for i in range(0,n+1):
        sum = sum + i
    print(f"the sum is {sum}")
except:
    print("enter non integer number / non negative / invalid")
# 7. Write a program to display sum of all numbers from 1 to n

n = int(input("Enter the value of a number: "))

try:
    n = int(n)
    sum = int(n/2*(n+1)) # Use the sum formula S = n/2 * (n+1) which gives time complexity O(1) instead of a loop which gives time complexity O(n)
    print(f"the sum is {sum}")
except ValueError: # don't use bare except clause, specify the error you are catching.
    print("enter non integer number / non negative / invalid")

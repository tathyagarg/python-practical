# 10.Take an integer input N from the user. Find Factorial of N and print it

N = int(input("enter a number: "))
factorial = 1

if N < 0:
    print("number cannot be negative.")
elif N == 0:
    print(f"factorial of {N} is 1")
elif N > 0:
    for i in range(1,N+1):
        factorial = factorial*i
    print(f"factorial of {N} is {factorial}")
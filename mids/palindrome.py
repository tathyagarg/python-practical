x = input("Enter a number: ")
if x == x[::-1]:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")
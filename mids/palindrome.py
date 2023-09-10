x = input("Enter a number: ")
print(f"{x} is {'' if x==x[::-1] else 'not '}a palindrome")

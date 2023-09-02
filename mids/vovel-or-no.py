# 4. Write a program to check given character is vowel or not.

letter = input("enter a letter: ")

vovels = ['A','E','I','O','U','a','e','i','o','u']

if letter in vovels:
    print(f"the letter {letter} is a vovel")
else:
    print(f"the letter {letter} is not a vovel")
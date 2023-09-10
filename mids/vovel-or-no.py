# 4. Write a program to check given character is vowel or not.

letter = input("enter a letter: ")
vowels = 'AEIOUaeiou'
print(f"{letter} is {'not ' if letter not in vowels else ""}a vowel")

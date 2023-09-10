"""
8. Write a program to display the following pattern using for loops.
* 1
** 22
*** 333
**** 4444
"""

def pattern(s):
    for i in range(1, s+1):
        print("*"*i, str(i)*i)

pattern(int(input("enter ending number: ")))

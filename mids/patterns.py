"""
8. Write a program to display the following pattern using for loops.
* 1
** 22
*** 333
**** 4444
"""

def p_stars(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print('* ', end="")
        for k in range(1,i+1):
            print(f'{i}', end="")
        print()

n = int(input("enter ending number"))
p_stars(n)
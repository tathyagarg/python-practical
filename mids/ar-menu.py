"""
6. Write a menu driven program to calculate:
1. Area of circle[A=πr2]
2. Area of square [A=a*a]
"""

import math

def ar_circl(unit):
    if unit == 'r':
        radius = float(input("enter the radius of the circle: "))
        ar_rcircl = math.pi * ( radius ** 2 )
        print(f"area of circle is {ar_rcircl}")
    elif unit == 'd':
        diameter = float(input("enter the diameter of the circle: "))
        ar_dcircl = math.pi * (( diameter ** 2) / 4)
        print(f"area of cirlce is {ar_dcircl}")

    return unit

def ar_square(ar_sq):
    print(f"area of circle is {ar_sq}")
    
    return ar_sq

choice = input("Do you want area of circle or square as 'cirle' or 'square'")

if choice == 'circle':
    unit = input("do you have radius or diameter as 'r' or 'd': ")
    print(ar_circl(unit))
elif choice == 'square':
    side = float(input("enter the side length: "))
    ar_sq = side ** 2
    print(ar_square(ar_sq))
else:
    print("invalid choice, please use either 'circle' or 'square'")
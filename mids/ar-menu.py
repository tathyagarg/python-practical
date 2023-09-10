"""
6. Write a menu driven program to calculate:
1. Area of circle[A=πr2]
2. Area of square [A=a*a]
"""

import math

def menu() -> tuple[int, bool|None]:
    val = int(input("1. Find area of circle\n2. Find area of square\nEnter your choice: "))
    if val == 1:
        r_d = input('Enter \'r\' for radius as input and \'d\' for diameter: ').lower()
        if r_d not in 'rd':
            print("Error")
            return
        val = val, r_d=='r'
    else: val = val, None
    return val

def circle(unit: bool) -> None:
    v = int(input(f"Enter the {['diameter', 'radius'][unit]}: "))
    print(f"Area of the circle is {math.pi * (v/(2-unit))**2:.2f}")

def square(buffer: None) -> None:
    side = int(input('Enter the length of the square\'s side: '))
    print(f"Area of the square is: {side**2}")

func_map = {1: circle, 2: square}

if __name__ == "__main__":
    f, i = menu()
    func_map[f](i)

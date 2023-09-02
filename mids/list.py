"""
13.Create a list L=[3,5,7,9,0,2,4,6]
a. Change 0 to 10
b. Add 8 at the end of the list
c. Add your name at the beggning of the list
d. Display 1st 4 elements
e. Display last 3 elements
f. display 3, 9, 4 from the list using slicing
"""

L=[3,5,7,9,0,2,4,6]

L[4] = 10
print(f'a, {L}')

L.append('8')
print(f'b, {L}')

name = 'atharv'
L.insert(0,str(name))
print(f'c, {L}')

print(f'd, {L[0:4]}')

print(f'e, {L[-3:]}')

print(f'f, {L[1:9:3]}')

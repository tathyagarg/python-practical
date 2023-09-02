'''
Write a program to input marks of 3 subjects, compute average and then calculate grades as per following guidelines:
A+ → 90% and above
A → 80 to 90 %
B → 70-79%
C → 60-69%
D → 50-59%
E → 40-49%
R → 39% and below
'''

physics_c_mech = float(input("enter marks in physics_c_mech: "))
chemistry = float(input("enter marks in chemistry: "))
calculus_bc = float(input("enter marks in calculus_bc: "))

max_ = float(input("enter maximum marks: "))

total = physics_c_mech + chemistry + calculus_bc
average = total / 3
percentage = (average/max_)*100

print(f"Your average is {average} and your percentage is {percentage}")
if percentage >= 91:
    print("Your grade is A+")
elif percentage >= 81 and percentage <= 90:
    print("Your grade is A")
elif percentage >= 71 and percentage <= 80:
    print("Your grade is B")
elif percentage >= 61 and percentage <= 70:
    print("Your grade is C")
elif percentage >= 51 and percentage <= 60:
    print("Your grade is D")
elif percentage >= 41 and percentage <= 50:
    print("Your grade is E")
elif percentage <= 40:
    print("Your grade is F. Please give RT.")
else:
    print("invalid percentage")
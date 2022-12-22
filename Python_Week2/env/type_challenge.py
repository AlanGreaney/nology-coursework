import math
import random

userFloat = float(input("Enter a float: "))

newInt = int(userFloat/5)
print(userFloat)
print(newInt)

userString = input("What... is your name?: ")
print("Hello, " + userString +  "!")

if (random.randint(1, 100) > 20):
    input("What... is your favorite colour?: ")
else:
    input("What... is the airspeed velocity of an unladen swallow?: ")

f_name = "Ben"
l_name = "Bruton"

initials = [f_name[0], l_name[0]]

print(initials)

print(f_name + " " + l_name + " -> " + initials[0] + "." + initials[1])

age = int(input("What... is your age?: "))
grade = "Get a job."
if age < 3:
    grade = "Not crying all night"
elif age < 5:
    grade = "Preschool"
elif age < 7:
    grade = "Kindergarten"
elif age < 11:
    grade = "Elementary School"
elif age < 15:
    grade = "Middle School"
elif age < 19:
    grade = "High School"
elif age < 23:
    grade = "College"

print("Age is " + str(age) + ". Life focus should be: " + grade)
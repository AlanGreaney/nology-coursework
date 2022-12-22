import math

num_1 = 1 #int
float_1 = 1.00 #float
str_1 = '1' #str
bool_1 = True #bool must be cap'd

print(num_1)
print(float_1)
print(str_1)
print(bool_1)

print(type(num_1))
print(type(float_1))
print(type(str_1))
print(type(bool_1))

from math import sqrt as sq

x = 5
y = 6
if x == y:
    print("Equal")
elif x < y:
    print("y bigger")
else:
    print("y smaller")

#ternary
age = 12
age_group = "Minor" if age < 18 else "Adult"
print(age_group)

print(sq(25))

name = "Bill"
name += "ly Shakes"

print(name)

print(name[3])

print(len(name))
print(name.upper())
print(name.lower())

print(name.replace("Bill", "Bare"))

print(name.split(" "))
print(name.lower().split("s"))

#strings are arrays
for c in name:
    print(c)

print("My name is {} and I am {} years old.".format("Steve", 25))

f_name = "Romeo"
l_name = "Montague"
print("{} was a member of the {} family.".format(f_name, l_name))

print(f"{f_name} was a member of the {l_name} family.")

print("life" in "life is but a poor player") #boolean output

input_desired = int(input("Enter a number: "))

print(type(input_desired))
print(input_desired)

new_float = float(num_1)

print(type(new_float))
print(new_float)
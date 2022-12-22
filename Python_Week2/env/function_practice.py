import math
import random

def add(num1, num2):
    return num1 + num2


print(add(5, 10))
print("10 + 10 is " + str(add(10, 10)))

def change_name():
    global name
    name = "New Name"

name = "Old Name"
change_name()
print(name)

x = lambda a,b: a + b
print(x(2, 2))

y = lambda a, b, c: a + b - c
print(y(2, 3, 4))


def multiplyFunc(n):
    return lambda x: x * n

doubler = multiplyFunc(2)
print(doubler(10))

tripler = multiplyFunc(3)
print(tripler(10))

#doing operations on individual elements of a list
my_list = [2, 3, 4]
final_list = list(map(lambda x: x * 2, my_list))
print(final_list)

list_of_numbers = range(1, 10)
evens = list(filter(lambda x: x % 2 == 0, list_of_numbers))
odds = list(filter(lambda x: x % 2 != 0, list_of_numbers))

print("-")
print(list(list_of_numbers))
print(evens)
print(odds)

from functools import reduce

sum1 = reduce((lambda a, b: a + b), [1, 2, 3])
product = reduce((lambda a, b: a * b), [3, 3, 3])

print(type(sum1))
print(type(product))
print(sum1)
print(product)

print("-")
def my_args(arg1, *args):
    for arg in args:
        print(arg)

    print(arg1)

my_args(1, 2, 3, "yon", "五")

def my_f_function(**friend):
    print("My friend is named " + friend["name"] + ". he lives at " + friend["address"])

my_f_function(address="123 Main St", name="Bob")

my_f_function(address="619 South Blvd", name="Steve")

def keyword_function(**data):
    for k, v in data.items():
        print(k + ": " + v)

keyword_function(firstName = "Herbert", lastName = "Hoover")

#kwarg = keyword arguments

def intro(**kwargs):
    for key, value in kwargs.items():
        print("My " + key + " is: " + str(value))

intro(fName="Slim", lName="Shady", age=32, location="Detroit")
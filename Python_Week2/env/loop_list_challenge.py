import math

numbers = [10, 20, 30, 40]
numbers2 = [-10, 20, -30, 40]

final_list = list(map(lambda x: round(math.sqrt(x), 2), numbers))

print(final_list)

final_final_list = list(filter(lambda x: x < 0, numbers2))

print(final_final_list)


multi_dim = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        multi_dim[i][j] = i*j

for i in range(10):
    for j in range(10):
        print(multi_dim[i][j], end=" || ")

print("-")
print("-")
print(multi_dim[5][5])

###

print("-")
print("-")

myTuple = ('Vladimir Lenin', 'Tsar Nick')

leaderDictionary = {
    myTuple: "Russia",
    ('Thomas Jefferson'): "US",
    ('Barack Obama'): "US",
    ('Tsar Nicolas III'): "Russia",
    ('John Curtin'): "Australia",
}

print(leaderDictionary)
print("-")
print("-")

###






customers = []
while True:
    user_input = input("Enter another name?: (Yes/No) ")
    user_input = user_input[0].lower()
    if user_input.lower() == "n" or user_input.lower() == "no":
        break
    else:
        first_name, last_name = input("Enter your name (first/last): ").split()
        customers.append({"first name": first_name, "last name": last_name})

print(customers)

for c in customers:
    print(c["first name"], c["last name"])

###

import time
start1 = time.time()

iterations = 20

for i in range (iterations):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(str(i))

end1 = time.time()
print("-")
print("-")

start2 = time.time()

for i in range (iterations):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if len(output) == 0:
        output = str(i)

    print(output)

end2 = time.time()

print(start1)
print(end1)
print("Method 1: " + str(end1-start1)) #11.6 seconds
print("Method 2: " + str(end2-start2)) #12.0 seconds
#bigger nums, method 2 may be faster
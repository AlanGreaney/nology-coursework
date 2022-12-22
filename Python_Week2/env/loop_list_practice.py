#list []
#tuple () locked list, unchangeable
#set {} list but unordered and unchangeable - only one of each value
#dictionaries {key, value}

nums = [1, 2, 3, 4, 5]
print(type(nums))

print(nums[1])
print(nums[0])
print(nums[-1])
print(nums[-2])


print(nums)
nums.insert(1, 9)
print(nums)

print(nums.pop()) # last
print(nums)

print(nums.pop(2)) # remove the element at index 2
print(nums)

nums.insert(1, 67)
nums.insert(1, 7)
print(nums)
nums.sort()
print(nums)

#initial : end : indexstep
#last 3
print(nums[-3::])

print(nums[-3::2])

print(nums[-3:-1:])

print("Banana"[-3::])
print("Banana"[0:3:])
print("Banana"[0::2])

###

multi_dim = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        multi_dim[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(multi_dim[i][j], end=" || ")


###

#list = only one type, less memory

import array as arr

myArray = arr.array("i", [1,2,3,4,5])

print("-")
print("-")
print(myArray)
print(type(myArray))

#append extend pop reverse count

###

my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))
print(my_tuple)

my_tuple2 = 1, 2, 3, 4, 5 #default info 
print(type(my_tuple2))
print(my_tuple2)

my_list = [1, 2, 3, 4, 5]
my_tuple3 = tuple(my_list)
print(type(my_tuple3))
print(my_tuple3)

changing_tuple = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

changing_tuple[0].append(4)
print(changing_tuple)

aTuple = 123, 321, "hi"
print(aTuple)

x, y, z = aTuple
print(x)
print(z)
print(y)

###



dictionary = {
    "firstName" : "Barrack",
    "lastName" : "Obama",
    "address" : "17 Penn Ave.",
} #unordered

dictionary["job"] = "President"

print(dictionary)
print(dictionary["lastName"])
dictionary["job"] = "Retired"
print(dictionary["job"])

print("job" in dictionary)
print("car" in dictionary)

print(dictionary.keys())
print(dictionary.values())

for k, v in dictionary.items():
    print(k, v)

print(dictionary.get("job", "No job given"))
print(dictionary.get("middle_name", "No middle name given"))

del dictionary["lastName"]

for i in dictionary:
    print(i) #keys

dictionary.clear()

print(dictionary)


###


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

words = "this is a string"
for letter in words:
    print(letter)

for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break

for fruit in fruits:
    if fruit == "banana":
        continue    
    print(fruit)

for n in range(10):
    if n % 2 == 0:
        print(n)

for n in range(1, 10):
    if n % 2 == 0:
        print(n)

for n in range(99, 107):
    print(n)

i = 10
while(i > 0):
    i-=1
    print(i)
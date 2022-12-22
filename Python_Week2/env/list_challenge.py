mixedList = [1, 2, "three", 4, 5, "six", "seven", 8, "nine", 10]

integersOnly = list(filter(lambda x: type(x) is int, mixedList))
stringsOnly = list(filter(lambda x: type(x) is str, mixedList))

print("Original list: ")
print(mixedList)
print("Method one: ")
print(integersOnly)
print(stringsOnly)

integersOnly2, stringsOnly2 = [], []
for x in mixedList:
    stringsOnly2.append(x) if type(x) is str else integersOnly2.append(x)

print("Method two: ")
print(integersOnly2)
print(stringsOnly2)
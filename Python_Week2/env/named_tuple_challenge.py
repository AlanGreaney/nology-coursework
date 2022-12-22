from collections import namedtuple

Pen = namedtuple("Pen", "size inkcolor beveled")

penOne = Pen(2, "Red", True)
penTwo = Pen(4, "Blue", True)
penThree = Pen(5, "Black", False)

print(penOne._asdict())
print(penTwo._asdict())
print(penThree._asdict())

print("Pen - Size:" + str(penOne.size) + ", Ink Color: " + penOne.inkcolor + ", Bevelling: " + str(penOne.beveled))


print("-")
print("-")
print("-")


Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=2, y=1) 
p2 = Point(x=4, y=7) 

def calculateSlope(p1, p2):
    output = "(p2.y - p1.y)/(p2.x - p1.x)"
    return output + " = " + str(eval(output))

print(p1)
print(p2)
print(calculateSlope(p1, p2))

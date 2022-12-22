from collections import namedtuple

Point = namedtuple('Point', ['x', 'y']) #class with 2uple properties
p = Point(x=11, y=22) #instance of object w/ attributes

print(type(Point))

print(p[0])
print(p[1])

x, y = p

print(x, y)


EmployeeRecord = namedtuple("EmployeeRecord", "name age title")
emp_rec = EmployeeRecord("Micheal Corleone", 45, "The Godfather")

print(emp_rec.name)
print(emp_rec.title)

Parent = namedtuple("Parent", "name children")

vito = Parent("Vito Corleone", ["Sonny", "Micheal"])

print(vito.name)
print(vito.children)

vito.children.append("Banana")
print(vito.children)

Developer = namedtuple("Developer", "name level language", defaults = ["Junior", "Python"]) #defaults assigned to 1, 2, 3, etc

dev = Developer("Steve")

print(dev)


Person = namedtuple("Person", "name age height")
john = Person._make(["John", 25, 1.75])

job_bob = Person("Joe Bob", 30, 1.8)

print(john)
print(job_bob._asdict())

job_bob2 = job_bob._replace(age=26, name="Job Bob")

print(job_bob2)

ExtendedPerson = namedtuple("ExtendedPerson", [*Person._fields, "weight"])
dave = ExtendedPerson("dave", 28, 1.75, 190)

print(dave)

for field, value in zip(dave._fields, dave):
    print(field, " -> ", value)




Car = namedtuple("Car", "doors color isAvailable")
car = Car(4, "Gray", True)

if car.doors == 4 and car.color == "Gray" and car.isAvailable:
    print("Gray Sedan Selected")



print(divmod(8,4))
print(divmod(8,3))

def custom_divmod(a, b):
    DivMod = namedtuple("DivMod", "quotient remainder")
    return DivMod(*divmod(a,b)) # the * unpacks

print(custom_divmod(8, 4))
print(custom_divmod(8, 3))

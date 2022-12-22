class Person:
    #"properties"
    name = "Ben"
    age = 37
    def intro(self):
        print("My name is " + self.name)

person1 = Person()

class Cat:
    def __init__(self, name, breed = "Alley Cat", age = 1):
        self.name = name
        self.breed = breed
        self.age = age
    numberOfLives = 9

    def meow(self):
        return self.name + " goes: Meow"

zeal = Cat("Zeal", "Street", 2)
ardor = Cat("Ardor")

def main():
    """
    print(person1.name)
    print(person1.age)
    person1.name = "Tom"
    print(person1.name)
    person1.intro()

    person1.location = "USA"
    print(person1.location)
    """


    print(zeal.name)
    print(zeal.breed)
    print(zeal.numberOfLives)
    print(ardor.breed)
    print(ardor.meow())

    print(person3)
    print(person4)

    print(person3.isAdult(person3.age))

    print(new_circle.radius)
    new_circle.radius = "5"
    print(new_circle.radius)
    print(new_circle.get_area())

from datetime import date
import math


class Circle:
    def __init__(self, radius = 0):
        self._radius = radius

    @property
    def radius(self):
        print("getter")
        return self._radius

    @radius.setter
    def radius(self, newValue):
        if newValue.isdigit():
            print("setter")
            self._radius = newValue
        else:
            print("radius not int")

    def get_area(self):
        return pow(int(self._radius), 2) * math.pi


new_circle = Circle(10)
#3.10.7

class PersonTwo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod #means it can create the class
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    #A static method doesn’t have access to the class and instance variables 
    #because it does not receive an implicit first argument like self and cls. 
    #Therefore it cannot modify the state of the object or class.
    @staticmethod
    def isAdult(age):
        return age >= 18



    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


person3 = PersonTwo("Ben", 37)
person4 = PersonTwo.fromBirthYear("Allen", 1982)



#encapsulation - prevent direct modification (getters/setters)
#inheritance - sharing properties among classes
#abstraction - reducing complexity
#polymorphism - overloading methods




if __name__ == "__main__":
    main()
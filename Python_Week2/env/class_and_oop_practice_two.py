#encapsulation - prevent direct modification (getters/setters)
#inheritance - sharing properties among classes
#abstraction - reducing complexity
#polymorphism - overloading methods #overwrite class func/etc to better fit in child class

#magic methods
#special __ methods, aka duner
#init, initialize only in classes
#__str__ for class defined in a way easy to read, outputs all members of class. debugging


#__gt__ __lt__ __add__

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print("My name is " + self.first_name + " " + self.last_name)


class Coach(Person):
    def __init__(self, first_name, last_name, cohort):

        super().__init__(first_name, last_name) #<-- child object class use
        self.cohort = cohort #<-- child only

    def welcome(self):
        print("Welcome to the " + self.cohort + ", I am your coach " + self.first_name + " " + self.last_name)
        

class Bird:
    def __init__(self, name =""):
        self.name = name

    def flight(self):
        print("There are many kinds of birds, some fly, some cannot.")

class Sparrow(Bird):
    def __init__(self, name):
        super().__init__(name)

    def flight(self):
        print("A " + self.name + " can fly")

class Ostrich(Bird):
    def __init__(self, name):
        super().__init__(name)

    def flight(self):
        print("The " + self.name + " cannot fly")

class Wallet:
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __add__(self, value2):
        return Wallet(self.value + value2.value)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


ben_person = Person("Ben", "Bruton")
coach_person = Coach("John", "Madden", "NFL")
ben_coach= Coach("Ben", "Bruton", "ASML Class")

bird = Bird()
sparrow = Sparrow("sparrow")
ostrich = Ostrich("ostrich")

my_wallet = Wallet(5000)
wallet2 = Wallet(100)
wallet3 = my_wallet + wallet2

def main():
    ben_person.print_name()
    coach_person.welcome()
    ben_coach.welcome()

    bird.flight()
    sparrow.flight()
    ostrich.flight()

    print(wallet3)


if __name__ == "__main__":
    main()
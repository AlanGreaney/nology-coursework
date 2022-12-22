class Rectange:
    def __init__(self, height = 1, width = 1):
        self._height = height
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, newValue):
        self._height = newValue

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, newValue):
        self._width = newValue

    def getArea(self):
        return self._width * self._height

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Vehicle:
    def __init__(self, modelName, year, brand):
        self.modelName = modelName
        self.year = year
        self.brand = brand

    def getInfo(self):
        print("Vehicle Type: " + str(self.year) + " " + self.brand + " " + self.modelName)

class Car(Vehicle):
    def __init__(self, modelName, year, brand, mileage):
        super().__init__(modelName, year, brand)
        self.mileage = mileage

    def getInfo(self):
        print("This is a  " + str(self.year) + " " + self.brand + " " + self.modelName + 
        " with " + str(self.mileage) + " miles.")


def main():
    rectangleObj = Rectange()
    print(rectangleObj)

    rectangleObj.width = 5
    rectangleObj.height = 10

    print(rectangleObj)
    print("-")
    print("The area of the rectangle is: " + str(rectangleObj.getArea()))

    print("-")
    print("-")

    my_old_car = Vehicle("Camry", 2011, "Toyota")
    my_new_car = Car("Miata", 1995, "Mazda", 220000)

    my_old_car.getInfo();
    my_new_car.getInfo();


if __name__ == "__main__":
    main()
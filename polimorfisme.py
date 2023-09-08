class Car:
    def _init(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def _init_(self, brand, model):
       self.brand = brand
       self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def _init(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a car class
boat1 = Boat("Ibiza", "Touring 20") #Create a car class
plane1 = Plane("Boeing", "747")     #Create a car class

for x in (car1, boat1, plane1):
    x.move()
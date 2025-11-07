""" Day 13: Advanced OOP - Inheritance & Polymorphism """

# Practice Exercise 1: Vehicle Inheritance

class Vehicle:          # Mum
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return f"{self.brand} {self.model} is starting"
    
class Car(Vehicle):     # Daughter
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def honk(self):
        return "Beep beep!"
    
class Motorcycle(Vehicle):      # Son
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def wheelie(self):
        return "Doing a wheelie"
    
car = Car("Tesla", "Model X")
print(car.start())
print(car.honk())

r7 = Motorcycle("Yamaha", "R7")
print(r7.start())
print(r7.wheelie())
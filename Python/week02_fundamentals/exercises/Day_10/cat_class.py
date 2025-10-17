""" Day 10: Object-Oriented Programming (OOP) - Part 1 """

# Practice Exercise 1: Create a Cat Class

class Cat:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def meow(self):
        return f"{self.name} says Meow!"
    
    def get_info(self):
        return self.name, self.age, self.colour
    
sparkles = Cat("Sparkles", 5, "Fluffy Grey")
smokey = Cat("Smokey", 3, "Silky Grey")

print(sparkles.meow())
print(smokey.get_info())
""" Day 10: Object-Oriented Programming (OOP) - Part 1 """

# Practice Exercise 2: Create a Rectangle Class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height
        
# Test
rect1 = Rectangle(5, 10)
rect2 = Rectangle(4, 4)

print(rect1.calculate_area())
print(rect1.is_square())
print(rect2.is_square())

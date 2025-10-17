1. DAY 10 OOP REFERENCE

# Day 10: Object-Oriented Programming (OOP) Reference

## Date: October 16, 2025

---

## What is OOP?

Object-Oriented Programming is a way to organize code using **objects** that contain both data (attributes) and functions (methods).

- **Class** = Blueprint (design)
- **Object** = Instance (actual thing created from blueprint)

---

## Pattern 1: Simple Class

### Syntax:
```python
class ClassName:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2
    
    def method_name(self):
        return something

# Create object
obj = ClassName(value1, value2)

# Use it
result = obj.method_name()

Example: Dog Class

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_age_in_dog_years(self):
        return self.age * 7

# Usage
buddy = Dog("Buddy", 3)
print(buddy.bark())                    # "Buddy says Woof!"
print(buddy.get_age_in_dog_years())    # 21

- - - 

Pattern 2: Class with Calculations

Syntax:
class ClassName:
    def __init__(self, data):
        self.data = data
    
    def calculate_something(self):
        result = # calculation with self.data
        return result

Example: Rectangle Class
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

# Usage
rect = Rectangle(5, 10)
print(rect.calculate_area())      # 50
print(rect.is_square())            # False

- - -

Pattern 3: Class with Collections

Syntax:
class ClassName:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items = [i for i in self.items if i != item]
    
    def get_items(self):
        return self.items

Example: Playlist Class
class Playlist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, title, artist):
        self.songs.append({"title": title, "artist": artist})
    
    def remove_song(self, title):
        self.songs = [s for s in self.songs if s["title"] != title]
    
    def get_song_count(self):
        return len(self.songs)
    
    def display_playlist(self):
        for song in self.songs:
            print(f"{song['title']} by {song['artist']}")

# Usage
playlist = Playlist()
playlist.add_song("Bohemian Rhapsody", "Queen")
playlist.display_playlist()

- - -

Pattern 4: Classes Working Together

Syntax:
class ClassA:
    def __init__(self, data):
        self.data = data

class ClassB:
    def __init__(self):
        self.items = []
    
    def add_item(self, obj):
        self.items.append(obj)  # obj is a ClassA object
    
Example: Library System
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def get_info(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def find_book(self, title):
        for book in self.books:
            if title == book.title:
                return book
        return None
    
    def display_books(self):
        for book in self.books:
            print(book.get_info())

# Usage
library = Library()
library.add_book(Book("Python Basics", "Author", 123))
library.display_books()

Pattern 5: Class Variables vs Instance Variables

Syntax:
class ClassName:
    class_variable = value  # Shared by ALL objects
    
    def __init__(self, param):
        self.instance_variable = param  # Unique to each object
        ClassName.class_variable += 1
    
    @classmethod
    def get_class_variable(cls):
        return cls.class_variable

Example: Student Counter
class Student:
    total_students = 0  # CLASS VARIABLE
    
    def __init__(self, name, grade):
        self.name = name      # INSTANCE VARIABLE
        self.grade = grade    # INSTANCE VARIABLE
        Student.total_students += 1
    
    def get_info(self):
        return f"{self.name}: Grade {self.grade}"
    
    @classmethod
    def get_total_students(cls):
        return cls.total_students

# Usage
s1 = Student("Alice", 85)
s2 = Student("Bob", 92)

print(s1.name)                        # "Alice" (instance)
print(s2.name)                        # "Bob" (instance)
print(Student.total_students)         # 2 (class variable - shared)

- - -

Key Concepts

__init__ Method:

Constructor/initializer
Runs automatically when object is created
Sets up initial attributes
First parameter is always self

self Parameter:

Refers to the current object
Must be first parameter in instance methods
Used to access attributes and methods

Instance Variables:

Defined in __init__ with self.
Unique to each object
Example: self.name, self.age

Class Variables:

Defined at class level (not in __init__):
Shared by all objects
Access with ClassName.variable

Instance Methods:

Functions inside a class
First parameter is self
Can access instance and class variables

Class Methods:

Decorated with @classmethod
First parameter is cls (the class itself)
Work with class variables

- - -

Common Patterns

Safe Item Removal from List:
# Don't modify list while looping
# Create new list without unwanted items
self.items = [item for item in self.items if condition]

Checking Empty Collections:
def get_average(self):
    if not self.grades:  # Check if empty
        return 0
    return sum(self.grades) / len(self.grades)

Using Comprehensions in Classes:
def get_class_average(self):
    total = sum(student.get_average() for student in self.students)
    return total / len(self.students)

Finding Items in Collections:
def find_item(self, name):
    for item in self.items:
        if item.name == name:
            return item
    return None  # After checking all items

- - -

Complete Example: Student Management System
class Student:
    total_students = 0
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
        Student.total_students += 1
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_info(self):
        return f"Name: {self.name}, ID: {self.student_id}, Grades: {self.grades}"
    
    def is_passing(self):
        return self.get_average() >= 60

class Classroom:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def get_class_average(self):
        if not self.students:
            return 0
        total = sum(student.get_average() for student in self.students)
        return total / len(self.students)
    
    def get_passing_students(self):
        return [s for s in self.students if s.is_passing()]
    
    def display_all_students(self):
        for student in self.students:
            print(student.get_info())

# Usage
math_class = Classroom()
s1 = Student("Alice", "S001")
s1.add_grade(85)
s1.add_grade(90)
math_class.add_student(s1)
math_class.display_all_students()

- - -

Quick Tips

✅ Use __init__ to set up object attributes
✅ Always use self to access attributes/methods
✅ Class variables for shared data, instance variables for unique data
✅ Use comprehensions for filtering/transforming collections
✅ Check for empty collections before calculations
✅ Return after checking all items in search methods
✅ Use @classmethod for methods that work with class variables

- - -

Common Mistakes to Avoid

❌ Forgetting self parameter in methods
❌ Not using self. to access attributes
❌ Modifying list while looping through it
❌ Returning too early in search methods
❌ Forgetting to increment class variables
❌ Using class variables when you need instance variables

- - -

End of Day 10 OOP Reference

# 1
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

# 2
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

# 3
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Bark")

# 4
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 4
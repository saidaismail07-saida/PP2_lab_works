# 1
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

# 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return 16

# 3
class Person:
    def info(self):
        print("Person")

class Student(Person):
    def info(self):
        print("Student")

# 4
class Vehicle:
    def move(self):
        print("Move")

class Car(Vehicle):
    def move(self):
        print("Drive")
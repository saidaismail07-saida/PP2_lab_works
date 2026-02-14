# 1
class A:
    pass

class B:
    pass

class C(A, B):
    pass

# 2
class Fly:
    def fly(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly, Swim):
    pass

# 3
class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass

# 4
class Read:
    pass

class Write:
    pass

class Student(Read, Write):
    pass
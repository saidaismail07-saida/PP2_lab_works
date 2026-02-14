# 1 Default argument
def power(x, p=2):
    return x ** p

# 2 Keyword arguments
def introduce(name, age):
    print(f"My name is {name}, I am {age}")

# 3 Positional parameters
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("cat", "Alice")

# 4 Optional argument
def greet(name="Guest"):
    print("Hello,", name)
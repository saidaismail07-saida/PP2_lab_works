# 1 Example: Using *args to add numbers
def add_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total

print(add_numbers(1, 2, 3))        # 6
print(add_numbers(10, 20, 30, 40)) # 100


# 2 Example: Using *args to find maximum
def find_max(*args):
    maximum = args[0]
    for number in args:
        if number > maximum:
            maximum = number
    return maximum

print(find_max(3, 7, 2, 9, 5))  # 9


# 3 Example: Using **kwargs to print student info
def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ":", value)

student_info(name="Alice", age=20, grade="A")

#4
def my_function(**kid):
  print("Her last name is " + kid["lname"])

my_function(fname = "Saida", lname = "Ismail")

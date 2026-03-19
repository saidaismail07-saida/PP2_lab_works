from functools import reduce

nums = [1, 2, 3, 4, 5]

# map
squares = list(map(lambda x: x**2, nums))
print(squares)

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# reduce
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)
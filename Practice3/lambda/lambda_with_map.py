nums = [1, 2, 3, 4]

# 1 square
print(list(map(lambda x: x*x, nums)))

# 2 double
print(list(map(lambda x: x*2, nums)))

# 3 absolute
nums2 = [-1, -2, 3]
print(list(map(lambda x: abs(x), nums2)))

# 4 power 3
print(list(map(lambda x: x**3, nums)))
# 1 sort numbers
nums = [4,1,3,2]
print(sorted(nums, key=lambda x: x))

# 2 reverse
print(sorted(nums, key=lambda x: -x))

# 3 sort by length
words = ["apple","kiwi","banana"]
print(sorted(words, key=lambda x: len(x)))

# 4 sort tuples
pairs = [(1,3),(2,1),(3,2)]
print(sorted(pairs, key=lambda x: x[1]))
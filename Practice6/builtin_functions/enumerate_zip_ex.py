words = ["cat", "dog", "fish"]

# enumerate
for i, w in enumerate(words):
    print(i, w)

# zip
nums = [1, 2, 3]
for w, n in zip(words, nums):
    print(w, n)

# type checking
x = 5
print(isinstance(x, int))
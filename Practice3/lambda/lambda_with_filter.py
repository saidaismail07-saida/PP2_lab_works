nums = [1,2,3,4,5,6]

# 1 even
print(list(filter(lambda x: x%2==0, nums)))

# 2 odd
print(list(filter(lambda x: x%2!=0, nums)))

# 3 >3
print(list(filter(lambda x: x>3, nums)))

# 4 positive
nums2 = [-2,-1,0,1,2]
print(list(filter(lambda x: x>0, nums2)))

#sets are similar to lists or dictionaries

num_set = {1,2,3,4,5}
print(3 in num_set)

nums={1,2,1,3,1,4,5,6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

"""
It is faster, using the in operator.
Sets cannot contain duplicate elements.
"""

first = {1,2,3,4,5,6}
second= {4,5,6,7,8,9}
print('first = ',first)
print('second= ',second)
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)


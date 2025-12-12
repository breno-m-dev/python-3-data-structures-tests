# 5) Basic list comprehension

# Task:
# Given the list nums = [1, 2, 3, 4, 5], create a new list where each value is multiplied by 10.

# Expected output:

# [10, 20, 30, 40, 50]

nums = [1, 2, 3, 4, 5]

#newlist = nums*10 this makes nums repeat itself 10 times like: 
#1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 

newlist = []

for i in nums:
    newlist.append(i*10)

print(newlist)
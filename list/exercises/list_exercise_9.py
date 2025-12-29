# 9) Filter even numbers

# Task:
# Given the list nums = [1, 2, 3, 4, 5, 6, 7, 8], create a new list containing only the even numbers.

# Expected output:

# [2, 4, 6, 8]

nums = [1, 2, 3, 4, 5, 6, 7, 8]
evenNumbs = []

for i in nums:
    if i % 2 != 0:
        evenNumbs.append(i)


print(evenNumbs)

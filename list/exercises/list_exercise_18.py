# this is a remake of exercise 10 but using list comprehension to solve it

#18)Remove duplicates (keep order) using list comprehension

# Task:
# Given the list values = [1, 2, 2, 3, 1, 4, 3], create a new list without duplicates, keeping the original order.

# Expected output:

# [1, 2, 3, 4]

values = [1, 2, 2, 3, 1, 4, 3]
output =[]
output = [values[i] for i in range(len(values)) if values[i] not in values[0:i:1] ]
print(output)

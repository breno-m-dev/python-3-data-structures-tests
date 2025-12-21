# this is a remake of exercise 14 
# but using list comprehension to solve it

#19)Flatten a list with list comprehension

# Task:
# Given:

# nested = [[1, 2], [3, 4], [5]]


# Create a single list containing all numbers.

# Expected output:

# [1, 2, 3, 4, 5]

nested = [[1, 2], [3, 4], [5]]

flattened = [i for sublist in nested for i in sublist]

# bellow the equivalent for, 
# just to clarify what we are doing
# for sublist in nested:
#     for i in sublist:
#         flattened.append(i)

print(flattened)
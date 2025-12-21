# 24) Flatten and filter

# Task:
# Given:

# nested = [[1, 2, 3], [4, 5], [6, 7, 8]]


# Create a flat list containing only numbers greater than 4.

# Expected output:

# [5, 6, 7, 8]


nested = [[1, 2, 3], [4, 5], [6, 7, 8]]

output = [ item for sublist in nested for item in sublist if item > 4]

print(output)
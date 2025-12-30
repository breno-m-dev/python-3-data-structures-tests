# 23) Sliding window

# Task:
# Given:
# data = (1, 2, 3, 4, 5)

# Create a tuple of overlapping windows of size 3.

# Expected output:

# ((1, 2, 3), (2, 3, 4), (3, 4, 5))

data = (1, 2, 3, 4, 5, 6, 7, 8, 9)
output = tuple( (data[index], data[index+1],data[index+2] ) for index in range(len(data) - 2) )
print(output)
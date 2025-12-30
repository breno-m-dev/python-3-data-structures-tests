# 25) Validate tuple shape

# Task:
# Given:

# points = ((1, 2), (3, 4), (5, 6))


# Check if all elements are tuples of size 2.
# Print True or False.

# Expected output:

# True
points = ((1,1), (3, 1), (5, 2))
for index in range(len(points)):
    if len(points[index]) != 2:
        print(False)
        break
    if index == len(points) -1:
        print(True)
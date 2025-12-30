
# 29) Immutable update

# Task:
# Given:

# data = (10, 20, 30, 40)


# Create a new tuple where the value 30 is replaced with 99.

# Expected output:

# (10, 20, 99, 40)

data = (10, 20, 30, 40)
output = tuple(item if item != 30 else 99 for item in data)
print(output)
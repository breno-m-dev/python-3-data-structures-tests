# 11) Filter tuple

# Task:
# Given:

# values = (5, 12, 7, 18, 3)


# Create a tuple containing only the values greater than 10.

# Expected output:

# (12, 18)

values = (5, 12, 7, 18, 3)

output = tuple(i for i in values if i > 10)
print(output)

# 10) Tuple comprehension (generator expression)

# ⚠️ Tuples don’t have real list comprehension, but they can use generator expressions.

# Task:
# Given:

# nums = (1, 2, 3, 4)


# Create a tuple containing the square of each number.

# Expected output:

# (1, 4, 9, 16)

nums = (1, 2, 3, 4)

output = tuple(i*i for i in nums )
print(output)
# 30) Tuple pipeline

# Task:
# Given:

# data = (1, 2, 3, 4, 5, 6)


# Using only tuple logic and generator expressions, create a tuple that:

# keeps only even numbers

# squares them

# Expected output:

# (4, 16, 36)

data = (1, 2, 3, 4, 5, 6)
output = tuple(item  for item in data if item %2 == 0)
print(output)
# 26) Replace values with condition

# Task:
# Given the list nums = [1, 2, 3, 4, 5],
# create a new list where:

# even numbers become "even"

# odd numbers become "odd"

# Expected output:

# ['odd', 'even', 'odd', 'even', 'odd']

nums = [1, 2, 3, 4, 5]

output = ["odd" if i % 2 != 0 else "even" for i in nums]

print(output)
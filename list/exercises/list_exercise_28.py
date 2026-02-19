# 28) Remove falsy values

# Task:
# Given the list:
# values = [0, 1, "", "hello", [], [1, 2], None]
# Create a new list containing only truthy values.
# Expected output:

# [1, 'hello', [1, 2]]


values = [0, 1, "", "hello", [], [1, 2], None]
output = [value for value in values if value]
print(output)


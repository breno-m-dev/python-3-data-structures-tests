# 25) Get vowels from a string

# Task:
# Given the string text = "list comprehension",
# create a list containing only the vowels, in order.

# Expected output:

# ['i', 'o', 'e', 'e', 'i', 'o']

text = "list comprehension"

output = [ char for char in text if char in ['a','e', 'i', 'o', 'u', 'A', 'E', 'I' 'O', 'U']]

print(output)
# 23) Uppercase words with condition

# Task:
# Given the list names = ["ana", "bob", "christopher", "eva", "bren"],
# create a list with the names in uppercase, but only those with more than 3 characters.

# Expected output:

# ['CHRISTOPHER', 'BREN']

names = ["ana", "bob", "christopher", "eva", "bren"]

output = [name.upper() for name in names if len(name) > 3]

print(output)
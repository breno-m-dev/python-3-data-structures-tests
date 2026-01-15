# 23 Find duplicated characters

# Task:
# Given:

# text = "mississippi"


# Create a set with characters that appear more than once.

# Expected output:

# {'i', 's', 'p'}

text = "mississippi"

output = set()
aux = set()
for char in text:
    if char in aux:
        output.add(char)
    else:
        aux.add(char)
print(output)
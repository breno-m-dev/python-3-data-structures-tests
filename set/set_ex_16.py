# 1️⃣6️⃣ Set of unique characters

# Task:
# Given:

# text = "programming"


# Create a set containing all unique characters excluding vowels.
# Expected output:

# {'p', 'r', 'g', 'm', 'n'}

text = "programming"
output = set()

for char in text:
    if char not in ['a','e','i','o','u']:
        output.add(char)
print(output)
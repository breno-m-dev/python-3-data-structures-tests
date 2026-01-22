# 9️⃣ Dictionary comprehension

# Task:
# Create a dictionary where keys are numbers and values are their squares.

# data = [1, 2, 3, 4]


# Expected output:

# {1: 1, 2: 4, 3: 9, 4: 16}

data = [1, 2, 3, 4]
output = { key:key*key for key in data}
print(output)
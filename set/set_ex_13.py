# 1️⃣3️⃣ Detect duplicates using a set

# Task:
# Given:

# data = [1, 2, 3, 2, 4, 1, 5]

# Create a set containing only the duplicated values.

# Expected output:

# {1, 2}

data = [1, 2, 3, 2, 4, 1, 5]
aux = []
duplicates =set()
for item in data:
    if item not in aux:
        aux.append(item)
    else:
        duplicates.add(item)

print(duplicates)
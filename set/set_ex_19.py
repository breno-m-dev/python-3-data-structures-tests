# 1️⃣9️⃣ Advanced: group values by uniqueness

# data = [1, 2, 2, 3, 3, 3, 4]
# Create two sets:
# one with values that appear exactly once
# one with values that appear more than once

# Expected output:
# unique: {1, 4}
# duplicates: {2, 3}

data = [1, 2, 2, 3, 3, 3, 4]
aux = []
duplicates = set()
unique = set()
for item in data:
    if item not in aux:
        aux.append(item)
        unique.add(item)
    else:
        duplicates.add(item)
        if item in unique:
            unique.remove(item)

print(unique)
print(duplicates)
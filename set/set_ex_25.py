# 2️⃣5️⃣Partition values using sets

# Task:
# Given:

# data = range(1, 11)

# Create two sets:
# one with even numbers
# one with odd numbers
# Expected output:

# even: {2, 4, 6, 8, 10}
# odd: {1, 3, 5, 7, 9}

data = range(1, 11)
even = list(data[1:len(data)+1:2])
odd = list(data[0:len(data)+1:2])
print(even)
print(odd)
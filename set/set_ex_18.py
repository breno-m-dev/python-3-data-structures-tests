# 1️⃣8️⃣ Advanced: remove items present in a blacklist

# Task:
# Given:

# items = {"apple", "banana", "cherry", "date"}
# blacklist = {"banana", "date"}

# Create a new set without the blacklisted items.

# Expected output:

# {'apple', 'cherry'}

items = {"apple", "banana", "cherry", "date"}
blacklist = {"banana", "date"}

items.difference_update(blacklist)
print(items)
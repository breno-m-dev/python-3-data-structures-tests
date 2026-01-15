# 2️⃣8️⃣ Boss level 🐉: validate set relationships

# Task:
# Given:
# admins = {"alice", "bob"}
# editors = {"bob", "carol"}
# users = {"alice", "bob", "carol", "dave"}

# Check and print:

# if admins is a subset of users
# if editors is a subset of users
# if admins and editors overlap

# Expected output:
# True
# True
# True
admins = {"alice", "bob"}
editors = {"bob", "carol"}
users = {"alice", "bob", "carol", "dave"}
print(admins.issubset(users))
print(editors.issubset(users))
print(not admins.isdisjoint(editors))
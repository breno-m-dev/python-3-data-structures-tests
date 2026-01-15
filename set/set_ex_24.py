# 2️⃣4️⃣ Set-based filtering with multiple conditions

# Task:
# Given:

# allowed = {"read", "write", "execute"}
# blocked = {"execute"}
# requested = ["read", "execute", "delete", "write"]


# Create a list with permissions that are allowed and not blocked.

# Expected output:

# ['read', 'write']

allowed = {"read", "write", "execute"}
blocked = {"execute"}
requested = ["read", "execute", "delete", "write"]

output = allowed.intersection(requested)
output = list(output.difference(blocked))


print(output)
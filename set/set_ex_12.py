# 1️⃣2️⃣ Set-based filtering

# allowed = {"read", "write"}
# permissions = ["read", "execute", "write", "delete"]

# Create a list containing only permissions that are allowed.
# Expected output:

# ['read', 'write']

allowed = {"read", "write"}
permissions = ["read", "execute", "write", "delete"]
output = [i for i in permissions if i in allowed]
print(output)
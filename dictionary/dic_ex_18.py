# 18️⃣ Remove specific keys

# Task:
# Remove all keys that start with _.

# data = {"_id": 1, "name": "Ana", "_temp": 99}

# Expected output:

# {"name": "Ana"}
data = {"_id": 1, "name": "Ana", "_temp": 99}
output = { k:v for k,v in data.items() if k[0] != "_"}
print(output)

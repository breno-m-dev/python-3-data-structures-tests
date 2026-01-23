# 15️⃣ Find max and min value keys

# Task:
# Find the key with the highest value and the key with the lowest value.
# data = {"a": 5, "b": 1, "c": 9}

# Expected output:

# ("c", "b")
data = {"a": 5, "b": 1, "c": 9}
output = (max(data,key = data.get), min(data,key = data.get) )

print(output)
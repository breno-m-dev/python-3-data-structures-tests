# 8️⃣ Remove keys with empty values

# Task:
# Remove keys whose value is an empty list.

# data = {"a": [1, 2], "b": [], "c": [3]}


# Expected output:

# {"a": [1, 2], "c": [3]}
data = {"a": [1, 2], "b": [], "c": [3]}

output = {key:value for key,value in data.items() if len(value) > 0}
print(output)
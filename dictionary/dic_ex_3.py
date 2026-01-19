# 3️⃣ Filter by value

# Task:
# Create a new dictionary containing only items with value greater than 10.

# data = {"a": 5, "b": 15, "c": 25, "d": 8}


# Expected output:

# {"b": 15, "c": 25}

data = {"a": 5, "b": 15, "c": 25, "d": 8}
output = { key:value for key,value in data.items() if data[key] > 10 }
print(output)
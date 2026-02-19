# 2️⃣8️⃣ Remove duplicated values

# Task:
# Create a new dictionary keeping only the first key for each value.

# data = {"a": 1, "b": 2, "c": 1, "d": 2}


# Expected output:

# {"a": 1, "b": 2}

data = {"a": 1, "b": 2, "c": 1, "d": 2}

output = dict()
for k,v in data.items():
    if v not in output.values():
        output[k] = v
print(output)

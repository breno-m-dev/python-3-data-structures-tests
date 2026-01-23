# 14️⃣Invert keys and values

# Task:
# Invert the keys and values of a dictionary.

# data = {"a": 1, "b": 2, "c": 3}

# Expected output:

# {1: "a", 2: "b", 3: "c"}
data = {"a": 1, "b": 2, "c": 3}
output = { v:k for k,v in data.items()}
print(output)
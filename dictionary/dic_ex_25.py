# 2️⃣5️⃣ Dictionary difference

# Task:
# Create a dictionary with keys that exist in d1 but not in d2.

# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"b": 2}


# Expected output:

# {"a": 1, "c": 3}

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 2}

output = { k:v for k,v in d1.items() if k not in d2.keys()}

print(output)

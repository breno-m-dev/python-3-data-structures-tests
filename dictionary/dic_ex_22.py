# 2️⃣2️⃣ Invert dictionary with lists

# Task:
# Invert the dictionary so values become keys.
# Group keys that share the same value into a list.

# data = {"a": 1, "b": 2, "c": 1}

# Expected output:

# {1: ["a", "c"], 2: ["b"]}

data = {"a": 1, "b": 2, "c": 1}
output = dict()
for k,v in data.items():
    if v in output.keys():
        output[v].append(k)
    else:
        output[v] = [k]

print(output)


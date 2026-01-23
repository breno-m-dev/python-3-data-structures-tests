# 19️⃣ Merge dictionaries (sum shared keys)

# Task:
# Merge two dictionaries.
# If a key exists in both dictionaries, sum their values.

# d1 = {"a": 2, "b": 3}
# d2 = {"b": 4, "c": 1}
# Expected output:

# {"a": 2, "b": 7, "c": 1}

d1 = {"a": 2, "b": 3}
d2 = {"b": 4, "c": 1}
keys = set(d1.keys()).union(d2.keys())

output = { k:d1[k] if k in d1 and k not in d2 
           else d2[k] if k in d2 and k not in d1 
           else d1[k]+d2[k]
           for k in keys

          }
print(output)
#second solution
d1 = {"a": 2, "b": 3}
d2 = {"b": 4, "c": 1}
keys = set(d1.keys()).union(d2.keys())
output = {
    k: d1.get(k, 0) + d2.get(k, 0)
    for k in keys
}
print(output)
# 4️⃣ Merge dictionaries

# Task:
# Merge two dictionaries. If a key exists in both, sum the values.

# a = {"x": 1, "y": 2}
# b = {"y": 3, "z": 4}

# Expected output:
# {"x": 1, "y": 5, "z": 4}

a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

c = {}
c.update(a)
c.update(b)

output = { key: a[key]+b[key] 
          if key in a and key in b
          else c[key] 
          for key in c
          }
print(output)

# in case i wanted a different key depending on the if result
# {
#     ("A_" + key if key in a else key): c[key]
#     for key in c
# }
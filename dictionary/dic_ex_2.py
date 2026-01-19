# 2️⃣ Invert dictionary

# Task:
# Swap old_keys and old_values.

# data = {"a": 1, "b": 2, "c": 3}
# Expected output:
# {1: "a", 2: "b", 3: "c"}

data = {"a": 1, "b": 2, "c": 3}
#A dicitionary is formated by Key: value, 
#so we're doing the opposite to invert them. 
#Old val means old value, 
#Meaning it's what was a value but now is a key.
#Old key is what was a key but now is a value.
output = {old_val: old_key for old_key, old_val in data.items()}
 
print(output)
# 1️⃣ Count occurrences

# Task:
# Count how many times each element appears.
# data = ["a", "b", "a", "c", "b", "a"]
# Expected output:

# {"a": 3, "b": 2, "c": 1}

data = ["a", "b", "a", "c", "b", "a"]
my_dict = {}
for i in data:
    if i not in my_dict:
        my_dict.update({i:1})
    else:
        my_dict[i] = my_dict[i] + 1

print(my_dict)
        
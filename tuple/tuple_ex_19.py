# 19) Tuple-based frequency

# Task:
# Given:

# data = ("a", "b", "a", "c", "b", "a")


# Create a tuple of (item, count) without duplicates, preserving order.

# Expected output:

# (('a', 3), ('b', 2), ('c', 1))


data = ("a", "b", "a", "c", "b", "a")

used = []
output = []
for item in data:
    if item not in used:
        output.append((item, data.count(item)))
        used.append(item)
output = tuple(output)
print(output)
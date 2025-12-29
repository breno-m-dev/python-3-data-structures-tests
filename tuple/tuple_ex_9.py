# 9) Nested tuples

# Task:
# Given:

# data = (
#     ("Alice", 25),
#     ("Bob", 30),
#     ("Carol", 27)
# )


# Print only the names.

# Expected output:

# Alice
# Bob
# Carol

data = (
    ("Alice", 25),
    ("Bob", 30),
    ("Carol", 27)
)

for sub_tup in data:
    print(sub_tup[0])
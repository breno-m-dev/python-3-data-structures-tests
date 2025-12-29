# 13) Nested loop with lists

# Task:
# Given:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# Print all elements, one per line.

# Expected output:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for i in matrix:
    for k in i:
        print(k)
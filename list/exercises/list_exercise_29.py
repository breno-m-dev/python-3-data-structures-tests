# 29) Transpose a matrix

# Task:
# Given:

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# Create a transposed version of the 
# matrix using list comprehension.

# Expected output:

# [[1, 4], [2, 5], [3, 6]]


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = [
    [ row[col] for row in matrix ]
    for col in range(len(matrix[0]))
]

print(transposed)
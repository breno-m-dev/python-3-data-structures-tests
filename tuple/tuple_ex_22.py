# 22) Transpose a tuple matrix

# Task:
# Given:

# matrix = (
#     (1, 2, 3),
#     (4, 5, 6)
# )


# Create the transposed version using tuple-based logic.

# Expected output:

# ((1, 4), (2, 5), (3, 6))

matrix = (
    (1, 2, 3),
    (4, 5, 6)
)


output = tuple( tuple(row[col] for row in matrix)
                    for col in range(len(matrix[0]))  )
                        

print(output)

        
# row  = (1, 2, 3) - > (4, 5, 6)

# row[0] = (1,4)
# row[1] = (2,5)
# row[2] = (3,6)

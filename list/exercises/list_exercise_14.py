# 14) Flatten a list

# Task:
# Given:

# nested = [[1, 2], [3, 4], [5]]


# Create a single list containing all numbers.

# Expected output:

# [1, 2, 3, 4, 5]

nested = [[1, 2], [3, 4], [5]]
output = []
for i in nested:
    print(i)
    for k in i:
        output.append(k)

print(output)
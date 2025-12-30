# 18) Remove consecutive duplicates

# Task:
# Given:

# data = (1, 1, 2, 2, 2, 3, 1, 1)


# Create a new tuple with consecutive duplicates removed.

# Expected output:

# (1, 2, 3, 1)
data = (1, 1, 2, 2, 2, 3, 1, 1)
output = []

for index in range(len(data)):
    if index > 0:
        if data[index] != data[index-1]:
            output.append(data[index])
    else:
        output.append(data[index])
output = tuple(output)
print(output)
# 16) Rotate a list

# Task:
# Given the list items = [1, 2, 3, 4, 5],
# rotate it one position to the left.

# Expected output:

# [2, 3, 4, 5, 1]

items = [1, 2, 3, 4, 5]
output =[]
            #list [starting value : ending value : step]
output.extend(items[1 : len(items) : ])
output.append(items[0])
print(output)
        
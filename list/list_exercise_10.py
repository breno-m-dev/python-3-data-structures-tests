# 10) Remove duplicates (keep order)

# Task:
# Given the list values = [1, 2, 2, 3, 1, 4, 3], create a new list without duplicates, keeping the original order.

# Expected output:

# [1, 2, 3, 4]

values = [1, 2, 2, 3, 1, 4, 3, 2, 2, 2, 2]

repeatedValues = values.copy()#temporary list to help us doing this operation
output = []

for i in values:

    if i not in output: 
            output.append(i)  

print(output)
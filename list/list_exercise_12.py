# 12) Find common elements

# Task:
# Given:

# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7]


# Create a list containing the elements that appear in both lists.

# Expected output:

# [4, 5]


a = [1, 2, 3, 4, 5]
b = [4, 4, 5, 6, 7]
output =[]

for i in a:
    for k in b:
        #the "k not in output" is to avoid adding a value multiple times, For the exercise it's not needed, but I thought it was a nice touch
        if k == i and k not in output:
                output.append(k)

print(output)
# 1️⃣1️⃣ Remove duplicates from multiple lists

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# list3 = [4, 5, 6, 7]

# Create a set containing all unique values from all lists.

# Expected output:

# {1, 2, 3, 4, 5, 6, 7}

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]

#sets by default already don't repeat values. So we just have to
#add all lists and make a set out of it
output = set(list1 + list2 + list3)
print(output)
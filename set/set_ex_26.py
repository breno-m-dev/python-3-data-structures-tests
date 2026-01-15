# 2️⃣6️⃣

# Advanced: detect overlap in many lists
# Given:
# lists = [
#     [1, 2, 3],
#     [2, 3, 4],
#     [3, 4, 5]
# ]

# Create a set with values that appear in all lists.

# Expected output:
# {3}

lists = [
    [1, 2, 3],
    [2, 3, 4, 1],
    [3, 4, 5, 1]
]
output = set()

list_of_sets= []
for sub_list in lists:
    list_of_sets.append(set(sub_list))

output.update(list_of_sets[0])

for index in range(1,len(list_of_sets),1):
    output.intersection_update(list_of_sets[index])
print(output)
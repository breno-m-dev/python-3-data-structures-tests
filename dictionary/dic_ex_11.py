# 11️⃣ Count occurrences

# Task:
# Given a list of words, create a dictionary counting how many times each word appears.

# data = ["cat", "dog", "cat", "bird", "dog", "cat"]


# Expected output:

# {"cat": 3, "dog": 2, "bird": 1}

def count_occurence(in_list, counted_item):
    count = 0
    for i in in_list:
        if i == counted_item:
            count += 1
    return count

data = ["cat", "dog", "cat", "bird", "dog", "cat"]
#in the following dictionary comprehension set(data) is used
#because set data structures do not have repeated values
output = { key:count_occurence(data, key) for key in set(data)}
print(output)

#SECOND SOLUTION
data = ["cat", "dog", "cat", "bird", "dog", "cat"]
output = {}

for item in data:
    output[item] = output.get(item, 0) + 1

print(output)

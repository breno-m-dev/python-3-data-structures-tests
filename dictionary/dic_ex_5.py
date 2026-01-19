# 5️⃣ Group values by key

# Task:
# Group values that share the same key.

# data = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]

# Expected output:

# {"a": [1, 3], "b": [2, 4]}


#first solution
#data = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
# output = {}
# for tup in data:
#     output[tup[0]] = []
# for tup in data:
#     output[tup[0]].append(tup[1])
# print(output)

data = [("a", 1), ("b", 2), ("a", 3), ("b", 4)]
output = {}
for key, value in data:
    #setdefault returns a reference to the value
    #linked to the sent key. 
    # Since we made a list(an empty one)
    #we can use .append() on the same line we do setdefault().
    #Since setdefault NEVER deletes or replace values, 
    #This works well
    output.setdefault(key, []).append(value)

print(output)
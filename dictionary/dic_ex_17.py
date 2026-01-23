# 17️⃣ Group words by length

# Task:
# Group words by their length.

# data = ["hi", "hello", "hey", "world"]


# Expected output:

# {
#   2: ["hi"],
#   3: ["hey"],
#   5: ["hello", "world"]
# }
data = ["hi", "hello", "hey", "world"]
output = dict()
for i in data:
    if len(i) in output:
        output[len(i)].append(i)
    else:
        output[len(i)] = [i]
print(output)

#second solution

output = {}

for word in data:
    output.setdefault(len(word), []).append(word)
print(output)

#third solution

from collections import defaultdict

#the following line, says that everytime a
#key that isnt in output is used. The system
#will create that key inside output, and the value
#associated to it will be an empty list
output = defaultdict(list)

for word in data:
    output[len(word)].append(word)

print(dict(output))
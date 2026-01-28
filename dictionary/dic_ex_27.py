# 2️⃣7️⃣ Group numbers by parity

# Task:
# Group numbers into "even" and "odd" keys.

# data = [1, 2, 3, 4, 5]


# Expected output:

# {"odd": [1, 3, 5], "even": [2, 4]}

data = [1, 2, 3, 4, 5]
output = {"odd":[], "even":[]}
for i in data:
    #checks if i is multiple of 2
    if i % 2 == 0:
        output["even"].append(i)
    else:
        output["odd"].append(i)
print(output)
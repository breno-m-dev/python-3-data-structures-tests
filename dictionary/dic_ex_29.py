# 2️⃣9️⃣ Normalize values (sum = 1)

# Task:
# Normalize values so their sum equals 1.

# data = {"x": 2, "y": 3}


# Expected output:

# {"x": 0.4, "y": 0.6}

data = {"x": 2, "y": 3}
# The following expression explains the solution
# To solve this it was considered the values 3 and 2
# but it works for any positive numeric value
# (2+3) = 5 = total ->  (2+3)/5 = 1 = total/total
total = sum(data.values())

output = {
    k: v / total
    for k, v in data.items()
}
print(output)
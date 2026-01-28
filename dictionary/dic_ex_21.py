# 2️⃣1️⃣ Count word lengths

# Task:
# Create a dictionary where the keys are words and the values are their lengths.

# data = ["apple", "hi", "banana"]


# Expected output:

# {"apple": 5, "hi": 2, "banana": 6}

data = ["apple", "hi", "banana"]

output = { item:len(item) for item in data}
print(output)
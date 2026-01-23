# 1️⃣3️⃣ Filter per value

# Create a new dictionary where values are bigger than 50

# data = {"math": 80, "history": 40, "science": 90}


# Expected output:

# {"math": 80, "science": 90}

data = {"math": 80, "history": 40, "science": 90}
output = { k:v for k,v in data.items() if v > 50}
print(output)
# 2️⃣3️⃣ Filter keys by substring

# Task:
# Create a new dictionary containing only keys that contain "id".

# data = {"user_id": 10, "name": "Ana", "order_id": 99}


# Expected output:

# {"user_id": 10, "order_id": 99}

data = {"user_id": 10, "name": "Ana", "order_id": 99}
output = {k:v for k,v in data.items() if "id" in k}
print(output)

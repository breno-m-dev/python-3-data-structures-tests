# 2️⃣6️⃣ Nested value extraction

# Task:
# Create a dictionary mapping names to ages.

# data = {
#     "Alice": {"age": 25, "country": "Brazil"},
#     "Bob": {"age": 30, "country": "USA"}
# }

# Expected output:

# {"Alice": 25, "Bob": 30}

data = {
    "Alice": {"age": 25, "country": "Brazil"},
    "Bob": {"age": 30, "country": "USA"}
}
output = {}
for k,v in data.items():
    output[k] = data[k]["age"]
print(output)
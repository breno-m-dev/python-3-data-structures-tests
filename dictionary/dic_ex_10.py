# 🔟 Nested dictionary update

# Task:
# Update Alice’s age to 26.

data = {
    "Alice": {"age": 25, "country": "Brazil"},
    "Bob": {"age": 30, "country": "USA"}
}

# Expected output:
# {
#     "Alice": {"age": 26, "country": "Brazil"},
#     "Bob": {"age": 30, "country": "USA"}
# }

data["Alice"]["age"] = 26
print(data["Alice"])
# 16️⃣ Update with fallback

# Task:
# Increase the value of the key "views" by 1.
# If the key does not exist, it should start at 1.

# data = {}
# Expected output:

# {"views": 1}
data = dict()
data["views"] = data.get("views",0) + 1
print(data)
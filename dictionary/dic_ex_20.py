# 20️⃣ Normalize values

# Task:
# Create a new dictionary where each value is divided by the total sum of all values.

# data = {"a": 2, "b": 3, "c": 5}


# Expected output:

# {"a": 0.2, "b": 0.3, "c": 0.5}
data = {"a": 2, "b": 3, "c": 5}
sum_data = sum(data.values())
output ={ k:v/sum_data  for k,v in data.items()}
print(output)
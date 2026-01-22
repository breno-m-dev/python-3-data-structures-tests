# 7️⃣ Find max value key

# Task:
# Find the key with the highest value.
# data = {"a": 10, "b": 30, "c": 20}
# Expected output:

# "b"

data = {"a": 10, "b": 30, "cd": 20}
output = None

for key in data:
    #it's important to use data.get() and not data[output]
    #since on first loop output is 0, and this is not a key in data
    if data[key] > data.get(output,0):
        output = key
print(output)

#alternative solution
print(max(data, key=data.get))
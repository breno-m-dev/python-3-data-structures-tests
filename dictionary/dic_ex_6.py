# 6️⃣ Count characters (ignore spaces)

# Task:
# Count how many times each character appears (ignore spaces).
# text = "hello world"

# Expected output:

# {"h": 1, "e": 1, "l": 3, "o": 2, "w": 1, "r": 1, "d": 1}

text = "hello world"
output = {}
for char in text:
    if char not in output:
        output.update({char:1})
    else:
        output[char] = output[char] + 1
if " " in output:
    output.pop(" ")
print(output)
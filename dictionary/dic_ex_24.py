# 2️⃣4️⃣ Count character frequency (ignore case)

# Task:
# Count how many times each character appears, ignoring case.

# text = "AaBbA"


# Expected output:

# {"a": 3, "b": 2}

text = "AaBbA"
output = dict()

for char in text.lower():
    output[char] = output.get(char,0) + 1

print( output)
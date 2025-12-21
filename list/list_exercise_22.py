# 22) Length of each word

# Task:
# Given the list words = ["python", "rust", "code", "list"],
# create a list containing the length of each word.

# Expected output:
# [6, 4, 4, 4]

words = ["python", "rust", "code", "list"]

output = [len(word) for word in words]

print(output)
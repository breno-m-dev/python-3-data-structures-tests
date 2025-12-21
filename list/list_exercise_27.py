# 27) Index + value

# Task:
# Given the list letters = ["a", "b", "c", "d"],
# create a list of strings in the format "index:value".

# Expected output:

# ['0:a', '1:b', '2:c', '3:d']

letters = ["a", "b", "c", "d"]

output = [ str(index)+":"+letters[index] for index in range(len(letters)) ]

print(output)
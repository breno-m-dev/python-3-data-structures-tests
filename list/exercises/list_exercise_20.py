
# this is a remake of exercise 15 but using list comprehension to solve it

# 15) Find the index of all occurrences with list comprehension

# Task:
# Given the list letters = ["a", "b", "a", "c", "a"],
# find all indexes where "a" appears.

# Expected output:
# [0, 2, 4]

letters = ["a", "b", "a", "c", "a"]

output = [index for index in range( len ( letters ) ) if letters[index] == 'a']

print(output)
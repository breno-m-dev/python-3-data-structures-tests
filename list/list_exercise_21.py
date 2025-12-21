# 21) Squares of even numbers

# Task:
# Given the list nums = [1, 2, 3, 4, 5, 6], create a new list containing the square of only the even numbers.

# Expected output:

# [4, 16, 36]


nums = [1, 2, 3, 4, 5, 6]
output =[ ( i*i ) for i in nums if i % 2 == 0 ]
print(output)
# this is a remake of exercise 9 but using list comprehension to solve it

# # 17) Filter even numbers with list comprehension

# # Task:
# # Given the list nums = [1, 2, 3, 4, 5, 6, 7, 8], create a new list containing only the even numbers.

# # Expected output:

# # [2, 4, 6, 8]
nums = [1, 2, 3, 4, 5, 6, 7, 8]
output = [x for x in nums if x % 2 == 0]
print(output)
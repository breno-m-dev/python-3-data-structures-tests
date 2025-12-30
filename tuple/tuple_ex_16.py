# 16) Swap pairs in a tuple

# Task:
# Given the tuple:

# data = (1, 2, 3, 4, 5, 6)


# Create a new tuple where every pair of elements is swapped.

# Expected output:

# (2, 1, 4, 3, 6, 5)

data = (1, 2, 3, 4, 5, 6)
# index_even = tuple( data[index] for index in range(len(data))  if index % 2 == 0)
# index_odd = tuple( data[index] for index in range(len(data))  if index % 2 != 0)
print(index_even)

output = tuple( data[index+1] if index % 2 == 0  and index + 1 < len(data) 
                else data[index-1] for index in range(len(data)))
print(output)

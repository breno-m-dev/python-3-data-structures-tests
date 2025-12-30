# 24) Group by index parity

# Task:
# Given:

# data = ("a", "b", "c", "d", "e", "f")


# Group elements by even index and odd index into two tuples.

# Expected output:

# (('a', 'c', 'e'), ('b', 'd', 'f'))

data = ("a", "b", "c", "d", "e", "f")

# MY first solution
# output = ( tuple( data[index] for index in range(0, len(data), 2)  ),
#                 tuple( data[index] for index in range(1, len(data), 2)  ) )

# Second solution, which is a bit more elegant
output = (data[::2], data[1::2])
print(output)
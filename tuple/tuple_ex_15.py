# 15) Advanced unpacking

# Task:
# Given:

# values = (1, 2, 3, 4, 5)


# Unpack it so that:

# first gets 1

# middle gets (2, 3, 4)

# last gets 5

# Then print all three.

# Expected output:

# 1
# (2, 3, 4)
# 5
values = (1, 2, 3, 4, 5)
(out_1, *out_2, out_3) = values
print(out_1)
print(out_2)
print(out_3)
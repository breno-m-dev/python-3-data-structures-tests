# 26) Rotate a tuple

# data = (1, 2, 3, 4, 5)

# Rotate the tuple two positions to the right.

# Expected output:

# (4, 5, 1, 2, 3)

data = (1, 2, 3, 4, 5)
output = (data[-2],) + (data[-1],) + data[0:-2:] 
print(output)
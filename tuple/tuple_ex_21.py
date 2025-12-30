# 21) Flatten a tuple of tuples

# Given: data = (((1,(33, 0, 2)), 2), (3, 4), (), (5,))

# Create a flat tuple containing all numbers.

# Expected output:
# (1, 33, 0, 2, 2, 3, 4, 5)

def unpack_tuple(tup):
    output = []

    for item in tup:
        if isinstance(item, tuple):
            output.extend(unpack_tuple(item))
        else:
            output.append(item)
    return output

data = (((1,(33, 0, 2)), 2), (3, 4), (), (5,))
output = tuple(unpack_tuple(data))
print(output)


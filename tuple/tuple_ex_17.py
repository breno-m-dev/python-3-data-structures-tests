# 17) Chunk a tuple

# Task:
# Given:

# data = (1, 2, 3, 4, 5, 6, 7)


# Split the tuple into chunks of size 2.
# If the last chunk is incomplete, keep it as is.

# Expected output:

# ((1, 2), (3, 4), (5, 6), (7,))

data = (1, 2, 3, 4, 5, 6, 7)

output = []
#The index will be incremented by 2 every loop. So it will be 0 -> 2 -> 4 ...
for index in range(0, len (data), 2): 
    if index + 1 < len(data):
        output.append((data[index],data[index + 1]))
    else:
        output.append((data[index],))

output = tuple(output)
print(output)
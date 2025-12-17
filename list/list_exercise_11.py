# 11) Reverse a list manually

# Task:
# Given the list data = [10, 20, 30, 40], create a new list that is the reverse of it.
# ⚠️ Do not use reverse() or slicing.

data = [10, 20, 30, 40]
output=[]
for i in range( -1,  (-len( data )) -1, -1 ):
    output.append(data[i])
    print(i)

print(output)
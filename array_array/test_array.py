from array import array

array1 = array("w", ["o", "i", "e"])
#array1.append(1) gives an error, since each array can only acept 1 type of variable
print(array1[0])

for i in array1:
    print(i)
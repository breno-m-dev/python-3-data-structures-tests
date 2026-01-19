# list1 = [1,2,3]
# list2 = list1.copy()
# list2.append(4)

# print(list1)

# list1 = [[1,2,3]]
# list2 = list1.copy()
# list2[0].append(4)

# print(list1)

list1 = [[1,2,3]]
#shallow copy of the SUBLIST [0] 
#of list1 not the list1 itself
list2 = list1[0].copy() 
list2.append(4)

print(list1)


import copy
list1 = [[1,2,3]]
#The only deep copy on these tests
list2 =  copy.deepcopy(list1) 
list2.append(4)
                
print(list1)

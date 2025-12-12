#a set of tests to have a better understanding of how to join one list into another
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]


#this joins list2 on list1
list1 = list1 + list2
print(list1)

list1 = ["a", "b", "c"]

#a more complex way of doing it
for i in list1:
    list2.append(i)

print(list2)

list1 = ["a", "b", "c"]

#the most simple way
list1.extend(list2)
print(list1)
#a set of tests to have a better understanding of how references on lists works

list1 =["orange", "blue", "yellow"]
list2 = ["pink", "purple", "green"]

#if I do the following, list3 will be a reference to list1
#meaning any changes made in list3 will affect list1

list3 = list1
list3.append("cyan")
print("list1: "+ str(list1))
print("list3: "+ str(list3))
print("................................................")

#If I do the following, list3 will be a copy not a reference, so changes in list3
# will only affect list3

list1 =["orange", "blue", "yellow"]

list3 = list1.copy()
list3.append("cyan")
print("list1: "+ str(list1))
print("list3: "+ str(list3))
print("................................................")

#the following doesn't make any reference; It creates a new list by concatenating list1 and list2
#so changes on each list only alter themselves
list3 = list1 + list2
print(list3)

list3.append("red")
print("list1: "+ str(list1))
print("list2: "+ str(list2))
print("list3: "+ str(list3))
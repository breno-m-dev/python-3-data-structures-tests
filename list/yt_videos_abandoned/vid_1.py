#####################################
######## List declaration and indexes 
list = []
list = [1, 2.2, "Jerryyy","Jerryyy", False, "Who is this?"]

# print(list[0])
# print(list[4])

# print(list[-1])
# print(list[-5])

#####################################
######## Going through a list with a loop
# for item in list:
#     print(item)

### print(list[0])
### print(list[1])
### print(list[2])
### print(list[3])
### print(list[4])

# for index in range(len(list)):
#     print(list[index])

# for index in range(-1,-(len(list)+1),-1):
#     print(list[index])

# for index in [-1,-2,-3,-4,-5]:
#       print(list[index])

#####################################
######## Adding elements to a list
# list.append("Pretzels make me thirsty")
# print(list)

# list.insert(2,"Beets")
# print(list)

# list2 = [5, 4.4]
# list.extend(list2)
# print(list)


###list.extend( [5,4.4] )

# list2 = [5, 4.4]
# list = list + list2
# print(list)

#####################################
######## Removing elements from a list
###list = [1, 2.2, "Jerryyy","Jerryyy", False, "Who is this?"]


# list.remove("Jerryyy")
# print(list)

###DO NOT DO IT LIKE THIS
# for item in list:
#     if item == "Jerryyy":
#         list.remove("Jerryyy")
# print(list)

# list2 = []
# for item in list:
#     if item != "Jerryyy":
#         list2.append(item)

###list = [1, 2.2, "Jerryyy","Jerryyy", False, "Who is this?"]
# remov_count = 0
# for index in range(len(list)):
#     if list[index - remov_count] == "Jerryyy":
#         list.remove("Jerryyy")
#         remov_count += 1
# print(list)


# print(  ("Jerryyy" in list)  )
# while ("Jerryyy" in list):
#     list.remove("Jerryyy")
# print(  ("Jerryyy" in list)  )
# print(list)

####list.pop()
####list.clear()

#####################################
######## List slicing

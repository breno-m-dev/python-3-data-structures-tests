# 6) Remove elements

# Task:
# Given the list animals = ["cat", "dog", "rat", "elephant"],
# remove "rat" and print the list.

# Expected output:

# ['cat', 'dog', 'elephant']

animals = ["cat", "dog", "rat", "elephant","rat","desert rat"]

#animals.remove("rat")#removes only first occurence of rat

#this is used to not get list index out of range because we will remove values from list
#so its size will be reduced

deletion_counter = 0
#following delets "rat" but not names that contain rat like "desert rat"

for i in range(len(animals)):
    if animals[i - deletion_counter] == "rat":
        animals.pop(i - deletion_counter)
        deletion_counter = deletion_counter + 1
        
print(animals)

# to include names that contain "rat" substring, use the following if inside the for
# if "rat" in animal[i - deletion_counter]: 
#exercise 3

# 3) Count elements

# Task:
# Given the list fruits = ["apple", "grape", "banana", "grape", "orange", "grape"], count how many times "grape" appears.

# Expected output:

# 3

fruits = ["apple", "grape", "banana", "grape", "orange", "grape"]

print(fruits.count("grape")) # count can be usefull

#lets test it with upper case, also trying to catch words like  "grapefruit"

fruits2 = ["apple", "Grape", "banana", "graPe", "orange", "grapefruit", "grapeorange", "wild grapes"]

#we're gonna make all letters lower case to make the count case insensitive 

fruits2LowerCase = []
#print(fruits2.lower())
for i in fruits2:
    fruits2LowerCase.append(i.lower())
    
    
#print(fruits2LowerCase.count("grape"))#this  does NOT count "grapefruit", "grapeorange" nor "wild grapes"

#the following is used to check how many words contains the grape string in it.
counter = 0
for i in fruits2LowerCase:
    if "grape" in i: #in check if the word "grape" is in the string i. We could also use the str function .find()
        counter = counter + 1

print(counter)


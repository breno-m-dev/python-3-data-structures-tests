# 15) Find the index of all occurrences

# Task:
# Given the list letters = ["a", "b", "a", "c", "a"],
# find all indexes where "a" appears.

# Expected output:

# [0, 2, 4]
letters = ["a", "b", "a", "c", "a"]
temp = letters.copy()
indexes =[]
i=0
while (True):
    try:
        i = letters.index("a", i) # letter that is being searched, starting index to look)
        indexes.append(i)
        #we have to increment i in 1, because it's beeing used as starting index of search in the index functioin
        #if we don't increment letters.index() would return the exact same value every single loop
        # in the ["a", "b", "a", "c", "a"], on the first iteration of the loop, "i" will be 0,
        # on the second iteration "i" will start as the value 1, meaning the function index will
        # find the first occurance of "a" from index 1 and forward on the list. If it wasnt incremented
        # the function would be in an infinite loop of index returning the value 0
        i += 1 
    except ValueError:
        break
print(indexes)
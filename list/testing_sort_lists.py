#a set of tests to have a better understanding of  List's sort function.

list1 = ["Porcupine","alligattor", "Cow", "cat", "bee", "boar", "Anaconda"]

list1.sort() # This is case sensitive. Prioritezes Upper case as first. Then considers alphabetical order. In this case Cow will come before
#all becose it starts with upper case.

print(list1)

list1.sort(reverse=True)
print (list1)

list1.sort(key = str.lower)#case insensitive version of sort

print(list1)


# The following sort uses a customized key, to organize the list based on the quantity of letters "a" in each word.
# The .lower function, is used so the count function receives all letters in lower case. This is made so the counter
# counts both upper and lower case "a"s.

list1.sort(key = lambda in_str: in_str.lower().count("a"), reverse=True)
print(list1)
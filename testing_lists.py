#This code is just a set of tests I made to understand python's lists with more depth.

list1 = [1 , 2 , "i"]
x = None
for i in list1:
    #x = x + i #gives the error : "unsupported operand types(s) for +: 'int' and 'str'"
    #x = x + str(i) # gives the error: "unsupported operand type(s) for +: 'NoneType' and 'str'"
    #x = int(x) +int(i) # doesn't work aswell.
    x = str(x) + str(i) # This works, but treats the int values 1 and 2 as str
print(x)

list2= ["1", "2", "oioi"]
print(list2[0]+list2[1]+list2[2])


#x = "" #converts x to str
x = list2[0]+list2[1]+list2[2] # here x becomes also could become a str, so the line above is negligible. Types in python are wild.
print(x)

print("................................")

x=""

for i in list2:
    x = x + i #this works
    
print("concatenating list2 values \n" + x)

list3 =["oioi", "tiautiau", "hihi"]

x=""
for i in list3:
    x = x + i

print("Concatenating list 3 values \n" + x)
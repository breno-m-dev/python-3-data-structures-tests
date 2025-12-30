
# 27) Tuple-based zip

# Task:
# Given:

# a = (1, 2, 3)
# b = ("x", "y", "z")

# Create a tuple of paired elements without using zip().
# Expected output:

# ((1, 'x'), (2, 'y'), (3, 'z'))
a = (1, 2, 3)
b = ("x", "y", "z", "a", "b")
#assuming a and b are the same lenght
if len(a) >= len(b):
    #this is used to fill up the "void", in case one tuple is bigger than the other.
    #So we can still organize the tuples in pairs for all values, regardless of both tuples sizes.
    
    none_tup = tuple( None for i in range(len(a) - len(b)) )
    output = tuple( (a[index],(b+none_tup)[index]) for index in range(len(a)) )
    print( output )

#in case b is bigger in lenght than a
else:
    none_tup = tuple( None for i in range(len(b) - len(a)) )
    output = tuple( (( a+none_tup)[index] , b[index] ) for index in range(len(b)) )
    print( output )




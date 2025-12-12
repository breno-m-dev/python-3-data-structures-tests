# So on tutorials if i use a list.index(value), they say it will return the 
# index of the first ocurrance of that value.

# But in the following code I have the exit 0 1 2 3 4. In my opinion it should be 0 1 2 1 4. 
# Since the blue occurs the first time on 0 not on 3.

colors = ["red", "blue", "green", "blue", "pink"]
for i in colors:
    print(i)
    print(colors.index(i))
        
print(colors)
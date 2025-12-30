# <!-- 
# 28) Pattern detection

# Task:
# Given:

# data = (1, 2, 3, 1, 2)


# Check if the tuple ends with the same pattern it starts with ((1, 2)).

# Expected output:

# True -->

data = (1, 2, 3, 1, 2)

if((data[0],data[1]) == (data[-2] , data[-1] )):
    print(True)
else:
    print(False)
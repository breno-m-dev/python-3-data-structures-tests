#I used this script to easily create a file
#for each exercise I plan to do.
#Usually I do 30 exercises per topic.
import os

start = 2
end = 30
for i in range(start,end+1,1):
    open("dic_ex_"+ str(i) + ".py", "w")

#this is not a list, but it's more effectiuve than one, if there's a lot of numbers involved. Like a list with all integers
#from 1 to 100
range_test = range(10) 


#this prints the text "range(0,10)""
print (range_test) 

#this actually prints all numbers from 0 to 9. not 10 though. Showing it always stop 1 number before the limit.
for i in range_test:
    print(i)


#range_test = range(start = 3, stop = 21.7, step = 1.1) # Step cannot be a float value, it must be an integer
#range_test = range(start = 3, stop = 22, step = 2) gives an error because these are not expositional parameters
#range_test = range(3, 22, 200) this doesnt give an error, but will only generate the first number. Since the step is bigger than the stop limmit

range_test = range(3, 22, 2)

for i in range_test:
    print(i)


text = "wuba lub dub dub"

for i in range(len(text)):
    print(text[i])
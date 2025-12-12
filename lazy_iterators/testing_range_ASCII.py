

#ord() gest the ASCII code for the letter sent as an argument
#chr() treats the argument as a ASCII code character
for i in range(ord("A"), ord("Z") + 1):
    print(chr(i))

for i in range(ord("A"), ord("z") + 1, 3):
    print(chr(i))
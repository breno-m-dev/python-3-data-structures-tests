# 4) Replace a value

# Task:
# Create a list colors = ["red", "blue", "green"].
# Replace "blue" with "yellow" and print the list.

# Expected output:

# ['red', 'yellow', 'green']

colors = ["red", "blue", "green"]

colors[1] = "yellow"

print(colors)

#the following is a way to do it in a more generic way. To replace it anywhere
colors = ["red", "blue", "green", "blue", "pink"]
for i in colors:
    print(i)
    print(colors.index(i))
    if i == "blue":
        colors[colors.index(i)] = "yellow"
        

print(colors)

for i in range(len(colors)):
    if colors[i] == "blue":
        colors[i] = "yellow"
print(colors)
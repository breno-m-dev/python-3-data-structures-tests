# 8️⃣ Unique words in a sentence

# Task:
# Given the sentence:

# text = "sets are cool and sets are fast"


# Create a set containing all unique words.

# Expected output:

# {'sets', 'are', 'cool', 'and', 'fast'}
my_set = set()
text = "sets are cool and sets are fast"
word_start =0
for i in range(len(text)):
    if text[i] == " ":
        my_set.add(text[word_start: i : ])
        word_start = i+1
    elif i == len(text)-1:
        my_set.add(text[word_start:: ])
print(my_set)
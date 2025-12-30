# 20) Deep unpacking

# Task:
# Given:

# record = ("Alice", (25, "Brazil"), ("Engineer", "Remote"))


# Unpack the tuple and print:
# name
# age
# country
# job title
# work mode
# Expected output:

# Alice
# 25
# Brazil
# Engineer
# Remote

record = ("Alice", (25, "Brazil"), ("Engineer", "Remote"))

( name , ( age , country ) , ( job , mode) ) = record
print(name)
print(age)
print(country)
print(job)
print(mode)


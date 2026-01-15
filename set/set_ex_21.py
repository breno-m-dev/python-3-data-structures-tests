# 2️⃣1️⃣ Set comprehension

# Task:
# Create a set containing the squares of all even numbers from 1 to 10.

# Expected output:

# {4, 16, 36, 64, 100}


print(set( { i*i for i in range(2,11,2) }   ) )
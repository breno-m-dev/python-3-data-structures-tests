# 2️⃣2️⃣ Find missing values

# Task:
# Given:

# expected = {1, 2, 3, 4, 5, 6}
# received = {1, 2, 4, 6}


# Create a set with values that are missing from received.

# Expected output:

# {3, 5}

expected = {1, 2, 3, 4, 5, 6}
received = {1, 2, 4, 6}

print(expected.difference(received))
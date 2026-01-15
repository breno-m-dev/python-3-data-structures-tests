# 2️⃣7️⃣ Power set (hard 💀)

# Task:
# Given:

# data = {1, 2, 3}

# Create a list containing all subsets of the set.
# Expected output (order may vary):

# [
#   set(),
#   {1}, {2}, {3},
#   {1,2}, {1,3}, {2,3},
#   {1,2,3}
# ]

data = {1, 2, 3}

power_set = [set()]

for item in data:
    new_subsets = []
    for subset in power_set:
        new_subsets.append(subset | {item})
    power_set.extend(new_subsets)

print(power_set)


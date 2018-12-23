# Write a Python program to remove an item from a set if it is present in the set.

num_set = set([1, 2, 3, 4, 5])
print(num_set)

# after discard the items

if 4 in num_set:
    num_set.discard(4)
print(num_set)


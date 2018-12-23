# Write a Python program to use of frozensets.

set1 = set([1, 2, 3, 4, 6, 7])
set2 = set([0, 2, 3, 4])
# use isdisjoint(). Return True if the set has no elements in common with other.

print(set1.isdisjoint(set2))

# use difference(). Return a new set with elements in the set that are not in the others.
print(set1.difference(set2))

# new set with elements from both set1 and set2
print(set1 | set2)

# Write a Python program to create the colon of a tuple.

from copy import  deepcopy

tuple1 = ("abc", 6, [], True)
print(tuple1)

# make a copy of a tuple using deepcopy() function
tuple1_clone = deepcopy(tuple1)
print(tuple1_clone)

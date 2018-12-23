# Write a Python program to unpack a tuple in several variables.

# creat a tuple

tuple1 = 4, 2, 3
print(tuple1)

n1, n2, n3 = tuple1
# unpack tuple in variabels
print(n1 + n2 + n3)

# the number of variables must be equal to the number of items of the tuple
n1, n2, n3, n4= tuple1

# # Write a Python program to reverse a tuple.
#
# tuple1 = "abhishekSingh"
# rev_tuple = reversed(tuple1)
# print(tuple(rev_tuple))



import time

st = time.time()
a =  tuple(range(0, 100000000))

a = set(a)
a = list(a)
print(a)
ed = time.time()
to = ed - st
print(time.time() - st)
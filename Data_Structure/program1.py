# Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through in

from array import *
array_int = array('i', [1,3,5,7,9])
for i in array_int:
    print(i)

array_index = int(input("enter number of index which you want: "))
print(array_int[array_index])

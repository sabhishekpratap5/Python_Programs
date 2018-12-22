# Write a Python program to remove the first occurrence of a specified element from an array

from array import *
array_num = list()
num = int(input("enter number of element: "))
for i in  range(num):
    num_array = int(input("enter the element of the array: "))
    array_num.append(num_array)
print(array_num)

rev_num = int(input("enter number which you want first occurrence remove: "))
array_num.remove(rev_num)
print(array_num)